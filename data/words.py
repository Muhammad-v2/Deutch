# -*- coding: utf-8 -*-
# База слов для изучения немецкого. Формат: de, ru, level, category, pos
# pos: n (сущ), v (глагол), adj (прилагательное), adv (наречие), other

def W(de, ru, level, cat, pos="other"):
    return {"de": de, "ru": ru, "level": level, "category": cat, "pos": pos}


WORDS = []

# ---------- ZAHLEN ----------
zahlen = [
    ("null", "ноль"), ("eins", "один"), ("zwei", "два"), ("drei", "три"), ("vier", "четыре"),
    ("fünf", "пять"), ("sechs", "шесть"), ("sieben", "семь"), ("acht", "восемь"), ("neun", "девять"),
    ("zehn", "десять"), ("elf", "одиннадцать"), ("zwölf", "двенадцать"), ("zwanzig", "двадцать"),
    ("dreißig", "тридцать"), ("vierzig", "сорок"), ("fünfzig", "пятьдесят"), ("hundert", "сто"),
    ("tausend", "тысяча"), ("Million", "миллион"), ("erste", "первый"), ("letzte", "последний"),
]
WORDS += [W(de, ru, "A1", "Zahlen", "n") for de, ru in zahlen]

# ---------- PRONOMEN ----------
pron = [
    ("ich", "я"), ("du", "ты"), ("er", "он"), ("sie", "она"), ("es", "оно"), ("wir", "мы"),
    ("ihr", "вы (неформ.)"), ("Sie", "Вы (вежл.)"), ("mein", "мой"), ("dein", "твой"),
    ("unser", "наш"), ("jemand", "кто-то"), ("niemand", "никто"), ("etwas", "что-то"), ("nichts", "ничто"),
    ("alle", "все"), ("jeder", "каждый"), ("man", "некто/люди (безлич.)"),
]
WORDS += [W(de, ru, "A1", "Pronomen", "other") for de, ru in pron]

# ---------- FAMILIE ----------
familie = [
    ("die Familie", "семья"), ("die Mutter", "мама"), ("der Vater", "папа"), ("das Kind", "ребёнок"),
    ("der Sohn", "сын"), ("die Tochter", "дочь"), ("der Bruder", "брат"), ("die Schwester", "сестра"),
    ("die Großmutter", "бабушка"), ("der Großvater", "дедушка"), ("die Eltern", "родители"),
    ("der Mann", "мужчина/муж"), ("die Frau", "женщина/жена"), ("der Freund", "друг"),
    ("die Freundin", "подруга"), ("die Ehe", "брак"), ("der Enkel", "внук"), ("die Tante", "тётя"),
    ("der Onkel", "дядя"), ("der Cousin", "кузен"),
]
WORDS += [W(de, ru, "A1", "Familie", "n") for de, ru in familie]

# ---------- ESSEN UND TRINKEN ----------
essen = [
    ("das Brot", "хлеб"), ("das Wasser", "вода"), ("die Milch", "молоко"), ("der Kaffee", "кофе"),
    ("der Tee", "чай"), ("der Saft", "сок"), ("das Bier", "пиво"), ("der Wein", "вино"),
    ("das Obst", "фрукты"), ("das Gemüse", "овощи"), ("der Apfel", "яблоко"), ("die Banane", "банан"),
    ("die Kartoffel", "картофель"), ("die Tomate", "помидор"), ("das Fleisch", "мясо"),
    ("der Fisch", "рыба"), ("der Käse", "сыр"), ("das Ei", "яйцо"), ("der Zucker", "сахар"),
    ("das Salz", "соль"), ("die Suppe", "суп"), ("der Kuchen", "торт/пирог"), ("das Frühstück", "завтрак"),
    ("das Mittagessen", "обед"), ("das Abendessen", "ужин"), ("der Reis", "рис"), ("die Nudeln", "макароны"),
    ("das Restaurant", "ресторан"), ("die Rechnung", "счёт"), ("die Speisekarte", "меню"),
    ("süß", "сладкий"), ("sauer", "кислый"), ("scharf", "острый"), ("lecker", "вкусный"),
    ("satt", "сытый"), ("hungrig", "голодный"), ("durstig", "испытывающий жажду"),
]
WORDS += [W(de, ru, "A1", "Essen und Trinken", "n") for de, ru in essen]

