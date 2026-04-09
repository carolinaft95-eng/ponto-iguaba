import streamlit as st
from datetime import date

# 1. TÍTULO DO SITE (Apenas para a aba do navegador)
st.set_page_config(page_title="RH - Iguaba Grande", layout="centered")

# 2. FUNÇÃO PARA CRIAR O DOCUMENTO FORMATADO
def gerar_documento(dados):
    # Este bloco abaixo é HTML/CSS, usado para desenhar o papel
    html_layout = f"""
    <div style="border: 2px solid black; padding: 25px; font-family: Arial, sans-serif; color: black; background-color: white;">
        <div style="text-align: center; line-height: 1.2;">
            <h3 style="margin: 0;">PREFEITURA MUNICIPAL DE IGUABA GRANDE</h3>
            <h4 style="margin: 0;">ESTADO DO RIO DE JANEIRO</h4>
            <h4 style="margin: 0;">SECRETARIA MUNICIPAL DE SAÚDE</h4>
            <h2 style="margin: 15px 0; text-decoration: underline;">JUSTIFICATIVA DE PONTO</h2>
        </div>
        
        <div style="margin-top: 20px;">
            <p style="background-color: #f0f0f0; padding: 5px; font-weight: bold; border: 1px solid black;">IDENTIFICAÇÃO DO SERVIDOR</p>
            <p><b>NOME COMPLETO:</b> {dados['nome'].upper()}</p>
            <p><b>SETOR:</b> {dados['setor']} | <b>MATRÍCULA:</b> {dados['mat']}</p>
        </div>

        <div style="margin-top: 10px;">
            <p style="background-color: #f0f0f0; padding: 5px; font-weight: bold; border: 1px solid black;">DETALHES DA OCORRÊNCIA</p>
            <p><b>TIPO:</b> {dados['tipo']} | <b>MÊS:</b> {dados['mes']}</p>
            <p><b>DATA DA OCORRÊNCIA:</b> {dados['data_ocorr']}</p>
            <p><b>POSSUI DOCUMENTO COMPROBATÓRIO?</b> {dados['tem_doc']}</p>
            <p><b>JUSTIFICATIVA:</b> {dados['just']}</p>
        </div>

        <div style="margin-top: 40px; text-align: center;">
            <p>Iguaba Grande, {date.today().strftime('%d/%m/%Y')}</p>
        </div>

        <div style="margin-top: 60px; display: flex; justify-content: space-between;">
            <div style="width: 45%; border-top: 1px solid black; text-align: center; padding-top: 5px;">SERVIDOR (A)</div>
            <div style="width: 45%; border-top: 1px solid black; text-align: center; padding-top: 5px;">CHEFIA IMEDIATA</div>
        </div>
    </div>
    <br>
    <p style="color: blue; font-weight: bold;">DICA: Aperte Ctrl + P no teclado para salvar como PDF ou imprimir esta folha.</p>
    """
    return html_layout

# 3. INTERFACE DO USUÁRIO (O que aparece no site)
st.title("Formulário de Justificativa")
st.write("Preencha os campos abaixo conforme o documento oficial.")

with st.form("meu_formulario"):
    nome = st.text_input("Nome Completo")
    matricula = st.text_input("Matrícula")
    setor = st.text_input("Setor", value="APS-CRECHES")
    
    col1, col2 = st.columns(2)
    with col1:
        tipo = st.selectbox("Tipo de Ocorrência", [
            "1. Atraso", "2. Saída Antecipada", "5. Falta (Integral)", 
            "10. Atestado Médico", "11. Convocação Judicial", "13. Outros"
        ])
        data_ocorr = st.date_input("Data da Ocorrência")
    with col2:
        mes = st.text_input("Mês de Referência")
        tem_doc = st.radio("Possui Documento?", ["Sim", "Não"], horizontal=True)
    
    justificativa = st.text_area("Justificativa")
    
    enviar = st.form_submit_button("Gerar Documento para Impressão")

# 4. LÓGICA FINAL
if enviar:
    if nome and matricula:
        # Criamos um "dicionário" (pasta) com as respostas
        dados_servidor = {
            "nome": nome, "mat": matricula, "setor": setor,
            "tipo": tipo, "mes": mes, "data_ocorr": data_ocorr.strftime('%d/%m/%Y'),
            "tem_doc": tem_doc, "just": justificativa
        }
        # Mostra o desenho do papel na tela
        st.markdown(gerar_documento(dados_servidor), unsafe_allow_html=True)
    else:
        st.error("Por favor, preencha o Nome e a Matrícula.")
