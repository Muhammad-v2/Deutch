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

# ============================================================
# ЧАСТЬ 2: РАСШИРЕНИЕ СЛОВАРЯ (+800 слов)
# ============================================================

# ---------- BERUFE (профессии) ----------
berufe2 = [
    ("der Ingenieur", "инженер"), ("die Ärztin", "врач (жен.)"), ("der Anwalt", "адвокат"),
    ("die Krankenschwester", "медсестра"), ("der Polizist", "полицейский"), ("der Feuerwehrmann", "пожарный"),
    ("der Koch", "повар"), ("der Kellner", "официант"), ("der Verkäufer", "продавец"),
    ("der Fahrer", "водитель"), ("der Pilot", "пилот"), ("die Stewardess", "стюардесса"),
    ("der Bauer", "фермер"), ("der Handwerker", "ремесленник"), ("der Elektriker", "электрик"),
    ("der Klempner", "сантехник"), ("der Friseur", "парикмахер"), ("der Zahnarzt", "стоматолог"),
    ("der Apotheker", "фармацевт"), ("der Journalist", "журналист"), ("der Schriftsteller", "писатель"),
    ("der Künstler", "художник"), ("der Musiker", "музыкант"), ("der Schauspieler", "актёр"),
    ("der Fotograf", "фотограф"), ("der Architekt", "архитектор"), ("der Programmierer", "программист"),
    ("der Wissenschaftler", "учёный"), ("der Buchhalter", "бухгалтер"), ("der Manager", "менеджер"),
    ("der Unternehmer", "предприниматель"), ("der Handwerksmeister", "мастер"), ("der Landwirt", "земледелец"),
    ("der Richter", "судья"), ("der Soldat", "солдат"), ("der Priester", "священник"),
    ("der Bäcker", "пекарь"), ("der Metzger", "мясник"), ("der Tischler", "столяр"),
    ("der Ingenieurin", "инженер (жен.)"), ("der Übersetzer", "переводчик"),
]
WORDS += [W(de, ru, "A2", "Berufe", "n") for de, ru in berufe2]

# ---------- LÄNDER UND NATIONALITÄTEN ----------
laender = [
    ("Deutschland", "Германия"), ("Russland", "Россия"), ("Österreich", "Австрия"),
    ("die Schweiz", "Швейцария"), ("Frankreich", "Франция"), ("Italien", "Италия"),
    ("Spanien", "Испания"), ("England", "Англия"), ("die USA", "США"), ("China", "Китай"),
    ("Japan", "Япония"), ("Polen", "Польша"), ("die Türkei", "Турция"), ("die Ukraine", "Украина"),
    ("Kasachstan", "Казахстан"), ("Usbekistan", "Узбекистан"), ("Ägypten", "Египет"),
    ("Indien", "Индия"), ("Brasilien", "Бразилия"), ("Kanada", "Канада"),
    ("der Deutsche", "немец"), ("die Deutsche", "немка"), ("der Russe", "русский"),
    ("die Russin", "русская"), ("der Ausländer", "иностранец"), ("die Sprache", "язык"),
    ("die Nationalität", "национальность"), ("das Land", "страна"), ("die Hauptstadt", "столица"),
    ("der Kontinent", "континент"), ("Europa", "Европа"), ("Asien", "Азия"),
    ("Afrika", "Африка"), ("Amerika", "Америка"), ("Australien", "Австралия"),
    ("die Grenze überqueren", "пересекать границу"), ("die Botschaft", "посольство"),
    ("die Staatsangehörigkeit", "гражданство"), ("einheimisch", "местный/коренной"),
    ("das Ausland", "заграница"),
]
WORDS += [W(de, ru, "A2", "Länder und Nationalitäten", "n") for de, ru in laender]

# ---------- ZAHLEN ERWEITERT ----------
zahlen2 = [
    ("dreizehn", "тринадцать"), ("vierzehn", "четырнадцать"), ("fünfzehn", "пятнадцать"),
    ("sechzehn", "шестнадцать"), ("siebzehn", "семнадцать"), ("achtzehn", "восемнадцать"),
    ("neunzehn", "девятнадцать"), ("einundzwanzig", "двадцать один"), ("dreißig", "тридцать"),
    ("sechzig", "шестьдесят"), ("siebzig", "семьдесят"), ("achtzig", "восемьдесят"),
    ("neunzig", "девяносто"), ("zweite", "второй"), ("dritte", "третий"), ("vierte", "четвёртый"),
    ("fünfte", "пятый"), ("die Hälfte", "половина"), ("das Drittel", "треть"),
    ("das Viertel", "четверть"), ("doppelt", "двойной"), ("die Summe", "сумма"),
    ("die Anzahl", "количество"), ("ungerade", "нечётный"), ("gerade Zahl", "чётное число"),
    ("die Ziffer", "цифра"), ("rechnen", "считать/вычислять", "v"), ("addieren", "складывать", "v"),
    ("subtrahieren", "вычитать", "v"), ("multiplizieren", "умножать", "v"),
]
WORDS += [W(t[0], t[1], "A2", "Zahlen erweitert", t[2] if len(t) > 2 else "n") for t in zahlen2]

# ---------- MÖBEL / HAUSHALT ERWEITERT ----------
moebel2 = [
    ("das Sofa", "диван"), ("der Sessel", "кресло"), ("das Regal", "полка"),
    ("die Kommode", "комод"), ("der Teppich", "ковёр"), ("der Vorhang", "штора"),
    ("das Kissen", "подушка"), ("die Decke", "одеяло/потолок"), ("die Matratze", "матрас"),
    ("der Herd", "плита"), ("der Backofen", "духовка"), ("der Kühlschrank", "холодильник"),
    ("die Spülmaschine", "посудомоечная машина"), ("die Mikrowelle", "микроволновка"),
    ("der Wasserkocher", "чайник электрический"), ("die Bügeleisen", "утюг"),
    ("der Besen", "веник"), ("der Eimer", "ведро"), ("die Mülltonne", "мусорный бак"),
    ("die Steckdose", "розетка"), ("der Schalter", "выключатель"), ("die Glühbirne", "лампочка"),
    ("die Heizung", "отопление"), ("die Klimaanlage", "кондиционер"), ("der Balkon", "балкон"),
    ("der Keller", "подвал"), ("der Dachboden", "чердак"), ("der Flur", "коридор"),
    ("die Treppe", "лестница"), ("der Aufzug", "лифт"),
]
WORDS += [W(de, ru, "A2", "Haushalt erweitert", "n") for de, ru in moebel2]

# ---------- WERKZEUGE ----------
werkzeuge = [
    ("der Hammer", "молоток"), ("die Schraube", "шуруп/винт"), ("der Schraubenzieher", "отвёртка"),
    ("die Zange", "плоскогубцы"), ("die Säge", "пила"), ("der Nagel", "гвоздь"),
    ("die Bohrmaschine", "дрель"), ("die Leiter", "лестница-стремянка"), ("der Kleber", "клей"),
    ("das Klebeband", "скотч"), ("die Schere", "ножницы"), ("das Messer", "нож"),
    ("die Batterie", "батарейка"), ("die Taschenlampe", "фонарик"), ("das Kabel", "кабель"),
]
WORDS += [W(de, ru, "B1", "Werkzeuge", "n") for de, ru in werkzeuge]

# ---------- KOCHEN / KÜCHE ----------
kochen = [
    ("schneiden", "резать", "v"), ("braten", "жарить", "v"), ("backen", "печь", "v"),
    ("kochen", "варить/готовить", "v"), ("grillen", "жарить на гриле", "v"), ("rühren", "мешать/размешивать", "v"),
    ("würzen", "приправлять", "v"), ("mischen", "смешивать", "v"), ("schälen", "чистить (овощи)", "v"),
    ("die Pfanne", "сковорода", "n"), ("der Topf", "кастрюля", "n"), ("der Teller", "тарелка", "n"),
    ("die Gabel", "вилка", "n"), ("der Löffel", "ложка", "n"), ("die Schüssel", "миска", "n"),
    ("das Rezept", "рецепт", "n"), ("die Zutat", "ингредиент", "n"), ("das Gewürz", "приправа", "n"),
    ("der Pfeffer", "перец", "n"), ("das Öl", "масло (растительное)", "n"), ("die Butter", "сливочное масло", "n"),
    ("der Honig", "мёд", "n"), ("das Mehl", "мука", "n"), ("die Sahne", "сливки", "n"),
    ("der Joghurt", "йогурт", "n"), ("die Marmelade", "варенье", "n"), ("das Gebäck", "выпечка", "n"),
    ("die Schokolade", "шоколад", "n"), ("das Eis", "мороженое", "n"), ("der Snack", "перекус", "n"),
]
WORDS += [W(t[0], t[1], "A2", "Kochen und Küche", t[2] if len(t) > 2 else "n") for t in kochen]

