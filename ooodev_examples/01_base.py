import sys
from ooodev.loader.lo import Lo
from ooodev.calc import CalcDoc


def main():
    delay = 1500
    with Lo.Loader(connector=Lo.ConnectPipe()):
        doc = CalcDoc.create_doc(visible=True)
        # TODO: измените на visible=False и запустите
        sheet = doc.get_active_sheet()

        # Записываем данные с задержкой после каждой операции
        sheet["A1"].value = "ID Студента"
        Lo.delay(delay)

        sheet["B1"].value = "Статус"
        Lo.delay(delay)

        sheet["A2"].value = 101
        Lo.delay(delay)

        sheet["B2"].value = "Сдал"
        Lo.delay(delay * 2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
