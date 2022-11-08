from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyBot:
  DRIVER_PATH = 'chromedriver'
  options = Options()
  options.headless = True
  options.add_argument("--window-size=1920,1200")
  driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
  proxy = "124.240.187.80:82"
  webdriver.DesiredCapabilities.CHROME['proxy'] = {
   "httpProxy":proxy,
   "ftpProxy":proxy,
   "sslProxy":proxy,
   "noProxy":None,
   "proxyType":"MANUAL",
   "class":"org.openqa.selenium.Proxy",
   "autodetect":False
}
  driver.delete_all_cookies()
  driver.get("https://www.youtube.com/watch?v=M4FIulTzNxc")
  driver.implicitly_wait(30)
  driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)
  time.sleep(10)
  driver.save_screenshot('screenshot4.png')
  driver.quit()


  # vidoo="bernafas tanpamu" #video yang mau di search
  # driver.get("https://www.youtube.com/results?search_query=" + str(vidoo))

  # Untuk menekan tombol enter
  # for i in range(10):
  #   print(i)
  #   time.sleep(1)
  # video = driver.find_element(By.XPATH,'//*[@id="movie_player"]/div[1]/video')
  # video.send_keys(Keys.SPACE) #hits space
  # video.click()   