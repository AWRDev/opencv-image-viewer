import os
import cv2
import numpy as np

import pprint as pp

from main import view
class ImageViewer:
    def __init__(self) -> None:
        self.opened_windows : int = 0
        self.current_path : str = ""
        self.content : list
        self.image_number = 0
    def __show(self):
        current_image = cv2.imread(f"{self.current_path}\{self.content[self.image_number]}")
        current_image = cv2.resize(current_image, (0,0), fx=0.25, fy=0.25)
        cv2.imshow("Image Viewer", current_image)
    def select_folder(self, path):
        self.content = os.listdir(path)
        self.current_path = path
        self.__show()
    def next_image(self):
        self.image_number += 1
        self.__show()
    def prev_image(self):
        self.image_number -= 1
        self.__show()
    def _debug(self):
        print(type(self.current_path), type(self.opened_windows))
class Image:
    def __init__(self, filename) -> None:
        self.image = cv2.imread(filename)
    
viewer = ImageViewer()
viewer.select_folder(r"C:\Projects\Python\OpenCV\Essentials\display_positves_raw")
while True:
    key_pressed = cv2.waitKeyEx(0)
    print(key_pressed)
    #if key_pressed & 0xff == 2555904: #Arrow right
    if key_pressed == 2555904: #Arrow right
        viewer.next_image()
    elif key_pressed == 2424832: #Arrow left
        viewer.prev_image()
    elif key_pressed & 0xff == ord('q'):
         exit()
#viewer._debug()
#image = Image(r"C:\Projects\Python\OpenCV\Essentials\display_positves_raw\IMG_20211011_180031.jpg")
