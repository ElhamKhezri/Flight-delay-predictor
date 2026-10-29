# Flight Delay Predictor ✈️📊

Ein professionelles Data-Analyst-Portfolio-Projekt zur Analyse von Flugverspätungen, inklusive Machine-Learning-Modell und interaktiver Streamlit-Web-App.

## 🛠️ Projektübersicht & Methodik (Workflow)
Das Projekt wurde von der rohen Datenbasis bis zur produktreifen Web-Anwendung in folgenden Schritten umgesetzt:

- **1. Datenerhebung & -bereitstellung:**
  - Verwendung umfangreicher Flugdatensätze (`flight_data_2024.csv`, ca. 1,31 GB) als Grundlage für die Analyse.
- **2. Explorative Datenanalyse (EDA) & Bereinigung:**
  - Untersuchung der Daten auf Muster, Trends und Korrelationen im Jupyter Notebook (`Flight_delay_project.ipynb`).
  - Bereinigung des Datensatzes (Behandlung von Fehlwerten, Filtern relevanter Features für Abflüge und Verspätungen).
- **3. Modellierung (Machine Learning):**
  - Training eines Random-Forest-Modells (`flight_rf_model.pkl`) zur Vorhersage von Flugverspätungen basierend auf Datum, Uhrzeit und Fluggesellschaft.
- **4. Entwicklung der Streamlit-App:**
  - Erstellung eines interaktiven Dashboards (`flt_delay_app.py`), das Nutzern ermöglicht, Flugdetails einzugeben und das Verspätungsrisiko live zu berechnen.


## 🚀 Lokale Ausführung

Falls du das Projekt lokal klonen und ausführen möchtest:

1. Klone das Repository:
   ```bash
   git clone [https://github.com/ElhamKhezri/flight-delay-predictor.git](https://github.com/ElhamKhezri/flight-delay-predictor.git)
pip install streamlit pandas numpy joblib
streamlit run flt_delay_app.py


👩‍💻 Autorin
Elham Khezri
Project Manager Data Analyst
