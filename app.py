import streamlit as st
import pandas as pd
from datetime import date

# --- CONFIGURAÇÕES INICIAIS ---
st.set_page_config(page_title="RH - Iguaba Grande", layout="centered")

# Variável para controlar se o formulário foi enviado
if "enviado" not in st.session_state:
    st.session_state.enviado = False

# --- ESTILO PARA IMPRESSÃO ---
# Esse bloco de código CSS ajuda a esconder os botões do Streamlit na hora de imprimir
st.markdown("""
    <style>
    @media print {
        .stButton, .stDownloadButton, header, footer {
            display: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO DO FORMULÁRIO ---
def mostrar_formulario():
    st.image("https://www.iguaba.rj.gov.br/wp-content/uploads/2021/03/logo-prefeitura.png", width=80)
    st.title("Justificativa de Ponto - SMS")
    
    with st.form("form_justificativa"):
        st.subheader("IDENTIFICAÇÃO")
        nome = st.text_input("NOME COMPLETO")
        setor = st.text_input("SETOR", value="APS-CRECHES")
        matricula = st.text_input("MATRÍCULA")
        
        st.markdown("---")
        st.subheader("DETALHES DA OCORRÊNCIA")
        
        tipo = st.selectbox("TIPO DE OCORRÊNCIA", [
            "1. Atraso", "2. Saída Antecipada", "3. Ausência de Marcação",
            "4. Falta (Meio Período)", "5. Falta (Integral)", "6. Trabalho Externo",
            "7. Óbito", "8. Folga", "9. Hora Extra", "10. Atestado Médico",
            "11. Convocação Judicial", "12. Casamento/Nasc.", "13. Outros"
        ])
        
        mes = st.selectbox("MÊS DE REFERÊNCIA", ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
        data_ocorrido = st.date_input("DATA DA OCORRÊNCIA")
        doc = st.radio("POSSUI DOCUMENTO COMPROBATÓRIO?", ["Sim", "Não"], horizontal=True)
        justificativa = st.text_area("JUSTIFICATIVA / OBSERVAÇÕES")
        
        btn_enviar = st.form_submit_button("ENVIAR E GERAR PARA IMPRESSÃO")
        
        if btn_enviar:
            if nome and matricula:
                # Aqui guardamos os dados para a tela de impressão
                st.session_state.dados = {
                    "nome": nome, "setor": setor, "mat": matricula,
                    "tipo": tipo, "mes": mes, "data": data_ocorrido.strftime('%d/%m/%Y'),
                    "doc": doc, "just": justificativa
                }
                st.session_state.enviado = True
                st.rerun()
            else:
                st.error("Por favor, preencha Nome e Matrícula.")

# --- FUNÇÃO DE IMPRESSÃO ---
def mostrar_impressao():
    d = st.session_state.dados
    
    # Estrutura HTML que imita o papel timbrado
    st.markdown(f"""
    <div style="border: 2px solid #000; padding: 30px; font-family: 'Arial'; color: black; background-color: white;">
        <div style="text-align: center;">
            <h2 style="margin: 0;">PREFEITURA MUNICIPAL DE IGUABA GRANDE</h2>
            <h3 style="margin: 0;">SECRETARIA MUNICIPAL DE SAÚDE</h3>
            <h4 style="text-decoration: underline;">JUSTIFICATIVA DE PONTO</h4>
        </div>
        <br>
        <p><b>NOME:</b> {d['nome'].upper()}</p>
        <p><b>SETOR:</b> {d['setor']} | <b>MATRÍCULA:</b> {d['mat']}</p>
        <p><b>OCORRÊNCIA:</b> {d['tipo']} | <b>MÊS:</b> {d['mes']}</p>
        <p><b>DATA DO EVENTO:</b> {d['data']} | <b>POSSUI DOC:</b> {d['doc']}</p>
        <p><b>JUSTIFICATIVA:</b> {d['just']}</p>
        <br><br><br>
        <p style="text-align: center;">Iguaba Grande, {date.today().strftime('%d/%m/%Y')}</p>
        <br><br>
        <table style="width: 100%; border: none;">
            <tr>
                <td style="width: 45%; border-top: 1px solid black; text-align: center;">SERVIDOR (A)</td>
                <td style="width: 10%;"></td>
                <td style="width: 45%; border-top: 1px solid black; text-align: center;">CHEFIA IMEDIATA</td>
            </tr>
        </table>
    </div>
    <br>
    <p style="color: red;">Pressione <b>Ctrl + P</b> no teclado para salvar como PDF ou imprimir.</p>
    """, unsafe_allow_html=True)
    
    if st.button("Voltar ao Formulário"):
        st.session_state.enviado = False
        st.rerun()

# --- LÓGICA DE NAVEGAÇÃO ---
if st.session_state.enviado:
    mostrar_impressao()
else:
    mostrar_formulario()
