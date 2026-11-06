# Idee: Tinkercad-Anleitung als Windows-App in der Taskleiste

## Kurz

Die Anleitung gibt es zusätzlich (oder statt der Streamlit-Seite) als kleine Windows-App. Ihr Icon sitzt fest **direkt neben der Windows-Suche** in der Taskleiste. Ein Klick öffnet über der Taskleiste ein kleines Fenster mit Suchfeld und den Anleitungen.

## Warum

- **Streamlit und Chatbot passen schlecht zusammen.** Streamlit schickt zuerst nur ein leeres JavaScript-Gerüst, der Text kommt danach über eine WebSocket-Verbindung. Ein Crawler wie ChatbotGen sieht deshalb sehr wahrscheinlich keinen Inhalt. Außerdem schlafen Apps in der Streamlit Community Cloud bei Inaktivität ein.
- **Die App bringt die Inhalte selbst mit.** Sie funktioniert ohne Internet, braucht kein Hosting, und die Schülerinnen und Schüler finden sie sofort in der Taskleiste.

## So soll es aussehen

- Das Icon ist angeheftet, als erstes Programm direkt hinter der Suche.
- Ein Klick oder ein Tastenkürzel öffnet ein Fenster unten über der Taskleiste: oben ein Suchfeld, darunter Treffer und Artikel.
- Die Inhalte sind die vorhandenen `wissen/*.md`. Sie werden weiter hier im Repo gepflegt, und die App bringt sie mit.
- Optional später: den ChatbotGen-Bot in der App einbetten (WebView2).

## Technik und Rahmen

- **Direkt in die Taskleiste einbauen geht nicht.** Windows 10 kannte dafür „Deskbands“ (eigene Leisten in der Taskleiste), Windows 11 unterstützt sie nicht mehr. Deshalb wird es ein normales angeheftetes Icon.
- **Anheften per Gruppenrichtlinie:** GPO „Startlayout“ (Administrative Vorlagen › Startmenü und Taskleiste) mit einer Taskleisten-XML, darin `PinListPlacement="Replace"` und unsere App als erster Eintrag. Die Reihenfolge in der XML entspricht der Reihenfolge in der Taskleiste von links nach rechts.
- **Abheften bringt nichts:** Per Richtlinie angeheftete Icons kommen beim nächsten Richtlinien-Update zurück, solange in der XML kein `PinGeneration` gesetzt ist.
- **Zusätzliche GPOs:** „Anheften von Programmen an die Taskleiste nicht zulassen“ (damit niemand eigene Icons davorsetzt) und den Aufgabenansicht-Button ausblenden (sonst steht der zwischen Suche und Icon).
- **Verschieben lässt sich nicht komplett sperren.** Die Position soll deshalb der **Hausmeister** (das HPG-Tool, das schon das Desktop-Layout herstellt) bei der An- oder Abmeldung wiederherstellen. Das geht nur über einen inoffiziellen Weg (Pin-Ordner `User Pinned\TaskBar` plus Registry-Schlüssel `Taskband`) und muss getestet werden. Zurückgesetzt wird nicht alle paar Minuten, weil dafür der Explorer neu starten müsste.
- **Verteilung** als MSI über das HPG-Softwarecenter.

## Offen

- Womit wird die App gebaut? Zum Beispiel C#/.NET wie der Hausmeister.
- Auf einem Test-PC prüfen: Setzt die Richtlinie auch eine per Ziehen geänderte Reihenfolge zurück?
- Name und Icon der App.

Quelle zur Taskleisten-Richtlinie: [Microsoft Learn – Configure the applications pinned to the taskbar](https://learn.microsoft.com/en-us/windows/configuration/taskbar/pinned-apps)
