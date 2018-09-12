#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import matplotlib.patheffects as path_effects

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, ConversationHandler
import matplotlib.pyplot as plt



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


answers = {"Да": 2, "Скорее да": 1, "Скорее нет": -1, "Нет": -2}
keyboard = [[InlineKeyboardButton("Да", callback_data="Да"),
             InlineKeyboardButton("Скорее да", callback_data="Скорее да"),
             InlineKeyboardButton("Скорее нет", callback_data="Скорее нет"),
             InlineKeyboardButton("Нет", callback_data="Нет")]]

reply_markup = InlineKeyboardMarkup(keyboard)
start_button = InlineKeyboardMarkup([[InlineKeyboardButton("Начать тест", callback_data="start")]])

meaning = {"Лингвистический": "Скорее всего Вам нравится писать, читать и слушать. Вам следовало бы обратить на "
                              "такие виды деятельности, как проведение докладов, написание литературы, дебаты.",
           "Математико-логический": "Вероятно Вы быстро решаете арифметические задача, любите анализировать данные." 
                                    "Вам рекомендуется упражнятся в  построении логических цепочек, построении "
                                    "графиков, экспериментах.",
           "Визуально-пространственный": "Видимо Вы мыслите образами и любите рисовать, красить, лепить, "
                                          "рассматривать. Хорошо воспринимаете карты и диаграммы. Вам советуется "
                                          "заняться рисованием, фотографией, черчением.",
           "Музыкальный": "Скорее всего Вы чувствительны к разнообразию звуков в окружающей среде, "
                          "имеете хорошее чувство ритма. Вам следовало бы заняться игрой на музыкальном инструменте "
                          "или пением.",
           "Внутриличностный": "Похоже, что Вы сильно погружены в свой мир и демонстрируете чувство независимости. Вам "
                               "рекомендуется заняться самостоятельной работой/исследованиями, написанием литературы,"
                               " мысленными экспериментами.",
           "Межличностный": "Видимо Вы открытый человек и любите находиться в кругу людей, имеете много друзей."
                            "Вы могли бы попробовать себя в работе в команде, участии в дебатах,"
                            "интервьюировании",
           "Кинестетический": "Похоже, что вы отлично владеете своим телом и хорошо манипулируете предметами. "
                              "Попробуйте заняться спортом, танцами."}


def start(bot, update, user_data):
    user_data["Лингвистический"] = 0
    user_data["Математико-логический"] = 0
    user_data["Визуально-пространственный"] = 0
    user_data["Музыкальный"] = 0
    user_data["Межличностный"] = 0
    user_data["Внутриличностный"] = 0
    user_data["Кинестетический"] = 0
    update.message.reply_text(
        'Я бот-классификатор интеллекта. Данный опрос поможет определить ваш тип интеллекта из 7 предложенных '
        'по метрике Гарднера. Здесь будет дано 28 предложений, нажимайте на утверждения, которые наибольшим образом '
        'соответствуют Вам. Нажмите на кнопку, чтобы начать тест.',
        reply_markup=start_button)
    return 1


def message(bot, update):
    update.message.reply_text('Чтобы ответить на вопросы нажимайте на кнопки. Писать не нужно.')


