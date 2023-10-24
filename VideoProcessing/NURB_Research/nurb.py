import numpy as np
import cv2
import geomdl

# Load the image
image = cv2.imread("pic.jpg")

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image to 100x100 pixels
resized_image = cv2.resize(grayscale_image, (100, 100))

# Create a NURBS surface
from geomdl.NURBS import BSpline
surface = BSpline.Surface()
surface.degree_u = 2
surface.degree_v = 2
surface.ctrlpts2d = list(resized_image.reshape(-1, 2).astype(np.float32))

# Project the image onto the surface
surface.surfpts(100, 100)

# Save the surface to a file
surface.write("surface.nurbs")
