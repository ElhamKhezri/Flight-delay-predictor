import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Titel & Beschreibung des Dashboards
st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️", layout="centered")

st.title("✈️ Flight Delay Risk Detector")
st.write("Wählen Sie die Flugdetails aus, um das statistische Risiko für eine Verspätung vorherzusagen.")

# 2. Modell laden
@st.cache_resource
def load_model():
    return joblib.load('flight_rf_model.pkl')

model = load_model()

# 3. Eingabeformular für den Nutzer aufbauen
st.header("📋 Flugdaten eingeben")

col1, col2 = st.columns(2)

with col1:
    month = st.selectbox("Monat", options=list(range(1, 13)), index=5)
    day_of_week = st.selectbox("Wochentag (1=Mo, 7=So)", options=list(range(1, 8)), index=4)
    crs_dep_time = st.slider("Geplante Abflugzeit (HHMM, z.B. 1430)", min_value=0, max_value=2359, value=1430, step=15)

with col2:
    carrier_code = st.number_input("Airline ID (Kategorie-Code)", min_value=0, max_value=100, value=5)
    origin_code = st.number_input("Abflughafen ID (Kategorie-Code)", min_value=0, max_value=400, value=100)
    dest_code = st.number_input("Zielflughafen ID (Kategorie-Code)", min_value=0, max_value=400, value=200)

day_of_month = st.slider("Tag des Monats", min_value=1, max_value=31, value=15)

# 4. Vorhersage-Button
if st.button("🔮 Verspätungs-Risiko berechnen", type="primary"):
    # Eingaben in das passende Format bringen
    input_data = pd.DataFrame({
        'month': [month],
        'day_of_month': [day_of_month],
        'day_of_week': [day_of_week],
        'op_unique_carrier': [carrier_code],
        'origin': [origin_code],
        'dest': [dest_code],
        'crs_dep_time': [crs_dep_time]
    })
    
    # Wahrscheinlichkeit berechnen
    prob = model.predict_proba(input_data)[0][1] * 100
    
    st.markdown("---")
    st.subheader("Ergebnis der Analyse:")
    
    # Optische Ampel anzeigen
    if prob >= 50:
        st.error(f"⚠️ **Hohes Verspätungsrisiko:** ca. **{prob:.1f}%**")
        st.warning("Empfehlung an Operations: Pufferzeiten beim Catering & Crew-Wechsel einplanen.")
    elif prob >= 30:
        st.warning(f"⚡ **Moderate Gefahr:** ca. **{prob:.1f}%** Verspätungswahrscheinlichkeit.")
    else:
        st.success(f"✅ **Geringes Risiko:** ca. **{prob:.1f}%** Verspätungswahrscheinlichkeit (Flug voraussichtlich pünktlich).")
