#2nd part of registerph

from passwords import log_pass
from passwords import log_name
from passwords import log_name1
from passwords import log_age
from registerph import main

login = input('Enter your login: ')
pasword = input('Enter your password: ')
while log_pass != pasword or log_name != login:
    if log_pass != pasword or log_name != login:
            print('incorrect data')
            login = input('Enter your login: ')
            pasword = input('Enter your password: ')
            continue
    while True:
        print()
        print('--------------------------')
        print('\nCommands:')
        print("'sd' - show data")
        print("'rereg' - re-registration")
        print("'passchange' - change password")
        print("'exit' - shutting down")
        a = input("Enter a command: ")


        if a.lower() == 'rereg':
            with open('passwords.py', 'w', encoding='utf-8') as f:
                pass
            main()
        elif a.lower() == 'sd':
            print(f'Profile:\n First name: {log_name}\n Last name: {log_name1}\n Age: {log_age}')
        elif a.lower() == 'passchange':
            from passwords import log_pass, log_name, log_name1, log_age

            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm new password: ")

            if len(new_password) < 6 or new_password != confirm_password:
                print("Incorrect password or passwords do not match.")
            else:
                with open('passwords.py', 'w', encoding='utf-8') as f:
                    f.write(
                        f'log_pass = str("{new_password}")\nlog_name = str("{log_name}")\nlog_name1 = str("{log_name1}")\nlog_age = str("{log_age}")')
                print('Password successfully changed')
        elif a.lower() == 'exit':  # checking for exit
            print("Shuitting down...")
            break  # breaking cycle after 'exit' command



