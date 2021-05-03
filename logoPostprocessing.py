import random
import subprocess

import matplotlib.font_manager

import tkinter

tkinter.Frame().destroy()

available_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
available_colors = [
    "AliceBlue",
    "AntiqueWhite",
    "Aqua",
    "Aquamarine",
    "Azure",
    "Beige",
    "Bisque",
    "Black",
    "BlanchedAlmond",
    "Blue",
    "BlueViolet",
    "Brown",
    "BurlyWood",
    "CadetBlue",
    "Chartreuse",
    "Chocolate",
    "Coral",
    "CornflowerBlue",
    "Cornsilk",
    "Crimson",
    "Cyan",
    "DarkBlue",
    "DarkCyan",
    "DarkGoldenRod",
    "DarkGray",
    "DarkGrey",
    "DarkGreen",
    "DarkKhaki",
    "DarkMagenta",
    "DarkOliveGreen",
    "DarkOrange",
    "DarkOrchid",
    "DarkRed",
    "DarkSalmon",
    "DarkSeaGreen",
    "DarkSlateBlue",
    "DarkSlateGray",
    "DarkSlateGrey",
    "DarkTurquoise",
    "DarkViolet",
    "DeepPink",
    "DeepSkyBlue",
    "DimGray",
    "DimGrey",
    "DodgerBlue",
    "FireBrick",
    "FloralWhite",
    "ForestGreen",
    "Fuchsia",
    "Gainsboro",
    "GhostWhite",
    "Gold",
    "GoldenRod",
    "Gray",
    "Grey",
    "Green",
    "GreenYellow",
    "HoneyDew",
    "HotPink",
    "IndianRed",
    "Indigo",
    "Ivory",
    "Khaki",
    "Lavender",
    "LavenderBlush",
    "LawnGreen",
    "LemonChiffon",
    "LightBlue",
    "LightCoral",
    "LightCyan",
    "LightGoldenRodYellow",
    "LightGray",
    "LightGrey",
    "LightGreen",
    "LightPink",
    "LightSalmon",
    "LightSeaGreen",
    "LightSkyBlue",
    "LightSlateGray",
    "LightSlateGrey",
    "LightSteelBlue",
    "LightYellow",
    "Lime",
    "LimeGreen",
    "Linen",
    "Magenta",
    "Maroon",
    "MediumAquaMarine",
    "MediumBlue",
    "MediumOrchid",
    "MediumPurple",
    "MediumSeaGreen",
    "MediumSlateBlue",
    "MediumSpringGreen",
    "MediumTurquoise",
    "MediumVioletRed",
    "MidnightBlue",
    "MintCream",
    "MistyRose",
    "Moccasin",
    "NavajoWhite",
    "Navy",
    "OldLace",
    "Olive",
    "OliveDrab",
    "Orange",
    "OrangeRed",
    "Orchid",
    "PaleGoldenRod",
    "PaleGreen",
    "PaleTurquoise",
    "PaleVioletRed",
    "PapayaWhip",
    "PeachPuff",
    "Peru",
    "Pink",
    "Plum",
    "PowderBlue",
    "Purple",
    "Red",
    "RosyBrown",
    "RoyalBlue",
    "SaddleBrown",
    "Salmon",
    "SandyBrown",
    "SeaGreen",
    "SeaShell",
    "Sienna",
    "Silver",
    "SkyBlue",
    "SlateBlue",
    "SlateGray",
    "SlateGrey",
    "Snow",
    "SpringGreen",
    "SteelBlue",
    "Tan",
    "Teal",
    "Thistle",
    "Tomato",
    "Turquoise",
    "Violet",
    "Wheat",
    "White",
    "WhiteSmoke",
    "Yellow",
    "YellowGreen"
]


def getRandomColor():
    return available_colors[random.randrange(0, len(available_colors))]


def getRandomFont():
    return available_fonts[random.randrange(0, len(available_fonts))]


def tiled(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-tile", "pattern:checkerboard", "-annotate", "+28+68", text, image_name])


def gradient(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-tile", "gradient:", "-annotate", "+28+68", text, image_name])


def hardShadow(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-draw", "text 28,68 " + text, "-fill",
         getRandomColor(), "-draw", "text 25,65 " + text, image_name])


def sheardShadow(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x115", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "0x0+12+55", text, "-fill",
         getRandomColor(), "-annotate", "0x130+25+80", text, image_name])


def slanted(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-draw",
         "translate 28,68  skewX -20  text 0,0 " + text, image_name])


def stamped(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+24+64", text, "-fill",
         getRandomColor(), "-annotate", "+26+66", text, "-fill", getRandomColor(), "-annotate", "+25+65", text,
         image_name])


def extruded(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+29+69", text, "-annotate", "+28+68",
         text, "-annotate", "+27+67", text, "-annotate", "+26+66", text, "-annotate", "+25+65", text, "-annotate",
         "+24+64", text, "-fill", getRandomColor(), "-annotate", "+23+63", text, image_name])


def outlined(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x100", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+24+64", text, "-annotate", "+26+64",
         text, "-annotate", "+26+66", text, "-annotate", "+24+66", text, "-fill", getRandomColor(), "-annotate",
         "+25+65", text, image_name])


def stroke(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-annotate", "+25+65",
         text, image_name])


def thickStroke(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "5",
         "-annotate", "+25+65", text, "-stroke", "none", "-annotate", "+25+65", text, image_name])


def thinStroke(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-annotate", "+25+65",
         text, image_name])


def doubleOutline(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "3",
         "-annotate", "+25+65", text, "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "1",
         "-annotate", "+25+65", text, image_name])


