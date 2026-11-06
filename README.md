# Tinkercad 3D – Anleitung

Eine minimalistische, deutschsprachige Wissenswebsite für **Tinkercad 3D Design**.
Sie ist als Informationsquelle für einen späteren Chatbot gedacht.

## Projektstruktur

```text
tinkercad_3d_guide/
├── app.py
├── requirements.txt
├── README.md
└── wissen/
    ├── 01_start.md
    ├── 02_oberflaeche.md
    ├── 03_formen.md
    ├── 04_objekte_bearbeiten.md
    ├── 05_ausrichten_und_gruppieren.md
    ├── 06_lochformen.md
    └── 07_export.md
```

## Lokal starten

1. Python auf dem Computer installieren.
2. Im Projektordner ein Terminal öffnen.
3. Abhängigkeiten installieren:

   ```bash
   pip install -r requirements.txt
   ```

4. Website starten:

   ```bash
   streamlit run app.py
   ```

## Auf GitHub hochladen

1. Auf GitHub ein neues Repository erstellen, z. B. `tinkercad-3d-guide`.
2. Alle Dateien und den Ordner `wissen` in das Repository hochladen.
3. Das Repository speichern.

## Mit Streamlit Community Cloud veröffentlichen

1. https://share.streamlit.io/ öffnen und mit GitHub anmelden.
2. **Create app** auswählen.
3. Repository `tinkercad-3d-guide`, Branch `main` und Datei `app.py` auswählen.
4. **Deploy** anklicken.
5. Nach dem Start die öffentliche `*.streamlit.app`-Adresse öffnen.

## ChatbotGen

Wenn die Website öffentlich erreichbar ist, kann ihre öffentliche HTTPS-Adresse als Quelle in ChatbotGen eingetragen werden.
Danach prüfen wir, ob ChatbotGen die Inhalte der Streamlit-Seite zuverlässig lesen kann.
Falls der Crawler die gerenderte Seite nicht vollständig erfasst, können wir zusätzlich eine öffentliche, crawlerfreundliche Wissensseite oder separate Markdown-/HTML-Dokumentation bereitstellen.

## Inhalte erweitern

Neue Anleitungen als `.md`-Dateien im Ordner `wissen` ablegen. Die App liest diese Dateien automatisch ein.
