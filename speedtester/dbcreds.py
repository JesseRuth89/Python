# Creates a credential file.
from cryptography.fernet import Fernet
import ctypes
import time
import os
import sys


class Credentials:

    def __init__(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        key_file = 'db.key'
        key_ini = 'db.ini'
        self.__username = ''
        self.__key = ''
        self.__password = ''
        self.__key_file = os.path.join(directory, key_file)
        self.__key_ini = os.path.join(directory, key_ini)
        self.__time_of_exp = -1

    # ----------------------------------------
    # Getter setter for attributes
    # ----------------------------------------

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        while (username == ''):
            username = input('Enter a proper User name, blank is not accepted:')
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__key = Fernet.generate_key()
        f = Fernet(self.__key)
        self.__password = f.encrypt(password.encode()).decode()
        del f

    @property
    def expiry_time(self):
        return self.__time_of_exp

    @expiry_time.setter
    def expiry_time(self, exp_time):
        if (exp_time >= 2):
            self.__time_of_exp = exp_time

    def create_cred(self):
        # generating key_ini and key_file
        with open(self.__key_ini, 'w') as file_in:
            file_in.write(f'#Credential file:'
                          f'\nUsername={self.__username}'
                          f'\nPassword={self.__password}'
                          f'\nExpiry={self.__time_of_exp}\n')
            file_in.write('++' * 20)

        # If there exists an older key file, This will remove it.
        if (os.path.exists(self.__key_file)):
            os.remove(self.__key_file)

        # Open the Key.key file and place the key in it.
        # The key file is hidden.
        try:

            os_type = sys.platform
            if (os_type == 'linux'):
                self.__key_file = '.' + self.__key_file

            with open(self.__key_file, 'w') as key_in:
                key_in.write(self.__key.decode())
                # Setting the key file to hidden
                if (os_type == 'win32'):
                    ctypes.windll.kernel32.SetFileAttributesW(self.__key_file, 2)
                else:
                    pass

        except PermissionError as error:
            os.remove(self.__key_file)
            print(f'A Permission error occurred {error}.'
                  f'\n Please re run the script')
            sys.exit()

        self.__username = ''
        self.__password = ''
        self.__key = ''
        self.__key_file

    def getpass(self):
        with open(self.__key_file, 'r') as key_in:
            key = key_in.read().encode()
        f = Fernet(key)
        with open(self.__key_ini, 'r') as cred_in:
            # need to use compression here :P
            for line in cred_in.readlines():
                r = line.rstrip('\n').split('=', 1)
                if r[0] == 'Password':
                    return f.decrypt(r[1].encode()).decode()

    def getuser(self):
        with open(self.__key_ini, 'r') as cred_in:
            # need to use compression here :P
            for line in cred_in.readlines():
                r = line.rstrip('\n').split('=', 1)
                if r[0] == 'Username':
                    return r[1]


def main():
    # Creating an object for Credentials class
    creds = Credentials()

    # Accepting credentials
    creds.username = input('Enter UserName:')
    creds.password = input('Enter Password:')
    print('Enter the epiry time for key file in minutes, [default:Will never expire]')
    creds.expiry_time = int(input('Enter time:') or '-1')

    # calling the Credit
    creds.create_cred()
    print('**' * 20)
    print(f'Cred file created successfully at {time.ctime()}')
    print('**' * 20)
    print(f'My password is {creds.getpass()}')
    print(f'My Username is {creds.getuser()}')


if __name__ == '__main__':
    main()