# ---------- HAUS UND WOHNUNG ----------
haus = [
    ("das Haus", "дом"), ("die Wohnung", "квартира"), ("das Zimmer", "комната"), ("die Küche", "кухня"),
    ("das Bad", "ванная"), ("das Schlafzimmer", "спальня"), ("das Wohnzimmer", "гостиная"),
    ("der Tisch", "стол"), ("der Stuhl", "стул"), ("das Bett", "кровать"), ("der Schrank", "шкаф"),
    ("das Fenster", "окно"), ("die Tür", "дверь"), ("der Boden", "пол"), ("die Wand", "стена"),
    ("das Dach", "крыша"), ("der Garten", "сад"), ("der Schlüssel", "ключ"), ("die Miete", "аренда"),
    ("der Nachbar", "сосед"), ("die Lampe", "лампа"), ("der Spiegel", "зеркало"), ("die Dusche", "душ"),
]
WORDS += [W(de, ru, "A1", "Haus und Wohnung", "n") for de, ru in haus]

# ---------- KLEIDUNG ----------
kleidung = [
    ("die Kleidung", "одежда"), ("das Hemd", "рубашка"), ("die Hose", "брюки"), ("das Kleid", "платье"),
    ("der Rock", "юбка"), ("die Jacke", "куртка"), ("der Mantel", "пальто"), ("die Schuhe", "обувь"),
    ("die Mütze", "шапка"), ("der Hut", "шляпа"), ("der Gürtel", "ремень"), ("die Socke", "носок"),
    ("die Tasche", "сумка"), ("die Brille", "очки"), ("der Ring", "кольцо"), ("die Uhr", "часы"),
]
WORDS += [W(de, ru, "A1", "Kleidung", "n") for de, ru in kleidung]

# ---------- KÖRPER ----------
koerper = [
    ("der Kopf", "голова"), ("das Auge", "глаз"), ("die Nase", "нос"), ("der Mund", "рот"),
    ("das Ohr", "ухо"), ("die Hand", "рука (кисть)"), ("der Arm", "рука"), ("das Bein", "нога"),
    ("der Fuß", "стопа"), ("der Rücken", "спина"), ("der Bauch", "живот"), ("das Herz", "сердце"),
    ("die Haut", "кожа"), ("das Haar", "волосы"), ("der Finger", "палец"), ("der Zahn", "зуб"),
]
WORDS += [W(de, ru, "A1", "Körper", "n") for de, ru in koerper]

# ---------- FARBEN ----------
farben = [
    ("rot", "красный"), ("blau", "синий"), ("grün", "зелёный"), ("gelb", "жёлтый"),
    ("schwarz", "чёрный"), ("weiß", "белый"), ("grau", "серый"), ("braun", "коричневый"),
    ("orange", "оранжевый"), ("rosa", "розовый"), ("lila", "фиолетовый"),
]
WORDS += [W(de, ru, "A1", "Farben", "adj") for de, ru in farben]

# ---------- ZEIT ----------
zeit = [
    ("die Zeit", "время"), ("der Tag", "день"), ("die Woche", "неделя"), ("der Monat", "месяц"),
    ("das Jahr", "год"), ("die Stunde", "час"), ("die Minute", "минута"), ("heute", "сегодня"),
    ("morgen", "завтра"), ("gestern", "вчера"), ("jetzt", "сейчас"), ("früh", "рано"), ("spät", "поздно"),
    ("Montag", "понедельник"), ("Dienstag", "вторник"), ("Mittwoch", "среда"), ("Donnerstag", "четверг"),
    ("Freitag", "пятница"), ("Samstag", "суббота"), ("Sonntag", "воскресенье"), ("der Frühling", "весна"),
    ("der Sommer", "лето"), ("der Herbst", "осень"), ("der Winter", "зима"), ("die Uhrzeit", "время (часы)"),
    ("das Wochenende", "выходные"), ("der Feiertag", "праздник"), ("die Vergangenheit", "прошлое"),
    ("die Zukunft", "будущее"), ("die Gegenwart", "настоящее"),
]
WORDS += [W(de, ru, "A1", "Zeit", "n") for de, ru in zeit]

