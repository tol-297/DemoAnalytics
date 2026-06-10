from ooodev.loader.lo import Lo
from ooodev.write import WriteDoc


def create_invoice_template(file_name: str = "template_invoice.ott"):
    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем новый текстовый документ
        doc = WriteDoc.create_doc()

        # 2. Добавляем содержимое
        cursor = doc.get_cursor()
        cursor.append("СЧЕТ № ")
        cursor.add_bookmark("InvoiceNumber")  # Создаем закладку
        cursor.append("\n\nКому: ")
        cursor.add_bookmark("ClientName")
        cursor.append("\nДата: ")
        cursor.add_bookmark("Date")
        cursor.append("\n\nИтого к оплате: ")
        cursor.add_bookmark("TotalAmount")

        # 3. Сохраняем как шаблон (.ott)
        doc.save_doc(file_name)
        print(f"Шаблон {file_name} успешно создан!")

        # 4. Закрываем документ
        doc.close_doc()


# Запуск функции
create_invoice_template()