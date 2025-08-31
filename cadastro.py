import streamlit as st
import os
import datetime
data_mais_recente = datetime.date(2025, 12, 31)

#titula de aplicacao
st.title('Cadstro do Cliente')

# Campos de entrada para os dados do cliente
nome = st.text_input('Digite o nome do Cliente')
endereco = st.text_input('Digite o endereço')
dt_nasc = st.date_input('Escolha data de nascimento',min_value=datetime.date(1960, 1, 1), max_value=data_mais_recente) # retorna objeto datetime.date
tipo_cliente= st.selectbox('Tipo de Cliente',['Pessoa Fisica', 'Pessoa Juridica'])

#Botão para submeter o formulario
cadastrar = st.button('Cadstrar Cliente')

#Ação 'Cadastrar Cliente'
if cadastrar:
    #validação simples dos campos 
    if nome and endereco:
        NOME_ARQUIVO= 'clientes.csv'
        
        #Verifica se o arquivo CVS ja existe para decidir se escreve o cabeçalho
        escrever_cabecalho = not os.path.exists(NOME_ARQUIVO)
        
        try:
            with open(NOME_ARQUIVO, 'a', encoding='uft-8', mewline= '') as arquivo:
                if escrever_cabecalho:
                    arquivo.write('Nome,Endereço,Data de nascimento, Tipo de Cliente\n')
                
                #Escreve os dados do cliente no arquivo CSV, separados por virgula
                # O objeto dt_nasc (data) será convertido para string formato para string formato YYYY-MM-DD
                arquivo.write(f', {nome}, {endereco},{dt_nasc},{tipo_cliente}\n')   
            st.success('Cliente cadastrado com sucesso!!')
        
        except Exception as e:
            st.error(f'Ocorreu um erro ao salvar os dados: {e}')  
    else:
        st.warning('Por favor, preencha o nome e o endereço do cliente.')      
        
# Para exibir os dados
if st.checkbox('mostrar clientes cadastrados'):
    NOME_ARQUIVO = 'clientes.csv'
    if os.path.exists(NOME_ARQUIVO):
        try:
            #usando pandas para ler e exibir o CSV
            import pandas as pd
            dt_cliente = pd.read_csv(NOME_ARQUIVO)
            #st.dataframe(dt_clientes)
            st.table(dt_cliente)
        except Exception as e:
            st.error(f'Erro ao ler o arquivo do cliente: {e}')    
            st.write(f'Verifique se o arquivo {NOME_ARQUIVO} está formatado')
            
    else: 
        st.info('Ainda não há clientes cadastrados')       
            

