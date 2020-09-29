#Gabriel Lopes - FEI
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
def pegar_conta():
    arquivo=open("contas.txt","r")
    conta=arquivo.readlines()
    conta=conta[0].split(":")
    return conta[0],conta[1]
class InstagramBot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'geckodriver\geckodriver.exe')
    def Logar(self):
        driver=self.driver
        driver.get("https://www.instagram.com")
        sleep(2)
        campo_usuario=driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha=driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        sleep(2)
    def PegarFotos(self,link):
        driver=self.driver
        driver.get(link)
        sleep(3)
        for x in range(0,4):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        links = driver.find_elements_by_xpath('//a[@href]')
        self.fotos=[]
        for link in links:
            link=link.get_attribute('href')
            if "/p/" in link:
               self.fotos.append(link)
    def CurtirFotos(self):
        driver=self.driver
        fotos=self.fotos
        contador=0
        for foto in fotos:
            driver.get(foto)
            sleep(1)
            driver.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(1)
            contador+=1
        print("BOT: Curti %s fotos"%str(contador))
    def Comentar(self,comentario):
        driver=self.driver
        fotos=self.fotos
        contador=0
        for foto in fotos:
            driver.get(foto)
            sleep(1)
            driver.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
            sleep(0.5)
            driver.find_element_by_class_name('Ypffh').send_keys(comentario)
            sleep(0.5)
            driver.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
            contador+=1
            sleep(1)
        print("BOT: Comentei em %s fotos"%str(contador))
link=input("Link do perfil alvo (EXEMPLO: https://www.instagram.com/BOT_123/): ")
escolha=''
while escolha.isdigit()==False or 1<int(escolha)>2:
    escolha=input("1-Para Curtir\n2-Para comentar\nEscolha: ")
if int(escolha)==2: comentario=input("Comentario: ")
login,senha=pegar_conta()
bot=InstagramBot(login,senha)
bot.Logar()
bot.PegarFotos(link)
if int(escolha)==1: bot.CurtirFotos()
else:   bot.Comentar(comentario)