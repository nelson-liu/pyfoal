import pyfoal


def phoneme_to_index(phoneme):
    """Convert phoneme as a string to an integer index"""
    # Cache map
    if not hasattr(phoneme_to_index, 'map'):
        with open(pyfoal.ASSETS_DIR / 'monophones') as file:
            phoneme_to_index.map = {
                phoneme: i for i, phoneme in enumerate(file.readlines())}

    # Convert
    return phoneme_to_index.map[phoneme]


def index_to_phoneme(index):
    """Convert integer index representing a phoneme to a string"""
    # Cache map
    if not hasattr(index_to_phoneme, 'map'):
        with open(pyfoal.ASSETS_DIR / 'monophones') as file:
            index_to_phoneme.map = {
                i: phoneme for i, phoneme in enumerate(file.readlines())}

    # Convert
    return index_to_phoneme.map[index]