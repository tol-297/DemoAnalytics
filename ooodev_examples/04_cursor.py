"""
Демонстрация работы программного курсора в LibreOffice Calc.

Основные операции:
- Создание курсора через create_cursor()
- Движение курсора: go_to_start(), go_to_offset(), go_to_end_of_used_area()
- Поиск использованного диапазона: find_used_range_obj()
- Применение стилей к диапазону, найденному курсором
"""

from ooodev.loader.lo import Lo
from ooodev.calc import CalcDoc
from ooodev.utils.color import StandardColor, Color
from ooodev.format.calc.direct.cell.font import Font
from ooodev.format.calc.direct.cell.background import Color as BgColor


def main():
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем новый документ
        doc = CalcDoc.create_doc(visible=True)
        sheet = doc.get_active_sheet()

        # 2. Заполняем данные
        headers = ["Продукт", "Цена", "Кол-во"]
        data = [
            ["Яблоки", 100, 10],
            ["Бананы", 80, 15],
            ["Вишня", 200, 5],
        ]

        # 3. Записываем заголовки
        sheet.get_range(range_name="A1:C1").set_array([headers])

        # 4. Записываем данные
        sheet.get_range(range_name="A2:C4").set_array(data)
        Lo.delay(2000)

        # 5. Создаем курсор и позиционируем его
        cursor = sheet.create_cursor()

        # Перемещаемся в начало
        cursor.go_to_start()
        print("✓ Курсор перемещен в начало")

        # Перемещаемся на одну строку вниз и два столбца вправо
        cursor.go_to_offset(col_offset=2, row_offset=1)
        print("✓ Курсор смещен на +1 строку и +2 столбца")

        # Расширяем выделение до конца используемого диапазона
        cursor.go_to_end_of_used_area(expand=True)
        print("✓ Выделение расширено до конца используемого диапазона")

        # 6. Находим объект диапазона, выделенный курсором
        range_obj = cursor.find_used_range_obj()
        cell_range = sheet.get_range(range_obj=range_obj)

        # 7. Применяем стили к найденному диапазону
        cursor_style = [
            Font(size=12, b=True, color=StandardColor.WHITE),
            BgColor(color=StandardColor.GREEN),
        ]
        Lo.delay(2000)
        cell_range.apply_styles(*cursor_style)
        print("✓ Стили применены к диапазону, найденному курсором")

        Lo.delay(1000)
        # 8. Сохраняем документ
        doc.save_doc("cursor_example.ods")


if __name__ == "__main__":
    main()
