import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


def print_pic(img):
    """
    Shows gray image
    """
    imgplot = plt.imshow(img)
    plt.show()


def LZW_encode(uncompressed):
    """
    Build the dictionary.
    only big letters
    """
    dict_size = 26
    dictionary = {chr(i + ord('A')): i for i in range(dict_size)}

    p = ""
    output = []
    for c in uncompressed:
        temp = p + c
        if temp in dictionary:
            p = temp
        else:
            output.append(dictionary[p])
            # Add temp to the dictionary.
            dictionary[temp] = dict_size
            dict_size += 1
            p = c

    # Output the code for w.
    if len(p):
        output.append(dictionary[p])
    return output


def LZW_decode(compressed):
    """
    Decodes compressed array
    """
    # Build the dictionary.
    dict_size = 26
    dictionary = {i: chr(i + ord('A')) for i in range(dict_size)}

    result = ""
    p = ""
    bol = False
    for k in compressed:

        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = p + p[0]

        result += entry

        # Add p+entry[0] to the dictionary unless it's first element
        if bol:
            dictionary[dict_size] = p + entry[0]
            dict_size += 1

        p = entry
        bol = True
    return result


def inttochar(z):
    """
    Transforms to character
    """
    return chr((z // 10) + 65)


def chartoint(z):
    """
    Transforms to integer
    """
    return (ord(z) - 65) * 10
