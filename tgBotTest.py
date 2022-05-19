import telebot
import requests
from bs4 import BeautifulSoup

url = ''
bot = telebot.TeleBot('')


def search(text):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    words = soup.find('div', class_='tpl-block-list-objects tpl-block-171-list')
    data = words.text.strip().split('\n')
    for line in data:
        if text.lower() in line.lower():
            return line
    return 'Не найдено'


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Сонник')
    else:
        chat_id = message.from_user.id
        text = message.text
        response = search(text=text)
        bot.send_message(chat_id, response)


bot.polling(none_stop=True)
