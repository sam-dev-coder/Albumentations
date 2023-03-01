# Albumentations
Image Augmentation Pipeline
This Python code implements an image augmentation pipeline using the albumentations library. The pipeline performs various augmentations on input images and corresponding labels, and saves the augmented images and labels in separate directories.

# Dependencies
Python 3.x
OpenCV (cv2) library
albumentations library

# Usage
Place the input images and corresponding labels in separate directories named "Images" and "Labels", respectively.
Run the Python code to generate augmented images and labels.
The augmented images and labels will be saved in separate directories named "augmented_images" and "augmented_labels", respectively.

# Augmentations
The following augmentations are performed on input images and corresponding labels:
Horizontal Flip
Vertical Flip
Random Rotation (90 degrees)
Rotation (up to 45 degrees)

# Output
The augmented images and labels are saved in separate directories named "augmented_images" and "augmented_labels", respectively. The output files are named in the format "i_j.png", where "i" is the index of the input image and "j" is the index of the augmented image.
