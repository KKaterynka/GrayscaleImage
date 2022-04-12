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
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                self.setitem(i, j, value)

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
        c = 0

        for i in range(self.height()):
            for j in range(self.width()):
                try:
                    img_gray.setitem(i, j, cipher[c])
                    c += 1
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
        # print(j)
        print_pic(self.img)  # ORIGINAL
        print_pic(j)  # RECOVERED from comp.


if __name__ == "__main__":
    pixels = GrayscaleImage(6, 6)
    print(pixels.height(), pixels.width())
    pixels.setitem(3, 4, 12)
    print(pixels.getitem(3, 4))

    img_gray = GrayscaleImage()
    img_gray.from_file('try.jpg')
    # print(img_gray.lzw_compression())
    img_gray.lzw_decompression(img_gray.lzw_compression())
    print(img_gray.getitem(0, 0))
