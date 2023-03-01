import albumentations as A
import cv2
import os

# Define the image and mask augmentation pipeline
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.Rotate(limit=45, p=0.5),
])

# Define the data generators for images and masks
data_gen_args = dict(
    rescale=1./255,
    preprocessing_function=transform,
    horizontal_flip=True,
    vertical_flip=True,
    rotation_range=45
)

# Create directories for augmented images and masks
if not os.path.exists("aug_images"):
    os.mkdir("aug_images")
if not os.path.exists("aug_labels"):
    os.mkdir("aug_labels")

# Define the paths to the original images and masks
image_dir = "Images"
mask_dir = "Labels"

# Create a list of all image and mask filenames
image_filenames = os.listdir(image_dir)
mask_filenames = os.listdir(mask_dir)

# Define the number of augmented images and masks to generate
num_augmentations = 5 # Number of augmentations per image (4 types of flips)

# Generate augmented images and masks and save them to disk
for i, (image_filename, mask_filename) in enumerate(zip(image_filenames, mask_filenames)):
    # Load the original image and mask
    image_path = os.path.join(image_dir, image_filename)
    mask_path = os.path.join(mask_dir, mask_filename)
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)
    for j in range(num_augmentations):
        # Augment the image and mask
        augmented = transform(image=image, mask=mask)
        augmented_image = augmented["image"]
        augmented_mask = augmented["mask"]
        # Save the augmented image and mask
        new_image_filename = f"aug_images/{i*num_augmentations+j+2001}.png"
        new_mask_filename = f"aug_labels/{i*num_augmentations+j+2001}.png"
        cv2.imwrite(new_image_filename, augmented_image)
        cv2.imwrite(new_mask_filename, augmented_mask)