def psychedalic(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "25",
         "-annotate", "+25+65", text, "-stroke", getRandomColor(), "-strokewidth", "20", "-annotate", "+25+65", text,
         "-stroke", getRandomColor(), "-strokewidth", "15", "-annotate", "+25+65", text, "-stroke", getRandomColor(),
         "-strokewidth", "10", "-annotate", "+25+65", text, "-stroke", getRandomColor(), "-strokewidth", " 5",
         "-annotate", "+25+65", text, "-stroke", "none", "-annotate", "+25+65", text, image_name])


def balloon(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "5",
         "-annotate", "+25+65", text, "-fill", getRandomColor(), "-stroke", getRandomColor(), "-strokewidth", "1",
         "-annotate", "+25+65", text, image_name])


def joinedChars(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-kerning", "-6", "-strokewidth", "4", "-fill", getRandomColor(), "-stroke",
         getRandomColor(), "-annotate", "+28+68", text, "-stroke", "none", "-annotate", "+28+68", text, image_name])


def overlappedChars(text, font_used, font_size, font_width, image_name):
    outline_color = getRandomColor()
    options = ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font",
               font_used, "-pointsize", str(font_size), "-stroke", getRandomColor(), "-strokewidth", "4", "-fill",
               getRandomColor()]
    for i in range(len(text)):
        options.append("-stroke")
        options.append(outline_color)
        options.append("-annotate")
        options.append("+%d+68" % (28 + i * 30))
        options.append(text[i])
        options.append("-stroke")
        options.append("none")
        options.append("-annotate")
        options.append("+%d+68" % (28 + i * 30))
        options.append(text[i])
    options.append(image_name)
    subprocess.run(options)


def jitteredChars(text, font_used, font_size, font_width, image_name):
    outline_color = getRandomColor()
    options = ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font",
               font_used, "-pointsize", str(font_size), "-stroke", getRandomColor(), "-strokewidth", "4", "-fill",
               getRandomColor()]
    for i in range(len(text)):
        multiplier = 1 if (i <= (len(text) / 2)) else -1
        options.append("-stroke")
        options.append(outline_color)
        options.append("-annotate")
        options.append("+%d+%d" % (28 + i * 20, 80 + multiplier * i * 5))
        options.append(text[i])
        options.append("-stroke")
        options.append("none")
        options.append("-annotate")
        options.append("+%d+%d" % (28 + i * 20, 80 + multiplier * i * 5))
        options.append(text[i])
    options.append(image_name)

    subprocess.run(options)


def fuzzyShadow(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-annotate", "+30+70", text, "-blur", "0x4", "-fill", getRandomColor(),
         "-stroke", getRandomColor(), "-annotate", "+25+65", text, image_name])


def softOutline(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-annotate", "+25+65", text, "-blur", "0x5", "-fill", getRandomColor(),
         "-annotate", "+25+65", text, image_name])


def denserSoftOutline(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-stroke", getRandomColor(), "-strokewidth", "8", "-annotate", "+25+65", text,
         "-blur", "0x8", "-fill", getRandomColor(), "-stroke", "none", "-annotate", "+25+65", text, image_name])


def dirtyPrint(text, font_used, font_size, font_width, image_name):
    subprocess.run(["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white",
                    "-font", font_used, "-pointsize", str(font_size), "-annotate", "+25+65", text, "-spread", "1",
                    "-blur", "0x1", "-threshold", "50%", "-blur", "0x1", image_name])


def beveled(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+25+65", text, "-shade", "140x45",
         image_name])


def conical(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+25+65", text, "-gamma", "2", "+level",
         "0,1000", "-white-threshold", "999", "-morphology", "Distance", "Euclidean:4,1000", "-auto-level", "-shade",
         "135x30", "-auto-level", "+level", "10,90%", image_name])


def arched(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+25+65", text, "-transparent",
         getRandomColor(), "-wave", "-50x640", "-crop", "x110+0+10", image_name])


def arc(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+25+65", text, "-distort", "Arc", "120",
         "-trim", "+repage", "-bordercolor", getRandomColor(), "-border", "10", image_name])


def circle(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-font", font_used, "-pointsize", "32", "-transparent", getRandomColor(), "-fill",
         getRandomColor(), "label:" + text, "-virtual-pixel", "background", "-distort", "Arc", "340", image_name])


def comet(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+45+95", text, "-motion-blur",
         "0x25+65", "-fill", getRandomColor(), "-annotate", "+45+95", text, "-motion-blur", "0x1+65", image_name])


def smoking(text, font_used, font_size, font_width, image_name):
    subprocess.run(
        ["magick", "convert", "-size", str(font_width) + "x120", "xc:none", "-background", "white", "-font", font_used,
         "-pointsize", str(font_size), "-fill", getRandomColor(), "-annotate", "+25+95", text, "-motion-blur",
         "0x25+90", "-transparent", getRandomColor(), "-rotate", "60", "-wave", "3x35", "-rotate", "-60", "-gravity",
         "center", "-crop", str(font_width) + "x120+0+0", "+repage", "+gravity", "-fill", getRandomColor(), "-annotate",
         "+25+95", text, image_name])





functions = [tiled,
             gradient,
             hardShadow,
             sheardShadow,
             extruded,
             stamped,
             slanted,
             outlined,
             stroke,
             thickStroke,
             doubleOutline,
             psychedalic,
             balloon,
             joinedChars,
             overlappedChars,
             jitteredChars,
             softOutline,
             denserSoftOutline,
             conical,
             beveled,
             dirtyPrint,
             arched,
             arc,
             circle,
             smoking,
             comet,
             ]

# merge("logo.png", image_name + ".png, width)

# generateText("Deep\ Logo")
