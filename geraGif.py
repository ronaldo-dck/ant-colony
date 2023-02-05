from PIL import Image
import os
import glob

frames = list()
files = glob.glob("./Img/*.png")
files.sort(key=os.path.getmtime)
for file in files:
    frames.append(Image.open(file))
frame_one = frames[0]
frame_one.save("./Img/evolucao.gif", format="GIF", append_images=frames, save_all=True, duration=250, loop=1)
