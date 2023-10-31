
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