# ---------- KLEIDUNG ERWEITERT ----------
kleidung2 = [
    ("der Pullover", "свитер"), ("die Jeans", "джинсы"), ("der Schal", "шарф"),
    ("die Handschuhe", "перчатки"), ("der Anzug", "костюм"), ("die Krawatte", "галстук"),
    ("der Badeanzug", "купальник"), ("die Unterwäsche", "нижнее бельё"), ("der Schlafanzug", "пижама"),
    ("der Stiefel", "сапог"), ("die Sandalen", "сандалии"), ("die Sportschuhe", "кроссовки"),
    ("die Größe passen", "подходить по размеру"), ("eng", "тесный/узкий"), ("weit", "широкий (об одежде)"),
    ("anziehen", "надевать", "v"), ("ausziehen", "снимать", "v"), ("tragen", "носить (одежду)", "v"),
]
WORDS += [W(t[0], t[1], "A1", "Kleidung erweitert", t[2] if len(t) > 2 else "n") for t in kleidung2]

# ---------- SPORT ----------
sport = [
    ("der Fußball", "футбол"), ("der Basketball", "баскетбол"), ("das Tennis", "теннис"),
    ("das Schwimmen", "плавание"), ("das Radfahren", "велоспорт"), ("das Skifahren", "катание на лыжах"),
    ("das Turnen", "гимнастика"), ("die Leichtathletik", "лёгкая атлетика"), ("das Boxen", "бокс"),
    ("das Team", "команда"), ("der Trainer", "тренер"), ("das Training", "тренировка"),
    ("der Wettkampf", "соревнование"), ("die Meisterschaft", "чемпионат"), ("der Sieger", "победитель"),
    ("verlieren im Spiel", "проиграть в игре"), ("das Tor schießen", "забить гол"),
    ("die Mannschaft", "команда"), ("der Schiedsrichter", "судья (спорт.)"), ("das Stadion", "стадион"),
    ("fit sein", "быть в форме"), ("trainieren", "тренироваться", "v"), ("joggen", "бегать трусцой", "v"),
    ("Rad fahren", "кататься на велосипеде", "v"), ("Fußball spielen", "играть в футбол", "v"),
]
WORDS += [W(t[0], t[1], "A2", "Sport", t[2] if len(t) > 2 else "n") for t in sport]

# ---------- MUSIK UND KUNST ----------
kunst = [
    ("die Kunst", "искусство"), ("das Gemälde", "картина"), ("die Skulptur", "скульптура"),
    ("das Instrument", "инструмент (муз.)"), ("das Klavier", "пианино"), ("die Gitarre", "гитара"),
    ("die Geige", "скрипка"), ("die Trommel", "барабан"), ("die Stimme", "голос"),
    ("der Sänger", "певец"), ("die Band", "группа (муз.)"), ("das Lied", "песня"),
    ("die Melodie", "мелодия"), ("der Rhythmus", "ритм"), ("die Ausstellung besuchen", "посетить выставку"),
    ("der Künstlerin", "художница"), ("das Kunstwerk", "произведение искусства"), ("kreativ", "креативный", "adj"),
    ("zeichnen", "рисовать (карандашом)", "v"), ("malen", "рисовать (красками)", "v"),
]
WORDS += [W(t[0], t[1], "B1", "Musik und Kunst", t[2] if len(t) > 2 else "n") for t in kunst]

# ---------- GEOGRAPHIE ----------
geo = [
    ("der Kontinent", "континент"), ("der Ozean", "океан"), ("das Gebirge", "горный массив"),
    ("die Wüste", "пустыня"), ("die Küste", "побережье"), ("die Halbinsel", "полуостров"),
    ("die Grenze", "граница"), ("die Region", "регион"), ("das Gebiet", "область/территория"),
    ("die Karte", "карта"), ("der Norden", "север"), ("der Süden", "юг"), ("der Osten", "восток"),
    ("der Westen", "запад"), ("die Hauptstadt", "столица"), ("die Bevölkerung", "население"),
    ("der Kilometer", "километр"), ("die Entfernung", "расстояние"), ("die Höhe", "высота"),
    ("die Tiefe", "глубина"),
]
WORDS += [W(de, ru, "B1", "Geographie", "n") for de, ru in geo]

# ---------- TIERE ERWEITERT ----------
tiere2 = [
    ("der Affe", "обезьяна"), ("der Tiger", "тигр"), ("der Wolf", "волк"),
    ("der Hirsch", "олень"), ("die Ziege", "коза"), ("das Schaf", "овца"),
    ("die Ente", "утка"), ("das Huhn", "курица"), ("der Hahn", "петух"),
    ("die Gans", "гусь"), ("der Schmetterling", "бабочка"), ("die Biene", "пчела"),
    ("die Spinne", "паук"), ("die Mücke", "комар"), ("die Schlange", "змея"),
    ("der Frosch", "лягушка"), ("die Schildkröte", "черепаха"), ("der Delfin", "дельфин"),
    ("der Wal", "кит"), ("der Hai", "акула"), ("die Krabbe", "краб"),
    ("die Ratte", "крыса"), ("das Eichhörnchen", "белка"), ("der Igel", "ёж"),
    ("das Reh", "косуля"), ("die Kröte", "жаба"), ("die Feder", "перо"),
    ("das Fell", "мех/шерсть"), ("der Käfig", "клетка"), ("die Herde", "стадо"),
]
WORDS += [W(de, ru, "A2", "Tiere erweitert", "n") for de, ru in tiere2]

# ---------- PFLANZEN ----------
pflanzen = [
    ("die Wurzel", "корень"), ("das Blatt", "лист"), ("der Ast", "ветка"),
    ("die Rinde", "кора"), ("der Samen", "семя"), ("die Ernte", "урожай"),
    ("der Pilz", "гриб"), ("die Eiche", "дуб"), ("die Tanne", "ель"),
    ("die Rose", "роза"), ("die Sonnenblume", "подсолнух"), ("das Gänseblümchen", "маргаритка"),
    ("pflanzen", "сажать", "v"), ("gießen", "поливать", "v"), ("wachsen lassen", "выращивать"),
]
WORDS += [W(t[0], t[1], "B1", "Pflanzen", t[2] if len(t) > 2 else "n") for t in pflanzen]

# ---------- WETTER ERWEITERT ----------
wetter2 = [
    ("der Blitz", "молния"), ("der Donner", "гром"), ("der Sturm", "буря"),
    ("der Hagel", "град"), ("das Eis", "лёд"), ("der Frost", "мороз"),
    ("die Feuchtigkeit", "влажность"), ("die Temperatur", "температура"), ("der Grad", "градус"),
    ("die Vorhersage", "прогноз"), ("es regnet", "идёт дождь"), ("es schneit", "идёт снег"),
    ("die Klimaerwärmung", "глобальное потепление"), ("der Regenschirm", "зонт"),
    ("wolkig", "облачно", "adj"), ("sonnig", "солнечно", "adj"), ("neblig", "туманно", "adj"),
    ("windig", "ветрено", "adj"),
]
WORDS += [W(t[0], t[1], "A2", "Wetter erweitert", t[2] if len(t) > 2 else "n") for t in wetter2]

