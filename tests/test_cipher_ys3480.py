from cipher_ys3480 import cipher_ys3480

import pytest


def test_cipher_word():
    example = 'abstruse'
    expected = 'bctusvtf'
    actual = cipher_ys3480.cipher('abstruse', 1)
    assert actual == expected

test_cipher_word()