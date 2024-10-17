import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard") #titulo

uploaded_file = st.file_uploader("Choose a CSV File", type="csv") #Upload do arquivo

if uploaded_file is not None: #Se o arquivo não estiver vazio leia:
    df = pd.read_csv(uploaded_file)

    st.subheader("Pré Visualização") #pré Visualização
    st.write(df.head())

    st.subheader('Data Summary') #Sumário
    st.write(df.describe())

    st.subheader('Filter Data') 
    columns = df.columns.tolist() #Editando df(data frames) em colunas/listas
    selected_column = st.selectbox("Select Column to filter by", columns) #lendo a coluna na caixa de seleção
    unique_values = df[selected_column].unique() #extraindo informações da primeira caixa de coluna
    selected_value = st.selectbox("Select Values", unique_values) # informações secundarias da primeira caixa em uma caixa secundaria

    filtered_df = df[df[selected_column] == selected_value] #monstrando filtro na tela de acordo com as colunas escolhidas
    st.write(filtered_df) 

    st.subheader('Plot Data') #subtitulo e criando grafico
    x_column = st.selectbox('Select x-axis column', columns)
    y_column = st.selectbox('Select y-axis column', columns)

    if st.button('Generate Plot'): #imprimindo gráfico na tela
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else: #se caso não fizer upload isso estará na tela ao inicio do programa
    st.write('Waiting on uploaded file...')