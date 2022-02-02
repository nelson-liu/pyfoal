import librosa

import pyfoal


###############################################################################
# Loading
###############################################################################


def audio(file):
    """Load audio from file"""
    # Using librosa to load audio at its native sampling rate. We use this
    # instead of the original soundfile to automatically convert
    # stereo to mono.
    audio, sample_rate = librosa.load(file, sr=None)

    # Resample
    return pyfoal.resample(audio, sample_rate)


def phonemes():
    """Load list of phonemes"""
    # Cache phonemes
    if not hasattr(phonemes, 'phonemes'):
        with open(pyfoal.ASSETS_DIR / 'monophones') as file:
            phonemes.phonemes = [line.rstrip() for line in file.readlines()]

    return phonemes.phonemes
