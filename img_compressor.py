import PIL
import os

from PIL import Image

#_COMPRESS AND SAVE THE IMAGE
def compressor(path_to_file: str):
    f = path_to_file
    img = Image.open(f)
    img.save(f, optimize=True, quality=30)
    print("Successfully compressed " + os.path.basename(os.path.normpath(path_to_file)))
    
    # Add print statement for newley compressed file sizes kb,
