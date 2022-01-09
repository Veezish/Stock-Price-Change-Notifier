import yagmail
import os
import time
from selenium import webdriver
#webdriver is tool which instructs the behaiviour of a web open

def get_driver():
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")

  return driver

def clean_text(text):
  output = float(text.split(" %")[0])
  return output

def main():
  driver = get_driver()
  while True:
    time.sleep(30)
    element = driver.find_element(by="xpath",value="/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
    text = clean_text(element.text)

    if text <= -0.10:
      sender = "testm0410@gmail.com"
      receiver = "testm0410@gmail.com"

      subjects = "Stock Price Below -0.10%"

      content = f"""
      The Stock Price of CROBEX has fallen to {text}% 
      """
      yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
      yag.send(to=receiver, subject=subjects, contents=content)
      print("Email sent")


print(main())