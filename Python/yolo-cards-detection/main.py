from image_operations import *
import glob
import os

iterations = 20

objects_files = glob.glob('dataset_original/*')
objects_files = ["J_H", "Q_H", "K_H", "A_H", "J_S", "Q_S", "K_S", "A_S"]
objects = [os.path.splitext(os.path.basename(path))[0] for path in objects_files]
backgrounds_files = glob.glob('backgrounds/*')
backgrounds = [os.path.splitext(os.path.basename(path))[0] for path in backgrounds_files]
print(objects)

total_length = len(backgrounds) * iterations
counter = 0

for background_file_name in backgrounds:
    for i in range(iterations):
        image = ImageAugmenter(objects, background_file_name, 0)
        image.save(i)
        counter += 1
        print("Progress:", counter, "/", total_length)

# for i in range(54):
#     # if i == 53:
#     #     print(i)
#     #     continue
#     # print(i, '\\n', end='', sep='')
#     print(i)
