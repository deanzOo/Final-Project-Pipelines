from PipelineSystem import Pipeline
from scripts import CreateLogo, generateText, merge
import os


def pipe1(model="netG_checkpoint_009.pt"):
    return CreateLogo(model)


def pipe2(model="netG_checkpoint_009.pt", text=''):
    logo_image_name = CreateLogo(model)
    text_image, width = generateText(text)
    if not text_image:
        return logo_image_name
    merged_image_name = merge(logo_image_name, text_image, width)
    os.remove(logo_image_name)
    os.remove(text_image)
    return merged_image_name


p1 = Pipeline(pipe1)
p2 = Pipeline(pipe2)
pipelines = [p1, p2]