# ---------- VERBEN ERWEITERT ----------
verben2 = [
    ("aufstehen", "вставать"), ("aufwachen", "просыпаться"), ("einschlafen", "засыпать"),
    ("sich anziehen", "одеваться"), ("sich waschen", "умываться"), ("sich rasieren", "бриться"),
    ("sich kämmen", "причёсываться"), ("sich beeilen", "торопиться"), ("ausruhen", "отдыхать"),
    ("aufwachen lassen", "будить"), ("aufmachen", "открывать"), ("zumachen", "закрывать"),
    ("anmachen", "включать"), ("ausmachen", "выключать"), ("einschalten", "включать (прибор)"),
    ("ausschalten", "выключать (прибор)"), ("mitnehmen", "брать с собой"), ("wegnehmen", "забирать"),
    ("zurückgeben", "возвращать"), ("weggeben", "отдавать"), ("hineingehen", "входить"),
    ("hinausgehen", "выходить"), ("hochgehen", "подниматься"), ("runtergehen", "спускаться"),
    ("ankommen", "прибывать"), ("weggehen", "уходить"), ("vorbeigehen", "проходить мимо"),
    ("zurückkommen", "возвращаться"), ("umziehen", "переезжать"), ("ausziehen", "выезжать/раздеваться"),
    ("einziehen", "въезжать"), ("übernachten", "ночевать"), ("aufwachsen", "расти (о человеке)"),
    ("sich verlieben", "влюбляться"), ("heiraten", "жениться/выходить замуж"),
    ("sich scheiden lassen", "разводиться"), ("sich streiten", "ссориться"), ("sich versöhnen", "мириться"),
    ("sich verabreden", "договариваться о встрече"), ("absagen", "отменять"), ("zusagen", "соглашаться"),
    ("einladen", "приглашать"), ("besuchen", "навещать"), ("verabschieden", "прощаться"),
    ("begrüßen", "приветствовать"), ("vorstellen", "представлять (кого-то)"), ("sich vorstellen", "представляться"),
    ("teilen", "делить(ся)"), ("verteilen", "распределять"), ("sammeln", "собирать"),
    ("aufbewahren", "хранить"), ("verlieren", "терять"), ("finden", "находить"),
    ("suchen", "искать"), ("stehlen", "красть"), ("verstecken", "прятать"),
    ("sich verstecken", "прятаться"), ("retten", "спасать"), ("schützen", "защищать"),
    ("angreifen", "нападать"), ("kämpfen", "бороться"), ("gewinnen", "выигрывать"),
    ("aufgeben", "сдаваться"), ("überwinden", "преодолевать"), ("schaffen", "справляться/создавать"),
    ("gelingen", "удаваться"), ("scheitern", "терпеть неудачу"), ("versagen", "подводить/не справляться"),
    ("sich bemühen", "стараться"), ("üben", "тренироваться"), ("wiederholen", "повторять"),
    ("prüfen", "проверять"), ("kontrollieren", "контролировать"), ("bestätigen", "подтверждать"),
    ("ablehnen", "отклонять"), ("akzeptieren", "принимать"), ("vorschlagen", "предлагать"),
    ("zustimmen", "соглашаться"), ("widersprechen", "возражать"), ("diskutieren", "обсуждать"),
    ("streiten", "спорить"), ("überzeugen", "убеждать"), ("beweisen", "доказывать"),
    ("behaupten", "утверждать"), ("zweifeln", "сомневаться"), ("vermuten", "предполагать"),
    ("erwarten", "ожидать"), ("hoffen", "надеяться"), ("befürchten", "опасаться"),
    ("sich sorgen", "беспокоиться"), ("sich freuen", "радоваться"), ("bereuen", "сожалеть"),
]
WORDS += [W(de, ru, "B1", "Verben erweitert", "v") for de, ru in verben2]

# ---------- ADJEKTIVE ERWEITERT ----------
adjektive2 = [
    ("erfolgreich", "успешный"), ("berühmt", "известный"), ("beliebt", "популярный"),
    ("bekannt", "знакомый/известный"), ("unbekannt", "неизвестный"), ("üblich", "обычный"),
    ("ungewöhnlich", "необычный"), ("selten", "редкий"), ("häufig", "частый"),
    ("normal", "нормальный"), ("seltsam", "странный"), ("komisch", "смешной/странный"),
    ("ernsthaft", "серьёзный"), ("verrückt", "сумасшедший"), ("klug", "умный"),
    ("dumm", "глупый"), ("weise", "мудрый"), ("naiv", "наивный"), ("genial", "гениальный"),
    ("talentiert", "талантливый"), ("begabt", "одарённый"), ("kreativ", "креативный"),
    ("praktisch", "практичный"), ("theoretisch", "теоретический"), ("logisch", "логичный"),
    ("vernünftig", "разумный"), ("rücksichtsvoll", "внимательный к другим"), ("höflich", "вежливый"),
    ("unhöflich", "невежливый"), ("aufmerksam", "внимательный"), ("gleichgültig", "равнодушный"),
    ("aktiv", "активный"), ("passiv", "пассивный"), ("energisch", "энергичный"),
    ("entspannt", "расслабленный"), ("angespannt", "напряжённый"), ("empfindlich", "чувствительный"),
    ("stabil", "стабильный"), ("instabil", "нестабильный"), ("flexibel", "гибкий"),
    ("stur", "упрямый"), ("konsequent", "последовательный"), ("spontan", "спонтанный"),
    ("organisiert", "организованный"), ("chaotisch", "хаотичный"), ("ordentlich", "аккуратный"),
    ("unordentlich", "неаккуратный"), ("pünktlich", "пунктуальный"), ("unpünktlich", "непунктуальный"),
    ("effektiv", "эффективный"), ("nützlich", "полезный"), ("nutzlos", "бесполезный"),
    ("sinnvoll", "осмысленный"), ("sinnlos", "бессмысленный"), ("wesentlich", "существенный"),
    ("bedeutend", "значимый"), ("unwichtig", "неважный"), ("dringend", "срочный"),
    ("aktuell", "актуальный"), ("veraltet", "устаревший"), ("zukünftig", "будущий"),
]
WORDS += [W(de, ru, "B1", "Adjektive erweitert", "adj") for de, ru in adjektive2]

# ---------- ADVERBIEN / PARTIKELN ERWEITERT ----------
adverbien2 = [
    ("insgesamt", "в целом"), ("hauptsächlich", "главным образом"), ("teilweise", "частично"),
    ("völlig", "полностью"), ("komplett", "полностью/совсем"), ("gänzlich", "совершенно"),
    ("ausschließlich", "исключительно"), ("gleichzeitig", "одновременно"), ("nacheinander", "по очереди"),
    ("gegenseitig", "взаимно"), ("absichtlich", "намеренно"), ("zufällig", "случайно"),
    ("versehentlich", "нечаянно"), ("bewusst", "осознанно"), ("unbewusst", "неосознанно"),
    ("ausdrücklich", "явно/специально"), ("offensichtlich", "очевидно"), ("angeblich", "якобы"),
    ("tatsächlich", "действительно"), ("vermutlich", "предположительно"), ("möglicherweise", "возможно"),
    ("eventuell", "возможно/при случае"), ("unbedingt", "обязательно"), ("keinesfalls", "ни в коем случае"),
    ("jedenfalls", "в любом случае"), ("immerhin", "всё-таки/по крайней мере"),
    ("schließlich", "в конце концов"), ("letztendlich", "в итоге"), ("inzwischen", "тем временем"),
    ("mittlerweile", "тем временем/уже"),
]
WORDS += [W(de, ru, "B2", "Adverbien erweitert", "adv") for de, ru in adverbien2]

# ---------- ZEIT ERWEITERT ----------
zeit2 = [
    ("der Kalender", "календарь"), ("der Termin", "назначенная встреча"), ("die Frist", "срок/дедлайн"),
    ("die Dauer", "продолжительность"), ("der Zeitpunkt", "момент времени"), ("der Zeitraum", "период времени"),
    ("die Verspätung", "опоздание"), ("pünktlich sein", "быть вовремя"), ("rechtzeitig", "своевременно"),
    ("die Verabredung", "договорённость о встрече"), ("das Jahrhundert", "век"), ("das Jahrzehnt", "десятилетие"),
    ("die Epoche", "эпоха"), ("die Uhrzeit angeben", "указать время"), ("der Wecker", "будильник"),
    ("übermorgen", "послезавтра"), ("vorgestern", "позавчера"), ("neulich", "недавно"),
    ("demnächst", "в ближайшее время"), ("künftig", "в будущем"), ("regelmäßig", "регулярно"),
    ("gelegentlich", "иногда/периодически"), ("dauerhaft", "постоянный"), ("vorübergehend", "временный"),
    ("die Pause", "перерыв"), ("die Vergangenheit erinnern", "вспоминать прошлое"),
]
WORDS += [W(de, ru, "B1", "Zeit erweitert", "n") for de, ru in zeit2]

