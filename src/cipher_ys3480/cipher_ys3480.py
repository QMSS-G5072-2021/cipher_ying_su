def cipher(text, shift, encrypt=True):
    
    """
    Encrypts and decrypts messages.

    Parameters
    ----------
    text : str 
      A string of any length.
    shift : int
      The encryption key. This will be an integer. This stipulates how many shifts backwards the key to the message will be.
    encrypt: bool
      True if you'd like to encrypt the string, False if you'd like to decrypt the string. Default is True.

    Returns
    -------
    str 
      The encrypted (or decrypted) message.

    Examples
    --------
    >>> from cipher_ys3480 import cipher_ys3480
    >>> text = 'abstruse'
    >>> shift = 1
    >>> encrypt = True
    >>> cipher_ys3480.cipher(text, shift, encrypt)
    'bctusvtf'
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

