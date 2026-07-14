import re
import random


def progress_bar(current: int, total: int, length: int = 10) -> str:
    if total <= 0:
        total = 1
    filled = min(length, round(length * current / total))
    return "█" * filled + "░" * (length - filled)


def normalize_de(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = re.sub(r"^(der|die|das)\s+", "", text)  # артикль необязателен для ответа
    text = re.sub(r"[^a-z ]", "", text)
    return text.strip()


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    la, lb = len(a), len(b)
    if la == 0:
        return lb
    if lb == 0:
        return la
    prev = list(range(lb + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * lb
        for j, cb in enumerate(b, 1):
            cost = 0 if ca == cb else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    return prev[lb]


def fuzzy_match(user_answer: str, correct: str) -> bool:
    ua = normalize_de(user_answer)
    ca = normalize_de(correct)
    if ua == ca:
        return True
    # допускаем 1 опечатку на короткие слова, 2 на длинные
    max_dist = 1 if len(ca) <= 5 else 2
    return levenshtein(ua, ca) <= max_dist


def shuffle_word_letters(word: str) -> list[str]:
    core = word.replace("der ", "").replace("die ", "").replace("das ", "")
    letters = list(core.lower())
    random.shuffle(letters)
    # избегаем случая когда перемешка = оригинал (для коротких слов)
    tries = 0
    while "".join(letters) == core.lower() and tries < 5:
        random.shuffle(letters)
        tries += 1
    return letters


def strip_article(word: str) -> str:
    return re.sub(r"^(der|die|das)\s+", "", word, flags=re.IGNORECASE)
