import os
import imageio
import imgaug as ia
from imgaug import augmenters as iaugmenters
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from random import *
from PIL import Image as PIL_Image

seq = iaugmenters.Sequential([
    iaugmenters.Crop(percent=(0, 0.1)),
    iaugmenters.Sometimes(
        0.5,
        iaugmenters.GaussianBlur(sigma=(0, 0.5))
    ),
    iaugmenters.LinearContrast((0.75, 1.5)),
    iaugmenters.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    iaugmenters.Multiply((0.8, 1.2), per_channel=0.2),
    iaugmenters.Affine(
        scale={"x": (0.8, 1), "y": (0.8, 1)},
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
        rotate=(-10, 10),
        shear=(-8, 8)
    )
], random_order=True)

class ImageAugmenter:
    def __init__(self, file_name, background_file_name, yolo_class_name):
        # SETUP
        self.yolo_class_name = yolo_class_name
        self.file_name = file_name
        self.background_file_name = background_file_name

        # BOUNDING BOXES INIT
        self.bounding_boxes_on_image = BoundingBoxesOnImage([], shape=(1080, 1920))

        # ADD OBJECT ON BACKGROUND
        self.apply_image_on_background()

        # RELOAD IMAGE
        self.image = imageio.imread('image_temp.jpg')
        #ia.imshow(self.bounding_boxes_on_image.draw_on_image(self.image, size=10))

        # AUGMENT
        self.image_augmented, self.bounding_boxes_on_image_augmented = self.augment()


    def apply_image_on_background(self):
        # load image
        img = PIL_Image.open(os.getcwd() + '/dataset_original/' + self.file_name + '.jpg', 'r').convert('RGBA')
        img_w, img_h = img.size
        background = PIL_Image.open(os.getcwd() + '/backgrounds/' + self.background_file_name + '.jpg', 'r')
        bg_w, bg_h = background.size

        # save modified left part
        position = (randint(200, bg_w / 2 - img_w), randint(0, bg_h - img_h))
        background.paste(img, position)
        background.save("image_temp.jpg")

        # add bounding boxes
        self.add_bounding_box(position, (img_w, img_h))

        # save modified right part
        position = (randint(bg_w / 2, bg_w - img_w - 200), randint(0, bg_h - img_h))
        background.paste(img, position)
        background.save("image_temp.jpg")

        # add bounding boxes
        self.add_bounding_box(position, (img_w, img_h))

    def add_bounding_box(self, position, size):
        offset_x1 = 50
        offset_y1 = 30
        offset_x2 = -50
        offset_y2 = -200
        self.bounding_boxes_on_image.bounding_boxes.append(
            BoundingBox(position[0] + offset_x1, position[1] + offset_y1,
                        position[0] + size[0] + offset_x2, position[1] + size[1] + offset_y2)
        )

    def augment(self):
        image_augmented, bounding_boxes_augmented = seq(image=self.image, bounding_boxes=self.bounding_boxes_on_image)

        return image_augmented, bounding_boxes_augmented

    def save(self, number):
        path = os.getcwd() + "/dataset_augmented/" + self.file_name + "_" + self.background_file_name + "_" + str(number);
        imageio.imwrite(path + ".jpg", self.image_augmented)
        print("saving to", path)

        text = ""

        for box in self.bounding_boxes_on_image_augmented.to_xyxy_array():
            text += str(self.yolo_class_name) + " "
            x1 = box[0]
            y1 = box[1]
            x2 = box[2]
            y2 = box[3]

            x_center = (x1 + x2) / 2 / self.image_augmented.shape[1]
            y_center = (y1 + y2) / 2 / self.image_augmented.shape[0]
            width = abs(x1-x2) / self.image_augmented.shape[1]
            height = abs(y1-y2) / self.image_augmented.shape[0]

            text += str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height) + "\n"

        #ia.imshow(self.bounding_boxes_on_image_augmented.draw_on_image(self.image_augmented, size=10))

        file = open(path + ".txt", "w")
        file.write(text)

