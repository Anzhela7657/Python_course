@bot.message_handler(commands=['newrequest'])
def handle_new_request(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Пропуск таксі")
    button2 = types.KeyboardButton(text="Проблема парковки")
    button3 = types.KeyboardButton(text="Пропуск гостей")
    button4 = types.KeyboardButton(text="Пропуск кур'єра")
    button5 = types.KeyboardButton(text="Заявка на інше")
    button6 = types.KeyboardButton(text="Скасувати")
    keyboard.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Оберіть тип заявки:", reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text in ["Пропуск таксі", "Проблема парковки", "Пропуск гостей", "Пропуск кур'єра", "Заявка на інше"])
def handle_request_type(message):
    request_type = message.text
    user_id = message.from_user.id
    match request_type:
        case "Пропуск таксі":
            bot.send_message(message.chat.id, "Введіть номер автомобіля таксі:")
        case "Пропуск кур'єра":
            bot.send_message(message.chat.id, "Введіть номер автомобіля кур'єра:")
        case "Пропуск гостей":
            bot.send_message(message.chat.id, "Введіть номер автомобіля або оберіть варіант 'гості без авто':")
        case "Проблема парковки":
            bot.send_message(message.chat.id, "Введіть номер автомобіля порушника:")
        case "Заявка на інше":
            bot.send_message(message.chat.id, "Напишіть текст заявки або прикріпіть фото, місцезнаходження або надішліть файл:")

    @bot.message_handler(func=lambda message: True)
    def handle_request_details(message):
        additional_info = message.text

        bot.send_message(message.chat.id, 'Дякуємо! Ваша заявка була успішно збережена.')
    bot.register_next_step_handler(message, handle_request_details)
