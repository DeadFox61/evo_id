import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from urllib.parse import urlparse

from loguru import logger



#chrome_options.add_argument("user-data-dir=selenium") 

#LOGIN = "maximoous4@gmail.com"
#PASS = "Melbet007123"

#LOGIN = "301357285"
#PASS = "86Yx52"

LOGIN = "aga.ugu.11@gmail.com"
PASS = "Aga007123"

#LOGIN = "296453143"
#PASS = "Melbet007123"

#LOGIN = "16601693"
#PASS = "Qq261961"

    #document.getElementById("auth_id_email").value = "{LOGIN}";
    #document.getElementById("auth-form-password").value = "{PASS}";
def get_current_url():
    while True:
        try:
            red_url = "https://dns.google.com/resolve?name=melb.heartmagic.xyz&type=txt"
            hostname = requests.get(red_url).json()["Answer"][0]['data']
            res_url = f"https://m.{hostname}/casino/?products=%5B46%5D"
            return res_url
        except Exception as e:
            logger.error(e)
            time.sleep(10)
def login(driver):
    try:
        driver.add_cookie({"name": "SESSION", "value": "8e773074149282db434ad33d5b7c183d"})
        driver.refresh()
    except Exception as e:
        pass
def mob_get_id(driver):
    driver.get(get_current_url())
    time.sleep(15)
    login(driver)
    time.sleep(20)
    driver.execute_script("""
    document.getElementsByClassName("slots-grid__game")[0].getElementsByClassName("casino-games__window")[0].click();
    """)
    time.sleep(5)
    driver.get("https://live.fantasysportnetwork.com/")
    time.sleep(5)
    for cookie in driver.get_cookies():
        if cookie["name"] == "EVOSESSIONID":
            logger.debug(cookie["value"])
            driver.get("https://google.com")
            return cookie["value"]

@logger.catch
def parse_evo_id():
    driver = webdriver.Remote(
       command_executor='http://chrome:4444',
       desired_capabilities=DesiredCapabilities.CHROME)
    while True:
        try:
            sess_id = mob_get_id(driver)
            if sess_id:
                with open("evo_id/evo_id.txt","w") as file:
                    file.write(sess_id)
                    file.close()
            time.sleep(120)
        except Exception as e:
            logger.error(e)
