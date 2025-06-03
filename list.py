# import streamlit as st
# import datetime

# # Datas limite
# data_inicial = datetime.date(2025, 1, 1)
# data_final = datetime.date(2025, 5, 5)

# # Widget de intervalo de datas
# intervalo = st.date_input(
#     "Selecione um intervalo de datas",
#     value=(data_inicial, data_final),
#     min_value=data_inicial,
#     max_value=data_final
# )

# # Exibir resultado
# if isinstance(intervalo, tuple):
#     st.write("Início:", intervalo[0].strftime("%d.%m.%Y"))
#     st.write("Fim:", intervalo[1].strftime("%d.%m.%Y"))
# else:
#     st.warning("Por favor, selecione um intervalo de datas.")


import streamlit as st
import datetime

# Definindo o intervalo de datas
data_inicial = datetime.date(2025, 1, 1)
data_final = datetime.date(2025, 5, 5)

# Slider de data
data_selecionada = st.slider(
    "Selecione uma data",
    min_value=data_inicial,
    max_value=data_final,
    value=data_inicial,  # valor inicial selecionado
    format="DD.MM.YYYY"
)

st.write("Data selecionada:", data_selecionada.strftime("%d.%m.%Y"))
