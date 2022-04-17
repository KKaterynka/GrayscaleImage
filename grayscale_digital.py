from arrays import Array2D
from lzw import LZW_encode, inttochar, LZW_decode, chartoint, print_pic
import PIL
import numpy as np
import cv2


class GrayscaleImage:
    """
    Defines GrayscaleImage
    class
    """

    def __init__(self, nrows=1, ncols=1):
        """
        Takes number of rows and columns.
        Transforms to 2D array.
        Sets each pixel to 0
        """
        self._grid = Array2D(nrows, ncols)
        self.img = 0
        self.clear()

    def width(self):
        """
        Returns width of image
        """
        return self._grid.num_cols()

    def height(self):
        """
        Returns height of image
        """
        return self._grid.num_rows()

    def clear(self, value=0):
        """
        Configures the img ground
        """
        for row in range(self._grid.num_rows()):
            for col in range(self._grid.num_cols()):
                self.setitem(row, col, value)

    def setitem(self, row, column, value):
        """
        Sets pixel to given value
        """
        self._grid[row, column] = value

    def getitem(self, row, col):
        """
        Gets item based on
        its row and column
        """
        return self._grid[row, col]

    def from_file(self, path):
        """
        Takes path to img
        """
        self.path = path
        self.img = cv2.imread(path, 0)
        height, width = self.img.shape
        self._grid = Array2D(height, width)
        self.clear()

        cipher = self.lzw_compression()
        cipher_counter = 0

        for row in range(self.height()):
            for col in range(self.width()):
                try:
                    img_gray.setitem(row, col, cipher[cipher_counter])
                    cipher_counter += 1
                except IndexError:
                    continue

    def lzw_compression(self):
        """
        Compresses the picture
        """
        s = ""
        for x in range(self.height()):
            for y in range(self.width()):
                s += str(inttochar(self.img[x, y]))
        return LZW_encode(s)

    def lzw_decompression(self, cipher):
        """
        Decompresses the picture
        """
        reconstruct = []
        plain = LZW_decode(cipher)

        for c in plain:
            reconstruct.append(chartoint(c))

        j = np.reshape(reconstruct, (self.height(), self.width()))

        print_pic(j)  # RECOVERED from comp.


if __name__ == "__main__":
    # create 2DArray image
    # with width and height 6
    pixels = GrayscaleImage(6, 6)
    print(f"Height: {pixels.height()}, width: {pixels.width()}")
    pixels.setitem(3, 4, 12)
    pixels.setitem(0, 0, 17)
    pixels.setitem(5, 3, 18)
    pixels.setitem(5, 2, 4)
    print(f"Extracting specific item: {pixels.getitem(3, 4)}")
    # manually build array of pixels to decompress(for compression image is needed). Just for trial
    compressed = []
    for i in range(len(pixels._grid.rows)):
        for j in range(len(pixels._grid.rows)):
            compressed.append(pixels._grid.rows[i][j])
    pixels.lzw_decompression(compressed)
    # get the specific pixel
    print(f"Array for trial to decompress: {compressed}")

    # compress and decompress image(example with jpg format)
    img_gray = GrayscaleImage()
    img_gray.from_file('try.jpg')
    # compress the image
    compressed = img_gray.lzw_compression()
    # decompress the image
    img_gray.lzw_decompression(compressed)
    # get the specific pixel for image
    print(f"Extracting specific pixel from image: {img_gray.getitem(0, 0)}")
