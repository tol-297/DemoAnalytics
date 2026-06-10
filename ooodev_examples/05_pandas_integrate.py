"""
Демонстрация интеграции pandas с LibreOffice Calc через ooodev.

Основные операции:
- Создание pandas DataFrame
- Запись DataFrame в LibreOffice Calc
- Применение стилей к данным из pandas
- Сохранение в файл ODS
"""

from ooodev.loader.lo import Lo
from ooodev.calc import CalcDoc
import pandas as pd
from ooodev.utils.color import StandardColor, Color
from ooodev.format.calc.direct.cell.font import Font
from ooodev.format.calc.direct.cell.background import Color as BgColor


def main():
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем pandas DataFrame
        df = pd.DataFrame({
            "Продукт": ["Яблоки", "Бананы", "Вишня", "Апельсины"],
            "Цена": [100, 80, 200, 120],
            "Количество": [10, 15, 5, 8],
            "Сумма": [1000, 1200, 1000, 960],
        })

        # 2. Создаем новый документ Calc
        doc = CalcDoc.create_doc()
        sheet = doc.get_active_sheet()

        # 3. Подготавливаем данные: заголовки + строки
        data = [df.columns.tolist()] + df.values.tolist()

        # 4. Записываем данные начиная с A1
        sheet.set_array(name='A1', values=data)
        print(f"✓ Данные из pandas записаны: {len(df)} строк")

        # 5. Применяем стили к заголовку
        header_style = [
            Font(size=12, b=True, color=StandardColor.WHITE),
            BgColor(color=StandardColor.BLUE),
        ]
        sheet.get_range(range_name=f"A1:D1").apply_styles(*header_style)
        print("✓ Заголовок стилизован")

        # 6. Применяем стили к данным
        data_style = [
            Font(size=11),
            BgColor(color=Color(0xF5F5F5)),
        ]
        num_rows = len(df)
        sheet.get_range(range_name=f"A2:D{num_rows+1}").apply_styles(*data_style)
        print("✓ Данные стилизованы")


        # 8. Вычисляем статистику из pandas
        print("\nСтатистика по данным:")
        print(df.describe())

        # 9. Сохраняем документ
        doc.save_doc("pandas_example.ods")
        print("\n✓ Документ успешно создан: pandas_example.ods")


if __name__ == "__main__":
    main()

