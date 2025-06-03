import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import time

# Conexão com SQLite
conn = sqlite3.connect('db_kt_argentina.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS table_kt (
    input_id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    task_name TEXT,
    status_kt TEXT,
    status_dtp TEXT
)''')
conn.commit()

def obter_dados():
    return pd.read_sql_query("SELECT * FROM table_kt", conn)

def consultar_ultimo_status():
    return pd.read_sql_query("SELECT * FROM table_kt", conn)

def buscar_registro(task_name, data):
    query = "SELECT COUNT(*) FROM table_kt WHERE task_name = ? AND data = ?"
    result = c.execute(query, (task_name, data)).fetchone()
    return result[0] > 0  # True se existe, False se não existe

def inserir_ou_atualizar(data, task_name, status_kt, status_dtp):
    # Primeiro verifica se existe
    if buscar_registro(task_name, data):
        # Atualiza
        c.execute("UPDATE table_kt SET status_kt = ?, status_dtp = ? WHERE task_name = ? AND data = ?", 
        (status_kt, status_dtp, task_name, data))
    else:
        # Insere novo
        c.execute("INSERT INTO table_kt (data, task_name, status_kt, status_dtp) VALUES (?, ?, ?, ?)",
        (data, task_name, status_kt, status_dtp))
    conn.commit()


# Mapeamento de status para números (ordem crescente)
status_dict_kt = {
    'Não iniciado': 1,
    'Observando': 2,
    'Executando com orientação': 3,
    'Executando sozinho': 4,
    'Execução validada': 5,
    "KT concluído":6,
}

status_dict_dtp = {
    'Não iniciado': 1,
    'Em preparação': 2,
    'Finalizado': 3,
    'Revisado': 4,
    'Disponível no sistema': 5,
}

list_tasks = [
    "1.2.12.2 Process automatic supplier, Travel & Expense, customer and down payments",
    "1.2.12.3 Process intercompany netting",
    "1.2.12.4 Process manual payments (receive, validate, enter, request, and archive)",
    "1.2.12.5 Post and reconcile outgoing payments and follow up on errors",
    "1.2.13.1 Perform supplier onboarding",
    "1.2.13.2 Send invoice to bank",
    "1.2.13.3 Perform reconciliation and settlement",
    "1.2.13.4 Bridge supplier needs with the banks (login / banking system, resolve differences, etc)",
    "1.2.14.1 Perform AP/GL account reconciliations",
    "1.2.14.3 Close AP and produce AP reporting",
    "1.2.2.2 Validate and approve requests",
    "1.2.8.1 Handle external queries",
    "1.2.8.2 Handle internal queries"
]

# Abas Streamlit
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
abas = st.tabs(["➕ Inserir Atividade", "📊 Dashboard"])

with abas[0]:
    st.header("Registrar nova atividade")
    text_task = st.selectbox('Qual a atividade que você aprendeu hoje?',list_tasks)
    text_status_kt = st.selectbox('Qual o status do KT dessa atividade?', list(status_dict_kt.keys()))
    text_status_dtp = st.selectbox('Qual o status do DTP dessa atividade?', list(status_dict_dtp.keys()))
    data = date.today()
    if st.button('Inserir Atualização de Atividade'):
        inserir_ou_atualizar(data, text_task, text_status_kt,text_status_dtp)
        st.success("Atualização de atividade registrada com sucesso.")
        time.sleep(3)
        st.rerun()

with abas[1]:
    df = obter_dados()
    
    if df.empty:
        st.warning("Nenhuma atividade registrada ainda.")
    else:
        # Preparação inicial dos dados
        df['data'] = pd.to_datetime(df['data'])
        df['data_formatada'] = df['data'].dt.strftime('%d/%m/%Y')
        df = df.sort_values(by=['task_name', 'data_formatada'])
        
        # Mapeia o status para números
        df['status_num_kt'] = df['status_kt'].map(status_dict_kt)
        df['status_num_dtp'] = df['status_dtp'].map(status_dict_dtp)
        
        # Criar sidebar APÓS preparar os dados
        all_tasks = df['task_name'].unique()
        all_tasks_todas = np.append('Todas as Atividades', all_tasks)
        all_status_KT_todos = np.append('Todos os Status', list(status_dict_kt.keys()))
        all_status_DTP_todos = np.append('Todos os Status', list(status_dict_dtp.keys()))
        
        task = st.sidebar.selectbox('Atividade', list(all_tasks_todas), index=0)
        status_KT_task = st.sidebar.selectbox('Status KT', all_status_KT_todos, index=0)
        status_DTP_task = st.sidebar.selectbox('Status DTP', all_status_DTP_todos, index=0)
        
        st.header("📈 Visualização dos dados")
        
        # APLICAR FILTROS CUMULATIVOS
        df_filtered = df.copy()
        
        # Filtro por atividade
        if task != 'Todas as Atividades':
            df_filtered = df_filtered[df_filtered['task_name'] == task]
            tasks_to_use = [task]
        else:
            tasks_to_use = all_tasks
        
        # Filtro por status KT (aplicado sobre o df já filtrado)
        if status_KT_task != 'Todos os Status':
            df_filtered = df_filtered[df_filtered['status_kt'] == status_KT_task]
        
        # Filtro por status DTP (aplicado sobre o df já filtrado)
        if status_DTP_task != 'Todos os Status':
            df_filtered = df_filtered[df_filtered['status_dtp'] == status_DTP_task]
        
        # Verificar se ainda há dados após os filtros
        if df_filtered.empty:
            st.warning("Nenhum dado encontrado com os filtros aplicados.")
        else:
            # Criar full_index baseado nas tarefas e datas filtradas
            all_dates = pd.date_range(start=df_filtered['data'].min(), end=df_filtered['data'].max())
            
            # Usar apenas as tarefas que restaram após o filtro
            tasks_remaining = df_filtered['task_name'].unique()
            full_index = pd.MultiIndex.from_product([all_dates, tasks_remaining], names=['data', 'task_name'])
            
            df_filtered.fillna(1, inplace=True)
            
            # CORREÇÃO AQUI: Processamento KT preservando valores atualizados
            df_kt = df_filtered.sort_values(['data', 'task_name', 'input_id']).groupby(['data', 'task_name'])['status_num_kt'].last().reset_index()
            df_kt = df_kt.set_index(['data', 'task_name'])
            
            # Criar DataFrame vazio com full_index e preencher com dados reais
            df_kt_full = pd.DataFrame(index=full_index)
            df_kt_full['status_num_kt'] = None
            
            # Sobrescrever com os dados reais onde existem
            df_kt_full.update(df_kt)
            
            # Agora fazer o forward fill por tarefa, mas preservando os valores reais
            df_kt = df_kt_full.groupby('task_name')['status_num_kt'].ffill().reset_index()
            df_kt = df_kt.sort_values(by=['data'], ascending=True)
            df_kt.fillna(1, inplace=True)

            # CORREÇÃO AQUI: Processamento DTP preservando valores atualizados  
            df_dtp = df_filtered.sort_values(['data', 'task_name', 'input_id']).groupby(['data', 'task_name'])['status_num_dtp'].last().reset_index()
            df_dtp = df_dtp.set_index(['data', 'task_name'])
            
            # Criar DataFrame vazio com full_index e preencher com dados reais
            df_dtp_full = pd.DataFrame(index=full_index)
            df_dtp_full['status_num_dtp'] = None
            
            # Sobrescrever com os dados reais onde existem
            df_dtp_full.update(df_dtp)
            
            # Agora fazer o forward fill por tarefa, mas preservando os valores reais  
            df_dtp = df_dtp_full.groupby('task_name')['status_num_dtp'].ffill().reset_index()
            df_dtp = df_dtp.sort_values(by=['data'], ascending=True)
            df_dtp.fillna(1, inplace=True)
            
            # Criar mapeamento reverso para exibição nos gráficos
            reverse_status_kt = {v: k for k, v in status_dict_kt.items()}
            reverse_status_dtp = {v: k for k, v in status_dict_dtp.items()}
            
            # Função para identificar pontos de mudança de status
            def add_change_markers(df, status_col):
                df_markers = []
                for task in df['task_name'].unique():
                    task_data = df[df['task_name'] == task].sort_values('data')
                    # Detectar mudanças de status
                    changes = task_data[status_col].diff() != 0
                    # Incluir o primeiro ponto sempre
                    changes.iloc[0] = True
                    # Incluir o último ponto se for diferente do anterior
                    if len(task_data) > 1:
                        changes.iloc[-1] = True
                    
                    change_points = task_data[changes]
                    df_markers.append(change_points)
                
                return pd.concat(df_markers, ignore_index=True) if df_markers else pd.DataFrame()
            
            df_kt_markers = add_change_markers(df_kt, 'status_num_kt')
            df_dtp_markers = add_change_markers(df_dtp, 'status_num_dtp')

            # Gráfico KT
            fig_timeline_kt = px.line(df_kt, x='data', y='status_num_kt', color='task_name',
                title="Status do KT")

            if not df_kt_markers.empty:
                fig_markers_kt = px.scatter(df_kt_markers, x='data', y='status_num_kt', color='task_name')
                for trace in fig_markers_kt.data:
                    trace.showlegend = False  # Não duplicar a legenda
                    fig_timeline_kt.add_trace(trace)
            
            fig_timeline_kt.update_yaxes(
                title="ETAPAS",
                tickmode='array',
                tickvals=list(status_dict_kt.values()),
                ticktext=list(status_dict_kt.keys()),
                range=[0.5, max(status_dict_kt.values()) + 0.5]
            )
            st.info('Clique uma vez no rótulo da tarefa para ocultá-la e clique duas vezes para manter somente ela.')
            fig_timeline_kt.update_xaxes(title="Data")
            st.plotly_chart(fig_timeline_kt, use_container_width=True)
            
            # Gráfico DTP
            fig_timeline_dtp = px.line(df_dtp, x='data', y='status_num_dtp', color='task_name',
                title="Status do DTP")

            if not df_dtp_markers.empty:
                fig_markers_dtp = px.scatter(df_dtp_markers, x='data', y='status_num_dtp', color='task_name')
                for trace in fig_markers_dtp.data:
                    trace.showlegend = False 
                    fig_timeline_dtp.add_trace(trace)
            
            fig_timeline_dtp.update_yaxes(
                title="ETAPAS",
                tickmode='array',
                tickvals=list(status_dict_dtp.values()),
                ticktext=list(status_dict_dtp.keys()),
                range=[0.5, max(status_dict_dtp.values()) + 0.5]
            )
            fig_timeline_dtp.update_xaxes(title="Data")
            st.plotly_chart(fig_timeline_dtp, use_container_width=True)

            st.subheader("📋 Dados completos")
            df_nomes_bonitos = df_filtered.drop(columns=['status_num_kt', 'status_num_dtp'])
            df_nomes_bonitos = df_nomes_bonitos.rename(columns={
                'data': 'Data de Atualização',
                'task_name': 'Nome da Atividade', 
                'status_kt': 'Status do KT',
                'status_dtp': 'Status do DTP'
            })
            st.dataframe(df_nomes_bonitos)