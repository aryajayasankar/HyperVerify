"""
Image Processing Service
"""

from backend.utils.image_utils import (
    convert_to_gray,
    get_image_info,
    load_image,
    save_image,
    show_image,
)


def main():

    image_path = "datasets/sample_images/Arya_image.png"

    image = load_image(image_path)

    get_image_info(image)

    show_image("Original Image", image)

    gray = convert_to_gray(image)

    show_image("Grayscale Image", gray)

    save_image(gray, "assets/output/gray_image.png")

    print("\nGrayscale image saved successfully!")


if __name__ == "__main__":
    main()