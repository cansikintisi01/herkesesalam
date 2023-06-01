import webbrowser

# Youtube linki iste
youtube_link = input("Link: ")

# Youtube linkine git
webbrowser.open(youtube_link)

# Videoyu tam ekran yap
webbrowser.get().switch_to_fullscreen()

# Videonun bitmesini bekle
webbrowser.get().wait_until_closed()

# Tarayıcıyı kapat
webbrowser.get().close()



