import os
import cv2
import numpy as np

import pprint as pp

WINDOW_NAME = "Image Viewer"

VIEWER_GO_FORWARD = 1
VIEWER_GO_BACKWARD = 2

editable_image = None

class ImageViewer:
    #TODO: implement backhround caching
    #TODO: Refactor image imdex system
    def __init__(self) -> None:
        self.opened_windows : int = 0
        self.current_path : str = ""
        self.content : list
        self.content_length: int = 0
        self.image_index = 0
        self.__welcome_message()

    def __show(self):
        cv2.imshow(WINDOW_NAME, self.current_image)
        cv2.setWindowTitle(WINDOW_NAME, f"Image Viewer {self.current_path}\{self.content[self.image_index]}")
    def select_folder(self, path):
        self.content = os.listdir(path)
        self.current_path = path
        self.content_length = len(self.content)-1
        self.prepare_workspace()
    def prepare_workspace(self):
        prev_image_index : int = self.image_index - 1
        next_image_index : int = self.image_index + 1
        if self.image_index == 0:
            prev_image_index = self.content_length
        elif self.image_index == self.content_length:
            next_image_index = 0
        self.current_image = cv2.imread(f"{self.current_path}\{self.content[self.image_index]}")
        self.current_image = cv2.resize(self.current_image, (0,0), fx=0.25, fy=0.25)
        self.next_image = cv2.imread(f"{self.current_path}\{self.content[next_image_index]}")
        self.next_image = cv2.resize(self.next_image, (0,0), fx=0.25, fy=0.25)
        self.prev_image = cv2.imread(f"{self.current_path}\{self.content[prev_image_index]}")
        self.prev_image = cv2.resize(self.prev_image, (0,0), fx=0.25, fy=0.25)
        self.__show()
    def __update_workspace(self, action):
        self.__update_image_numbers(action)
        if action == VIEWER_GO_FORWARD:
            self.prev_image = self.current_image
            self.current_image = self.next_image
            self.next_image = cv2.imread(f"{self.current_path}\{self.content[self.next_image_index]}")
            self.next_image = cv2.resize(self.next_image, (0,0), fx=0.25, fy=0.25)
        elif action == VIEWER_GO_BACKWARD:
            self.next_image = self.current_image
            self.current_image = self.prev_image
            self.prev_image = cv2.imread(f"{self.current_path}\{self.content[self.prev_image_index]}")
            self.prev_image = cv2.resize(self.prev_image, (0,0), fx=0.25, fy=0.25)
        self.__show()
    def __update_image_numbers(self, action):
        if action == VIEWER_GO_FORWARD:
            self.image_index += 1
        elif action == VIEWER_GO_BACKWARD:
            self.image_index -= 1
        self.prev_image_index : int = self.image_index - 1
        self.next_image_index : int = self.image_index + 1
        if self.image_index == 0:
            self.prev_image_index = self.content_length
        elif self.image_index == self.content_length:
            self.next_image_index = 0
    def go_forward(self):
        self.__update_workspace(VIEWER_GO_FORWARD)
    def go_backward(self):
        self.__update_workspace(VIEWER_GO_BACKWARD)
    def __welcome_message(self):
        print('''
        OpenCV based Image Viewer
        Arrows right/left - go forward/backward
        q - exit''')
    def __change_blue(*args):
        #print("ARGS ", args)
        global editable_image
        #for i in range(500):
        editable_image[:,:,0] = 255
        cv2.imshow("Editor", editable_image)
        print(editable_image[0,0])
        #print(args[1])
    def __change_green(*args):
        #print("ARGS ", args)
        global editable_image
        #for i in range(500):
        editable_image[:,:,1] = 255
        cv2.imshow("Editor", editable_image)
        print(editable_image[0,0])
        #print(args[1])
    def __change_red(*args):
        #print("ARGS ", args)
        global editable_image
        #for i in range(500):
        editable_image[:,:,2] = 255
        cv2.imshow("Editor", editable_image)
        print(editable_image[0,0])
        #print(args[1])
    def edit_mode(self):
        global editable_image
        print("Edit mode enabled")
        editable_image = self.current_image
        cv2.namedWindow("Editor")
        #cv2.createTrackbar("Blue", "Editor", 127, 255, self.__change_blue)
        cv2.createTrackbar("Green", "Editor", 127, 255, self.__change_green)
        #cv2.createTrackbar("Red", "Editor", 127, 255, self.__change_red)
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
    elif key_pressed & 0xFF == ord('e'):
        viewer.edit_mode()
    elif key_pressed & 0xff == ord('q'):
         exit()
#viewer._debug()
#image = Image(r"C:\Projects\Python\OpenCV\Essentials\display_positves_raw\IMG_20211011_180031.jpg")
