"""Erzeugt data/verbs.json (unregelmäßige Verben aus Access 1/2): Grundform, Übersetzung, Simple past, Past participle.
Die Verbliste ergibt sich aus den Verbformen der Wortlisten (siehe „…“-Einträge) und den Access-1-Vergangenheitsformen.
Mehrere Varianten stehen mit „/“ (z. B. was/were)."""
import json, pathlib
V = """be|sein|was/were|been
become|werden|became|become
begin|beginnen, anfangen|began|begun
bend|biegen; sich bücken|bent|bent
blow|wehen; blasen|blew|blown
break|brechen; kaputt machen|broke|broken
bring|bringen|brought|brought
build|bauen|built|built
buy|kaufen|bought|bought
catch|fangen|caught|caught
choose|wählen, aussuchen|chose|chosen
come|kommen|came|come
cost|kosten|cost|cost
cut|schneiden|cut|cut
do|tun, machen|did|done
draw|zeichnen; ziehen|drew|drawn
drink|trinken|drank|drunk
drive|fahren (Auto)|drove|driven
eat|essen|ate|eaten
fall|fallen|fell|fallen
feed|füttern|fed|fed
feel|fühlen, sich anfühlen|felt|felt
fight|kämpfen|fought|fought
find|finden|found|found
fly|fliegen|flew|flown
forget|vergessen|forgot|forgotten
get|bekommen; holen; werden|got|got
give|geben|gave|given
go|gehen; fahren|went|gone/been
hang|hängen|hung|hung
have|haben|had|had
hear|hören|heard|heard
hide|verstecken|hid|hidden
hit|schlagen; treffen|hit|hit
hold|halten|held|held
hurt|verletzen; wehtun|hurt|hurt
keep|behalten; halten|kept|kept
know|wissen; kennen|knew|known
lead|führen|led|led
leave|verlassen; weggehen|left|left
let|lassen; erlauben|let|let
lie|liegen|lay|lain
light|anzünden; beleuchten|lit|lit
lose|verlieren|lost|lost
make|machen; herstellen|made|made
mean|bedeuten; meinen|meant|meant
meet|treffen|met|met
pay|bezahlen|paid|paid
put|legen, stellen, setzen|put|put
read|lesen|read|read
ride|reiten; (Rad) fahren|rode|ridden
ring|klingeln; anrufen|rang|rung
run|rennen, laufen|ran|run
say|sagen|said|said
see|sehen|saw|seen
sell|verkaufen|sold|sold
send|schicken|sent|sent
shine|scheinen; leuchten|shone|shone
sing|singen|sang|sung
sit|sitzen|sat|sat
sleep|schlafen|slept|slept
speak|sprechen|spoke|spoken
spend|ausgeben; verbringen|spent|spent
stand|stehen|stood|stood
swim|schwimmen|swam|swum
swing|schaukeln; schwingen|swung|swung
take|nehmen; brauchen; dauern|took|taken
teach|unterrichten, lehren|taught|taught
tear|zerreißen|tore|torn
tell|erzählen; sagen|told|told
think|denken; glauben|thought|thought
throw|werfen|threw|thrown
understand|verstehen|understood|understood
wake|aufwachen; wecken|woke|woken
wear|tragen (Kleidung)|wore|worn
win|gewinnen|won|won
write|schreiben|wrote|written"""
rows = []
for line in V.strip().split("\n"):
    b, de, p, pp = line.split("|")
    rows.append({"base": b, "de": de, "past": p, "pp": pp})
out = pathlib.Path(__file__).resolve().parent.parent / "data" / "verbs.json"
out.write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")), encoding="utf8")
print(len(rows), "Verben ->", out)