# ---------- WETTER / NATUR ----------
wetter = [
    ("das Wetter", "погода"), ("die Sonne", "солнце"), ("der Regen", "дождь"), ("der Schnee", "снег"),
    ("der Wind", "ветер"), ("die Wolke", "облако"), ("warm", "тёплый"), ("kalt", "холодный"),
    ("heiß", "жаркий"), ("das Gewitter", "гроза"), ("der Himmel", "небо"), ("der Nebel", "туман"),
]
WORDS += [W(de, ru, "A1", "Wetter", "n") for de, ru in wetter]

natur = [
    ("der Baum", "дерево"), ("der Wald", "лес"), ("die Blume", "цветок"), ("das Gras", "трава"),
    ("der Berg", "гора"), ("das Meer", "море"), ("der Fluss", "река"), ("der See", "озеро"),
    ("die Insel", "остров"), ("der Strand", "пляж"), ("die Umwelt", "окружающая среда"),
    ("die Landschaft", "пейзаж"), ("die Erde", "земля"), ("die Luft", "воздух"), ("die Pflanze", "растение"),
]
WORDS += [W(de, ru, "A2", "Natur", "n") for de, ru in natur]

# ---------- TIERE ----------
tiere = [
    ("der Hund", "собака"), ("die Katze", "кошка"), ("der Vogel", "птица"), ("das Pferd", "лошадь"),
    ("die Kuh", "корова"), ("das Schwein", "свинья"), ("der Löwe", "лев"), ("der Bär", "медведь"),
    ("der Fuchs", "лиса"), ("die Maus", "мышь"), ("das Kaninchen", "кролик"), ("der Elefant", "слон"),
]
WORDS += [W(de, ru, "A1", "Tiere", "n") for de, ru in tiere]

# ---------- STADT UND VERKEHR ----------
stadt = [
    ("die Stadt", "город"), ("die Straße", "улица"), ("der Platz", "площадь"), ("der Bahnhof", "вокзал"),
    ("der Flughafen", "аэропорт"), ("das Auto", "машина"), ("der Bus", "автобус"), ("die Bahn", "поезд/жд"),
    ("das Fahrrad", "велосипед"), ("das Taxi", "такси"), ("die Ampel", "светофор"), ("die Brücke", "мост"),
    ("die Kreuzung", "перекрёсток"), ("der Verkehr", "движение/трафик"), ("der Parkplatz", "парковка"),
    ("das Ticket", "билет"), ("die Haltestelle", "остановка"), ("die U-Bahn", "метро"),
    ("der Führerschein", "водительские права"), ("der Stau", "пробка"),
]
WORDS += [W(de, ru, "A2", "Stadt und Verkehr", "n") for de, ru in stadt]

# ---------- REISEN ----------
WORDS += [
    W("die Reise", "путешествие", "A2", "Reisen", "n"),
    W("der Urlaub", "отпуск", "A2", "Reisen", "n"),
    W("das Gepäck", "багаж", "A2", "Reisen", "n"),
    W("der Koffer", "чемодан", "A2", "Reisen", "n"),
    W("der Pass", "паспорт", "A2", "Reisen", "n"),
    W("das Hotel", "отель", "A1", "Reisen", "n"),
    W("die Buchung", "бронирование", "B1", "Reisen", "n"),
    W("der Ausflug", "экскурсия", "A2", "Reisen", "n"),
    W("die Grenze", "граница", "B1", "Reisen", "n"),
    W("das Visum", "виза", "A2", "Reisen", "n"),
    W("die Sehenswürdigkeit", "достопримечательность", "B1", "Reisen", "n"),
    W("der Tourist", "турист", "A1", "Reisen", "n"),
    W("die Ankunft", "прибытие", "B1", "Reisen", "n"),
    W("die Abfahrt", "отправление", "B1", "Reisen", "n"),
    W("verreisen", "уезжать в путешествие", "B1", "Reisen", "v"),
]

