from click import FileError
import basify
from cipher import file_to_int as fileint, int_to_file as intfile


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
    else:
        return FileError(
            "Extension can't be recognised, enter an output file name")

    with open(out, 'w', encoding='utf-8') as o:
        o.write(compressed_data)

    return None


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
        return FileError(
            "Extension can't be recognised, enter an output file name")

    data = basify.from_anybase(compressed_data, 65536, None, ord)
    return intfile(data, out)

#! Most imp functions left

def pixelize(path, out): pass


def unpixelize(path, out): pass
