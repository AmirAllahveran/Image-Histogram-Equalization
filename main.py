import numpy
from PIL import Image
import matplotlib.pyplot as plt


# TODO level 1
def read_image(path):
    im = Image.open(path)
    print(im.mode)
    pix = im.load()
    array = numpy.zeros([im.size[1], im.size[0]], dtype=numpy.uint8)
    print("the width and height of the image for iterating over", im.size)
    print("the RGBA Value of the a pixel of an image : pix[x,y]")
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            array[j, i] = rgb2gray(pix[i, j])

    img = Image.fromarray(array)
    img.save('grayscale.png')
    print("grayscale image created successfully")
    return 'grayscale.png'


def rgb2gray(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]

    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return int(gray)


# TODO level 2
def create_histogram(path):
    image = Image.open(path).getdata()
    histogram, bin_edges = numpy.histogram(image, bins=256, range=(0, 255))
    # configure and draw the histogram figure
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    plt.xlim([-10, 265])
    plt.plot(histogram)
    plt.show()
    return histogram


# TODO level 3
def cum_sum(histogram):
    return numpy.cumsum(histogram)


# TODO level 4
def create_map(path, histogram_cum_sum):
    color_levels = 256
    image = Image.open(path)
    image_area = image.size[0] * image.size[1]
    mapped_histogram = []
    for i in range(len(histogram_cum_sum)-1):
        mapped_histogram.append((round(color_levels - 1) * histogram_cum_sum[i]) / image_area)
    return mapped_histogram


# TODO level 5
def save_final(path, mapped_histogram):
    im = Image.open(path)
    pix = im.load()
    array = numpy.zeros([im.size[1], im.size[0]], dtype=numpy.uint8)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            array[j, i] = mapped_histogram[pix[i, j]]
    img = Image.fromarray(array)
    img.save('final_gray.png')


if __name__ == '__main__':
    # image_path = input("please enter image path : ")
    image_path = "image.png"
    x = read_image(path=image_path)
    h = create_histogram(x)
    h_cum_sum = cum_sum(h)
    m_h = create_map(x, h_cum_sum)
    save_final(x, m_h)
