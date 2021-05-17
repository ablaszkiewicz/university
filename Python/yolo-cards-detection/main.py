from image_operations import *
import glob
import os

objects = ["4_black"]
backgrounds_files = glob.glob('backgrounds/*')
backgrounds = [os.path.splitext(os.path.basename(path))[0] for path in backgrounds_files]
print(backgrounds)
for object_file_name in objects:
    for background_file_name in backgrounds:
        for i in range(10):
            image = ImageAugmenter(object_file_name, background_file_name, i)
            image.save(i)


