# pip install pyTelegramBotAPI
# pip install requests
# pip install beautifulsoup4
# pip install nltk

import telebot
import requests
from bs4 import BeautifulSoup as bbss
import time
import codecs
import string
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

t = 1.5
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}

TOKEN = 'need paste token'
#nltk.download('punkt')
#nltk.download('stopwords')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"Привет <u><b>{message.from_user.first_name}</b></u>, отправь команду /get и *ссылку на страницу*", parse_mode="html")

@bot.message_handler(commands=['get'])
def send_welcome(message):
    print(message.text.split(' '))
    link = message.text.split(' ')
    url = link[1]
    s = requests.Session()
    r = s.get(url, headers=header)
    time.sleep(t)
    print(r.status_code)
    soup = bbss(r.text, 'html.parser')
    time.sleep(t)
    links = soup.get_text()
    a = len(links)
    links = links.lower()
    spec_chars = string.punctuation + '\n\xa0«»\t—…'
    links = "".join([ch for ch in links if ch not in spec_chars])
    text_tokens = word_tokenize(links)
    russian_stopwords = stopwords.words("russian")
    russian_stopwords.extend(['это', 'нею'])
    text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
    links = nltk.Text(text_tokens)
    fdist_sw = FreqDist(links)
    b = fdist_sw.most_common(10)
    with codecs.open("Article.txt", "w+", "utf-8") as f:
        f.write(str(a) + " слов на этом сайте\nСамые частые " + str(b))
    fil = open('Article.txt', 'rb+')
    bot.send_document(message.chat.id, document=fil)

bot.polling(none_stop=True)