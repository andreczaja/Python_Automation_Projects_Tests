import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
df = pd.read_csv('supermarket_sales.csv',sep=';',decimal=',')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(['Date'])

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))

months = st.sidebar.selectbox('Mês',df['Month'].unique())

df_filtered = df[df['Month'] == months]

col1, col2 = st.columns([0.5,0.5])
col3, col4, col5 = st.columns([0.34,0.33,0.33])

fig_date = px.bar(df_filtered,x='Date',y ='Total',color = 'City',title='Faturamento por dia')
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered,x='Date',y ='Product line',color ='City',title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total,x='City',y ='Total',title='Faturamento por filial')
col3.plotly_chart(fig_city)

fig_kind = px.pie(df_filtered,values='Total',names='Payment',title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_kind)

rating_mean = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(rating_mean,x='City',y ='Rating',title='Rating por filial',text_auto=True)
fig_rating.update_traces(texttemplate='%{y:.2f}', textposition='outside')
col5.plotly_chart(fig_rating)




