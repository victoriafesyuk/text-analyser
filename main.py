
import spacy
from nltk import FreqDist


nlp = spacy.load("uk_core_news_sm")


def analyze_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    except OSError:
        print("Помилка: не вдалося прочитати файл.")
        return None

    if not text.strip():
        print("Помилка: файл порожній.")
        return None

    doc = nlp(text)

    words = [
        token.text.lower()
        for token in doc
        if token.is_alpha
    ]

    frequency = FreqDist(words)

    result = {
        "language": "Українська",
        "word_count": len(words),
        "frequency": dict(frequency)
    }

    return result


def main():
    file_path = "text.txt"
    result = analyze_text_file(file_path)

    if result is not None:
        print("Мова тексту:", result["language"])
        print("Кількість слів:", result["word_count"])
        print("Частотність слів:")

        for word, count in sorted(
            result["frequency"].items(),
            key=lambda item: (-item[1], item[0])
        ):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