# ---------- BERUF UND ARBEIT ----------
beruf = [
    ("die Arbeit", "работа"), ("der Beruf", "профессия"), ("der Chef", "начальник"),
    ("der Kollege", "коллега"), ("das Büro", "офис"), ("das Gehalt", "зарплата"),
    ("die Firma", "фирма/компания"), ("die Besprechung", "совещание"), ("der Termin", "встреча/приём"),
    ("die Bewerbung", "заявление о приёме на работу"), ("das Interview", "собеседование"),
    ("kündigen", "увольнять(ся)", "v"), ("die Erfahrung", "опыт"), ("die Karriere", "карьера"),
    ("der Vertrag", "договор"), ("die Firma leiten", "руководить фирмой"), ("verdienen", "зарабатывать", "v"),
    ("der Arbeitgeber", "работодатель"), ("der Arbeitnehmer", "работник"), ("die Rente", "пенсия"),
]
WORDS += [W(t[0], t[1], "A2", "Beruf und Arbeit", t[2] if len(t) > 2 else "n") for t in beruf]

# ---------- SCHULE UND BILDUNG ----------
schule = [
    ("die Schule", "школа"), ("der Lehrer", "учитель"), ("der Schüler", "ученик"),
    ("die Universität", "университет"), ("das Studium", "учёба (в вузе)"), ("die Prüfung", "экзамен"),
    ("die Note", "оценка"), ("das Buch", "книга"), ("das Heft", "тетрадь"), ("der Stift", "ручка"),
    ("die Hausaufgabe", "домашнее задание"), ("lernen", "учить/учиться", "v"),
    ("unterrichten", "преподавать", "v"), ("die Bildung", "образование"), ("das Wissen", "знание"),
    ("der Kurs", "курс"), ("das Zeugnis", "аттестат"), ("die Klasse", "класс"),
]
WORDS += [W(t[0], t[1], "A2", "Schule und Bildung", t[2] if len(t) > 2 else "n") for t in schule]

# ---------- GESUNDHEIT ----------
gesundheit = [
    ("die Gesundheit", "здоровье"), ("krank", "больной", "adj"), ("gesund", "здоровый", "adj"),
    ("der Arzt", "врач"), ("das Krankenhaus", "больница"), ("die Apotheke", "аптека"),
    ("die Medizin", "лекарство/медицина"), ("der Schmerz", "боль"), ("die Erkältung", "простуда"),
    ("das Fieber", "температура/жар"), ("die Untersuchung", "обследование"), ("sich erholen", "выздоравливать", "v"),
    ("die Versicherung", "страховка"), ("der Termin beim Arzt", "приём у врача"),
    ("die Impfung", "прививка"), ("die Verletzung", "травма"),
]
WORDS += [W(t[0], t[1], "A2", "Gesundheit", t[2] if len(t) > 2 else "n") for t in gesundheit]

# ---------- GEFÜHLE UND CHARAKTER ----------
gefuehle = [
    ("glücklich", "счастливый", "adj"), ("traurig", "грустный", "adj"), ("wütend", "злой", "adj"),
    ("müde", "уставший", "adj"), ("nervös", "нервный", "adj"), ("ruhig", "спокойный", "adj"),
    ("ängstlich", "тревожный/боязливый", "adj"), ("stolz", "гордый", "adj"), ("eifersüchtig", "ревнивый", "adj"),
    ("überrascht", "удивлённый", "adj"), ("die Liebe", "любовь", "n"), ("die Angst", "страх", "n"),
    ("die Freude", "радость", "n"), ("freundlich", "дружелюбный", "adj"), ("ehrlich", "честный", "adj"),
    ("faul", "ленивый", "adj"), ("fleißig", "трудолюбивый", "adj"), ("mutig", "смелый", "adj"),
    ("schüchtern", "застенчивый", "adj"), ("neugierig", "любопытный", "adj"), ("geduldig", "терпеливый", "adj"),
    ("großzügig", "щедрый", "adj"), ("egoistisch", "эгоистичный", "adj"), ("zuverlässig", "надёжный", "adj"),
]
WORDS += [W(t[0], t[1], "A2" if t[2] == "adj" else "A1", "Gefühle und Charakter", t[2]) for t in gefuehle]

