"""Erzeugt data/verb_examples.json: pro unregelmäßigem Verb ein kurzer Beispielsatz je Form
(Grundform, simple past, past participle) mit deutscher Übersetzung. Zielform in **…**.
Format je Zeile: base|EN1|EN2|EN3|DE1|DE2|DE3"""
import json, pathlib, re
T = """be|Please **be** quiet.|Yesterday I **was** very tired.|I have **been** to London twice.|Sei bitte leise.|Gestern war ich sehr müde.|Ich war schon zweimal in London.
become|Tadpoles **become** frogs.|Tom **became** a doctor.|She has **become** a good singer.|Kaulquappen werden zu Fröschen.|Tom wurde Arzt.|Sie ist eine gute Sängerin geworden.
begin|Lessons **begin** at eight.|The film **began** at six.|It has **begun** to rain.|Der Unterricht beginnt um acht.|Der Film begann um sechs.|Es hat angefangen zu regnen.
bend|Please **bend** your knees.|He **bent** down to tie his shoe.|I have **bent** the wire.|Beuge bitte deine Knie.|Er bückte sich, um seinen Schuh zu binden.|Ich habe den Draht gebogen.
blow|The wind can **blow** hard.|The wind **blew** my hat away.|The wind has **blown** all the leaves down.|Der Wind kann stark wehen.|Der Wind wehte meinen Hut weg.|Der Wind hat alle Blätter heruntergeweht.
break|Don't **break** the glass!|I **broke** my pencil.|Who has **broken** the window?|Zerbrich das Glas nicht!|Ich habe meinen Bleistift zerbrochen.|Wer hat das Fenster kaputt gemacht?
bring|Please **bring** your book.|She **brought** her dog to school.|I have **brought** some cake.|Bring bitte dein Buch mit.|Sie brachte ihren Hund mit in die Schule.|Ich habe Kuchen mitgebracht.
build|We **build** a sandcastle.|Dad **built** a tree house.|They have **built** a new school.|Wir bauen eine Sandburg.|Papa baute ein Baumhaus.|Sie haben eine neue Schule gebaut.
buy|I **buy** bread every day.|Mum **bought** a new bike.|I have **bought** a present.|Ich kaufe jeden Tag Brot.|Mama kaufte ein neues Fahrrad.|Ich habe ein Geschenk gekauft.
catch|Can you **catch** the ball?|He **caught** a big fish.|The cat has **caught** a mouse.|Kannst du den Ball fangen?|Er fing einen großen Fisch.|Die Katze hat eine Maus gefangen.
choose|You can **choose** a book.|I **chose** the red T-shirt.|Have you **chosen** a game?|Du kannst dir ein Buch aussuchen.|Ich wählte das rote T-Shirt.|Hast du ein Spiel ausgesucht?
come|Please **come** to my party.|Lucy **came** home late.|He has **come** by bus.|Komm bitte zu meiner Party.|Lucy kam spät nach Hause.|Er ist mit dem Bus gekommen.
cost|Apples **cost** one euro.|The ticket **cost** five pounds.|That bike has **cost** a lot.|Äpfel kosten einen Euro.|Die Karte kostete fünf Pfund.|Das Fahrrad hat viel gekostet.
cut|I **cut** the bread.|She **cut** her finger.|Dad has **cut** the grass.|Ich schneide das Brot.|Sie schnitt sich in den Finger.|Papa hat den Rasen gemäht.
do|I **do** my homework at four.|Tom **did** his homework.|I have **done** my homework.|Ich mache um vier meine Hausaufgaben.|Tom machte seine Hausaufgaben.|Ich habe meine Hausaufgaben gemacht.
draw|I **draw** a horse.|She **drew** a funny cat.|He has **drawn** a map.|Ich zeichne ein Pferd.|Sie zeichnete eine lustige Katze.|Er hat eine Karte gezeichnet.
drink|I **drink** milk every morning.|He **drank** a glass of water.|We have **drunk** all the juice.|Ich trinke jeden Morgen Milch.|Er trank ein Glas Wasser.|Wir haben den ganzen Saft getrunken.
drive|Dad can **drive** a bus.|We **drove** to the beach.|She has **driven** to town.|Papa kann Bus fahren.|Wir fuhren zum Strand.|Sie ist in die Stadt gefahren.
eat|I **eat** an apple at break.|We **ate** pizza yesterday.|Have you **eaten** yet?|Ich esse in der Pause einen Apfel.|Wir aßen gestern Pizza.|Hast du schon gegessen?
fall|Leaves **fall** in autumn.|Ben **fell** off his bike.|The vase has **fallen** down.|Im Herbst fallen die Blätter.|Ben fiel vom Fahrrad.|Die Vase ist heruntergefallen.
feed|I **feed** the ducks.|She **fed** the rabbit.|We have **fed** the cat.|Ich füttere die Enten.|Sie fütterte das Kaninchen.|Wir haben die Katze gefüttert.
feel|I **feel** happy today.|He **felt** sick yesterday.|I have **felt** cold all day.|Ich fühle mich heute glücklich.|Er fühlte sich gestern krank.|Mir ist den ganzen Tag kalt gewesen.
fight|Don't **fight** with your brother.|The knights **fought** bravely.|They have **fought** again.|Streite dich nicht mit deinem Bruder.|Die Ritter kämpften mutig.|Sie haben sich wieder gestritten.
find|I can't **find** my keys.|She **found** a coin.|Have you **found** your cap?|Ich kann meine Schlüssel nicht finden.|Sie fand eine Münze.|Hast du deine Mütze gefunden?
fly|Birds **fly** south in winter.|We **flew** to Spain.|The plane has **flown** to Rome.|Vögel fliegen im Winter nach Süden.|Wir flogen nach Spanien.|Das Flugzeug ist nach Rom geflogen.
forget|Don't **forget** your key.|I **forgot** my lunch box.|I have **forgotten** her name.|Vergiss deinen Schlüssel nicht.|Ich vergaß meine Brotdose.|Ich habe ihren Namen vergessen.
get|I **get** a letter every week.|Tom **got** a new phone.|She has **got** a cold.|Ich bekomme jede Woche einen Brief.|Tom bekam ein neues Handy.|Sie hat eine Erkältung.
give|I **give** my mum a flower.|He **gave** me a present.|She has **given** me a book.|Ich gebe meiner Mama eine Blume.|Er gab mir ein Geschenk.|Sie hat mir ein Buch gegeben.
go|We **go** to school by bus.|Yesterday we **went** to the zoo.|He has **gone** home.|Wir fahren mit dem Bus zur Schule.|Gestern gingen wir in den Zoo.|Er ist nach Hause gegangen.
hang|I **hang** my coat on the hook.|She **hung** the picture on the wall.|We have **hung** up the flags.|Ich hänge meinen Mantel an den Haken.|Sie hängte das Bild an die Wand.|Wir haben die Fahnen aufgehängt.
have|I **have** a little brother.|We **had** fun at the party.|I have **had** a great day.|Ich habe einen kleinen Bruder.|Wir hatten Spaß auf der Party.|Ich hatte einen tollen Tag.
hear|I can **hear** a bird.|She **heard** a loud noise.|I have **heard** that song before.|Ich höre einen Vogel.|Sie hörte ein lautes Geräusch.|Ich habe das Lied schon einmal gehört.
hide|Let's **hide** behind the tree.|The cat **hid** under the bed.|Who has **hidden** my shoes?|Verstecken wir uns hinter dem Baum.|Die Katze versteckte sich unter dem Bett.|Wer hat meine Schuhe versteckt?
hit|Don't **hit** the ball too hard.|He **hit** the ball over the fence.|I have **hit** my knee.|Schlag den Ball nicht zu hart.|Er schlug den Ball über den Zaun.|Ich habe mir das Knie angeschlagen.
hold|Please **hold** my bag.|She **held** the baby carefully.|I have **held** a snake.|Halte bitte meine Tasche.|Sie hielt das Baby vorsichtig.|Ich habe schon eine Schlange gehalten.
hurt|Does it **hurt**?|I **hurt** my foot yesterday.|I have **hurt** my arm.|Tut es weh?|Ich habe mir gestern den Fuß verletzt.|Ich habe mir den Arm verletzt.
keep|I **keep** my money in a box.|She **kept** the secret.|We have **kept** all the letters.|Ich bewahre mein Geld in einer Schachtel auf.|Sie behielt das Geheimnis für sich.|Wir haben alle Briefe aufbewahrt.
know|I **know** the answer.|He **knew** the way.|I have **known** her for years.|Ich kenne die Antwort.|Er kannte den Weg.|Ich kenne sie schon seit Jahren.
lead|This path will **lead** you to the lake.|She **led** us through the forest.|The guide has **led** many tours.|Dieser Weg führt dich zum See.|Sie führte uns durch den Wald.|Der Führer hat viele Touren geleitet.
leave|We **leave** at seven.|The bus **left** early.|She has **left** her bag at home.|Wir fahren um sieben ab.|Der Bus fuhr früh ab.|Sie hat ihre Tasche zu Hause gelassen.
let|Please **let** me help.|Mum **let** us play outside.|She has **let** the dog in.|Lass mich bitte helfen.|Mama ließ uns draußen spielen.|Sie hat den Hund hereingelassen.
lie|The cat likes to **lie** in the sun.|He **lay** on the sofa all day.|The book has **lain** there for weeks.|Die Katze liegt gern in der Sonne.|Er lag den ganzen Tag auf dem Sofa.|Das Buch hat wochenlang dort gelegen.
light|We **light** a candle.|Dad **lit** the fire.|She has **lit** all the candles.|Wir zünden eine Kerze an.|Papa zündete das Feuer an.|Sie hat alle Kerzen angezündet.
lose|Don't **lose** your key.|I **lost** my phone.|He has **lost** his cap.|Verlier deinen Schlüssel nicht.|Ich verlor mein Handy.|Er hat seine Mütze verloren.
make|I **make** a cake for Mum.|We **made** a snowman.|She has **made** a card.|Ich backe einen Kuchen für Mama.|Wir bauten einen Schneemann.|Sie hat eine Karte gebastelt.
mean|What does this word **mean**?|I **meant** the other book.|I have never **meant** to hurt you.|Was bedeutet dieses Wort?|Ich meinte das andere Buch.|Ich wollte dir nie wehtun.
meet|We **meet** after school.|I **met** Anna in town.|Have you **met** my cousin?|Wir treffen uns nach der Schule.|Ich traf Anna in der Stadt.|Hast du meinen Cousin schon kennengelernt?
pay|I **pay** for the ice cream.|Dad **paid** the bill.|Have you **paid** yet?|Ich bezahle das Eis.|Papa bezahlte die Rechnung.|Hast du schon bezahlt?
put|I **put** my bag on the chair.|She **put** the book on the shelf.|Who has **put** this here?|Ich stelle meine Tasche auf den Stuhl.|Sie stellte das Buch ins Regal.|Wer hat das hierhin gelegt?
read|I **read** a book every week.|Yesterday I **read** a funny story.|I have **read** this book twice.|Ich lese jede Woche ein Buch.|Gestern las ich eine lustige Geschichte.|Ich habe dieses Buch zweimal gelesen.
ride|I **ride** my bike to school.|She **rode** a horse.|Have you ever **ridden** a pony?|Ich fahre mit dem Rad zur Schule.|Sie ritt auf einem Pferd.|Bist du schon einmal auf einem Pony geritten?
ring|The bell will **ring** soon.|The phone **rang** twice.|The bell has **rung**.|Die Glocke läutet gleich.|Das Telefon klingelte zweimal.|Es hat geklingelt.
run|I **run** to the bus stop.|He **ran** very fast.|She has **run** a mile.|Ich renne zur Bushaltestelle.|Er rannte sehr schnell.|Sie ist eine Meile gelaufen.
say|Please **say** hello.|He **said** nothing.|She has **said** sorry.|Sag bitte Hallo.|Er sagte nichts.|Sie hat sich entschuldigt.
see|I can **see** a bird.|We **saw** a film.|Have you **seen** my cap?|Ich sehe einen Vogel.|Wir sahen einen Film.|Hast du meine Mütze gesehen?
sell|They **sell** fresh bread.|He **sold** his old bike.|We have **sold** all the cakes.|Sie verkaufen frisches Brot.|Er verkaufte sein altes Fahrrad.|Wir haben alle Kuchen verkauft.
send|I **send** a text to Tom.|She **sent** me a postcard.|I have **sent** the email.|Ich schicke Tom eine Nachricht.|Sie schickte mir eine Postkarte.|Ich habe die E-Mail geschickt.
shine|The sun can **shine** all day.|The moon **shone** last night.|The sun has **shone** all week.|Die Sonne kann den ganzen Tag scheinen.|Der Mond schien letzte Nacht.|Die Sonne hat die ganze Woche geschienen.
sing|I **sing** in the choir.|She **sang** a song.|They have **sung** it before.|Ich singe im Chor.|Sie sang ein Lied.|Sie haben es schon einmal gesungen.
sit|Please **sit** down.|He **sat** next to me.|We have **sat** here for an hour.|Setz dich bitte hin.|Er saß neben mir.|Wir sitzen schon eine Stunde hier.
sleep|I **sleep** for nine hours.|The baby **slept** all night.|I have not **slept** well.|Ich schlafe neun Stunden.|Das Baby schlief die ganze Nacht.|Ich habe nicht gut geschlafen.
speak|Can you **speak** French?|She **spoke** very quietly.|He has **spoken** to the teacher.|Sprichst du Französisch?|Sie sprach sehr leise.|Er hat mit dem Lehrer gesprochen.
spend|I **spend** my money on comics.|We **spent** a week at the sea.|She has **spent** all her money.|Ich gebe mein Geld für Comics aus.|Wir verbrachten eine Woche am Meer.|Sie hat ihr ganzes Geld ausgegeben.
stand|Please **stand** up.|He **stood** at the door.|We have **stood** in line for ages.|Steh bitte auf.|Er stand an der Tür.|Wir stehen schon ewig in der Schlange.
swim|I can **swim** very well.|We **swam** in the lake.|She has **swum** 20 lengths.|Ich kann sehr gut schwimmen.|Wir schwammen im See.|Sie ist 20 Bahnen geschwommen.
swing|The monkey can **swing** from tree to tree.|The monkey **swung** from branch to branch.|The children have **swung** all afternoon.|Der Affe kann von Baum zu Baum schwingen.|Der Affe schwang von Ast zu Ast.|Die Kinder haben den ganzen Nachmittag geschaukelt.
take|I **take** the bus to school.|She **took** a photo.|Who has **taken** my pen?|Ich nehme den Bus zur Schule.|Sie machte ein Foto.|Wer hat meinen Stift genommen?
teach|Mr Brown will **teach** us maths.|He **taught** us a song.|She has **taught** English for ten years.|Herr Brown unterrichtet uns in Mathe.|Er brachte uns ein Lied bei.|Sie unterrichtet seit zehn Jahren Englisch.
tear|Don't **tear** the page.|I **tore** my jeans.|The dog has **torn** the paper.|Reiß die Seite nicht ab.|Ich zerriss meine Jeans.|Der Hund hat das Papier zerrissen.
tell|I **tell** my mum everything.|He **told** me a joke.|I have **told** her the news.|Ich erzähle meiner Mama alles.|Er erzählte mir einen Witz.|Ich habe ihr die Neuigkeit erzählt.
think|I **think** it's a good idea.|She **thought** about it.|I have **thought** about it.|Ich finde, das ist eine gute Idee.|Sie dachte darüber nach.|Ich habe darüber nachgedacht.
throw|Can you **throw** the ball?|He **threw** it over the wall.|She has **thrown** the stone.|Kannst du den Ball werfen?|Er warf ihn über die Mauer.|Sie hat den Stein geworfen.
understand|I **understand** the question.|He **understood** the joke.|I have never **understood** this rule.|Ich verstehe die Frage.|Er verstand den Witz.|Ich habe diese Regel nie verstanden.
wake|I **wake** up at seven.|She **woke** up late.|I have **woken** the baby.|Ich wache um sieben auf.|Sie wachte spät auf.|Ich habe das Baby geweckt.
wear|I **wear** a uniform at school.|She **wore** a red dress.|He has **worn** these shoes for a year.|Ich trage in der Schule eine Uniform.|Sie trug ein rotes Kleid.|Er trägt diese Schuhe seit einem Jahr.
win|I want to **win** the game.|Our team **won** the match.|We have **won** a prize.|Ich will das Spiel gewinnen.|Unser Team gewann das Spiel.|Wir haben einen Preis gewonnen.
write|I **write** a letter to Gran.|He **wrote** a short story.|She has **written** a card.|Ich schreibe Oma einen Brief.|Er schrieb eine Kurzgeschichte.|Sie hat eine Karte geschrieben."""
verbs = {v["base"]: v for v in json.load(open(pathlib.Path(__file__).resolve().parent.parent / "data" / "verbs.json", encoding="utf8"))}
out = {}
for line in T.strip().split("\n"):
    b, e1, e2, e3, d1, d2, d3 = line.split("|")
    v = verbs[b]
    # Prüfung: die richtige Form steht fett im jeweiligen Satz
    for sent, form in ((e1, b), (e2, v["past"]), (e3, v["pp"])):
        bold = re.search(r"\*\*(.+?)\*\*", sent).group(1).lower()
        assert bold in [x.lower() for x in form.split("/")], (b, sent, form)
    out[b] = [[e1, d1], [e2, d2], [e3, d3]]
assert set(out) == set(verbs), set(verbs) ^ set(out)
(pathlib.Path(__file__).resolve().parent.parent / "data" / "verb_examples.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf8")
print(len(out), "Verben mit je 3 Sätzen")
