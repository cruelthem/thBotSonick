import telebot
# import requests
# from bs4 import BeautifulSoup

# url = 'https://bujan.ru/tainstvo/tolkovaniya/sonnik/'
#
# page = requests.get(url)
#
# soup = BeautifulSoup(page.text, 'lxml')
#
# words = soup.find('div', class_='tpl-block-list-objects tpl-block-171-list')
# print(words.text.strip())

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.char.id, 'Hello')

bot.polling(none_stop=True)