# ---------- FREIZEIT UND HOBBYS ----------
freizeit = [
    ("das Hobby", "хобби"), ("das Buch lesen", "читать книгу"), ("das Kino", "кино"),
    ("die Musik", "музыка"), ("der Film", "фильм"), ("das Konzert", "концерт"), ("das Spiel", "игра"),
    ("der Sport", "спорт"), ("schwimmen", "плавать", "v"), ("laufen", "бегать", "v"),
    ("tanzen", "танцевать", "v"), ("singen", "петь", "v"), ("malen", "рисовать", "v"),
    ("fotografieren", "фотографировать", "v"), ("kochen", "готовить", "v"), ("wandern", "ходить в поход", "v"),
    ("die Party", "вечеринка"), ("das Fest", "праздник/фестиваль"), ("die Ausstellung", "выставка"),
    ("das Museum", "музей"), ("das Theater", "театр"),
]
WORDS += [W(t[0], t[1], "A1", "Freizeit und Hobbys", t[2] if len(t) > 2 else "n") for t in freizeit]

# ---------- TECHNOLOGIE ----------
technik = [
    ("der Computer", "компьютер"), ("das Handy", "телефон"), ("das Internet", "интернет"),
    ("die App", "приложение"), ("die E-Mail", "имейл"), ("das Passwort", "пароль"),
    ("herunterladen", "скачивать", "v"), ("hochladen", "загружать", "v"), ("speichern", "сохранять", "v"),
    ("löschen", "удалять", "v"), ("die Software", "программное обеспечение"), ("das Gerät", "устройство"),
    ("die Datei", "файл"), ("das Netzwerk", "сеть"), ("aufladen", "заряжать", "v"),
    ("der Akku", "аккумулятор"), ("die Nachricht", "сообщение"), ("anrufen", "звонить", "v"),
]
WORDS += [W(t[0], t[1], "B1", "Technologie", t[2] if len(t) > 2 else "n") for t in technik]

# ---------- EINKAUFEN ----------
einkaufen = [
    ("das Geschäft", "магазин"), ("der Supermarkt", "супермаркет"), ("das Geld", "деньги"),
    ("der Preis", "цена"), ("billig", "дешёвый", "adj"), ("teuer", "дорогой", "adj"),
    ("kaufen", "покупать", "v"), ("verkaufen", "продавать", "v"), ("bezahlen", "оплачивать", "v"),
    ("die Kasse", "касса"), ("der Rabatt", "скидка"), ("die Quittung", "чек"),
    ("die Kreditkarte", "кредитная карта"), ("bar bezahlen", "платить наличными"),
    ("der Kunde", "клиент"), ("die Größe", "размер"), ("umtauschen", "обменивать", "v"),
]
WORDS += [W(t[0], t[1], "A1", "Einkaufen", t[2] if len(t) > 2 else "n") for t in einkaufen]

# ---------- ALLTAG / HAUSHALT ----------
alltag = [
    ("aufstehen", "вставать", "v"), ("frühstücken", "завтракать", "v"), ("aufräumen", "убираться", "v"),
    ("putzen", "чистить/убирать", "v"), ("waschen", "мыть/стирать", "v"), ("kochen", "готовить", "v"),
    ("einkaufen", "делать покупки", "v"), ("schlafen", "спать", "v"), ("sich duschen", "принимать душ", "v"),
    ("sich anziehen", "одеваться", "v"), ("sich ausruhen", "отдыхать", "v"), ("bügeln", "гладить", "v"),
    ("der Müll", "мусор", "n"), ("die Waschmaschine", "стиральная машина", "n"),
    ("der Staubsauger", "пылесос", "n"), ("die Routine", "рутина", "n"),
]
WORDS += [W(t[0], t[1], "A1", "Alltag", t[2] if len(t) > 2 else "n") for t in alltag]

