def encoder(password):
    new_password = []
    for char in str(password):
        new_password.append(int(char) + 3)
    return new_password
