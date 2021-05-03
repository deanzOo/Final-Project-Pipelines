from logoPostprocessing import functions, getRandomFont
import random
from tkinter import font as tkFont
import uuid
import torch
import torchvision.utils as vutils
from Generator import Generator
import subprocess

def CreateLogo(model="netG_checkpoint_009.pt"):
    ngpu = 1
    device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
    loaded_generator = Generator(ngpu).to(device)
    general_dict = torch.load(model, map_location=torch.device('cpu'))
    loaded_generator.load_state_dict(general_dict['model_state_dict'])
    loaded_generator.eval()
    # Create and feed random vector to trained Generator
    vector = torch.randn(1, 100, 1, 1, device=device)
    fake = loaded_generator(vector)
    image_name = str(uuid.uuid4()) + '.png'
    vutils.save_image(fake.detach(), image_name, normalize=True)
    return image_name

def generateText(text):
    f = functions[random.randrange(0, len(functions))]
    font_used = getRandomFont()
    size = random.randrange(32, 72)
    fnt = tkFont.Font(family=font_used, size=size)
    width = max(fnt.measure(text), 0)
    if width == 0:
        return False
    image_name = str(uuid.uuid4()) + '.png'
    f(text, font_used, size, width, image_name)
    return image_name, width

def merge(img1, img2, max_width):
    position1 = random.randrange(0, max_width - 32)
    position2 = random.randrange(0, 60)
    image_name = str(uuid.uuid4()) + ".png"
    subprocess.run(
        ["magick", "convert", "-page", "+" + str(position1) + "+" + str(position2), img1, "+page", "-alpha", "Set",
         "-virtual-pixel", "transparent", "-channel", "A", "-blur", "0x10", "-level", "50,100%", "+channel", "(",
         "-size", "200x200", img2, "-alpha", "Set", ")", "-insert", "0", "-background", "white", "-flatten",
         image_name])
    return image_name