# ---------- ВЫСОКОЧАСТОТНЫЕ ГЛАГОЛЫ ----------
verben = [
    ("sein", "быть"), ("haben", "иметь"), ("werden", "становиться"), ("können", "мочь"),
    ("müssen", "быть должным"), ("sollen", "быть должным (по чужой воле)"), ("wollen", "хотеть"),
    ("dürfen", "иметь разрешение"), ("mögen", "нравиться"), ("machen", "делать"), ("gehen", "идти"),
    ("kommen", "приходить"), ("sehen", "видеть"), ("wissen", "знать"), ("sagen", "говорить"),
    ("geben", "давать"), ("nehmen", "брать"), ("finden", "находить"), ("denken", "думать"),
    ("glauben", "верить/думать"), ("bleiben", "оставаться"), ("stehen", "стоять"), ("liegen", "лежать"),
    ("sitzen", "сидеть"), ("bringen", "приносить"), ("fahren", "ехать"), ("arbeiten", "работать"),
    ("spielen", "играть"), ("brauchen", "нуждаться"), ("fragen", "спрашивать"), ("antworten", "отвечать"),
    ("verstehen", "понимать"), ("erklären", "объяснять"), ("zeigen", "показывать"), ("beginnen", "начинать"),
    ("beenden", "заканчивать"), ("versuchen", "пытаться"), ("helfen", "помогать"), ("lieben", "любить"),
    ("hassen", "ненавидеть"), ("hoffen", "надеяться"), ("warten", "ждать"), ("suchen", "искать"),
    ("öffnen", "открывать"), ("schließen", "закрывать"), ("beginnen", "начинать"), ("gewinnen", "выигрывать"),
    ("verlieren", "проигрывать/терять"), ("entscheiden", "решать"), ("erinnern", "напоминать"),
    ("vergessen", "забывать"), ("passieren", "происходить"), ("erzählen", "рассказывать"),
    ("treffen", "встречать"), ("besuchen", "посещать"), ("kennen", "знать (кого-то)"),
    ("lernen", "учить(ся)"), ("lehren", "обучать"), ("schreiben", "писать"), ("lesen", "читать"),
    ("hören", "слышать"), ("sprechen", "говорить"), ("essen", "есть"), ("trinken", "пить"),
    ("kaufen", "покупать"), ("bezahlen", "платить"), ("reisen", "путешествовать"), ("fliegen", "летать"),
    ("ankommen", "прибывать"), ("abfahren", "отправляться"), ("wohnen", "жить (проживать)"),
    ("leben", "жить"), ("sterben", "умирать"), ("wachsen", "расти"), ("bauen", "строить"),
    ("zerstören", "разрушать"), ("reparieren", "чинить"), ("ändern", "менять"), ("bleiben", "оставаться"),
    ("erlauben", "разрешать"), ("verbieten", "запрещать"), ("empfehlen", "рекомендовать"),
    ("planen", "планировать"), ("organisieren", "организовывать"), ("entwickeln", "развивать"),
    ("benutzen", "использовать"), ("vergleichen", "сравнивать"), ("beschreiben", "описывать"),
    ("bemerken", "замечать"), ("interessieren", "интересовать"), ("überraschen", "удивлять"),
    ("beeindrucken", "впечатлять"), ("enttäuschen", "разочаровывать"), ("sich freuen", "радоваться"),
    ("sich beeilen", "торопиться"), ("sich entspannen", "расслабляться"), ("sich beschweren", "жаловаться"),
    ("sich entschuldigen", "извиняться"), ("gratulieren", "поздравлять"), ("danken", "благодарить"),
]
WORDS += [W(de, ru, "A2", "Verben", "v") for de, ru in verben]

