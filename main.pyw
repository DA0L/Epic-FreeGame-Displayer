import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import io
import base64
from urllib.request import urlopen
import urllib

DRIVER_PATH = r"C:/Users/gabri/Mine/apps/chromedriver/chromedriver.exe"
options = Options()
options.headless = True
options.add_argument("--window.size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

root = Tk()

#root.geometry("300x250")
root.title("Epic Games Holidays")


driver.get("https://www.epicgames.com/store/es-ES/")
time.sleep(15)
soup = BeautifulSoup(driver.page_source, "html5lib")
Gem = soup.find_all("img", "css-1s4ypbt-Picture-styles__image-OfferCardImageArt__picture-OfferCardImageLandscape__picture-Picture-styles__visible")

print(Gem[0].get("data-image"))

url = Gem[0].get("data-image")
data = urlopen(url)
image = ImageTk.PhotoImage(data=data.read())
Labe = Label(root, image=image).pack(side="left")

urll = Gem[1].get("data-image")
dat = urlopen(urll)
imag = ImageTk.PhotoImage(data=dat.read())
Lab = Label(root, image=imag).pack(side="right")

root.mainloop()

driver.quit()