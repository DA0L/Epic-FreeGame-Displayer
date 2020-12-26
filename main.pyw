from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import time
import math
import requests
import io
import base64
import urllib

DRIVER_PATH = r"C:/Users/gabri/Mine/apps/chromedriver/chromedriver.exe"
options = Options()
options.headless = True
# window size argument is necessary because of the simulated window size
options.add_argument("--window.size=1920,1200")

# Initialize webdriver with selected options
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

root = Tk()
root.title("Epic Games Holidays")

driver.get("https://www.epicgames.com/store/es-ES/")
time.sleep(15)
soup = BeautifulSoup(driver.page_source, "html5lib")
Game = soup.find_all("img", "css-1s4ypbt-Picture-styles__image-OfferCardImageArt__picture-OfferCardImageLandscape__picture-Picture-styles__visible")


# 1st Image
url = Game[0].get("data-image")
ImageUrl = urlopen(url)
ImageData = ImageTk.PhotoImage(data=ImageUrl.read())
LabelImg = Label(root, image=ImageData).pack(side="left")

# 2nd Image
url2 = Game[1].get("data-image")
ImageUrl2 = urlopen(url2)
ImageData2 = ImageTk.PhotoImage(data=ImageUrl2.read())
LabelImg2 = Label(root, image=ImageData2).pack(side="right")

root.mainloop()

driver.quit()