# ---------- ПРИЛАГАТЕЛЬНЫЕ ----------
adjektive = [
    ("groß", "большой"), ("klein", "маленький"), ("neu", "новый"), ("alt", "старый"),
    ("gut", "хороший"), ("schlecht", "плохой"), ("schön", "красивый"), ("hässlich", "некрасивый"),
    ("schnell", "быстрый"), ("langsam", "медленный"), ("stark", "сильный"), ("schwach", "слабый"),
    ("leicht", "лёгкий"), ("schwer", "тяжёлый/трудный"), ("einfach", "простой"), ("schwierig", "сложный"),
    ("wichtig", "важный"), ("interessant", "интересный"), ("langweilig", "скучный"), ("lustig", "весёлый"),
    ("ernst", "серьёзный"), ("modern", "современный"), ("traditionell", "традиционный"),
    ("sauber", "чистый"), ("schmutzig", "грязный"), ("voll", "полный"), ("leer", "пустой"),
    ("laut", "громкий"), ("leise", "тихий"), ("nah", "близкий"), ("weit", "далёкий"),
    ("hell", "светлый"), ("dunkel", "тёмный"), ("frisch", "свежий"), ("gesund", "здоровый"),
    ("bequem", "удобный"), ("unbequem", "неудобный"), ("sicher", "безопасный"), ("gefährlich", "опасный"),
    ("frei", "свободный"), ("beschäftigt", "занятый"), ("reich", "богатый"), ("arm", "бедный"),
    ("richtig", "правильный"), ("falsch", "неправильный"), ("notwendig", "необходимый"),
    ("möglich", "возможный"), ("unmöglich", "невозможный"), ("typisch", "типичный"),
]
WORDS += [W(de, ru, "A1", "Adjektive", "adj") for de, ru in adjektive]

# ---------- ФУНКЦИОНАЛЬНЫЕ СЛОВА / ПРЕДЛОГИ / СОЮЗЫ ----------
funktion = [
    ("und", "и"), ("oder", "или"), ("aber", "но"), ("weil", "потому что"), ("dass", "что (союз)"),
    ("wenn", "если/когда"), ("obwohl", "хотя"), ("deshalb", "поэтому"), ("trotzdem", "несмотря на это"),
    ("also", "итак/значит"), ("außerdem", "кроме того"), ("in", "в"), ("auf", "на"), ("unter", "под"),
    ("über", "над/о"), ("neben", "рядом с"), ("zwischen", "между"), ("vor", "перед"), ("hinter", "за"),
    ("durch", "через"), ("für", "для"), ("mit", "с"), ("ohne", "без"), ("gegen", "против"),
    ("seit", "с (какого-то времени)"), ("bis", "до"), ("während", "во время"), ("wegen", "из-за"),
    ("außer", "кроме"), ("nach", "после/в направлении"), ("vor allem", "прежде всего"),
]
WORDS += [W(de, ru, "A2", "Grammatik-Wörter", "other") for de, ru in funktion]

# ---------- АБСТРАКТНЫЕ ПОНЯТИЯ B1-B2 ----------
abstrakt = [
    ("die Meinung", "мнение"), ("die Entscheidung", "решение"), ("die Möglichkeit", "возможность"),
    ("die Erfahrung", "опыт"), ("die Verantwortung", "ответственность"), ("die Beziehung", "отношения"),
    ("die Gesellschaft", "общество"), ("die Kultur", "культура"), ("die Wirtschaft", "экономика"),
    ("die Politik", "политика"), ("die Regierung", "правительство"), ("das Gesetz", "закон"),
    ("die Freiheit", "свобода"), ("die Gerechtigkeit", "справедливость"), ("die Gleichheit", "равенство"),
    ("der Fortschritt", "прогресс"), ("die Herausforderung", "вызов/сложность"), ("das Ziel", "цель"),
    ("der Erfolg", "успех"), ("das Risiko", "риск"), ("der Vorteil", "преимущество"),
    ("der Nachteil", "недостаток"), ("die Ursache", "причина"), ("die Folge", "следствие"),
    ("die Bedeutung", "значение"), ("der Unterschied", "различие"), ("die Ähnlichkeit", "сходство"),
    ("die Entwicklung", "развитие"), ("die Veränderung", "изменение"), ("die Zusammenarbeit", "сотрудничество"),
    ("der Wettbewerb", "конкуренция"), ("die Nachhaltigkeit", "устойчивость (экологич.)"),
    ("der Klimawandel", "изменение климата"), ("die Digitalisierung", "цифровизация"),
    ("die Globalisierung", "глобализация"), ("die Menschenrechte", "права человека"),
    ("die Toleranz", "толерантность"), ("das Vorurteil", "предрассудок"), ("die Identität", "идентичность"),
]
WORDS += [W(de, ru, "B1", "Abstrakte Begriffe", "n") for de, ru in abstrakt]