# ---------- MEDIZIN ERWEITERT ----------
medizin2 = [
    ("die Behandlung", "лечение"), ("die Diagnose", "диагноз"), ("die Operation", "операция"),
    ("das Krankenhaus verlassen", "выписаться из больницы"), ("der Patient", "пациент"),
    ("die Nebenwirkung", "побочный эффект"), ("die Tablette", "таблетка"), ("die Salbe", "мазь"),
    ("der Verband", "повязка"), ("die Spritze", "укол"), ("die Röntgenaufnahme", "рентгеновский снимок"),
    ("die Allergie", "аллергия"), ("die Entzündung", "воспаление"), ("der Husten", "кашель"),
    ("der Schnupfen", "насморк"), ("die Übelkeit", "тошнота"), ("der Schwindel", "головокружение"),
    ("die Verstauchung", "растяжение"), ("der Knochenbruch", "перелом кости"), ("die Narbe", "шрам"),
    ("chronisch", "хронический"), ("akut", "острый (о болезни)"), ("ansteckend", "заразный"),
    ("sich erkälten", "простужаться"), ("sich verletzen", "получать травму"), ("heilen", "лечить/заживать"),
    ("die Ernährung", "питание"), ("die Diät", "диета"), ("abnehmen", "худеть"), ("zunehmen", "полнеть"),
]
WORDS += [W(t[0], t[1], "B1", "Medizin erweitert", t[2] if len(t) > 2 else "n") for t in medizin2]

# ---------- TECHNOLOGIE ERWEITERT ----------
technik2 = [
    ("der Bildschirm", "экран"), ("die Tastatur", "клавиатура"), ("die Maus", "мышь (компьютерная)"),
    ("der Drucker", "принтер"), ("der Server", "сервер"), ("die Cloud", "облако (хранилище)"),
    ("die künstliche Intelligenz", "искусственный интеллект"), ("der Algorithmus", "алгоритм"),
    ("die Verschlüsselung", "шифрование"), ("der Virus", "вирус (компьютерный)"), ("hacken", "взламывать"),
    ("die Sicherheitslücke", "уязвимость"), ("aktualisieren", "обновлять"), ("installieren", "устанавливать"),
    ("deinstallieren", "удалять (программу)"), ("konfigurieren", "настраивать"), ("die Einstellung", "настройка"),
    ("das Update", "обновление"), ("die Benachrichtigung", "уведомление"), ("streamen", "стримить"),
    ("hochladen", "загружать (в сеть)"), ("teilen", "делиться (контентом)"), ("folgen", "подписываться"),
    ("der Nutzer", "пользователь"), ("das Konto", "аккаунт"), ("anmelden", "входить в систему"),
    ("abmelden", "выходить из системы"), ("registrieren", "регистрироваться"), ("die Plattform", "платформа"),
    ("die Suchmaschine", "поисковая система"),
]
WORDS += [W(de, ru, "B1", "Technologie erweitert", "n") for de, ru in technik2]

# ---------- WIRTSCHAFT UND FINANZEN ----------
wirtschaft = [
    ("das Konto", "счёт (банковский)"), ("die Bank", "банк"), ("der Kredit", "кредит"),
    ("die Schulden", "долги"), ("sparen", "копить/экономить"), ("investieren", "инвестировать"),
    ("die Aktie", "акция"), ("der Zins", "процент (по вкладу)"), ("das Einkommen", "доход"),
    ("die Ausgabe", "расход"), ("das Budget", "бюджет"), ("die Steuer", "налог"),
    ("die Inflation", "инфляция"), ("der Markt", "рынок"), ("die Nachfrage", "спрос"),
    ("das Angebot", "предложение"), ("der Umsatz", "оборот (продаж)"), ("der Gewinn", "прибыль"),
    ("der Verlust", "убыток"), ("die Rechnung bezahlen", "оплатить счёт"), ("die Überweisung", "перевод (денег)"),
    ("das Bargeld", "наличные"), ("die Münze", "монета"), ("der Geldschein", "купюра"),
    ("die Versicherung", "страховка"), ("die Miete zahlen", "платить аренду"), ("der Mieter", "арендатор"),
    ("der Vermieter", "арендодатель"), ("der Wert", "стоимость/ценность"), ("wertvoll", "ценный"),
    ("kostenlos", "бесплатный"), ("die Kosten", "затраты"), ("finanzieren", "финансировать"),
    ("die Wirtschaftskrise", "экономический кризис"), ("das Wachstum", "рост (экон.)"),
]
WORDS += [W(de, ru, "B1", "Wirtschaft und Finanzen", "n") for de, ru in wirtschaft]

# ---------- POLITIK UND GESELLSCHAFT ERWEITERT ----------
politik2 = [
    ("die Wahl", "выборы"), ("wählen", "выбирать/голосовать"), ("die Partei", "партия"),
    ("der Kandidat", "кандидат"), ("die Abstimmung", "голосование"), ("die Demokratie", "демократия"),
    ("die Diktatur", "диктатура"), ("die Verfassung", "конституция"), ("das Parlament", "парламент"),
    ("der Bürger", "гражданин"), ("die Staatsbürgerschaft", "гражданство"), ("die Reform", "реформа"),
    ("das Ministerium", "министерство"), ("der Minister", "министр"), ("die Steuerpolitik", "налоговая политика"),
    ("der Protest", "протест"), ("die Demonstration", "демонстрация"), ("streiken", "бастовать"),
    ("die Gewerkschaft", "профсоюз"), ("die Öffentlichkeit", "общественность"), ("die Meinungsfreiheit", "свобода слова"),
]
WORDS += [W(de, ru, "B2", "Politik und Gesellschaft", "n") for de, ru in politik2]

# ---------- BILDUNG ERWEITERT ----------
bildung2 = [
    ("das Fach", "предмет (учебный)"), ("das Semester", "семестр"), ("das Stipendium", "стипендия"),
    ("der Abschluss", "диплом/окончание"), ("die Vorlesung", "лекция"), ("das Seminar", "семинар"),
    ("die Fakultät", "факультет"), ("der Dozent", "преподаватель вуза"), ("die Diplomarbeit", "дипломная работа"),
    ("die Dissertation", "диссертация"), ("das Auswendiglernen", "заучивание наизусть"),
    ("die Fähigkeit", "способность"), ("die Kompetenz", "компетенция"), ("die Fortbildung", "повышение квалификации"),
    ("weiterbilden", "повышать квалификацию"), ("der Lehrplan", "учебный план"), ("das Lehrbuch", "учебник"),
    ("die Bibliothek", "библиотека"), ("ausleihen", "брать напрокат (в библ.)"), ("die Fremdsprache", "иностранный язык"),
]
WORDS += [W(de, ru, "B1", "Bildung erweitert", "n") for de, ru in bildung2]

# ---------- UMWELT ERWEITERT ----------
umwelt2 = [
    ("der Müll trennen", "сортировать мусор"), ("recyceln", "перерабатывать (мусор)"),
    ("die Umweltverschmutzung", "загрязнение окружающей среды"), ("der Abgas", "выхлопной газ"),
    ("die erneuerbare Energie", "возобновляемая энергия"), ("die Solarenergie", "солнечная энергия"),
    ("die Windkraft", "энергия ветра"), ("der Klimawandel bekämpfen", "бороться с изменением климата"),
    ("aussterben", "вымирать"), ("bedroht sein", "быть под угрозой"), ("der Artenschutz", "охрана видов"),
    ("die Emission", "выброс (в атмосферу)"), ("nachhaltig leben", "жить экологично"),
    ("der ökologische Fußabdruck", "экологический след"), ("das Ökosystem", "экосистема"),
]
WORDS += [W(de, ru, "B2", "Umwelt erweitert", "n") for de, ru in umwelt2]

