import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
import numpy as np
import time
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

st.set_page_config(page_title='Acompanhamento em tempo real KT Argentina - SSC Latam',layout='wide', initial_sidebar_state='expanded')
# Carregar variáveis de ambiente
load_dotenv()

@st.cache_resource
def get_engine():
    return create_engine(os.getenv("DATABASE_URL"))

def init_db():
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text('''
        CREATE TABLE IF NOT EXISTS table_kt (
            input_id SERIAL PRIMARY KEY,
            data DATE,
            task_name TEXT,
            status_kt TEXT,
            status_dtp TEXT
            )
        '''))
    conn.commit()


# Inicializar DB
init_db()
data = date.today()

def obter_dados():
    engine = get_engine()
    df = pd.read_sql_query("SELECT * FROM table_kt", engine)
    return df


df_main = obter_dados()

def existe_registro(task_name, data):
    df_existe_registro = df_main[(df_main['task_name'] == task_name) & (df_main['data'] == str(data))]
    result = df_existe_registro['task_name'].count()
    return result > 0  # True se existe, False se não existe

def inserir_ou_atualizar(data, task_name, status_kt, status_dtp):
    engine = get_engine()
    with engine.connect() as conn:
        if existe_registro(task_name, data):
            conn.execute(
            """UPDATE table_kt SET status_kt = %s, status_dtp = %s 
                WHERE task_name = %s AND data = %s""",
                (status_kt, status_dtp, task_name, data)
            )
        else:
            conn.execute(
            text("INSERT INTO table_kt (data, task_name, status_kt, status_dtp) VALUES (:data, :task_name, :status_kt, :status_dtp)"),
                {
                    "data": str(data),
                    "task_name": task_name, 
                    "status_kt": status_kt,
                    "status_dtp": status_dtp
                }
            )
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

abas = st.tabs(["➕ Inserir Atividade", "📊 Dashboard"])


def desmarcar_tasks_avulsas():
    for task in all_tasks:
        if task in st.session_state:
            st.session_state[task] = False

def desmarcar_todas_as_atividades():
    if 'Todas as Atividades' in st.session_state:
        st.session_state['Todas as Atividades'] = False

# Checkbox exclusivo para "Todas as Atividades"
sidebar_page = st.sidebar
sidebar_page.header("Selecione os processos a visualizar:")
sidebar_page.checkbox('Todas as Atividades', key='Todas as Atividades', on_change=desmarcar_tasks_avulsas)
all_tasks = df_main['task_name'].unique()
for task in all_tasks:
    sidebar_page.checkbox(task, key=task, on_change=desmarcar_todas_as_atividades)
    dict_estados_escolha_tasks = {task: st.session_state.get(task, False) for task in all_tasks}
    dict_estados_escolha_tasks['Todas as Atividades'] = st.session_state.get('Todas as Atividades', False)

with abas[0]:
    st.header("Registrar nova atividade")
    text_task = st.selectbox('Qual a atividade que você aprendeu hoje?',list_tasks)
    text_status_kt = st.selectbox('Qual o status do KT dessa atividade?', list(status_dict_kt.keys()))
    text_status_dtp = st.selectbox('Qual o status do DTP dessa atividade?', list(status_dict_dtp.keys()))
    if st.button('Inserir Atualização de Atividade'):
        inserir_ou_atualizar(data, text_task, text_status_kt,text_status_dtp)
        st.success("Atualização de atividade registrada com sucesso.")
        st.rerun()
        st.session_state['Todas as Atividades'] = False
        time.sleep(0.5)
        st.session_state['Todas as Atividades'] = True


