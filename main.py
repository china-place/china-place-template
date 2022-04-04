import os.path
import re
from PIL import Image
from typing import List, Tuple
from os import walk

CONTAINER_SIZE_X = 6000
CONTAINER_SIZE_Y = 6000
CONTAINER_DEFAULT_COLOR = (0, 0, 0, 0)

PIXEL_GROUP_SIZE = 3

IMAGE_DEFAULT_PATH = "./images"

COORD_MATCHER = re.compile(r"\(([0-9]+)\,([0-9]+)\)\.png$")


class PixelImage:
    data: List[List[Tuple[int, int, int, int]]]
    startX: int
    startY: int

    def __init__(self):
        self.data = []
        self.startX = 0
        self.startY = 0

    def write(self, image: Image):
        maxWidth = len(self.data)
        maxHeight = len(self.data[0])

        for w in range(0, maxWidth):
            for h in range(0, maxHeight):
                pixel = self.data[w][h]
                drawX = self.startX + w * PIXEL_GROUP_SIZE + 1
                drawY = self.startY + h * PIXEL_GROUP_SIZE + 1
                image.putpixel((drawX, drawY), pixel)


def main():
    container = Image.new("RGBA", (CONTAINER_SIZE_X, CONTAINER_SIZE_Y), CONTAINER_DEFAULT_COLOR)

    images = findAvailableImages()

    for img in images:
        img.write(container)

    container.save("output.png")
    container.save("china_place_template.png")


def findAvailableImages() -> List[PixelImage]:
    images = []
    for (root, _, files) in walk(IMAGE_DEFAULT_PATH):
        for filename in files:
            findResult = COORD_MATCHER.findall(str(filename))
            if len(findResult) != 0:
                (w, h) = findResult[0]

                path = os.path.join(root, filename)

                image = createImage(path)
                image.startX = int(w) * PIXEL_GROUP_SIZE
                image.startY = int(h) * PIXEL_GROUP_SIZE

                images.append(image)


    return images


def createImage(path: str) -> PixelImage:
    print(f"Creating image from {path}")
    im = Image.open(path)
    maxWidth, maxHeight = im.size

    result = PixelImage()

    for w in range(0, maxWidth):
        row = []
        result.data.append(row)
        for h in range(0, maxHeight):
            value = im.getpixel((w, h))
            row.append(value)
    return result


if __name__ == '__main__':
    main()

