import streamlit as st
from datetime import date

# Configuração visual da página
st.set_page_config(page_title="RH - Iguaba Grande", page_icon="📋")

st.title("Justificativa de Ponto - SMS")
st.write("Preencha os dados abaixo para gerar o documento de impressão.")

# Criando as caixas de preenchimento (Variáveis)
nome = st.text_input("Nome Completo")
matricula = st.text_input("Matrícula")
setor = st.text_input("Setor", value="APS-CRECHES")

opcao = st.selectbox("Tipo de Ocorrência", [
    "1. Atraso", "2. Saída Antecipada", "5. Falta (Integral)", "10. Atestado Médico", "13. Outros"
])

justificativa = st.text_area("Justificativa")

# Botão para mostrar o resultado
if st.button("Gerar Documento"):
    if nome and matricula:
        st.success("Documento pronto! Use o comando Ctrl + P para imprimir.")
        st.markdown(f"""
        ---
        ### FORMULÁRIO DE JUSTIFICATIVA
        **Nome:** {nome}  
        **Matrícula:** {matricula} | **Setor:** {setor}  
        **Ocorrência:** {opcao}  
        **Data:** {date.today().strftime('%d/%m/%Y')}  
        **Descrição:** {justificativa}
        
        <br><br>
        __________________________________________  
        Assinatura do Servidor
        """, unsafe_allow_html=True)
    else:
        st.error("Por favor, preencha seu nome e matrícula.")
