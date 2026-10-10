
from dataclasses import dataclass
import pyfiglet


# =====================================================================
# DATA LAYER
# =====================================================================
@dataclass(frozen=True)
class AsciiConfig:
    """Контракт конфигурации для рендеринга ASCII-текста.

    Attributes:
        text: Исходная строка для преобразования.
        font: Название шрифта pyfiglet (например, 'slant', 'block').
    """

    text: str = "Hello world"
    font: str = "slant"


# =====================================================================
# LOGIC LAYER
# =====================================================================
def prepare_text(raw_text: str) -> str:
    """Очищает и валидирует входную строку согласно бизнес-правилам.

    Args:
        raw_text: Сырой пользовательский ввод.

    Returns:
        Очищенная строка без крайних пробельных символов.

    Raises:
        ValueError: Если передана пустая строка или строка из пробелов.
    """
    cleaned = raw_text.strip()
    if not cleaned:
        raise ValueError("Текст не может быть пустым.")
    return cleaned


# =====================================================================
# INTEGRATION LAYER
# =====================================================================
def generate_ascii_art(config: AsciiConfig) -> str:
    """Генерирует ASCII-арт через внешнюю библиотеку pyfiglet.

    Args:
        config: Объект с валидными параметрами текста и шрифта.

    Returns:
        Сформированное текстовое представление ASCII-арта.
    """
    try:
        return pyfiglet.figlet_format(config.text, font=config.font)
    except pyfiglet.FontNotFound:
        # NOTE: Шрифт 'standard' гарантированно поставляется с pyfiglet,
        # поэтому используется как безопасный фоллбэк.
        return pyfiglet.figlet_format(config.text, font="standard")


import argparse

# =====================================================================
# PRESENTATION LAYER
# =====================================================================
def run_cli() -> None:
    """Оркеструет исполнение приложения, парся аргументы CLI."""
    parser = argparse.ArgumentParser(
        description="Генератор ASCII-арта из командной строки."
    )
    
    # Объявление флагов
    parser.add_argument(
        "-t", "--text", 
        type=str, 
        default="Hello world", 
        help="Текст для преобразования"
    )
    parser.add_argument(
        "-f", "--font", 
        type=str, 
        default="slant", 
        help="Шрифт pyfiglet (slant, block, standard и т.д.)"
    )

    args = parser.parse_args()

    try:
        # Валидация через Logic Layer
        validated_text = prepare_text(args.text)
        
        # Сборка контракта Data Layer
        config = AsciiConfig(text=validated_text, font=args.font)

        # Вызов Integration Layer
        ascii_output = generate_ascii_art(config)
        print(ascii_output)
        
    except ValueError as err:
        print(f"[ERROR]: {err}")
    except Exception as err:
        print(f"[UNEXPECTED ERROR]: {err}")

if __name__ == "__main__":
    run_cli()