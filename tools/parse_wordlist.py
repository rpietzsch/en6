"""Wandelt die Wortliste (PDF) in data/words.json um.

Aufruf: python3 tools/parse_wordlist.py <wortliste.pdf>
Die ukrainische Spalte wird bewusst ignoriert. Benötigt `pdftotext` (poppler).
"""
import json, re, subprocess, sys, pathlib

pdf = sys.argv[1]
txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
lines = [l for l in txt.split("\n") if l.strip() and not l.startswith("©") and not l.startswith("Englisch ") and not l.startswith("\f")]
lines = [l.lstrip("\f") for l in lines]

# Einträge, die in der Layout-Ausgabe über zwei Zeilen laufen, zusammenführen
merged = []
for l in lines:
    s = l.strip()
    if "[" not in l and re.match(r"^\S", l) and merged is not None:
        merged.append(l.rstrip()); continue            # Englisch-Teil (steht allein, z. B. "sound: ...")
    if merged and merged[-1] and "[" not in merged[-1] and l.startswith(" ") and "[" in l and "]" in l and not re.match(r"^\s*\[", l) is None:
        merged[-1] = merged[-1] + " " + s; continue    # Fortsetzung "[ . ] Deutsch ..."
    if l.startswith(" " * 40) and "[" not in l and "]" not in l:
        continue                                        # reine Ukrainisch-Fortsetzung
    if l.startswith(" " * 40) and "]" in l and merged and "[" in merged[-1] and "]" not in merged[-1]:
        merged[-1] = merged[-1].rstrip() + " " + s; continue  # takeaway: Deutsch in Folgezeile
    merged.append(l.rstrip())

words, seen = [], set()
rx = re.compile(r"^(.*?)\s+\[ (.*?)\s*\]\s+(.*)$")
for l in merged:
    m = rx.match(l)
    if not m:
        print("übersprungen:", l[:100]); continue
    en, ipa, rest = (x.strip() for x in m.groups())
    de = re.split(r"\s{3,}", rest)[0].strip().lstrip("​")
    ipa = re.split(r"\s{3,}", ipa)[0].replace("], [", " / ")
    ipa = "" if ipa in (".", "") else ipa
    if de == ".": de = ""
    key = (en.lower(), de.lower())
    if key in seen: continue
    seen.add(key)
    ref = re.match(r"^siehe [„“\"”](.+?)[“\"”]$", de)
    w = {"id": len(words), "en": en, "de": de}
    if ipa: w["ipa"] = ipa
    if ref: w["form_of"] = ref.group(1)
    elif not de: w["form_of"] = ""   # Verbform ohne deutsche Angabe (z. B. been, made)
    words.append(w)

out = pathlib.Path(__file__).resolve().parent.parent / "data" / "words.json"
out.write_text(json.dumps(words, ensure_ascii=False, indent=0), encoding="utf8")
print(len(words), "Wörter ->", out)
