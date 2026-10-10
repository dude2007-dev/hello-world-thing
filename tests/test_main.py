# Импортируем функцию из твоего main.py
from main import prepare_text

def test_prepare_text_removes_spaces():
    # Мы говорим: "Эй, prepare_text, если я дам тебе '  hello  ',
    # ты ДОЛЖНА вернуть 'hello'. Если вернешь что-то другое — я обижусь."
    assert prepare_text("  hello  ") == "hello" 

import pytest
from main import prepare_text

def test_prepare_text_removes_spaces():
    assert prepare_text("  hello  ") == "hello"

def test_prepare_text_raises_on_empty_string():
    with pytest.raises(ValueError, match="Текст не может быть пустым."):
        prepare_text("   ")