# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:34:52 2022

@author: Lenovo
"""
from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.original_image = self.master.processed_image
        self.filtered_image = None
        
        self.negative_button = Button(master=self, text="Negative")
        self.black_white_button = Button(master=self, text="Black White")
        self.sepia_button = Button(master=self, text="Sepia")
        self.emboss_button = Button(master=self, text="Emboss")
        self.gaussian_blur_button = Button(master=self, text="Gaussian Blur")
        self.median_blur_button = Button(master=self, text="Median Blur")
        self.noise_reduction_button = Button(
            master=self, text="Noise Reduction")
        self.quality_detection_button = Button(
            master=self, text="Quality Detection")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.negative_button.bind(
            "<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind(
            "<ButtonRelease>", self.black_white_released)
        self.sepia_button.bind("<ButtonRelease>", self.sepia_button_released)
        self.emboss_button.bind("<ButtonRelease>", self.emboss_button_released)
        self.gaussian_blur_button.bind(
            "<ButtonRelease>", self.gaussian_blur_button_released)
        self.median_blur_button.bind(
            "<ButtonRelease>", self.median_blur_button_released)
        self.noise_reduction_button.bind(
            "<ButtonRelease>", self.noise_reduction_button_released)
        self.quality_detection_button.bind(
            "<ButtonRelease>", self.quality_detection_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.negative_button.pack()
        self.black_white_button.pack()
        self.sepia_button.pack()
        self.emboss_button.pack()
        self.gaussian_blur_button.pack()
        self.median_blur_button.pack()
        self.noise_reduction_button.pack()
        self.quality_detection_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()
        

    def negative_button_released(self, event):
        self.negative()
        self.show_image()

    def black_white_released(self, event):
        self.black_white()
        self.show_image()

    def sepia_button_released(self, event):
        self.sepia()
        self.show_image()

    def emboss_button_released(self, event):
        self.emboss()
        self.show_image()

    def gaussian_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def median_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def noise_reduction_button_released(self, event):
        self.noise_reduction()
        self.show_image()

    def quality_detection_button_released(self, event):
         self.quality_detection()
         self.show_image()    

    def apply_button_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (41, 41), 0)

    def median_blur(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 41)

    def noise_reduction(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 5)

    def quality_detection(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 5)
        img = cv2.imread(self.original_image, cv2.IMREAD_GRAYSCALE)
        #self.filtered_image = cv2.imread(self.original_image, cv2.IMREAD_GRAYSCALE)
        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()    
        if laplacian_var < 5:
            self.title("Blurry Image")
        else:
           self.title("Clean Image")
        
    def close(self):
        self.destroy()

