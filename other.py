import random
import pandas as pd


class DataGen:
    def __init__(self, len_of_name, len_of_password):
        self.len_of_name = len_of_name
        self.len_of_password = len_of_password
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

    def parse_names(self):
        self.url = 'https://www.babynamewizard.com/the-top-1000-baby-names-of-2011-united-states-of-america'
        self.tables = pd.read_html(self.url)
        self.fd = self.tables[0]
        with open('data_fol/mans.txt', 'a+') as self.write_man_names:
            for i in range(len(self.fd['Boys'])):
                self.write_man_names.write(self.fd['Boys'][i]+'\n')

        with open('data_fol/girls.txt', 'a+') as self.write_woman_names:
            for i in range(len(self.fd['Girls'])):
                self.write_woman_names.write(self.fd['Girls'][i]+'\n')

    def open_all_files(self):
        with open('data_fol/mans.txt', 'r+') as self.read_names_output:
            self.name = self.read_names_output.read().split('\n')

        with open('data_fol/last_names.txt', 'r+') as self.last_names_output:
            self.surname = self.last_names_output.read().split(',\n')

    def data_for_register(self):
        self.username = ''.join(random.choice(self.letters) for self.i in range(self.len_of_name))
        self.passwd = ''.join(random.choice(self.letters) for self.i in range(self.len_of_password))

        self.first_name = random.choice(self.name)

        self.last_name = random.choice(self.surname)
        return [self.username, self.passwd]

    def write_to_txt(self):
        with open('data_fol/pass.txt', 'w+') as self.output:
            print(self.username, self.passwd, self.first_name, self.last_name)
            self.output.write(f'Username: {self.username}\n'
                              f'Pass: {self.passwd}\n'
                              f'First name: {self.first_name}\n'
                              f'Surname: {self.last_name}')


if __name__ == '__main__':
    dg = DataGen(10, 10)
    # dg.parse_names()
    dg.open_all_files()
    dg.data_for_register()
    dg.write_to_txt()
