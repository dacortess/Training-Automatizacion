
#EMPRENDEDORES

class Emprendedores_seccion():
    def __init__(self):
        self.boxes_info = {
            'object' : 'article',
            'class' : {'class' : 'full-item'},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'class' : 'entry-title' },
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'h2',
            'class' : {'class' : 'full-item-title item-title entry-title' },
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'div',
            'class' : {'class' : 'entry-content' },
            'regex' : ">.*?</p>" ,
            'slice' : [1 , -5],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

class Portafolio():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : 'listing-item', 'itemtype' : "https://schema.org/NewsArticle"},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'class' : 'title'},
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'h3',
            'class' : {'class' : 'listing-title', 'itemprop' : 'headline' },
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'p',
            'class' : {'class' : 'epigraph'},
            'regex' : ">.*?</p>" ,
            'slice' : [1 , -4],
            'index' : 0
            }
    
    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

class Eleconomista():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : "article rightSide"},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'class' : 'articleTitle'},
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'a',
            'class' : {'itemprop' : 'mainEntityOfPage'},
            'regex' : "href=\".*?\"" ,
            'slice' : [8 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'p',
            'class' : {'style' : ''},
            'regex' : "<p><p>.*?</p>" ,
            'slice' : [6 , -4],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

#EMPRESA Y DISCAPACIDAD

class Iadb():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'article',
            'class' : None,
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'class' : 'entry-title'},
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'a',
            'class' : {'class' : 'entry-title-link'},
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'div',
            'class' : {'class' : 'entry-content'},
            'regex' : "p>.*?</p" ,
            'slice' : [2 , -3],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

class La_republica():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : 'col-7 pl-3 pr-3'},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'div',
            'class' : {'class' : 'mb-auto'},
            'regex' : "\n<span>.*?</span>" ,
            'slice' : [7 , -7],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'a',
            'class' : {'class' : 'responsabilidad-socialSect'},
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'div',
            'class' : {'class' : 'lead'},
            'regex' : "<p>.*?</p>" ,
            'slice' : [3 , -4],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

class Bussines_dis():
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : 'col-sm-6 col-lg-4'},
            'skip' : 0,
            'length' : 20
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'id' : 'skip-header'},
            'regex' : "\s\s.*?<hr" ,
            'slice' : [1 , -3],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'div',
            'class' : {'class' : 'without-video-box'},
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'div',
            'class' : {'class' : 'text-left'},
            'regex' : "<p> <p>.*?<" ,
            'slice' : [7 , -1],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]


#MIPYMES

class h4h():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : 'item mas_health'},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'div',
            'class' : {'class' : 'container'},
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 2
            }
        
        self.link_info = {
            'object' : 'div',
            'class' : {'class' : 'title'},
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'p',
            'class' : None,
            'regex' : "\s\s.*?\n" ,
            'slice' : [34 , -2],
            'index' : 0
            }

    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]

class bbva():
    
    def __init__(self):
        self.boxes_info = {
            'object' : 'div',
            'class' : {'class' : 'noticia_groupInfo'},
            'skip' : 0,
            'length' : 0
            }
        
        self.title_info = {
            'object' : 'h1',
            'class' : {'class' : 'article-title'},
            'regex' : ">.*?</h1>" ,
            'slice' : [1 , -5],
            'index' : 0
            }
        
        self.link_info = {
            'object' : 'h2',
            'class' : {'class' : 'notTituloDest'},
            'regex' : "href=\".*?\"" ,
            'slice' : [6 , -1],
            'index' : 0
            }
        
        self.text_info = {
            'object' : 'div',
            'class' : {'class' : 'detContIntro'},
            'regex' : ">.*?</p>" ,
            'slice' : [1 , -4],
            'index' : 0
            }
    
    def get_data(self):
        return [self.boxes_info, self.title_info, self.link_info, self.text_info]
