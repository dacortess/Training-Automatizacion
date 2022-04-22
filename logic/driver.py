from logic.scraper import Boxes_Scraper
import logic.pages_info as pg_info

class Driver():
    def __init__(self):
        self.bx_scraper = Boxes_Scraper()
        self.news_emprendedores = list()
        self.news_empresa = list()
        self.news_mipymes = list()

    def set_news_emprendedores(self, comunidad) -> None:
        """
        Busca noticias en las webs de la comunidad Emprendedores

            Parametros:
                comunidad   : Comunidad a la que pertenece
                              la url
            
            Returns:
                None

        """
        
        l = list()

        emp_seccion = pg_info.Portafolio()

        url = "https://www.portafolio.co/negocios/emprendimiento"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        emp_seccion = pg_info.Eleconomista()

        url = "https://www.eleconomista.es/pymes/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()
        
        emp_seccion = pg_info.Emprendedores_seccion()

        url = "https://www.emprendedores.es/seccion/guia-juridica-fiscal/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        url = "https://www.emprendedores.es/seccion/casos-de-exito/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        self.news_emprendedores = l

    def set_news_empresa(self, comunidad) -> None:
        """
        Busca noticias en las webs de la comunidad Emprendedores

            Parametros:
                comunidad   : Comunidad a la que pertenece
                              la url
            
            Returns:
                None

        """
        
        l = list()

        emp_seccion = pg_info.Iadb()

        url = "https://blogs.iadb.org/conocimiento-abierto/es/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        url = "https://blogs.iadb.org/ideas-que-cuentan/es/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        emp_seccion = pg_info.La_republica()

        url = "https://www.larepublica.co/responsabilidad-social"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        emp_seccion = pg_info.Bussines_dis()
        
        url = "http://www.businessanddisability.org/es/news-feed/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        self.news_empresa = l

    def set_news_mipymes(self, comunidad) -> None:
        """
        Busca noticias en las webs de la comunidad Emprendedores

            Parametros:
                comunidad   : Comunidad a la que pertenece
                              la url
            
            Returns:
                None

        """
        
        l = list()

        emp_seccion = pg_info.h4h()

        url = "https://www.humans4health.es/actualidad"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        emp_seccion = pg_info.bbva()

        url = "https://www.bbva.com/es/especiales/bbva-compartiendo-conocimiento/"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()

        emp_seccion = pg_info.Portafolio()

        url = "https://www.portafolio.co/innovacion"
        self.bx_scraper.set_info(url, emp_seccion.get_data(), comunidad)
        l += self.bx_scraper.get_data()


        self.news_mipymes = l
