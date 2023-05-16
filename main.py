from selenium import webdriver
import os
import time

# WebDriver'ı başlatma
driver = webdriver.Chrome()

# YouTube linkini açma
youtube_link = "https://www.youtube.com/watch?v=VIDEO_ID"
driver.get(youtube_link)

# Videoyu tam ekran yapma
driver.find_element_by_class_name("ytp-fullscreen-button").click()

# Reklamları atlatma
try:
    driver.find_element_by_class_name("ytp-ad-skip-button").click()
except:
    pass

# Videonun bitmesini beklemek için zamanlama
video_duration = driver.execute_script("return document.getElementsByTagName('video')[0].duration")
time.sleep(video_duration)

# Bilgisayarı zorla kapatma
os.system("shutdown /s /t 0")