# ---------- MEDIEN ----------
medien = [
    ("die Zeitung", "газета"), ("die Zeitschrift", "журнал"), ("die Nachrichten", "новости"),
    ("der Artikel", "статья"), ("die Schlagzeile", "заголовок"), ("der Bericht", "репортаж/отчёт"),
    ("das Interview", "интервью"), ("die Werbung", "реклама"), ("der Sender", "телеканал/радиостанция"),
    ("die Sendung", "передача"), ("das Programm", "программа (ТВ)"), ("die Reportage", "репортаж"),
    ("veröffentlichen", "публиковать", "v"), ("berichten", "сообщать/докладывать", "v"),
    ("die Öffentlichkeit informieren", "информировать общественность"), ("die Quelle", "источник"),
    ("die Meinungsumfrage", "опрос общественного мнения"), ("die Zensur", "цензура"),
    ("die Pressefreiheit", "свобода прессы"), ("das soziale Netzwerk", "социальная сеть"),
]
WORDS += [W(t[0], t[1], "B1", "Medien", t[2] if len(t) > 2 else "n") for t in medien]

# ---------- RECHT ----------
recht = [
    ("das Gesetz", "закон"), ("das Recht", "право"), ("die Pflicht", "обязанность"),
    ("der Vertrag unterschreiben", "подписать договор"), ("die Klage", "иск"), ("verklagen", "подавать в суд"),
    ("das Gericht", "суд"), ("der Anwalt", "адвокат"), ("das Urteil", "приговор/решение суда"),
    ("die Strafe", "наказание"), ("die Geldstrafe", "штраф"), ("das Verbrechen", "преступление"),
    ("der Dieb", "вор"), ("stehlen", "красть", "v"), ("betrügen", "обманывать", "v"),
    ("die Genehmigung", "разрешение (офиц.)"), ("erlauben", "разрешать", "v"), ("verbieten", "запрещать", "v"),
    ("die Verantwortung tragen", "нести ответственность"), ("unschuldig", "невиновный"),
]
WORDS += [W(t[0], t[1], "B2", "Recht", t[2] if len(t) > 2 else "n") for t in recht]

# ---------- GEFÜHLE ERWEITERT ----------
gefuehle2 = [
    ("die Erleichterung", "облегчение"), ("die Verzweiflung", "отчаяние"), ("die Hoffnung", "надежда"),
    ("die Enttäuschung", "разочарование"), ("die Scham", "стыд"), ("die Schuld", "вина"),
    ("der Neid", "зависть"), ("das Mitleid", "жалость/сострадание"), ("die Dankbarkeit", "благодарность"),
    ("die Sehnsucht", "тоска/тяга"), ("die Einsamkeit", "одиночество"), ("die Verwirrung", "растерянность"),
    ("die Gelassenheit", "невозмутимость"), ("die Begeisterung", "воодушевление"), ("verlegen", "смущённый"),
    ("gerührt", "растроганный"), ("gelangweilt", "скучающий"), ("erschöpft", "измождённый"),
    ("erleichtert", "почувствовавший облегчение"), ("frustriert", "разочарованный/фрустрированный"),
]
WORDS += [W(de, ru, "B1", "Gefühle erweitert", "n") for de, ru in gefuehle2]

# ---------- REISEN ERWEITERT ----------
reisen2 = [
    ("die Kreuzfahrt", "круиз"), ("der Camping", "кемпинг"), ("das Zelt", "палатка"),
    ("der Rucksack", "рюкзак"), ("die Landkarte", "карта местности"), ("der Kompass", "компас"),
    ("die Route planen", "планировать маршрут"), ("die Abenteuerreise", "приключенческое путешествие"),
    ("der Reiseführer", "гид/путеводитель"), ("die Reisegruppe", "туристическая группа"),
    ("das Fernweh", "тяга к путешествиям"), ("die Zeitverschiebung", "разница во времени"),
    ("der Jetlag", "джетлаг"), ("umsteigen", "делать пересадку"), ("verpassen", "опаздывать на (транспорт)"),
    ("die Verspätung haben", "иметь задержку"), ("einchecken", "регистрироваться (в аэропорту)"),
    ("die Bordkarte", "посадочный талон"), ("der Zoll", "таможня"), ("die Sicherheitskontrolle", "досмотр безопасности"),
]
WORDS += [W(de, ru, "B1", "Reisen erweitert", "n") for de, ru in reisen2]

# ---------- STADT ERWEITERT ----------
stadt2 = [
    ("das Rathaus", "ратуша"), ("die Bibliothek", "библиотека"), ("die Kirche", "церковь"),
    ("die Moschee", "мечеть"), ("der Friedhof", "кладбище"), ("der Park", "парк"),
    ("der Spielplatz", "детская площадка"), ("das Wohnviertel", "жилой квартал"), ("die Innenstadt", "центр города"),
    ("der Vorort", "пригород"), ("die Fußgängerzone", "пешеходная зона"), ("der Bürgersteig", "тротуар"),
    ("die Baustelle", "стройка"), ("die Sanierung", "реконструкция"), ("die Verwaltung", "администрация"),
    ("das Standesamt", "ЗАГС"), ("das Gericht", "суд"), ("die Feuerwache", "пожарная станция"),
    ("die Polizeiwache", "полицейский участок"), ("das Einkaufszentrum", "торговый центр"),
]
WORDS += [W(de, ru, "A2", "Stadt erweitert", "n") for de, ru in stadt2]

# ---------- ALLTAGSAUSDRÜCKE (устойчивые выражения) ----------
ausdruecke = [
    ("Wie geht's?", "как дела?"), ("Alles klar", "всё понятно/окей"), ("Kein Problem", "без проблем"),
    ("Es tut mir leid", "мне жаль"), ("Entschuldigung", "извините"), ("Gern geschehen", "пожалуйста (в ответ на спасибо)"),
    ("Viel Glück", "удачи"), ("Viel Erfolg", "успехов"), ("Gute Besserung", "выздоравливай"),
    ("Herzlichen Glückwunsch", "поздравляю"), ("Guten Appetit", "приятного аппетита"),
    ("Bis bald", "до скорого"), ("Bis später", "до встречи позже"), ("Auf Wiedersehen", "до свидания"),
    ("Mach's gut", "пока/удачи (неформ.)"), ("Schade", "жаль"), ("Macht nichts", "ничего страшного"),
    ("Keine Ahnung", "понятия не имею"), ("Auf jeden Fall", "в любом случае"), ("Auf keinen Fall", "ни в коем случае"),
    ("Es kommt darauf an", "это зависит"), ("Meiner Meinung nach", "по моему мнению"),
    ("Im Gegenteil", "наоборот"), ("Zum Beispiel", "например"), ("Mit anderen Worten", "другими словами"),
    ("Es lohnt sich", "это того стоит"), ("Es macht Spaß", "это весело/это доставляет удовольствие"),
    ("Es tut weh", "это больно"), ("Ich bin dran", "моя очередь"), ("Das reicht", "этого достаточно"),
    ("Sei vorsichtig", "будь осторожен"), ("Pass auf", "будь внимателен/осторожно"),
    ("Beeil dich", "поторопись"), ("Warte mal", "подожди-ка"), ("Lass uns gehen", "пойдём"),
    ("Ich bin dabei", "я в деле/присоединяюсь"), ("Wie bitte?", "прошу прощения? (переспрос)"),
    ("Das ist mir egal", "мне всё равно"), ("Ich freue mich darauf", "я жду этого с нетерпением"),
    ("Es ist mir peinlich", "мне неловко"),
]
WORDS += [W(de, ru, "A2", "Alltagsausdrücke", "other") for de, ru in ausdruecke]

# ---------- FRAGEWÖRTER ----------
fragewoerter = [
    ("wer", "кто"), ("was", "что"), ("wo", "где"), ("wohin", "куда"), ("woher", "откуда"),
    ("wann", "когда"), ("warum", "почему"), ("wieso", "почему/отчего"), ("weshalb", "по какой причине"),
    ("wie", "как"), ("wie viel", "сколько"), ("wie viele", "сколько (мн.ч.)"), ("welcher", "который"),
    ("wozu", "для чего"), ("womit", "чем"),
]
WORDS += [W(de, ru, "A1", "Fragewörter", "other") for de, ru in fragewoerter]

