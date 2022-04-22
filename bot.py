from random import randint
from datetime import datetime
import pandas as pd
import pywhatkit
import os


def get_random_news() -> str:
    """
    Busca 5 noticias aleatorias en un excel, las organiza en un
    mensaje y las elimina del excel

        Parametros:
            None
            
        Returns:
            msg : mensaje con noticias organizadas

    """
    #Craga de datos
    df = pd.read_excel(r'data/scraped_data.xlsx')
    shape = df.shape[0]

    to_select = []

    #Seleccion de noticias a mostrar
    while len(to_select) < 5:
        num = randint(0, shape)
        if not num in to_select:
            to_select.append(num)

    news = df.iloc[to_select]

    #Eliminar noticias mostradas del excel
    df = df.drop(to_select, axis=0)

    os.remove(r'data/scraped_data.xlsx')
    df.to_excel(r'data/scraped_data.xlsx', index = True)

    #Creacion de mensaje
    news = news.to_dict()
    #pprint(news)

    msg = "Este es tu boletin de noticias diario:\n\n"

    for i in to_select:
        msg += news['Titulos'][i] + ':\n'
        msg += news['Descripciones'][i] + '\n'
        msg += "Link: " + news['Links'][i] + '\n\n'

    msg += "Esperamos sean de tu interes :)"

    return msg

#Configuracion tiempos envio
h, m = datetime.now().strftime('%H %M').split()

for i in range(30):
    msg = get_random_news()
    pywhatkit.sendwhatmsg_to_group("ByQzurLTzEVLsrTMOJ8KTE", msg, int(h), int(m)+2, 60, True, 5)