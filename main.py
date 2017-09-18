#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:48:02 2017

@author: kaku
"""
import cv2
import sys
from SLICcv import SLIC

img = cv2.imread(sys.argv[1])
nr_superpixels = int(sys.argv[2])
nc = int(sys.argv[3])

step = int((img.shape[0]*img.shape[1]/nr_superpixels)**0.5)

slic = SLIC(img, step, nc)
slic.generateSuperPixels()
slic.createConnectivity()
cv2.imshow("superpixels", slic.img)
cv2.waitKey(0)
cv2.imwrite("SLICimg.jpg", slic.img)