from selenium import webdriver
import os
import time


driver = webdriver.Chrome()


youtube_link = "https://www.youtube.com/watch?v=VIDEO_ID"
driver.get(youtube_link)


driver.find_element_by_class_name("ytp-fullscreen-button").click()


try:
    driver.find_element_by_class_name("ytp-ad-skip-button").click()
except:
    pass


video_duration = driver.execute_script("return document.getElementsByTagName('video')[0].duration")
time.sleep(video_duration)


os.system("shutdown /s /t 0 /f")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


video_link = "https://www.youtube.com/watch?v=VIDEO_ID"
driver.get(video_link)


video_player = driver.find_element_by_id("movie_player")
video_player.send_keys(Keys.F)

import selenium
from selenium import webdriver


driver = webdriver.Chrome("/path/to/chromedriver")


driver.get("https://www.youtube.com/")


video_link = "https://www.youtube.com/watch?v=video_id"


driver.find_element_by_link_text(video_link).click()


driver.find_element_by_id("player-full-screen").click()





driver.quit()
