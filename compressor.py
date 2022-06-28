import basify
from filedata import (
    file_to_int as fileint,
    int_to_file as intfile,
    visualise,
    getrgb,
    unpixel)
import os


def compress(path, out=None):
    '''Compresses a larger file to smaller output file with ext .utf8

    Args:
        path (str): File to compress
        out (str): Output file path
    '''
    data = fileint(path)
    compressed_data = basify.digitify(basify.base_unicode(data))

    if not out:
        out = path+'.utf8'

    with open(out, 'w', encoding='utf-8') as o:
        o.write(compressed_data)


def uncompress(path: str, out=None):
    '''Uncompresses the compressed file

    Args:
        path (str): The file compressed data is stored in
        out (str): The output file, remember the extension sha
    '''
    with open(path, encoding='utf-8') as f:
        compressed_data = f.read()

    if not out and path.endswith('.utf8'):
        out = path[:-5]

    data = basify.from_anybase(compressed_data, 1114111, None, ord)
    intfile(data, out)


def compress_ascii(path, out) -> None:
    '''Compresses a larger file to smaller output file with ext .ascii

    Args:
        path (str): File to compress
        out (str): Output file path
    '''
    data = fileint(path)
    compressed_data = basify.digitify(basify.base_ascii(data))

    if not out:
        out = path+'.ascii'

    with open(out, 'w', encoding='utf-8') as o:
        o.write(compressed_data)


def uncompress_ascii(path: str, out):
    '''Uncompresses the compressed file

    Args:
        path (str): The file compressed data is stored in
        out (str): The output file, remember the extension sha
    '''
    with open(path, encoding='utf-8') as f:
        compressed_data = f.read()

    if not out and path.endswith('.ascii'):
        out = path[:-6]
    else:
        return NameError(
            "Extension can't be recognised, enter an output file name")

    data = basify.from_anybase(compressed_data, 65536, None, ord)
    return intfile(data, out)


def pixelize(path: str, out: str = None) -> None:
    '''COnvert the data inside a file image

    Args:
        path (str): File path to convert to pixels
        out (str, optional): The output path of the converted image
    '''
    data = fileint(path)
    pixels = list(basify.base_pixel(data).values())

    if not out:
        out = path+'.png'

    visualise(pixels, out)


def unpixelize(path: str, out: str) -> None:
    '''Converts the data inside the image file back to original file

    Args:
        path (str): Path to the compressed data image
        out (str): The path for the output file
    '''

    pixels = getrgb(path)
    # data = sum(unpixel(pixel) for pixel in pixels)

    data = basify.from_anybase(pixels, 16777216, None, unpixel)

    if not out and path.endswith('.png'):
        out = path[:-4]

    intfile(data, out)


def pixelize_ascii(path: str, out: str = None) -> None:
    '''Returns the compressed file image after ascii compression

    Args:
        path (str): Path to the file to compress
        out (str): The output file path
    '''
    if not out:
        out = path+'.ascii.png'
    compress_ascii(path, 'temp.ascii')
    pixelize('temp.ascii', out)
    os.remove('temp.ascii')


#! Still buggy
def unpixelize_ascii(path: str, out: str = None) -> None:
    '''Converts the compressed file image back to the original file

    Args:
        path (str): Path to the ascii compressed file image
        out (str, optional): Path to the destination file. Defaults to None.
    '''
    if not out and path.endswith('.ascii.png'):
        out = path[:-10]
    uncompress(path, 'temp.ascii')
    uncompress_ascii('temp.ascii', out)
    os.remove('temp.ascii')
