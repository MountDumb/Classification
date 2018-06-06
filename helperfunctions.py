from os import walk, path, listdir


def get_absfilenames(directory):
    for dirpath, dirs, filenames in walk(directory):
        for f in filenames:
            yield path.abspath(path.join(dirpath, f))


def get_filenames(directory):
    for dirpath, dirs, filenames in walk(directory):
        yield from filenames
