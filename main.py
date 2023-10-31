#menu
def menu():
    # Printing the main menu:
    print('Menu')
    print('------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

#encoder that adds three to each digit
def encoder(password):
    new_password = []
    for char in str(password):
        new_password.append(int(char) + 3)
    return new_password

#decoder that varun yelchur added
def decoder(password):
    final_list = []
    temp_list = list(password.strip(" "))
    for i in temp_list:
        i = int(i)
        i -= 3
        i = str(i)
        final_list.append(i)
    password = str(''.join(final_list))
    return password

#main method
if __name__ == '__main__':
    choice = 0
    while choice != 3:
        menu()
        choice = input('Please enter an option: ')
        if choice == '1':
            user_pass = input('Please enter your password to encode: ')
            print(encoder(user_pass))
            print('Your password has been encoded and stored.')
        elif choice == '2':
            new_pass = input('Please enter your password to decode: ')
            print(decoder(new_pass))
        elif choice == '3':
            exit()
        else:
            print('Invalid choice, please try again.')
