"""
Image Utility Functions
-----------------------
Reusable image processing functions used throughout HyperVerify.
"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """
    Load an image from disk.

    Args:
        image_path: Path to image.

    Returns:
        Image as NumPy array.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Cannot load image: {image_path}")

    return image


def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Save image to disk.
    """

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(output_path, image)


def show_image(title: str, image: np.ndarray) -> None:
    """
    Display image using matplotlib.
    """

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(6, 6))
    plt.imshow(rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()


def convert_to_gray(image: np.ndarray) -> np.ndarray:
    """
    Convert BGR image to grayscale.
    """

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def get_image_info(image: np.ndarray) -> None:
    """
    Print useful image information.
    """

    print("=" * 40)
    print("Image Information")
    print("=" * 40)
    print(f"Shape      : {image.shape}")
    print(f"Height     : {image.shape[0]}")
    print(f"Width      : {image.shape[1]}")

    if len(image.shape) == 3:
        print(f"Channels   : {image.shape[2]}")
    else:
        print("Channels   : 1")

    print(f"Data Type  : {image.dtype}")
    print(f"Min Pixel  : {image.min()}")
    print(f"Max Pixel  : {image.max()}")