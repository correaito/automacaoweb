import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

produtos = pd.read_excel('Produtos.xlsx', index_col=[0])
#display(produtos)

# aqui vamos criar uma função para transformar os textos extraidos dos sites, e trata-los
def transformar_texto(texto):
    return float(texto.replace('\n', ',').replace('R$', '').replace('.', '').replace(',', '.').replace('à vista', ''))

# vamos instalar o webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.set_window_position(-10000,0)

enviar_email = False
desconto_min = 0.2

# nesse laço, vamos entrar em cada uma das lojas, e extrair o preço dos produtos da nossa tabela
for i, linha in produtos.iterrows():
    # pegar preço amazon
    driver.get(linha['Amazon'])
    try:
        # alguns sites tem componentes em flash que rodam antes do carregamento total da pagina, por isso apliquei o time sleep
        # e o webdriverwait para aguardar até o carregamento do elemento alvo
        time.sleep(2)
        preco_amazon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))).text
        preco_amazon = transformar_texto(preco_amazon)
    except:
        # caso o site sofrer alteração, vamos aplicar um except e aumentar a variavel 3x o valor original,
        # para que ele não se torne o menor valor da lista (linha 64)
        print(f"Produto {linha['Link Produto']} não encontrado na Amazon")
        preco_amazon = linha['Preço Original'] * 3


    #pegar o preço do mlivre
    driver.get(linha['Mercado Livre'])
    try:
        time.sleep(2)
        preco_mlivre = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'andes-money-amount__fraction'))).text
        preco_mlivre = transformar_texto(preco_mlivre)
    except:
        print(f"Produto {linha['Link Produto']} não encontrado no Mercado Livre")
        preco_mlivre = linha['Preço Original'] * 3
    

    #pegar o preço da magalu
    driver.get(linha['Magazine Luiza'])
    try:
        time.sleep(3)
        preco_magalu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-hYQoXb.OZNyS'))).text
        preco_magalu = transformar_texto(preco_magalu)
    except:
        print(f"Produto {linha['Link Produto']} não encontrado na Magazine Luiza")
        preco_magalu = linha['Preço Original'] * 3
            
    preco_original = linha['Preço Original']
    
    # aqui criamos uma lista com os valores extraidos dos sites, e vamos ordena-lo em ordem crescente
    lista_precos = [(preco_amazon, 'Amazon'), (preco_mlivre, 'Mercado Livre'), (preco_magalu, 'Magazine Luiza'), (preco_original, 'Original')]
    lista_precos.sort()
    
    # ...e aqui gravar o menor preço/loja em nossa tabela nas colunas respectivas
    produtos.loc[i,'Preço Atual'] = lista_precos[0][0]
    produtos.loc[i, 'Local'] = lista_precos[0][1]
    
    # se o valor for 20% mais barato que o original, vamos enviar o email notificando
    if lista_precos[0][0] <= preco_original*(1-desconto_min):
        enviar_email = True
        
#display(produtos)

# salvando o arquivo
produtos.to_excel('Produtos.xlsx')

# e aqui iremos enviar o email notificando o dpto Compras quando produto(s) da lista estiverem 20% mais baixos que original
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

desconto_min = 0.2
# enviar email
if enviar_email:
    mail = outlook.CreateItem(0)
    mail.To = 'correaito+compras@gmail.com'
    mail.Subject = f'Produto(s) Encontrado(s) com mais de {desconto_min:.0%} de Desconto'
    
    #filtrar a tabela de produtos    
    tabela_filtrada = produtos.loc[produtos['Preço Atual'] <= produtos['Preço Original'] * (1-desconto_min), :]    
    mail.HTMLBody = f'<p>Esses são os produtos com mais de {desconto_min:.0%} de desconto</p>{tabela_filtrada.to_html()}'
    #enviando o email
    mail.Send()
    
# finalizando o código
driver.quit() 
print('Fim da Análise')