with abas[1]:


    if df_main.empty:
        st.warning("Nenhuma atividade registrada ainda.")
    else:
        # Preparação inicial dos dados
        df_main['data'] = pd.to_datetime(df_main['data'])
        df_main['data_formatada'] = df_main['data'].dt.strftime('%d/%m/%Y')
        df_main = df_main.sort_values(by=['task_name', 'data'])

        # Mapeia o status para números
        df_main['status_num_kt'] = df_main['status_kt'].map(status_dict_kt)
        df_main['status_num_dtp'] = df_main['status_dtp'].map(status_dict_dtp)


        st.header("Contagem Atualizada por Status KT/DTP")

        df_filtered = df_main.copy()
        first_date = df_filtered['data'].min()
        last_date = df_filtered['data'].max()

        tasks_remaining = df_filtered['task_name'].unique()
        all_dates = pd.date_range(start=df_main['data'].min(), end=data)
        full_index = pd.MultiIndex.from_product([all_dates, tasks_remaining], names=['data', 'task_name'])
        df_filtered = df_filtered.sort_values(['data', 'task_name', 'input_id'])
        df_filtered = df_filtered.groupby(['data', 'task_name'])[['status_num_kt','status_num_dtp']].last().reset_index()
        df_filtered = df_filtered.set_index(['data', 'task_name'])
        df_filtered = df_filtered.reindex(full_index)
        df_filtered = df_filtered.reset_index()
        df_filtered.loc[df_filtered['data'] == first_date, ['status_num_kt','status_num_dtp']] = 1
        df_filtered = df_filtered.sort_values(['task_name','data'])
        df_filtered = df_filtered.ffill()

        reverse_status_dict_kt = {v: k for k, v in status_dict_kt.items()}
        reverse_status_dict_dtp = {v: k for k, v in status_dict_dtp.items()}
        df_kt = df_filtered.drop('status_num_dtp',axis=1)
        df_kt_hoje = df_kt[df_kt['data'] == last_date].drop('data',axis=1)
        df_dtp = df_filtered.drop('status_num_kt',axis=1)
        df_dtp_hoje = df_dtp[df_dtp['data'] == last_date].drop('data',axis=1)

        if st.session_state['Todas as Atividades'] == False:
            tasks_to_use = [task for task, estado in dict_estados_escolha_tasks.items() 
                        if estado == True and task != 'Todas as Atividades']
            
            for key, value in dict_estados_escolha_tasks.items():
                if key == 'Todas as Atividades' and value == True:
                    dict_estados_escolha_tasks[key] = False
                    st.session_state[key] = False
    
            # Aplicar filtros nos dataframes
            df_kt = df_kt[df_kt['task_name'].isin(tasks_to_use)]
            df_kt_hoje = df_kt_hoje[df_kt_hoje['task_name'].isin(tasks_to_use)]
            df_dtp = df_dtp[df_dtp['task_name'].isin(tasks_to_use)]
            df_dtp_hoje = df_dtp_hoje[df_dtp_hoje['task_name'].isin(tasks_to_use)]

        else:
            # Se "Todas as Atividades" está True, desmarcar todos os outros
            for key, value in dict_estados_escolha_tasks.items():
                if key != 'Todas as Atividades' and value == True:
                    dict_estados_escolha_tasks[key] = False
                    st.session_state.clear()
                    st.rerun()

            tasks_to_use = all_tasks
        
        # Verificar se ainda há dados após os filtros
        if df_filtered.empty:
            st.warning("Nenhum dado encontrado com os filtros aplicados.")
        else:
            def add_change_markers(df, status_col):
                df_markers = []
                for task in df['task_name'].unique():
                    task_data = df[df['task_name'] == task].sort_values('data')
                    changes = task_data[status_col].diff() != 0
                    changes.iloc[0] = True
                    if len(task_data) > 1:
                        changes.iloc[-1] = True
                    
                    change_points = task_data[changes]
                    df_markers.append(change_points)
                
                return pd.concat(df_markers, ignore_index=True) if df_markers else pd.DataFrame()
            
    
            df_kt_markers = add_change_markers(df_kt, 'status_num_kt')
            df_dtp_markers = add_change_markers(df_dtp, 'status_num_dtp')

            df_kt_hoje['status_num_kt'] = df_kt_hoje['status_num_kt'].map(reverse_status_dict_kt)
            df_dtp_hoje['status_num_dtp'] = df_dtp_hoje['status_num_dtp'].map(reverse_status_dict_dtp)
            
            df_depara = pd.merge(df_kt_hoje,df_dtp_hoje,how='inner',on=['task_name'])
            df_depara = df_depara.rename(columns={'task_name': 'Processo','status_num_kt': 'Status KT','status_num_dtp': 'Status DTP'})

            df_grouped_kt_count_status = df_depara.groupby('Status KT')['Processo'].count().reset_index()
            df_grouped_dtp_count_status = df_depara.groupby('Status DTP')['Processo'].count().reset_index()
            fig_kt_count_status = px.bar(df_grouped_kt_count_status, x='Status KT', y='Processo', 
            title='Status KT Hoje')
            fig_dtp_count_status = px.bar(df_grouped_dtp_count_status, x='Status DTP', y='Processo', 
            title='Status DTP Hoje')

            fig_kt_count_status.update_yaxes(title = 'Contagem',range=[0,df_grouped_kt_count_status['Processo'].max() +2])
            fig_dtp_count_status.update_yaxes(title = 'Contagem',range=[0,df_grouped_dtp_count_status['Processo'].max() +2])

            col1, col2 = st.columns([0.5,0.5])
            col1.plotly_chart(fig_kt_count_status)
            col2.plotly_chart(fig_dtp_count_status)
            st.header('Status por Processo')
            st.dataframe(df_depara, hide_index=True)

            st.header('Linha do Tempo')
            st.info('Clique uma vez no rótulo da tarefa para ocultá-la e clique duas vezes para manter somente ela.')

            all_status_KT_todos = np.append('Todos os Status', list(status_dict_kt.keys()))
            filtered_kt_timeline = st.selectbox('Filtre por Status do KT:', all_status_KT_todos)
            if filtered_kt_timeline != 'Todos os Status':
                df_tasks_kt_filtered = df_kt_hoje[df_kt_hoje['status_num_kt'] == filtered_kt_timeline]
                list_tasks_kt_filtered = [x for x in df_tasks_kt_filtered['task_name']]
                df_kt = df_kt[df_kt['task_name'].isin(list_tasks_kt_filtered)]
                df_kt_markers = df_kt_markers[df_kt_markers['task_name'].isin(list_tasks_kt_filtered)]
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
            fig_timeline_kt.update_xaxes(title="Data")

            st.plotly_chart(fig_timeline_kt, use_container_width=True)
            
            all_status_DTP_todos = np.append('Todos os Status', list(status_dict_dtp.keys()))
            filtered_dtp_timeline = st.selectbox('Filtre por Status do DTP:', all_status_DTP_todos)
            if filtered_dtp_timeline != 'Todos os Status':
                df_tasks_dtp_filtered = df_dtp_hoje[df_dtp_hoje['status_num_dtp'] == filtered_dtp_timeline]
                list_tasks_dtp_filtered = [x for x in df_tasks_dtp_filtered['task_name']]
                df_dtp = df_dtp[df_dtp['task_name'].isin(list_tasks_dtp_filtered)]
                df_dtp_markers = df_dtp_markers[df_dtp_markers['task_name'].isin(list_tasks_dtp_filtered)]
            # Gráfico KT
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

            df_dados_gerais = df_main.rename(columns={'task_name': 'Processo','status_kt': 'Status KT','status_dtp': 'Status DTP','data_formatada':'Data de Atualização'})
            df_dados_gerais['data'] = pd.to_datetime(df_main['data'])
            df_dados_gerais = df_dados_gerais.sort_values(by='data',ascending=True)
            df_dados_gerais.drop(['input_id','status_num_kt','status_num_dtp','data'],axis=1,inplace=True)
            
            st.dataframe(df_dados_gerais, hide_index=True)