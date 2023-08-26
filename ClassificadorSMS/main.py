import pickle
import string

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from nltk.corpus import stopwords


def process_text(text):
    sem_pontuacao = [char for char in text if char not in string.punctuation]
    sem_pontuacao = ''.join(sem_pontuacao)
    lista_palavras = [word for word in sem_pontuacao.split() if word.lower() not in stopwords.words('english')]
    return lista_palavras


class RootWidget(BoxLayout):
    def prever(self):
        sms = str(self.sms.text)
        sms_processado = process_text(sms)
        sms_vectorizado = bow.transform([" ".join(sms_processado)])
        resultado = model.predict(sms_vectorizado)[0]
        if resultado == 1:
            self.classificacao.text = 'O SMS é classificado como SPAM.'
        else:
            self.classificacao.text = 'O SMS NÃO é SPAM.'


class Main(App):
    def build(self):
        return RootWidget()


# Desserelializando os dados
model = pickle.load(open("model.pkl", "rb"))
bow = pickle.load(open("bow.pkl", "rb"))

Main().run()
