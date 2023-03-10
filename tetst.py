import requests
from bs4 import BeautifulSoup as bs
import codecs
import fake_useragent

class Parse():
    def req(self, url, header=fake_useragent.UserAgent().random):
        user = {
            'user-agent': header
        }
        self.s = requests.Session()
        self.res = self.s.get(url=url, headers=user)

    def parsing_text(self, contener, category) -> str:
        self.soup = bs(self.res.text, "html.parser")
        with codecs.open('parser_site.txt', 'a+', 'utf-8') as self.file:
            for i in self.soup.find_all(contener, class_= category):
                self.file.write(i.text + '\n')
    
    def parsing_href(self, contener, category) -> str:
        self.soup = bs(self.res.text, "html.parser")
        with codecs.open('parser_site.txt', 'a+', 'utf-8') as self.file:
            for i in self.soup.find_all(contener, class_= category):
                self.file.write(str(i.get('href')) + '\n')
    
    def parsing_img(self, contener, category) -> bytes:
        self.soup = bs(self.res.text, "html.parser")
        self.mas = []
        for i in self.soup.find_all(contener, class_= category):
            self.mas.append(i.get('src'))
        print(self.mas)
        for i in range(len(self.mas)):
            with open(f'parser_img{i+1}.jpg', 'wb+') as self.file:
                    self.img = requests.get(url=self.mas[i])
                    self.file.write(self.img.content)
parse = Parse()