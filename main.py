from logic.driver import Driver
import pandas as pd

drv = Driver()

#Busqueda de noticias
print("Cargando noticias comunidad Emprendedores:")
drv.set_news_emprendedores("Emprendedores")
print("Se cargaron ", len(drv.news_emprendedores), " noticias")

print("Cargando noticias comunidad Empresa y discapacidad:")
drv.set_news_empresa("Empresa y discapacidad")
print("Se cargaron ", len(drv.news_empresa), " noticias")

print("Cargando noticias comunidad Mipymes:")
drv.set_news_mipymes("Mipymes")
print("Se cargaron ", len(drv.news_mipymes), " noticias")


#Cracion dataframe
df = pd.DataFrame(columns = ['Comunidad', 'Titulos', 'Links', 'Descripciones'])

#Llenado dataframe
index = 1
for new in drv.news_emprendedores:
    df.loc[index] = [ new['Comunidad'], new['Titulos'], new['Links'], new['Descripciones'] ]
    index += 1

for new in drv.news_empresa:
    df.loc[index] = [ new['Comunidad'], new['Titulos'], new['Links'], new['Descripciones'] ]
    index += 1

for new in drv.news_mipymes:
    df.loc[index] = [ new['Comunidad'], new['Titulos'], new['Links'], new['Descripciones'] ]
    index += 1

#Guardado de dataframe como excel
print("Creando Excel...")
df.to_excel(r'data/scraped_data.xlsx', index = True)
df.to_excel(r'data/scraped_data_bk.xlsx', index = True)
print("Excel creado")
