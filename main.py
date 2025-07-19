
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analisi Portafoglio AI", layout="wide")

st.title("🧠 Analisi Portafoglio Clienti – Giancarlo Raimondi")

st.markdown("""
Questa Web App ti consente di:
- Caricare un file Excel con il portafoglio cliente
- Visualizzare anteprima e analisi base
- Generare output strutturati per ulteriori elaborazioni (PDF, suggerimenti AI)
""")

uploaded_file = st.file_uploader("📎 Carica il file Excel del portafoglio", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ File caricato correttamente!")
    st.subheader("📊 Anteprima del Portafoglio")
    st.dataframe(df)

    st.markdown("🔧 Funzionalità avanzate in arrivo:")
    st.markdown("- Analisi AI (rating, quartili, margini)")
    st.markdown("- Proposte di sostituzione")
    st.markdown("- Esportazione PDF")
else:
    st.info("⏳ In attesa di un file Excel per iniziare l'analisi.")