# ---------- KÖRPER ERWEITERT ----------
koerper2 = [
    ("die Schulter", "плечо"), ("der Ellbogen", "локоть"), ("das Handgelenk", "запястье"),
    ("die Hüfte", "бедро"), ("das Knie", "колено"), ("der Knöchel", "лодыжка"),
    ("die Wimper", "ресница"), ("die Augenbraue", "бровь"), ("die Lippe", "губа"),
    ("die Zunge", "язык (орган)"), ("der Kiefer", "челюсть"), ("die Wange", "щека"),
    ("das Kinn", "подбородок"), ("die Stirn", "лоб"), ("der Nagel", "ноготь"),
    ("die Ader", "вена"), ("die Lunge", "лёгкое"), ("die Leber", "печень"),
    ("der Magen", "желудок"), ("der Muskel", "мышца"),
]
WORDS += [W(de, ru, "B1", "Körper erweitert", "n") for de, ru in koerper2]

# ---------- ESSEN ERWEITERT (Gerichte) ----------
essen2 = [
    ("das Schnitzel", "шницель"), ("der Braten", "жаркое"), ("die Bratwurst", "жареная колбаска"),
    ("der Eintopf", "суп-рагу"), ("die Pizza", "пицца"), ("der Salat", "салат"),
    ("das Sandwich", "сэндвич"), ("der Döner", "донер"), ("die Currywurst", "карривурст"),
    ("das Müsli", "мюсли"), ("der Pfannkuchen", "блин/оладья"), ("der Knödel", "кнёдель"),
    ("das Sauerkraut", "квашеная капуста"), ("die Brezel", "крендель"), ("der Senf", "горчица"),
    ("die Mayonnaise", "майонез"), ("das Ketchup", "кетчуп"), ("die Sauce", "соус"),
    ("die Brühe", "бульон"), ("das Gericht", "блюдо"), ("die Portion", "порция"),
    ("die Vorspeise", "закуска"), ("die Nachspeise", "десерт"), ("die Hauptspeise", "основное блюдо"),
    ("vegetarisch", "вегетарианский"), ("vegan", "веганский"), ("die Kalorien", "калории"),
    ("roh", "сырой"), ("gekocht", "варёный"), ("gebraten", "жареный"), ("gebacken", "печёный"),
]
WORDS += [W(de, ru, "A2", "Essen erweitert", "n") for de, ru in essen2]

# ---------- FAMILIE ERWEITERT ----------
familie2 = [
    ("die Schwiegermutter", "свекровь/тёща"), ("der Schwiegervater", "свёкор/тесть"),
    ("die Schwägerin", "золовка/невестка"), ("der Schwager", "деверь/шурин"),
    ("die Verwandten", "родственники"), ("der Verwandte", "родственник"), ("die Stiefmutter", "мачеха"),
    ("der Stiefvater", "отчим"), ("das Einzelkind", "единственный ребёнок"), ("die Zwillinge", "близнецы"),
]
WORDS += [W(de, ru, "A2", "Familie erweitert", "n") for de, ru in familie2]

# ---------- CHARAKTEREIGENSCHAFTEN ----------
charakter = [
    ("verantwortungsbewusst", "ответственный"), ("selbstbewusst", "уверенный в себе"),
    ("bescheiden", "скромный"), ("arrogant", "высокомерный"), ("humorvoll", "с чувством юмора"),
    ("optimistisch", "оптимистичный"), ("pessimistisch", "пессимистичный"), ("realistisch", "реалистичный"),
    ("diszipliniert", "дисциплинированный"), ("kreativ denkend", "творчески мыслящий"),
    ("kommunikativ", "коммуникабельный"), ("introvertiert", "интровертный"), ("extrovertiert", "экстравертный"),
    ("empathisch", "эмпатичный"), ("loyal", "верный/лояльный"), ("misstrauisch", "недоверчивый"),
    ("vertrauensvoll", "доверчивый"), ("ausgeglichen", "уравновешенный"), ("impulsiv", "импульсивный"),
    ("hartnäckig", "упорный"),
]
WORDS += [W(de, ru, "B1", "Charaktereigenschaften", "adj") for de, ru in charakter]


# ============================================================
# ЧАСТЬ 3: УСИЛЕНИЕ B1/B2 (+~480 слов продвинутого уровня)
# ============================================================

# ---------- WISSENSCHAFT ----------
wissenschaft = [
    ("die Forschung", "исследование"), ("das Experiment", "эксперимент"), ("die Hypothese", "гипотеза"),
    ("die Theorie", "теория"), ("der Beweis", "доказательство"), ("die Methode", "метод"),
    ("das Ergebnis", "результат"), ("die Erkenntnis", "познание/вывод"), ("die Untersuchung", "исследование/обследование"),
    ("der Wissenschaftler", "учёный"), ("das Labor", "лаборатория"), ("die Studie", "исследование (науч.)"),
    ("die Statistik", "статистика"), ("die Analyse", "анализ"), ("die Auswertung", "оценка результатов"),
    ("die Formel", "формула"), ("die Substanz", "вещество"), ("das Molekül", "молекула"),
    ("die Zelle", "клетка (биол.)"), ("das Gen", "ген"), ("die Evolution", "эволюция"),
    ("das Universum", "вселенная"), ("die Physik", "физика"), ("die Chemie", "химия"),
    ("die Biologie", "биология"), ("die Mathematik", "математика"), ("die Philosophie", "философия"),
    ("die Psychologie", "психология"), ("die Soziologie", "социология"), ("die Medizin studieren", "изучать медицину"),
]
WORDS += [W(de, ru, "B2", "Wissenschaft", "n") for de, ru in wissenschaft]

# ---------- ABSTRAKTE KONZEPTE / PHILOSOPHIE ----------
philosophie = [
    ("das Bewusstsein", "сознание"), ("die Existenz", "существование"), ("der Sinn des Lebens", "смысл жизни"),
    ("die Wahrheit", "истина"), ("die Lüge", "ложь"), ("die Realität", "реальность"),
    ("die Illusion", "иллюзия"), ("der Zweifel", "сомнение"), ("die Gewissheit", "уверенность/достоверность"),
    ("die Moral", "мораль"), ("die Ethik", "этика"), ("das Prinzip", "принцип"),
    ("der Wert", "ценность"), ("die Weisheit", "мудрость"), ("die Vernunft", "разум"),
    ("das Schicksal", "судьба"), ("der Zufall", "случайность"), ("die Freiheit", "свобода"),
    ("die Verantwortung", "ответственность"), ("das Gewissen", "совесть"), ("die Seele", "душа"),
    ("der Geist", "дух/разум"), ("die Identität", "идентичность"), ("die Individualität", "индивидуальность"),
    ("der Widerspruch", "противоречие"), ("das Paradox", "парадокс"), ("die Perspektive wechseln", "менять точку зрения"),
    ("die Absicht", "намерение"), ("die Konsequenz tragen", "нести последствия"), ("die Selbstverwirklichung", "самореализация"),
]
WORDS += [W(de, ru, "B2", "Philosophie", "n") for de, ru in philosophie]

# ---------- GESCHÄFTSSPRACHE ERWEITERT ----------
geschaeft = [
    ("die Verhandlung", "переговоры"), ("verhandeln", "вести переговоры", "v"), ("der Kompromiss finden", "находить компромисс"),
    ("die Strategie", "стратегия"), ("die Zielgruppe", "целевая аудитория"), ("die Marketingkampagne", "маркетинговая кампания"),
    ("die Konkurrenz", "конкуренция/конкуренты"), ("der Wettbewerbsvorteil", "конкурентное преимущество"),
    ("die Geschäftsidee", "бизнес-идея"), ("das Startup", "стартап"), ("gründen", "основывать (компанию)", "v"),
    ("die Investition", "инвестиция"), ("der Investor", "инвестор"), ("das Risiko eingehen", "идти на риск"),
    ("die Fusion", "слияние (компаний)"), ("übernehmen", "поглощать/принимать на себя", "v"),
    ("die Zielsetzung", "постановка целей"), ("die Effizienz steigern", "повышать эффективность"),
    ("die Produktivität", "производительность"), ("outsourcen", "передавать на аутсорс", "v"),
    ("die Lieferkette", "цепочка поставок"), ("der Lieferant", "поставщик"), ("die Qualitätskontrolle", "контроль качества"),
    ("das Budget einhalten", "укладываться в бюджет"), ("die Frist einhalten", "соблюдать сроки"),
    ("delegieren", "делегировать", "v"), ("die Führungskraft", "руководитель"), ("das Personal", "персонал"),
    ("die Fluktuation", "текучесть кадров"), ("die Motivation steigern", "повышать мотивацию"),
    ("das Feedback geben", "давать обратную связь"), ("die Präsentation halten", "проводить презентацию"),
    ("der Geschäftspartner", "деловой партнёр"), ("die Zusammenarbeit vertiefen", "углублять сотрудничество"),
    ("die Expansion", "расширение (бизнеса)"), ("der Marktanteil", "доля рынка"), ("die Rentabilität", "рентабельность"),
    ("das Geschäftsmodell", "бизнес-модель"), ("skalieren", "масштабировать", "v"), ("die Innovation vorantreiben", "продвигать инновации"),
]
WORDS += [W(t[0], t[1], "B2", "Geschäftssprache", t[2] if len(t) > 2 else "n") for t in geschaeft]