def ask_1(bot, update):  # TODO
    query = update.callback_query

    bot.edit_message_text(text="|1 из 28| Я умело работаю с предметами.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 2


def ask_2(bot, update, user_data):
    query = update.callback_query
    user_data["Кинестетический"] += answers[query.data]
    bot.edit_message_text(text="|2 из 28| У меня хорошее чувство направления.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 3


def ask_3(bot, update, user_data):
    query = update.callback_query
    user_data["Визуально-пространственный"] += answers[query.data]
    bot.edit_message_text(text="|3 из 28| У меня есть естественная способность решать споры между друзьями.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 4


def ask_4(bot, update, user_data):
    query = update.callback_query
    user_data["Межличностный"] += answers[query.data]
    bot.edit_message_text(text="|4 из 28| Я могу легко запоминать слова песен.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 5


def ask_5(bot, update, user_data):
    query = update.callback_query
    user_data["Музыкальный"] += answers[query.data]
    bot.edit_message_text(text="|5 из 28| Я могу объяснять темы, которые другим объяснять тяжело.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 6


def ask_6(bot, update, user_data):
    query = update.callback_query
    user_data["Лингвистический"] += answers[query.data]
    bot.edit_message_text(text="|6 из 28| Я всегда делаю все поэтапно.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 7


def ask_7(bot, update, user_data):
    query = update.callback_query
    user_data["Математико-логический"] += answers[query.data]
    bot.edit_message_text(text="|7 из 28| Я хорошо знаю себя и всегда понимаю, почему я поступаю так, а не иначе.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 8


def ask_8(bot, update, user_data):
    query = update.callback_query
    user_data["Внутриличностный"] += answers[query.data]
    bot.edit_message_text(text="|8 из 28| Мне нравится работа с общественностью и общественные мероприятия.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 9


def ask_9(bot, update, user_data):
    query = update.callback_query
    user_data["Межличностный"] += answers[query.data]
    bot.edit_message_text(text="|9 из 28| Я хорошо учусь, слушая других.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 10


def ask_10(bot, update, user_data):
    query = update.callback_query
    user_data["Лингвистический"] += answers[query.data]
    bot.edit_message_text(text="|10 из 28| Когда я слушаю музыку, у меня меняется настроение.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 11


def ask_11(bot, update, user_data):
    query = update.callback_query
    user_data["Музыкальный"] += answers[query.data]
    bot.edit_message_text(text="|11 из 28| Мне нравятся загадки, кроссворды, логические задачи.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 12


def ask_12(bot, update, user_data):
    query = update.callback_query
    user_data["Математико-логический"] += answers[query.data]
    bot.edit_message_text(text="|12 из 28| Для моего обучения очень важно визуальное представление материала: таблицы, "
                               "графики, схемы.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 13


def ask_13(bot, update, user_data):
    query = update.callback_query
    user_data["Визуально-пространственный"] += answers[query.data]
    bot.edit_message_text(text="|13 из 28| Я чувствителен к настроению и переживаниям окружающих.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 14


def ask_14(bot, update, user_data):
    query = update.callback_query
    user_data["Межличностный"] += answers[query.data]
    bot.edit_message_text(text="|14 из 28| Я учусь лучше, когда мне что-то нужно делать самостоятельно.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 15


def ask_15(bot, update, user_data):
    query = update.callback_query
    user_data["Кинестетический"] += answers[query.data]
    bot.edit_message_text(text="|15 из 28| Перед тем как учить что-то, мне нужно понимать, "
                               "что в этом есть что-то нужное.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 16


def ask_16(bot, update, user_data):
    query = update.callback_query
    user_data["Внутриличностный"] += answers[query.data]
    bot.edit_message_text(text="|16 из 28| Я люблю одиночество и тишину во время работы и размышлений.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 17


def ask_17(bot, update, user_data):
    query = update.callback_query
    user_data["Внутриличностный"] += answers[query.data]
    bot.edit_message_text(text="|17 из 28| В сложных музыкальных произведениях я могу на слух вычленить отдельные "
                               "музыкальные инструменты.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 18


def ask_18(bot, update, user_data):
    query = update.callback_query
    user_data["Музыкальный"] += answers[query.data]
    bot.edit_message_text(text="|18 из 28| Я могу зрительно легко представить сцены, которые я помню, "
                               "или которые я придумал.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 19


def ask_19(bot, update, user_data):
    query = update.callback_query
    user_data["Визуально-пространственный"] += answers[query.data]
    bot.edit_message_text(text="|19 из 28| У меня богатый словарный запас.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 20


def ask_20(bot, update, user_data):
    query = update.callback_query
    user_data["Лингвистический"] += answers[query.data]
    bot.edit_message_text(text="|20 из 28| Я люблю делать записи, письменные зарисовки.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 21


def ask_21(bot, update, user_data):
    query = update.callback_query
    user_data["Лингвистический"] += answers[query.data]
    bot.edit_message_text(text="|21 из 28| У меня хорошее чувство равновесия, я люблю движение.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 22


def ask_22(bot, update, user_data):
    query = update.callback_query
    user_data["Кинестетический"] += answers[query.data]
    bot.edit_message_text(text="|22 из 28| Я могу видеть закономерности между понятиями и явлениями.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 23


def ask_23(bot, update, user_data):
    query = update.callback_query
    user_data["Математико-логический"] += answers[query.data]
    bot.edit_message_text(text="|23 из 28| В команде я сотрудничаю с другими, прислушиваюсь к их идеям.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 24


def ask_24(bot, update, user_data):
    query = update.callback_query
    user_data["Межличностный"] += answers[query.data]
    bot.edit_message_text(text="|24 из 28| Я наблюдателен и часто вижу то, что не видят другие.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 25


def ask_25(bot, update, user_data):
    query = update.callback_query
    user_data["Визуально-пространственный"] += answers[query.data]
    bot.edit_message_text(text="|25 из 28| Меня легко вывести из себя.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 26


def ask_26(bot, update, user_data):
    query = update.callback_query
    user_data["Кинестетический"] += answers[query.data]
    bot.edit_message_text(text="|26 из 28| Я люблю работать и учиться отдельно от других.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 27


def ask_27(bot, update, user_data):
    query = update.callback_query
    user_data["Внутриличностный"] += answers[query.data]
    bot.edit_message_text(text="|27 из 28| Я люблю сочинять музыку.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 28


def ask_28(bot, update, user_data):
    query = update.callback_query
    user_data["Музыкальный"] += answers[query.data]
    bot.edit_message_text(text="|28 из 28| Я могу оперировать числами и решать сложные математические задачи.",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=reply_markup)
    return 29


def finish(bot, update, user_data):
    query = update.callback_query
    user_data["Математико-логический"] += answers[query.data]
    intelligence_type = max(user_data.keys(), key=lambda x: user_data[x])
    bot.edit_message_text(text=f'Благодарим за прохождение теста! '
                               f'Вероятнее всего у вас "{intelligence_type}" тип интеллекта. '
                               + meaning[intelligence_type]
                               + '\nНад ботом работали:\n'
                                 'Дин Дмитрий, Гордовой Денис, Мельников Константин, Абдулмаликов Максуд, Петров Данил',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

    try:
        with open("intelligence_statistics.json", "r", encoding="utf8") as file:
            data_base = json.loads(file.read())

    except FileNotFoundError:
        data_base = {"Лингвистический": 0,
                     "Математико-логический": 0,
                     "Визуально-пространственный": 0,
                     "Музыкальный": 0,
                     "Межличностный": 0,
                     "Внутриличностный": 0,
                     "Кинестетический": 0}

    data_base[intelligence_type] += 1
    try:
        with open("intelligence_statistics.json", "w", encoding="utf8") as file:
            file.write(json.dumps(data_base))
    except:
        print("Вторая попытка записать файл!")
        with open("intelligence_statistics.json", "w", encoding="utf8") as file:
            file.write(json.dumps(data_base))

    send_pie(bot, update, data_base)


def send_pie(bot, update, data):
    colors = ['yellowgreen', 'lightskyblue', 'gold', 'lightcoral', 'seagreen', 'lightsteelblue', 'lightpink']
    explode = [0.01 for _ in range(7)]
    print(data)
    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)
    plt.axis('off')
    plt.title("Статистика по представителям 7 классов интеллекта")
    patches, text, auto_texts = ax.pie(data.values(),
                                       colors=colors,
                                       explode=explode,
                                       # labels=a.keys(),
                                       autopct='%1.1f%%',
                                       startangle=90,
                                       radius=0.4,
                                       wedgeprops={"linewidth": 6, },
                                       shadow=True,
                                       center=(0.5, 0.5),
                                       frame=True,
                                       pctdistance=1.125,
                                       )

    for patch in patches:
        patch.set_path_effects([path_effects.SimpleLineShadow(),
                                path_effects.Normal()])
    user_id = str(update.effective_user.id)
    plt.legend(data.keys())
    plt.savefig(user_id + ".png")
    bot.send_photo(chat_id=user_id, photo=open(user_id + ".png", 'rb'))


def stop(bot, update):
    update.message.reply_text("Прохождение теста приостановлено. Чтобы начать заново введите /start")
    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    token = "642728632:AAHYboT2irnD-ttxW377cLGccHM6PQF8PnI"
    updater = Updater(token)

    conv_handler = ConversationHandler(
        # Без изменений
        entry_points=[CommandHandler('start', start, pass_user_data=True)],
        # per_message=True,

        states={
            # Добавили user_data для сохранения ответа.
            1: [CallbackQueryHandler(ask_1)],
            2: [CallbackQueryHandler(ask_2, pass_user_data=True)],
            3: [CallbackQueryHandler(ask_3, pass_user_data=True)],
            4: [CallbackQueryHandler(ask_4, pass_user_data=True)],
            5: [CallbackQueryHandler(ask_5, pass_user_data=True)],
            6: [CallbackQueryHandler(ask_6, pass_user_data=True)],
            7: [CallbackQueryHandler(ask_7, pass_user_data=True)],
            8: [CallbackQueryHandler(ask_8, pass_user_data=True)],
            9: [CallbackQueryHandler(ask_9, pass_user_data=True)],
            10: [CallbackQueryHandler(ask_10, pass_user_data=True)],
            11: [CallbackQueryHandler(ask_11, pass_user_data=True)],
            12: [CallbackQueryHandler(ask_12, pass_user_data=True)],
            13: [CallbackQueryHandler(ask_13, pass_user_data=True)],
            14: [CallbackQueryHandler(ask_14, pass_user_data=True)],
            15: [CallbackQueryHandler(ask_15, pass_user_data=True)],
            16: [CallbackQueryHandler(ask_16, pass_user_data=True)],
            17: [CallbackQueryHandler(ask_17, pass_user_data=True)],
            18: [CallbackQueryHandler(ask_18, pass_user_data=True)],
            19: [CallbackQueryHandler(ask_19, pass_user_data=True)],
            20: [CallbackQueryHandler(ask_20, pass_user_data=True)],
            21: [CallbackQueryHandler(ask_21, pass_user_data=True)],
            22: [CallbackQueryHandler(ask_22, pass_user_data=True)],
            23: [CallbackQueryHandler(ask_23, pass_user_data=True)],
            24: [CallbackQueryHandler(ask_24, pass_user_data=True)],
            25: [CallbackQueryHandler(ask_25, pass_user_data=True)],
            26: [CallbackQueryHandler(ask_26, pass_user_data=True)],
            27: [CallbackQueryHandler(ask_27, pass_user_data=True)],
            28: [CallbackQueryHandler(ask_28, pass_user_data=True)],
            29: [CallbackQueryHandler(finish, pass_user_data=True)],
        },

        # Без изменений
        fallbacks=[CommandHandler('stop', stop)])

    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
