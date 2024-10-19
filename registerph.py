import os
import subprocess
#ph register code

def main():
    if os.path.exists('passwords.py') and os.path.getsize('passwords.py') <= 0:
        while True:
            name1 = input('Enter your first name: ')
            name2 = input('Enter your last name: ')
            age = input('Enter your age: ')
            password = input('Enter your password (min 6 symbols): ')
            password1 = input('Confirm your password: ')

            # conditions
            if int(age) < 18:
                print("You're underaged!")
                continue
            elif name1 and name1[0].isdigit() or name2 and name2[0].isdigit():
                print("incorrect name")
                continue
            elif password1 != password:
                print("incorrect password")
                continue
            elif len(password) < 6 or len(password1) < 6:
                print("incorrect password")
                continue
            else:
                with open('passwords.py', 'w', encoding='utf-8') as f:
                    f.write(f'log_pass = str("{password}")\nlog_name = str("{name1}")\nlog_name1 = str("{name2}")\nlog_age = str("{age}")')
                print(f'\nProfile:\n First name: {name1}\n Last name: {name2}\n Age: {age}')
                break  # successful registration, breaking cycle
    else:
        subprocess.run(['python', 'registerph1.py'])
    # menu after successful registration
    while True:
        print()
        print('--------------------------')
        print('Commands:\n')
        print("'rereg' - re-registration")
        print("'passchange' - change password'")
        print("'exit' - shutting down")
        a = input("Enter a command: ")

        if a.lower() == 'rereg':
            with open('passwords.py', 'w', encoding='utf-8') as f:
                pass
            main()  # summon the registration again
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
        if a.lower() == 'exit':  # checking for shut down
            print("Shutting down...")
            break  # breaking cycle after 'exit'

if __name__ == "__main__":
    main()