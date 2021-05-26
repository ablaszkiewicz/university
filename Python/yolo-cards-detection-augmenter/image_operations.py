import os
import imageio
import imgaug as ia
from imgaug import augmenters as iaugmenters
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from random import *
from PIL import Image as PIL_Image


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


seq = iaugmenters.Sequential([
    iaugmenters.Sometimes(
        0.5,
        iaugmenters.GaussianBlur(sigma=(0, 0.5))
    ),
    iaugmenters.LinearContrast((0.75, 1.5)),
    iaugmenters.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    iaugmenters.Multiply((0.8, 1.2), per_channel=0.2),
    iaugmenters.Affine(
        scale={"x": (1, 1.2), "y": (1, 1.2)},
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
        rotate=(-10, 10),
        shear=(-8, 8)
    )
], random_order=True)


class ImageAugmenter:
    def __init__(self, objects_paths, background_file_name, yolo_class_name):
        # SETUP
        self.yolo_class_name = yolo_class_name
        self.background_file_name = background_file_name

        # LOAD BACKGROUND
        background_path = os.getcwd() + '/backgrounds/' + self.background_file_name + '.jpg'
        self.background = PIL_Image.open(background_path, 'r')
        self.bg_w, self.bg_h = self.background.size

        # BOUNDING BOXES INIT
        self.bounding_boxes_on_image = BoundingBoxesOnImage([], shape=(self.bg_h, self.bg_w))

        # ADD OBJECT ON BACKGROUND
        for _ in range(30):
            self.file_name = objects_paths[randint(0, len(objects_paths)-1)]
            self.apply_image_on_background()
            self.reload_modified_background()

        # RELOAD IMAGE
        self.image = imageio.imread('image_temp.jpg')
        #ia.imshow(self.bounding_boxes_on_image.draw_on_image(self.image, size=1))

        # AUGMENT
        self.image_augmented, self.bounding_boxes_on_image_augmented = self.augment()

        # REMOVE OUT OF RANGE BOXES
        self.remove_out_of_range_bounding_boxes()

    def reload_modified_background(self):
        self.background = PIL_Image.open('image_temp.jpg')

    def apply_image_on_background(self):
        image_path = os.getcwd() + '/dataset_original/' + self.file_name + '.jpg'

        # load image
        img = PIL_Image.open(image_path, 'r').convert('RGBA')

        # scale image
        scale_factor = randint(30, 110) / 100
        # scale_factor = 1
        img = img.resize((int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)), 0)
        img_w, img_h = img.size


        # randomize position
        position = (randint(0, self.bg_w - img_w), randint(0, self.bg_h - img_h))
        # position = (0, 0)

        # remove overlapping bounding boxes
        self.remove_intersecting_bounding_boxes(BoundingBox(position[0], position[1], position[0]+img_w, position[1] + img_h))

        # apply left bounding box
        self.add_bounding_box_left(position, img.size)

        # apply right bounding box
        self.add_bounding_box_right(position, img.size)

        # save
        self.background.paste(img, position)
        self.background.save("image_temp.jpg")

    def add_bounding_box_left(self, position, size):
        x1 = position[0] + int(size[0] * 0.01)
        y1 = position[1] + int(size[1] * 0.01)
        x2 = position[0] + int(size[0] * 0.15)
        y2 = position[1] + int(size[1] * 0.27)
        bounding_box = BoundingBox(x1, y1, x2, y2)
        bounding_box.label = self.file_name
        self.bounding_boxes_on_image.bounding_boxes.append(bounding_box)

    def add_bounding_box_right(self, position, size):
        x1 = position[0] + int(size[0] * 0.85)
        y1 = position[1] + int(size[1] * 0.73)
        x2 = position[0] + int(size[0] * 0.99)
        y2 = position[1] + int(size[1] * 0.99)
        bounding_box = BoundingBox(x1, y1, x2, y2)
        bounding_box.label = self.file_name
        self.bounding_boxes_on_image.bounding_boxes.append(bounding_box)

    def remove_intersecting_bounding_boxes(self, original_box):
        boxes = self.bounding_boxes_on_image.bounding_boxes
        self.bounding_boxes_on_image.bounding_boxes = [box for box in boxes if not box.intersection(original_box)]

    def remove_out_of_range_bounding_boxes(self):
        boxes = self.bounding_boxes_on_image_augmented.bounding_boxes
        self.bounding_boxes_on_image_augmented.bounding_boxes = [box for box in boxes if box.is_fully_within_image(self.image_augmented)]

    def augment(self):
        image_augmented, bounding_boxes_augmented = seq(image=self.image, bounding_boxes=self.bounding_boxes_on_image)
        return image_augmented, bounding_boxes_augmented

    def convert_class_to_int(self, class_name):
        card_dictionary = {
            "2_C": 0,
            "3_C": 1,
            "4_C": 2,
            "5_C": 3,
            "6_C": 4,
            "7_C": 5,
            "8_C": 6,
            "9_C": 7,
            "10_C": 8,
            "J_C": 9,
            "Q_C": 10,
            "K_C": 11,
            "A_C": 12,

            "2_D": 13,
            "3_D": 14,
            "4_D": 15,
            "5_D": 16,
            "6_D": 17,
            "7_D": 18,
            "8_D": 19,
            "9_D": 20,
            "10_D": 21,
            "J_D": 22,
            "Q_D": 23,
            "K_D": 24,
            "A_D": 25,

            "2_H": 26,
            "3_H": 27,
            "4_H": 28,
            "5_H": 29,
            "6_H": 30,
            "7_H": 31,
            "8_H": 32,
            "9_H": 33,
            "10_H": 34,
            "J_H": 35,
            "Q_H": 36,
            "K_H": 37,
            "A_H": 38,

            "2_S": 39,
            "3_S": 40,
            "4_S": 41,
            "5_S": 42,
            "6_S": 43,
            "7_S": 44,
            "8_S": 45,
            "9_S": 46,
            "10_S": 47,
            "J_S": 48,
            "Q_S": 49,
            "K_S": 50,
            "A_S": 51,

            "J_1": 52,
            "J_2": 53,
        }

        card_dictionary = {
            "9_H": 0,
            "10_H": 1,
            "J_H": 2,
            "Q_H": 3,
            "K_H": 4,
            "A_H": 5,

            "9_S": 6,
            "10_S": 7,
            "J_S": 8,
            "Q_S": 9,
            "K_S": 10,
            "A_S": 11,

            "9_C": 12,
            "10_C": 13,
            "J_C": 14,
            "Q_C": 15,
            "K_C": 16,
            "A_C": 17,

            "9_D": 18,
            "10_D": 19,
            "J_D": 20,
            "Q_D": 21,
            "K_D": 22,
            "A_D": 23,
        }
        return str(card_dictionary[class_name])

    def get_yolo_text(self, box):
        class_name = self.convert_class_to_int(box.label)
        center_x = str(box.center_x / self.bg_w)
        center_y = str(box.center_y / self.bg_h)
        width = str(box.width / self.bg_w)
        height = str(box.height / self.bg_h)
        return class_name + " " + center_x + " " + center_y + " " + width + " " + height + "\n"

    def save(self, number):
        path = os.getcwd() + "/dataset_augmented/" + self.background_file_name + "_" + str(number)
        imageio.imwrite(path + ".jpg", self.image_augmented)

        text = ""

        for box in self.bounding_boxes_on_image_augmented.bounding_boxes:
            text += self.get_yolo_text(box)

        # ia.imshow(self.bounding_boxes_on_image_augmented.draw_on_image(self.image_augmented, size=10))

        file = open(path + ".txt", "w")
        file.write(text)

