import time
import schedule

# Функция для входа в аккаунт
def login(username, password):
    # Здесь должен быть код для входа в аккаунт через TikTok API
    # Поскольку TikTok не предоставляет официального API, этот код будет пустым
    print(f"Вход в аккаунт {username}...")
    time.sleep(2)
    print("Вход выполнен успешно!")

# Функция для отправки сообщения
def send_message(username, message):
    # Здесь должен быть код для отправки сообщения через TikTok API
    # Поскольку TikTok не предоставляет официального API, этот код будет пустым
    print(f"Сообщение отправлено пользователю {username}: {message}")

# Основная функция
def main():
    # Запрос логина и пароля
    username = input("Ник: ")
    password = input("Пароль: ")

    # Вход в аккаунт
    login(username, password)

    # Список ников для отправки сообщений
    usernames = ["sronya322", "rya_ddminet2.0", "fearofwomen2", "slouechka", "maksyt_off", "ykaaky816"]

    # Сообщение, которое будет отправлено
    message = "Привет! Это автоматическое сообщение."

    # Отправка сообщений
    for username in usernames:
        send_message(username, message)
        time.sleep(1)  # Пауза между отправкой сообщений

    print("Все сообщения отправлены.")

# Планирование выполнения скрипта на 12:00
schedule.every().day.at("12:00").do(main)

# Бесконечный цикл для выполнения планировщика
while True:
    schedule.run_pending()
    time.sleep(1)