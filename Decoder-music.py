# matin-cyber

from stepic import decode
from PIL import Image
from eyed3 import load
from os import system
import colorama

colorama.init()
class colorma:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print(f"""{colorma.CYAN}
    ╔══[Coded by : C Security,{colorma.RED}[Decoder music]{colorma.CYAN}]
    ║
    ╠═Author of tools : MatiN
    ╠═Team name : dark_shell
    ║
    ╠═(~BYE~)
    """)

audio = input("audio : ")
audio = load(audio) # Opening the audio file 

img = open("temp_img.png", "wb")
img.write(audio.tag.images[0].image_data) # Extract the Cover of audio file
img.close()

img = Image.open("temp_img.png")
text = decode(img) # Decode data from the extracted image
system("del {}".format("temp_img.png"))
print("Data : {}".format(text))
input()