# ---------- REDEWENDUNGEN / IDIOME ----------
idiome = [
    ("Daumen drücken", "держать кулачки"), ("die Nase voll haben", "быть сытым по горло"),
    ("ins Wasser fallen", "сорваться (о планах)"), ("Schwein haben", "везти (о удаче)"),
    ("auf den Punkt bringen", "выразить суть"), ("den Nagel auf den Kopf treffen", "попасть в точку"),
    ("die Kirche im Dorf lassen", "не преувеличивать"), ("um den heißen Brei reden", "ходить вокруг да около"),
    ("ins kalte Wasser springen", "решиться на новое без подготовки"), ("Hals über Kopf", "сломя голову"),
    ("unter vier Augen", "с глазу на глаз"), ("aus heiterem Himmel", "как гром среди ясного неба"),
    ("die Katze im Sack kaufen", "купить кота в мешке"), ("ins Gras beißen", "умереть (разг.)"),
    ("das Handtuch werfen", "сдаться/бросить попытки"), ("auf Wolke sieben schweben", "быть на седьмом небе"),
    ("Öl ins Feuer gießen", "подливать масла в огонь"), ("den Kürzeren ziehen", "оказаться в проигрыше"),
    ("etwas auf die lange Bank schieben", "откладывать в долгий ящик"), ("die Kurve kriegen", "справиться в последний момент"),
    ("jemandem die Daumen drücken", "болеть за кого-то"), ("sich ins Zeug legen", "прилагать все усилия"),
    ("Tomaten auf den Augen haben", "не замечать очевидного"), ("ein Auge zudrücken", "закрыть глаза на что-то"),
    ("Schwamm drüber", "забудем об этом"), ("null Bock haben", "не иметь никакого желания"),
    ("es faustdick hinter den Ohren haben", "быть хитрее, чем кажется"), ("auf dem Holzweg sein", "быть на ложном пути"),
    ("die Flinte ins Korn werfen", "опустить руки"), ("Hand und Fuß haben", "быть обоснованным/логичным"),
]
WORDS += [W(de, ru, "B2", "Redewendungen", "other") for de, ru in idiome]

# ---------- DISKURSMARKER / KONNEKTOREN ----------
konnektoren = [
    ("einerseits ... andererseits", "с одной стороны ... с другой стороны"), ("nichtsdestotrotz", "тем не менее"),
    ("dennoch", "тем не менее"), ("allerdings", "однако/впрочем"), ("jedoch", "однако"),
    ("infolgedessen", "вследствие этого"), ("demzufolge", "следовательно"), ("folglich", "следовательно"),
    ("somit", "таким образом"), ("mithin", "стало быть"), ("angesichts", "учитывая/ввиду"),
    ("unter der Voraussetzung", "при условии"), ("vorausgesetzt, dass", "при условии, что"),
    ("sofern", "если/при условии что"), ("es sei denn", "если только не"), ("insofern als", "в той мере, в какой"),
    ("im Hinblick auf", "в отношении/учитывая"), ("in Anbetracht", "принимая во внимание"),
    ("zumal", "тем более что"), ("geschweige denn", "не говоря уже о"), ("respektive", "соответственно/или"),
    ("beziehungsweise", "соответственно/или же"), ("nicht zuletzt", "не в последнюю очередь"),
    ("überdies", "к тому же"), ("des Weiteren", "далее/кроме того"),
]
WORDS += [W(de, ru, "B2", "Konnektoren", "other") for de, ru in konnektoren]

# ---------- PSYCHOLOGIE UND VERHALTEN ----------
psychologie = [
    ("das Verhalten", "поведение"), ("die Gewohnheit", "привычка"), ("die Angewohnheit", "привычка (часто дурная)"),
    ("die Motivation", "мотивация"), ("der Antrieb", "стремление/побуждение"), ("die Willenskraft", "сила воли"),
    ("die Selbstbeherrschung", "самообладание"), ("der Stress", "стресс"), ("die Belastung", "нагрузка/напряжение"),
    ("bewältigen", "справляться (с трудностями)", "v"), ("überfordert sein", "быть перегруженным", "v"),
    ("sich anpassen", "адаптироваться", "v"), ("die Resilienz", "жизнестойкость", "n"),
    ("das Trauma", "травма (психол.)", "n"), ("die Wahrnehmung", "восприятие", "n"),
    ("das Vorurteil", "предрассудок", "n"), ("die Voreingenommenheit", "предвзятость", "n"),
    ("die Selbstreflexion", "самоанализ", "n"), ("das Selbstwertgefühl", "самооценка", "n"),
    ("die Beziehung pflegen", "поддерживать отношения"), ("das Vertrauen aufbauen", "выстраивать доверие"),
    ("die Grenze setzen", "устанавливать границы"), ("die Empathie zeigen", "проявлять эмпатию"),
    ("manipulieren", "манипулировать", "v"), ("beeinflussen", "влиять", "v"), ("überreden", "уговаривать", "v"),
]
WORDS += [W(t[0], t[1], "B2", "Psychologie", t[2] if len(t) > 2 else "n") for t in psychologie]

# ---------- KUNST UND KULTUR ERWEITERT ----------
kultur2 = [
    ("das Kulturerbe", "культурное наследие"), ("die Tradition bewahren", "сохранять традицию"),
    ("der Brauch", "обычай"), ("das Ritual", "ритуал"), ("die Zeremonie", "церемония"),
    ("die Literatur", "литература"), ("der Roman", "роман"), ("die Erzählung", "рассказ"),
    ("die Gedichtsammlung", "сборник стихов"), ("der Autor", "автор"), ("das Meisterwerk", "шедевр"),
    ("die Inszenierung", "постановка (театр.)"), ("die Aufführung", "выступление/представление"),
    ("das Publikum", "публика"), ("der Applaus", "аплодисменты"), ("die Kritik üben", "критиковать"),
    ("das Genre", "жанр"), ("der Stil", "стиль"), ("die Epoche prägen", "определять эпоху"),
    ("das Symbol", "символ"), ("die Metapher", "метафора"), ("die Interpretation", "интерпретация"),
]
WORDS += [W(de, ru, "B2", "Kunst und Kultur", "n") for de, ru in kultur2]

# ---------- GESCHICHTE ----------
geschichte = [
    ("die Geschichte", "история"), ("das Ereignis", "событие"), ("die Epoche", "эпоха"),
    ("das Zeitalter", "эра"), ("der Krieg", "война"), ("der Frieden", "мир (не война)"),
    ("die Revolution", "революция"), ("die Unabhängigkeit", "независимость"), ("das Reich", "империя"),
    ("die Dynastie", "династия"), ("der Herrscher", "правитель"), ("die Kolonie", "колония"),
    ("die Entdeckung", "открытие"), ("die Erfindung", "изобретение"), ("der Fortschritt bringen", "приносить прогресс"),
    ("die Erinnerung bewahren", "хранить память"), ("das Denkmal", "памятник"), ("die Vergangenheit aufarbeiten", "прорабатывать прошлое"),
    ("historisch bedeutsam", "исторически значимый"), ("das Archiv", "архив"),
]
WORDS += [W(de, ru, "B2", "Geschichte", "n") for de, ru in geschichte]

