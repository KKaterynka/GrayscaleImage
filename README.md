
![](https://github.com/KateKo04/GrayscaleImage/blob/main/styles_rm/grayscaled_title.png)

In computer graphics, images in shades of grey is an image where each pixel codes information about its intensity. It's also named grayscale image, 'cause it contains only shades of gray, gradation of which is changing from intensive black to white.

In a nutshell, image in shades of grey, it is a two-dimensional illustration consisting of pixels, which are measured in [0,..,255] array, where 0 is black and 255 - white.

## Files
* arrays.py - contains the implemantation of 2DArray
* lzw.py - contains the compression algorithm of encoding and decoding, based on LZW
* grayscale_digital.py - contains Grayscale Image ADT and two examples of usage
* try.jpg - trial image for compression and decompression

## Grayscale Image ADT
is based on 2DArray ADT.
* GrayscaleImage(nrows, ncols): creates new object, which contains nrows * ncols pixels(by default has value of 0)
* width(): returns width of image
* height(): returns height of umage
* clear(value): clears the image setting each pixel to value
* getitem(row, col): returns value of intensity in given pixel. Coordninates of pixel must be in valid range
* setitem(row, col, value): sets value of intensity to the given pixel. Coordninates of pixel must be in valid range
* from_file(path): creates an object, based on the image(png or jpg)
* lzw_compression(): compression of image based on Lempel-Ziv-Welch(LZW)
* lzw_decompression(): shows the image that was compressed with the help of Lempel-Ziv-Welch(LZW) algorithm
