import pygame
import urllib.request
import tempfile
import os
import threading
from playsound3 import playsound

# URLs
IMAGE_URL = "https://raw.githubusercontent.com/gaers-svg/Jumpscare-thing/main/GEOFFDAMILLER.png"  # use PNG
MUSIC_URL = "https://raw.githubusercontent.com/gaers-svg/ishowthneeds/main/getyopoopycomputerouttaherebro.mp3"
DISPLAY_TIME = 3.5

# Download temp file
def download_temp(url, ext):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
    urllib.request.urlretrieve(url, tmp.name)
    return tmp.name

pygame.init()
pygame.mixer.init()

# Download image
img_path = download_temp(IMAGE_URL, ".png")

# Play music in separate thread
def music():
    threading.Thread(target=lambda: playsound(MUSIC_URL), daemon=True).start()

music()  # start playing audio

# Fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load and scale image
image = pygame.image.load(img_path).convert()
image = pygame.transform.scale(image, screen.get_size())

# Display image
screen.blit(image, (0, 0))
pygame.display.flip()

start_time = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False  # allow exit on any key press
        if event.type == pygame.QUIT:
            running = False

    # Auto exit after DISPLAY_TIME
    if (pygame.time.get_ticks() - start_time) > DISPLAY_TIME * 1000:
        running = False

pygame.quit()
os.remove(img_path)
