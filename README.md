# Vokabel-Trainer – Access 2 (Klasse 6)

Kleine Web-App zum Vokabellernen (nur Browser, kein Server, kein Login). Fortschritt wird im Browser (`localStorage`) gespeichert.

## Lernmethode
- **Abrufen statt Lesen:** Jede Karte fragt aktiv ab (eintippen oder laut sagen + selbst bewerten), beide Richtungen.
- **Verteiltes Wiederholen:** Boxen mit 1 → 3 → 7 → 14 → 30 Tagen; Fehler springen auf Box 0 (morgen wieder).
- **Kleine Portionen:** Standard 10 neue Wörter/Tag, erst Wiederholung, dann neue Wörter.
- **Tagesrunde (~15 Min.):** fällige Wörter → neue Wörter lernen und abfragen → gemischte Abfrage → 2–3 eigene Sätze.
- **Problemwörter:** oft falsche Wörter (oder per ⭐ markierte) werden extra geübt.
- **Hören, Sprechen, Schreiben:** Aussprache per Sprachausgabe des Geräts (🔊; iPhone: Stumm-Schalter aus), Modus „Hören & Schreiben“, Antwort tippen oder laut sagen und selbst bewerten.

## Daten
`data/words.json` wurde aus einer Wortliste (PDF) abgeleitet – ukrainische Spalte ist ausgelassen:

    python3 tools/parse_wordlist.py <Wortliste.pdf>

Die Unit-Zuordnung steht nicht in der Wortliste. In der App unter ⚙️ → „Units zuordnen“ können Wörter einer Unit eingefügt werden, danach lässt sich der Lernbereich auf eine Unit beschränken.

### Access 1 festigen
`data/words_a1.json` enthält 526 Wörter aus den Lösungen der Access-1-Vocabulary-Action-Sheets (Klasse 5, Ausgabe 2014), mit Unit (`HWG 1/2`, `1.1` … `5.2`). Die VAS enthalten nur Englisch; die deutschen Übersetzungen (`tools/a1_translations.py`) sind ergänzt und sollten stichprobenartig geprüft werden. Wörter, die schon in der Access-2-Liste stehen, sind dort nicht doppelt.


## PWA
Die Seite ist installierbar (`manifest.webmanifest`, Icons in `icons/`) und läuft nach dem ersten Laden offline (`sw.js`). iPhone/iPad: in Safari teilen → „Zum Home-Bildschirm“. Bei inhaltlichen Änderungen die Version `CACHE` in `sw.js` erhöhen.

## Veröffentlichen (GitHub Pages)
Settings → Pages → Source: *Deploy from a branch* → `main` / `/ (root)`.


## Beispielsätze
`data/examples.json` enthält zu jedem Wort einen kurzen englischen Satz mit deutscher Übersetzung (Zielwort in `**…**`), die auf den neuen Lernkarten angezeigt werden. Die Sätze sind maschinell erstellt und stichprobenartig geprüft.

## Unregelmäßige Verben
`data/verbs.json` (`tools/build_verbs.py`) enthält 77 unregelmäßige Verben aus Access 1/2, `data/verb_examples.json` (`tools/build_verb_examples.py`) je einen Beispielsatz pro Form mit deutscher Übersetzung. In der App gibt es pro Verb eine **Lernkarte** (Übersetzung, drei Formen, je ein Satz) und eine **Testkarte** (1–3 Lücken aus Übersetzung, Grundform, 2. und 3. Form). Drei Modi: **Lernen** (nur Lernkarten), **Mix** (zufällig gemischt, Testkarte immer erst nach der Lernkarte), **Test** (nur Testkarten). Wiederholung nach dem 1-3-7-14-30-Tage-Plan, Fehler kommen in derselben Runde nochmal; Filter nach Mustern (alle gleich / 1.=3. / 2.=3. / alle verschieden).
