
from main import analyze_text_file


def test_word_count_and_frequency(tmp_path):
    file_path = tmp_path / "text.txt"
    file_path.write_text(
        "Вона читає книжку. Вона читає.",
        encoding="utf-8"
    )

    result = analyze_text_file(file_path)

    assert result["word_count"] == 5
    assert result["frequency"]["вона"] == 2
    assert result["frequency"]["читає"] == 2
    assert result["frequency"]["книжку"] == 1


def test_empty_file(tmp_path, capsys):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    result = analyze_text_file(file_path)

    assert result is None
    assert "файл порожній" in capsys.readouterr().out


def test_missing_file(tmp_path, capsys):
    file_path = tmp_path / "missing.txt"

    result = analyze_text_file(file_path)

    assert result is None
    assert "не вдалося прочитати файл" in capsys.readouterr().out
