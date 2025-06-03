import streamlit as st

# Supondo que all_tasks_todas seja uma lista ou dicionário
all_tasks_todas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]  # exemplo

# Inicializar o dicionário
indice = {}

# Criar checkboxes
for item in range(len(all_tasks_todas)):
    indice[item] = st.checkbox(all_tasks_todas[item])

# Verificar resultados
st.write("Estado dos checkboxes:", indice)