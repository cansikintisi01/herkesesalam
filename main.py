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
