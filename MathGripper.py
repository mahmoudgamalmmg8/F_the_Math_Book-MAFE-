from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from img2pdf import convert
import urllib
import os
import img2pdf
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://eng.synceg.net/my/")
#
browser.find_element("id","username").send_keys("UR ID CUZ ONLY IDOITS PUT THEIR REAL INFO HERE ")
browser.find_element("id","password").send_keys("UR PASSWORD CUZ ONLY IDOITS PUT THEIR REAL INFO HERE")
browser.find_element("id","loginbtn").click()
print("this tool created by the one and only mahmoudgamlmmg8 ps(it's only gonna work on modern academy books and maybe other moodle based website)")
link=input("Enter your book link: ")
browser.get(f"{link}+&page=0")
sep=browser.find_element(By.CSS_SELECTOR,".mod_securepdf_pages").get_attribute('innerHTML').split("/ ")
maxp=int(sep[1])
fName = str(browser.find_element("xpath","/html/body/div[1]/div[3]/header/div/div/div/div[2]/div[1]/nav/ol/li[5]/a").get_attribute('innerHTML') )
image_list=[]

try:
    os.mkdir(fName)
except:
    print("file already exists")
os.chdir(fName)
for p in range(0,maxp):
    browser.get(f"{link}+&page={p}")
    sep=browser.find_element(By.CSS_SELECTOR,".mod_securepdf_pages").get_attribute('innerHTML').split("/ ")
    maxp=sep[0]
    src=browser.find_element("xpath","/html/body/div[1]/div[3]/div/div/section/div[1]/img").get_attribute("src")
    browser.get(src)
    browser.save_screenshot(f"{p}.png")
   
    image_list.append(f"{p}.png")
img = Image.open(image_list[0]).convert("RGB")
img_obj=[Image.open(image).convert("RGB") for image in image_list[1:]]
img.save(f"{fName}.pdf",save_all=True,append_images=img_obj)        