abstrakt_b2 = [
    ("die Nachhaltigkeit fördern", "способствовать устойчивому развитию"),
    ("die Auswirkung", "воздействие/последствие"), ("die Perspektive", "перспектива/точка зрения"),
    ("die Voraussetzung", "предпосылка/условие"), ("der Zusammenhang", "взаимосвязь"),
    ("die Konsequenz", "последствие"), ("die Effizienz", "эффективность"), ("die Vielfalt", "разнообразие"),
    ("das Bewusstsein", "осознанность/сознание"), ("die Verpflichtung", "обязательство"),
    ("der Kompromiss", "компромисс"), ("die Debatte", "дебаты"), ("die Kritik", "критика"),
    ("die Kontroverse", "спор/противоречие"), ("das Dilemma", "дилемма"), ("die Skepsis", "скепсис"),
    ("die Innovation", "инновация"), ("das Potenzial", "потенциал"), ("die Ressource", "ресурс"),
    ("die Infrastruktur", "инфраструктура"),
]
WORDS += [W(de, ru, "B2", "Abstrakte Begriffe", "n") for de, ru in abstrakt_b2]

# ---------- НАРЕЧИЯ / ВЫРАЖЕНИЯ ----------
adverbien = [
    ("sehr", "очень"), ("ziemlich", "довольно"), ("besonders", "особенно"), ("vielleicht", "может быть"),
    ("wahrscheinlich", "вероятно"), ("sicherlich", "наверняка"), ("leider", "к сожалению"),
    ("zum Glück", "к счастью"), ("natürlich", "конечно"), ("übrigens", "кстати"),
    ("eigentlich", "вообще-то/собственно"), ("sofort", "немедленно"), ("plötzlich", "внезапно"),
    ("langsam aber sicher", "медленно, но верно"), ("selten", "редко"), ("oft", "часто"),
    ("immer", "всегда"), ("nie", "никогда"), ("manchmal", "иногда"), ("gerade", "как раз/прямо сейчас"),
    ("schon", "уже"), ("noch", "ещё"), ("wieder", "снова"), ("fast", "почти"), ("genau", "точно"),
    ("ungefähr", "примерно"), ("besonders gern", "особенно охотно"), ("kaum", "едва"),
]
WORDS += [W(de, ru, "A2", "Adverbien", "adv") for de, ru in adverbien]

# ---------- ЧЕЛОВЕК / ОПИСАНИЕ ----------
person = [
    ("die Person", "человек/личность"), ("der Name", "имя"), ("das Alter", "возраст"),
    ("die Adresse", "адрес"), ("die Nationalität", "национальность"), ("geboren", "рождённый"),
    ("verheiratet", "женат/замужем"), ("ledig", "холост/не замужем"), ("die Größe", "рост"),
    ("das Gewicht", "вес"), ("die Persönlichkeit", "личность/характер"), ("das Aussehen", "внешность"),
]
WORDS += [W(de, ru, "A1", "Person", "n") for de, ru in person]

# ---------- УБИРАЕМ ДУБЛИКАТЫ (оставляем первое вхождение) ----------
_seen = set()
_unique = []
for _w in WORDS:
    _key = _w["de"].lower()
    if _key in _seen:
        continue
    _seen.add(_key)
    _unique.append(_w)
WORDS = _unique
