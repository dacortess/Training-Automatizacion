from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class Boxes_Scraper:
    def __init__(self):
        self.url = str()
        self.url_base = str()
        self.boxes_info = dict()
        self.title_info = dict()
        self.link_info = dict()
        self.text_info = dict()
        self.comunidad = str()

    def set_info(self, url: str, news_info: list, comunidad: str) -> None:
        """
        Carga la informacion necesaria para hacer el scraping

            Parametros:
                url         : url del sitio a scrapear
                news_info   : Informacion sobre la ubicacion de
                              lo que queremos scrapear
                comunidad   : Comunidad a la que pertenece
                              la url
            
            Returns:
                None

        """
        self.comunidad = comunidad
        self.url = url
        self.url_base = self.get_url_base()

        # {'object' : 'object type', 'class' : {'class' : 'class_name'} }
        self.boxes_info = news_info[0]

        # {'object' : 'object type' , 'class' : {'class' : 'class_name'} , 
        #  'regex' : 'regular expression' , slice: [param, param] }
        self.title_info = news_info[1]
        self.link_info = news_info[2]
        self.text_info = news_info[3]
    
    def get_url_base(self) -> str:
        """
        Retorna el dominio de la web a scrapear

            Parametros:
                None
            
            Returns:
                base_url : domino con la forma https://xxxxx.com

        """
        url_base = self.url.split("/")
        url_base = "".join([url_base[0],"//",url_base[2]])
        
        return url_base
    
    def create_soup(self, url) -> BeautifulSoup:
        """
        Crea un objeto de bs4 especifico para una url dada

            Parametros:
                url : url de la pagina a scrapear
            
            Returns:
                soup : objeto de bs4

        """
        try:
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
        except:
            page = urlopen(url)
            html = page.read().decode("latin-1")
            soup = BeautifulSoup(html, "html.parser")
        
        return soup

    def get_data(self) -> list:
        """
        Carga la informacion necesaria para hacer el scraping

            Parametros:
                None
            
            Returns:
                news : Listado de noticias encontradas en el sitio

        """
        
        soup = self.create_soup(self.url)
        news = list()

        #Busca todas las cajas con noticias
        boxes = soup.find_all( self.boxes_info['object'] , self.boxes_info['class'] )

        num_bx = len(boxes)

        if self.boxes_info["length"] != 0: num_bx = self.boxes_info["length"]

        for b in range(num_bx):
            if self.boxes_info['skip']-1 == b:
                continue

            soup = BeautifulSoup(str(boxes[b]), 'html.parser')

            #Busca el link de la noticia
            box_link = soup.find_all(  self.link_info['object'] , self.link_info['class'] )[self.link_info['index']]
            regex_link = re.compile( self.link_info['regex'] )
            link =  regex_link.findall(str(box_link))[0][ self.link_info['slice'][0] : self.link_info['slice'][1] ]

            if link[0] == "/":
                link = self.url_base + link
            if link[0:3] == "www":
                link = "https://" + link

            soup2 = self.create_soup(link)

            box_title = soup2.find_all( self.title_info['object'] , self.title_info['class'] )[self.title_info['index']]
            regex_title =   re.compile( self.title_info['regex'] )
            title = regex_title.findall(str(box_title))[0][ self.title_info['slice'][0] : self.title_info['slice'][1] ]

            box_text = soup2.find_all(  self.text_info['object'] , self.text_info['class'] )[self.text_info['index']]
            regex_text =    re.compile( self.text_info['regex'] )
            text =  regex_text.findall(str(box_text).rstrip("\t").rstrip("\r"))   [0][ self.text_info['slice'][0] : self.text_info['slice'][1] ]
            
            #Guarda la informacion de la noticia
            news.append( {'Comunidad' : self.comunidad , 'Titulos' : title, 'Links' : link, 'Descripciones' : text} )

        return news
    


