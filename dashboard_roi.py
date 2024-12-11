import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import locale

# Imposta il formato delle cifre
import locale

def format_currency(value):
    return locale.format_string("%.2f", value, grouping=True).replace(',', '.').replace('.', ',')


# Funzione per calcolare il ROI
def calcola_roi(costo_iniziale, costi_ricorrenti, incremento_vendite, risparmi_annuali, anni):
    investimento_totale = costo_iniziale + costi_ricorrenti * anni
    beneficio_totale = incremento_vendite + risparmi_annuali * anni
    roi = (beneficio_totale - investimento_totale) / investimento_totale * 100
    return roi

# Funzione per creare scenari "What-If"
def what_if(costo_iniziale, costi_ricorrenti, incremento_vendite, risparmi_annuali):
    anni = np.arange(1, 6)  # Periodo di analisi: 5 anni
    roi_valori = [calcola_roi(costo_iniziale, costi_ricorrenti, incremento_vendite, risparmi_annuali, anno) for anno in anni]

    # Creazione del grafico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(anni, roi_valori, marker='o', linestyle='-', label='ROI (%)')
    ax.axhline(0, color='red', linestyle='--', label='Break-even')

    # Aggiunta delle etichette con i valori di ROI
    for i, roi in enumerate(roi_valori):
        ax.text(anni[i], roi, f'{roi:.2f}%', fontsize=10, ha='center', va='bottom')

    ax.set_title('Simulazione ROI su 5 anni')
    ax.set_xlabel('Anni')
    ax.set_ylabel('ROI (%)')
    ax.legend()
    ax.grid()
    return fig

# Configurazione della dashboard Streamlit
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
    color: #000000;
}
input {
    font-size: 18px !important;
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #cccccc;
    margin-bottom: 10px;
}
label {
    font-size: 20px !important;  /* Aumenta la grandezza del font delle descrizioni */
    font-weight: bold;
    color: #0050b3;
    margin-bottom: 5px;
}
button {
    font-size: 18px !important;
    border: 2px solid #40a9ff;
    border-radius: 5px;
    background-color: #e6f7ff;
    color: red;
    padding: 10px 20px;
    cursor: pointer;
}
button:hover {
    background-color: #91d5ff;
}
section {
    backdrop-filter: blur(8px) brightness(0.9);
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color:rgba(0, 31, 63, 0.8); padding:10px; border-radius:5px; text-align:center;">
    <h1 style="color:#FFFFFF;">Dashboard per il Calcolo del ROI</h1>
</div>
""", unsafe_allow_html=True)

# Input Dati Generali
st.markdown("""
<div style="background-color:rgba(255, 255, 255, 0.8); padding:10px; border-left: 5px solid #40a9ff; margin-bottom:10px;">
    <h3 style="color:#0050b3;">Dati Generali</h3>
</div>
""", unsafe_allow_html=True)

costo_iniziale = st.number_input("Costo iniziale (€)", value=50000, step=1000, format="%d")
costi_ricorrenti = st.number_input("Costi ricorrenti annuali (€)", value=5000, step=100, format="%d")
risparmio_annuale = st.number_input("Risparmio annuale stimato (€)", value=30000, step=1000, format="%d")
incremento_vendite = st.number_input("Incremento delle vendite (€)", value=0, step=100, format="%d")

# Sezione ROI per 1-5 anni
st.markdown("""
<div style="background-color:rgba(255, 255, 255, 0.8); padding:10px; border-left: 5px solid #40a9ff; margin-bottom:10px;">
    <h3 style="color:#0050b3;">Calcolo ROI per 1-5 anni</h3>
</div>
""", unsafe_allow_html=True)

if st.button("Calcola ROI"):
    fig = what_if(costo_iniziale, costi_ricorrenti, incremento_vendite, risparmio_annuale)
    st.pyplot(fig)

# Sezione Calcoli Avanzati
st.markdown("""
<div style="background-color:rgba(255, 255, 255, 0.8); padding:10px; border-left: 5px solid #40a9ff; margin-bottom:10px;">
    <h3 style="color:#0050b3;">Analisi Avanzata del ROI</h3>
</div>
""", unsafe_allow_html=True)

st.write("Per questi calcoli si utilizzano i parametri inseriti sopra, che potete modificare a piacimento.")

# Input per ROI desiderato e anni
roi_desiderato = st.number_input("Inserisci la percentuale di ROI desiderata (%)", min_value=0, value=20, step=1)
anni_avanzati = st.number_input("Numero di anni per i calcoli avanzati", min_value=1, value=5, step=1)

# Calcolo Risparmio Minimo
costo_totale_progetto = costo_iniziale + costi_ricorrenti * anni_avanzati
risparmio_minimo = costo_totale_progetto * (1 + roi_desiderato / 100) / anni_avanzati
risparmio_minimo_formattato = locale.format_string("%.2f", risparmio_minimo, grouping=True)
st.markdown(f"""
<div style="background-color:rgba(230, 247, 255, 0.8); padding:10px; border-radius:5px; border: 1px solid #91d5ff; margin-bottom:10px;">
    <p style="font-size:18px; color:#0050b3;">
    Risparmio minimo annuale necessario per un ROI del {roi_desiderato}% su {anni_avanzati} anni: 
    <b>€{risparmio_minimo_formattato}</b></p>
</div>
""", unsafe_allow_html=True)

# Calcolo Range Prezzo Massimo
costo_massimo = risparmio_annuale * anni_avanzati / (1 + roi_desiderato / 100)
costo_massimo_formattato = locale.format_string("%.2f", costo_massimo, grouping=True)
st.markdown(f"""
<div style="background-color:rgba(246, 255, 237, 0.8); padding:10px; border-radius:5px; border: 1px solid #b7eb8f;">
    <p style="font-size:18px; color:#237804;">
    Prezzo massimo del progetto per un ROI del {roi_desiderato}% su {anni_avanzati} anni: 
    <b>€{costo_massimo_formattato}</b></p>
</div>
""", unsafe_allow_html=True)
