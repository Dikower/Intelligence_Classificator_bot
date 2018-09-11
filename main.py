from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Определяем функцию-обработчик сообщений.
# У нее два параметра, сам бот и класс updater, принявший сообщение.

answers = {"Да": 2, "Скорее да": 1, "Скорее нет": -1, "Нет": -2}


def start(bot, update, user_data):
    user_data = {"Лингвистический": 0,
                 "Математико-логический": 0,
                 "Визуально-пространственный": 0,
                 "Музыкальный": 0,
                 "Межличностный": 0,
                 "Внутриличностный": 0,
                 "Кинестетический": 0}

    update.message.reply_text('Я бот-классификатор интеллекта. Данный тест поможет определить ваш тип интеллекта из 7 предложенных по метрике  Пройдите опрос из 28 вопросов')


def echo(bot, update, user_data):
    # У объекта класса Updater есть поле message, являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str), отсылающий ответ пользователю, от которого получено сообщение.
    # update.message.reply_text(f'Our number is {user_data["i"]}')
    update.message.reply_text('Я получил сообщение "{}".'.format(update.message.text))


def ask_1(bot, update, user_data):  #TODO
    if update.message.text in answers.keys():
        user_data["Кинестетический"] += answers[update.message.text]
        update.message.reply_text("1/28 У меня хорошее чувство направления.")
    else:
        update.message.reply_text(f"Введите одно из предложенного: {', '.join(list(answers.keys()))}.")
        return None


def ask_2(bot, update, user_data):
    if update.message.text in answers.keys():
        user_data["Кинестетический"] += answers[update.message.text]
        update.message.reply_text("2/28 У меня хорошее чувство направления.")
    else:
        update.message.reply_text(f"Введите одно из предложенного: {', '.join(list(answers.keys()))}.")
        return None


def ask_3(bot, update, user_data):
    if update.message.text in answers.keys():
        user_data["Визуально-пространственный"] += answers[update.message.text]
        update.message.reply_text("3/28 У меня есть естественная способность решать споры между друзьями.")
    else:
        update.message.reply_text(f"Введите одно из предложенного: {', '.join(list(answers.keys()))}.")
        return None


def ask_4(bot, update, user_data):
    if update.message.text in answers.keys():
        user_data["Межличностный"] += answers[update.message.text]
        update.message.reply_text("4/28 Я могу легко запоминать слова песен.")
    else:
        update.message.reply_text(f"Введите одно из предложенного: {', '.join(list(answers.keys()))}.")
        return None


def ask_5(bot, update, user_data):
    if update.message.text in answers.keys():
        user_data["Музыкальный"] += answers[update.message.text]
        update.message.reply_text("5/28 Я могу объяснять темы, которые другим объяснять тяжело.")
    else:
        update.message.reply_text(f"Введите одно из предложенного: {', '.join(list(answers.keys()))}.")
        return None


def main():
    # Создаем объект updater. Вместо слова "TOKEN" надо разместить полученнй от @BotFather токен
    address = "178.76.203.134"
    port = 9999
    username = "telegram"
    password = "yandexlyceum"

    token = "576442066:AAG5q87UGk9KCCTcHRpLXt13dOkUSlMuuDw"
    updater = Updater(token, request_kwargs={'proxy_url': f'socks5://{address}:{port}/',
                                             'urllib3_proxy_kwargs': {'username': username,
                                                                      'password': password}})

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    # Создаем обработчик сообщений типа Filters.text из описанной выше функции echo()
    # Таким образом после регистрации обработчика в диспетчере,
    # эта функция будет вызываться при получении сообщения с типом "текст", т.е. текстовых сообщений.
    # Регистрируем обработчик в диспетчере.
    dp.add_handler(MessageHandler(Filters.text, echo, pass_user_data=True))
    dp.add_handler(CommandHandler("start", start, pass_user_data=True))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждем завершения приложения. (например, получение сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