# ---------- SOZIALES VERHALTEN ----------
sozial = [
    ("die Zusammengehörigkeit", "чувство общности"), ("die Solidarität", "солидарность"),
    ("die Toleranz üben", "проявлять толерантность"), ("die Integration", "интеграция"),
    ("sich integrieren", "интегрироваться", "v"), ("die Vielfalt schätzen", "ценить разнообразие"),
    ("die Ungleichheit", "неравенство"), ("die Chancengleichheit", "равенство возможностей"),
    ("die Diskriminierung", "дискриминация"), ("diskriminieren", "дискриминировать", "v"),
    ("die Ausgrenzung", "исключение из общества"), ("ausgrenzen", "исключать/изолировать (кого-то)", "v"),
    ("die Zugehörigkeit", "принадлежность"), ("die Gemeinschaft", "сообщество/общность"),
    ("das Ehrenamt", "волонтёрство"), ("sich engagieren", "проявлять активность/участвовать", "v"),
    ("die Nächstenliebe", "любовь к ближнему"), ("die Rücksichtnahme", "учёт интересов других"),
    ("der soziale Zusammenhalt", "социальная сплочённость"), ("die Generation", "поколение"),
]
WORDS += [W(t[0], t[1], "B2", "Soziales Verhalten", t[2] if len(t) > 2 else "n") for t in sozial]

# ---------- DIGITALISIERUNG UND ZUKUNFT ----------
digital = [
    ("die Automatisierung", "автоматизация"), ("die Digitalisierung vorantreiben", "продвигать цифровизацию"),
    ("die virtuelle Realität", "виртуальная реальность"), ("die Robotik", "робототехника"),
    ("das maschinelle Lernen", "машинное обучение"), ("die Datensicherheit", "безопасность данных"),
    ("der Datenschutz", "защита данных"), ("die Überwachung", "слежка/наблюдение"),
    ("die Vernetzung", "объединение в сеть"), ("die Fernarbeit", "удалённая работа"),
    ("die Homeoffice-Regelung", "правила работы из дома"), ("digital vernetzt sein", "быть в цифровой сети"),
    ("die Innovationskraft", "инновационный потенциал"), ("die technologische Entwicklung", "технологическое развитие"),
]
WORDS += [W(de, ru, "B2", "Digitalisierung", "n") for de, ru in digital]

# ---------- KOMMUNIKATION ----------
kommunikation = [
    ("die Kommunikation", "коммуникация"), ("das Missverständnis", "недопонимание"),
    ("sich missverstehen", "неправильно понимать друг друга", "v"), ("klarstellen", "прояснять", "v"),
    ("betonen", "подчёркивать", "v"), ("andeuten", "намекать", "v"), ("ausdrücken", "выражать", "v"),
    ("formulieren", "формулировать", "v"), ("vermitteln", "передавать (информацию)/посредничать", "v"),
    ("der Standpunkt", "точка зрения", "n"), ("die Argumentation", "аргументация", "n"),
    ("überzeugend", "убедительный", "adj"), ("nachvollziehbar", "понятный/логичный", "adj"),
    ("widersprüchlich", "противоречивый", "adj"), ("eindeutig", "однозначный", "adj"),
    ("zweideutig", "двусмысленный", "adj"), ("die Zwischenzeile lesen", "читать между строк"),
    ("nonverbal", "невербальный", "adj"), ("die Körpersprache", "язык тела", "n"),
]
WORDS += [W(t[0], t[1], "B2", "Kommunikation", t[2] if len(t) > 2 else "n") for t in kommunikation]

# ---------- ABSTRAKTE VERBEN (formal) ----------
verben3 = [
    ("sich auseinandersetzen mit", "разбираться/иметь дело с"), ("berücksichtigen", "учитывать"),
    ("vernachlässigen", "пренебрегать"), ("gewährleisten", "обеспечивать (гарантировать)"),
    ("ermöglichen", "делать возможным"), ("erschweren", "затруднять"), ("erleichtern", "облегчать"),
    ("fördern", "способствовать/поддерживать"), ("hemmen", "сдерживать/тормозить"),
    ("verursachen", "вызывать/быть причиной"), ("auslösen", "провоцировать/запускать"),
    ("beeinträchtigen", "негативно влиять"), ("beitragen zu", "способствовать чему-либо"),
    ("resultieren aus", "являться результатом"), ("basieren auf", "основываться на"),
    ("sich beziehen auf", "относиться к/ссылаться на"), ("sich auswirken auf", "влиять на"),
    ("hervorheben", "выделять/подчёркивать"), ("herausstellen", "выяснять/оказываться"),
    ("sich herausstellen als", "оказаться (кем-то/чем-то)"), ("nachweisen", "доказывать/подтверждать"),
    ("widerlegen", "опровергать"), ("belegen", "подтверждать доказательствами"),
    ("verallgemeinern", "обобщать"), ("differenzieren", "разграничивать/дифференцировать"),
    ("einschätzen", "оценивать"), ("bewerten", "оценивать (качество)"), ("einordnen", "классифицировать"),
    ("gliedern", "структурировать"), ("zusammenfassen", "суммировать/резюмировать"),
    ("erläutern", "разъяснять"), ("veranschaulichen", "иллюстрировать/наглядно показывать"),
    ("konkretisieren", "конкретизировать"), ("verallgemeinernd sprechen", "говорить обобщённо"),
    ("sich orientieren an", "ориентироваться на"), ("sich richten nach", "руководствоваться чем-либо"),
    ("abhängen von", "зависеть от"), ("voraussetzen", "предполагать (как условие)"),
    ("bedingen", "обусловливать"), ("verkörpern", "воплощать"),
]
WORDS += [W(de, ru, "B2", "Verben (formal)", "v") for de, ru in verben3]

# ---------- SUBSTANTIVE MIT PRÄFIXEN ----------
substantive_praefix = [
    ("die Verantwortung übernehmen", "брать на себя ответственность"), ("die Entwicklung fördern", "способствовать развитию"),
    ("die Entscheidung treffen", "принимать решение"), ("die Entstehung", "возникновение"),
    ("die Entfaltung", "раскрытие потенциала"), ("die Entspannung", "разрядка/расслабление"),
    ("die Enttäuschung überwinden", "преодолевать разочарование"), ("die Aufklärung", "просвещение/разъяснение"),
    ("der Aufschwung", "подъём (экономический)"), ("der Aufbau", "построение/структура"),
    ("die Auflösung", "роспуск/растворение"), ("die Auseinandersetzung", "спор/противостояние"),
    ("die Ausnahme", "исключение"), ("die Ausdauer", "выносливость"), ("die Ausstrahlung", "харизма/излучение"),
    ("die Verbindung", "связь/соединение"), ("die Verbesserung", "улучшение"), ("die Verschlechterung", "ухудшение"),
    ("die Vereinbarung", "договорённость"), ("die Verfügbarkeit", "доступность"), ("die Verpflichtung eingehen", "брать на себя обязательство"),
    ("die Vermeidung", "избегание"), ("die Vermittlung", "посредничество"), ("die Vereinigung", "объединение"),
    ("die Vertiefung", "углубление"), ("die Verwirklichung", "реализация"), ("die Vertretung", "представительство"),
    ("die Übertreibung", "преувеличение"), ("die Übereinstimmung", "согласие/совпадение"), ("die Überzeugung", "убеждение"),
]
WORDS += [W(de, ru, "B2", "Abstrakte Substantive", "n") for de, ru in substantive_praefix]

# ---------- EMOTIONALE NUANCEN ----------
emotionen2 = [
    ("die Genugtuung", "удовлетворение (моральное)"), ("die Ohnmacht", "бессилие"),
    ("die Verbitterung", "озлобленность"), ("die Wehmut", "тоска/грусть-светлая"),
    ("die Rührung", "растроганность"), ("die Erschütterung", "потрясение"), ("die Fassungslosigkeit", "растерянность/шок"),
    ("die Ungeduld", "нетерпение"), ("die Gleichgültigkeit", "безразличие"), ("die Zuneigung", "привязанность/симпатия"),
    ("die Abneigung", "неприязнь"), ("die Erregung", "возбуждение"), ("die Gelassenheit bewahren", "сохранять спокойствие"),
    ("überwältigt sein", "быть переполненным чувствами"), ("bewegt sein", "быть тронутым"),
    ("betroffen sein", "быть затронутым/огорчённым"), ("gefasst bleiben", "оставаться сдержанным"),
    ("außer sich sein", "быть вне себя"), ("aufgewühlt sein", "быть взволнованным"), ("beklommen", "тревожный/стеснённый"),
]
WORDS += [W(de, ru, "B2", "Emotionale Nuancen", "n") for de, ru in emotionen2]

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
