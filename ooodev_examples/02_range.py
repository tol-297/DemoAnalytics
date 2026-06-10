"""
Демонстрация работы с диапазонами (Range) в LibreOffice Calc.

Основные операции:
- Создание документа
- Получение диапазона через get_range()
- Запись данных в диапазон с помощью set_array()
- Сохранение документа
"""

from ooodev.loader.lo import Lo
from ooodev.calc import CalcDoc


def main():
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем новый документ Calc
        doc = CalcDoc.create_doc()
        sheet = doc.get_active_sheet()

        # 2. Данные для заполнения
        headers = ["ID", "Название", "Цена", "Количество"]
        data = [
            [1, "Яблоки", 100, 10],
            [2, "Бананы", 80, 15],
            [3, "Вишня", 200, 5],
            [4, "Апельсины", 120, 8],
        ]

        # 3. Получаем диапазон и записываем заголовки
        header_range = sheet.get_range(range_name="A1:D1")
        header_range.set_array([headers])  # set_array требует 2D массив

        # 4. Получаем диапазон для данных и записываем их
        data_range = sheet.get_range(range_name="A2:D5")
        data_range.set_array(data)

        # 5. Сохраняем документ
        doc.save_doc("range_example.ods")
        print("✓ Документ успешно создан: range_example.ods")
        print(f"  - Добавлено {len(headers)} заголовков")
        print(f"  - Добавлено {len(data)} строк данных")


if __name__ == "__main__":
    main()

