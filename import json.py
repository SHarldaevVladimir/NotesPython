import json
import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана.")

# Функция для просмотра всех заметок
def view_notes():
    if len(notes) == 0:
        print("Нет доступных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print("-------------------------")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Основная функция для работы с приложением
def main():
    global notes
    notes = read_notes()

    while True:
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")
        print("-------------------------")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск приложения
if __name__ == "__main__":
    main()