import os
import cv2
import numpy as np

import pprint as pp

WINDOW_NAME = "Image Viewer"

VIEWER_GO_FORWARD = 1
VIEWER_GO_BACKWARD = 2

class ImageViewer:
    #TODO: implement backhround caching
    def __init__(self) -> None:
        self.opened_windows : int = 0
        self.current_path : str = ""
        self.content : list
        self.content_length: int = 0
        self.image_number = 0

    def __show(self):
        cv2.imshow(WINDOW_NAME, self.current_image)
        cv2.setWindowTitle(WINDOW_NAME, f"Image Viewer {self.current_path}\{self.content[self.image_number]}")
    def select_folder(self, path):
        self.content = os.listdir(path)
        self.current_path = path
        self.content_length = len(self.content)-1
        self.prepare_workspace()
    def prepare_workspace(self):
        prev_image_number : int = self.image_number - 1
        next_image_number : int = self.image_number + 1
        if self.image_number == 0:
            prev_image_number = self.content_length
        elif self.image_number == self.content_length:
            next_image_number = 0
        self.current_image = cv2.imread(f"{self.current_path}\{self.content[self.image_number]}")
        self.current_image = cv2.resize(self.current_image, (0,0), fx=0.25, fy=0.25)
        self.next_image = cv2.imread(f"{self.current_path}\{self.content[next_image_number]}")
        self.next_image = cv2.resize(self.next_image, (0,0), fx=0.25, fy=0.25)
        self.prev_image = cv2.imread(f"{self.current_path}\{self.content[prev_image_number]}")
        self.prev_image = cv2.resize(self.prev_image, (0,0), fx=0.25, fy=0.25)
        self.__show()
    def __update_workspace(self, action):
        self.__update_image_numbers(action)
        if action == VIEWER_GO_FORWARD:
            self.prev_image = self.current_image
            self.current_image = self.next_image
            self.next_image = cv2.imread(f"{self.current_path}\{self.content[self.next_image_number]}")
            self.next_image = cv2.resize(self.next_image, (0,0), fx=0.25, fy=0.25)
        elif action == VIEWER_GO_BACKWARD:
            self.next_image = self.current_image
            self.current_image = self.prev_image
            self.prev_image = cv2.imread(f"{self.current_path}\{self.content[self.prev_image_number]}")
            self.prev_image = cv2.resize(self.prev_image, (0,0), fx=0.25, fy=0.25)
        self.__show()
    def __update_image_numbers(self, action):
        if action == VIEWER_GO_FORWARD:
            self.image_number += 1
        elif action == VIEWER_GO_BACKWARD:
            self.image_number -= 1
        self.prev_image_number : int = self.image_number - 1
        self.next_image_number : int = self.image_number + 1
        if self.image_number == 0:
            self.prev_image_number = self.content_length
        elif self.image_number == self.content_length:
            self.next_image_number = 0
    def go_forward(self):
        self.__update_workspace(VIEWER_GO_FORWARD)
    def go_backward(self):
        self.__update_workspace(VIEWER_GO_BACKWARD)
    def _debug(self):
        print(type(self.current_path), type(self.opened_windows))
    
viewer = ImageViewer()
viewer.select_folder(r"C:\Projects\Python\OpenCV\Essentials\display_positves_raw")
while True:
    key_pressed = cv2.waitKeyEx(0)
    print(key_pressed)
    #if key_pressed & 0xff == 2555904: #Arrow right
    if key_pressed == 2555904: #Arrow right
        viewer.go_forward()
    elif key_pressed == 2424832: #Arrow left
        viewer.go_backward()
    elif key_pressed & 0xff == ord('q'):
         exit()
#viewer._debug()
#image = Image(r"C:\Projects\Python\OpenCV\Essentials\display_positves_raw\IMG_20211011_180031.jpg")
