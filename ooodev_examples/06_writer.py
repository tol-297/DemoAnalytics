from pathlib import Path
from ooodev.loader.lo import Lo
from ooodev.write import WriteDoc

BASE_DIR = Path(__file__).resolve().parent

def main():
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Получаем путь к шаблону
        template_path = BASE_DIR / "template_invoice.ott"

        if not template_path.exists():
            print(f"❌ Шаблон не найден: {template_path}")
            return

        # 2. Создаем документ из шаблона
        doc = WriteDoc.create_doc_from_template(template_path)
        print(f"✓ Документ создан из шаблона: {template_path}")

        # 3. Получаем курсор для работы с документом
        cursor = doc.get_cursor()

        # 4. Заполняем данные в закладки

        # Ищем закладку InvoiceNumber и устанавливаем значение
        bookmark_invoice = doc.find_bookmark("InvoiceNumber")
        if bookmark_invoice:
            cursor.goto_range(bookmark_invoice.get_anchor())
            cursor.append("2024-001")
            print("✓ Номер счета заполнен: 2024-001")

        # Ищем закладку ClientName
        bookmark_client = doc.find_bookmark("ClientName")
        if bookmark_client:
            cursor.goto_range(bookmark_client.get_anchor())
            cursor.append("ООО 'Вектор Плюс'")
            print("✓ Имя клиента заполнено: ООО 'Вектор Плюс'")

        # Ищем закладку Date
        bookmark_date = doc.find_bookmark("Date")
        if bookmark_date:
            cursor.goto_range(bookmark_date.get_anchor())
            cursor.append("09.06.2026")
            print("✓ Дата заполнена: 09.06.2026")

        # Ищем закладку TotalAmount
        bookmark_total = doc.find_bookmark("TotalAmount")
        if bookmark_total:
            cursor.goto_range(bookmark_total.get_anchor())
            cursor.append("125 000 руб.")
            print("✓ Итоговая сумма заполнена: 125 000 руб.")

        # 5. Сохраняем документ
        output_path = "invoice_output.odt"
        doc.save_doc(output_path)
        print(f"\n✓ Документ успешно сохранен: {output_path}")
        print("  - Создан из шаблона template_invoice.ott")
        print("  - Заполнены все закладки")

        # 6. Закрываем документ
        doc.close_doc()


if __name__ == "__main__":
    main()



