def decoder(encoded_pass):
    orig_pass = ''
    for char in str(encoded_pass):
        orig_pass += str(int(char) - 3)
    return orig_pass
