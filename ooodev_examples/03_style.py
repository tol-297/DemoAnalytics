"""
Демонстрация работы со стилями в LibreOffice Calc.

Основные операции:
- Создание документа
- Применение стилей к ячейкам и диапазонам
- Стили для шрифта: размер, жирность, цвет
- Стили для фона: цвет, заливка
- Применение стилей через set_style() и apply_styles()
"""

from ooodev.loader.lo import Lo
from ooodev.calc import CalcDoc
from ooodev.utils.color import StandardColor, Color
from ooodev.format.calc.direct.cell.font import Font
from ooodev.format.calc.direct.cell.background import Color as BgColor


def main():
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем новый документ
        doc = CalcDoc.create_doc()
        sheet = doc.get_active_sheet()

        # 2. Определяем стили для заголовка
        header_style = [
            Font(size=14, b=True, color=StandardColor.WHITE),
            BgColor(color=StandardColor.BLUE),
        ]

        # 3. Определяем стили для обычных данных
        data_style = [
            Font(size=11),
            BgColor(color=Color(0xF0F0F0)),  # Светло-серый
        ]

        # 4. Определяем стили для итогов
        total_style = [
            Font(size=12, b=True, color=StandardColor.WHITE),
            BgColor(color=StandardColor.GREEN),
        ]

        # 5. Заполняем данные
        headers = ["Продукт", "Цена", "Кол-во", "Сумма"]
        data = [
            ["Яблоки", 100, 10, 1000],
            ["Бананы", 80, 15, 1200],
            ["Вишня", 200, 5, 1000],
        ]

        # 6. Применяем стили к заголовку
        sheet.get_range(range_name="A1:D1").set_array([headers])
        sheet.get_range(range_name="A1:D1").apply_styles(*header_style)

        # 7. Записываем и стилизуем данные
        sheet.get_range(range_name="A2:D4").set_array(data)
        sheet.get_range(range_name="A2:D4").apply_styles(*data_style)

        # 8. Добавляем итоговую строку
        sheet["A5"].value = "ИТОГО:"
        sheet["D5"].value = sum([row[3] for row in data])

        # Применяем стиль к итоговой строке
        sheet.get_range(range_name="A5:D5").apply_styles(*total_style)

        # 9. Сохраняем документ
        doc.save_doc("style_example.ods")

if __name__ == "__main__":
    main()

