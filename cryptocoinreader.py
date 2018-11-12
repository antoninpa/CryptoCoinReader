#!/usr/bin python3
# -*- coding: utf-8 -*-
# title           :cryptocoinreader.py
# description     :This program displays a cryptocurrency price reader
# author          :<antonin@paillet.fr>
# date            :
# version         :1
# usage           :python cryptocoinreader.py
# notes           :
# python_version  :3.5.6
# licence         :CC/BY-SA
# =======================================================================

import sys, os
import threading
import data  # import data.py
import requests
import numpy as np
import gnuplotlib as gp
import json


# =======================
#     MENUS FUNCTIONS
# =======================

class CryptoCoinReader:

    def __init__(self):

        # Data from data.py
        self.currencies = data.currencies
        self.header = data.header
        self.colors = data.colors

        # Chart default data
        self.from_cur = 'BTC'
        self.to_cur = 'USD'
        self.period = 'histohour'
        self.limit = '72'
        self.time_s = '72h'
        self.timeform = '%d/%m\\n%H:%M'
        self.refresh_time = 3600  # 1 hour.

        self.width = '210'
        self.height = '55'

        # Menu definition
        self.menu_actions = {
            'main_menu': self.main_menu,
            '1': self.change_cur,
            '2': self.time,
            '3': self.size,
            '8': self.credits,
            '9': self.back,
            '10': self.reader,
            '0': self.exit,
        }

    def colorize(self, string, color):
        if color not in self.colors:
            return string
        return self.colors[color] + string + '\033[0m'

    def requestData(self):
        r = requests.get(
            'https://min-api.cryptocompare.com/data/%s?fsym=%s&tsym=%s&limit=%s&aggregate=1&e=CCCAGG' %
            (
                self.period,
                self.from_cur,
                self.to_cur,
                self.limit
            )
        )

        jj = json.loads(r.text)  # loads it into json format
        price = [el['close'] for el in jj['Data']]
        _time = [el['time'] for el in jj['Data']]

        return price, _time

    def reader(self):
        """
        Chart screen
        Note : because of the raw_input only
        a threaded function can refresh x time (it seems)
        Also the thread is surrounded by 2 os.system('clear')
        otherwise they have no effect
        """
        os.system('clear')
        #threading.Timer(%d, self.reader).start() % self.refresh_time
        os.system('clear')

        y_price, x_time = self.requestData()
        y = np.array(y_price)
        x = np.array(x_time)
        my_title = '* %s/%s (%s) *' % (self.from_cur, self.to_cur, self.time_s)
        gp.plot(
            x,
            y,
            xlabel='\\nTime (GMT)',
            ylabel=self.to_cur,
            set=[
                'lmargin 12',
                'ylabel',
                'xlabel',
                'xdata time',
                'format x "%s"' % self.timeform
            ],
            unset='grid',
            _with='lines',
            terminal='dumb %s %s' % (self.width, self.height),
            title=my_title+'\\n'+'*'*(len(my_title))
        )

        print(self.colorize('[Enter] menu', 'grey'))
        choice = raw_input('')
        self.exec_menu(choice)

    def exec_menu(self, choice):
        os.system('clear')
        ch = choice.lower()
        if ch == '':
            self.menu_actions['main_menu']()
        else:
            try:
                self.menu_actions[ch]()
            except KeyError:
                print('Invalid selection, please try again.\n')
                self.menu_actions['main_menu']()
        return

    def main_menu(self):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print('Main menu')
        print('---------\n')
        print('1. Change currencies')
        print('2. Change time laps')
        print('3. Change size of the plot\n')

        print(self.colorize('8. Credits', 'green'))
        print(self.colorize('10. Back to reader', 'green'))
        print(self.colorize('0. Quit', 'red'))
        choice = raw_input('  >>  ')
        self.exec_menu(choice)
        return

    # ===============
    # CURRENCY MENUS
    # ===============

    # Menu currency - from
    def change_cur(self):

        # From currency - screen
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print("Choose the first currency to compare\n")

        print('\n'.join([el for el in self.currencies]))

        print('\n')
        print("9. Back")
        print("0. Quit")
        choice = raw_input(" >>  ")
        self.from_cur = choice

        # To Currency - screen
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print("Choose the currency to be compared to\n")

        print('\n'.join([el for el in self.currencies]))

        print('\n')
        print("9. Back")
        print("0. Quit")
        choice = raw_input(" >>  ")
        if choice not in self.currencies:
            print("Invalid selection, try again")
            self.menu_actions['1']()
        else:
            self.to_cur = choice
            self.exec_menu('10')
            return

    # ==========
    # TIME MENU
    # ==========

    def time(self, error=None):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))

        print("Change the time laps\n\n")

        print('1. Last 24H')
        print('2. Last 3 days')
        print('3. Last week')
        print('4. Last month')
        print('5. Last 6 months')
        print('6. Last year')

        print('\n')
        print("9. Back")
        print("0. Quit\n")
        print(self.colorize(error, 'red')) if error else ''
        choice = raw_input(" >>  ")
        if choice not in data.time:
            self.menu_actions['2']('Invalid selection, try again')
        else:
            self.period = data.time[choice][0]
            self.limit = data.time[choice][1]
            self.timeform = data.time[choice][2]
            self.refresh_time = data.time[choice][3]
            self.time_s = data.time[choice][4]
            self.exec_menu('10')

    # =================
    # CHART SIZE MENU
    # =================

    def size(self, error=None):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print('Change the size of the plot.\n')
        print('1. Set size manually')
        print('2. Size for a 1920*1080 monitor\n')

        print(self.colorize(error, 'red')) if error else ''
        choice = raw_input(' >>  ')
        if choice == '1':
            self.set_size_width()
        elif choice == '2':
            self.width = '210'
            self.height = '55'
            self.menu_actions['10']()
        else:
            self.menu_actions['3']('Invalid selection, try again')

    def set_size_width(self):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print('Change the width of the plot.\n')
        choice = raw_input('Size of the plot >>>')
        self.width = choice
        self.set_size_heigth()

    def set_size_heigth(self):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))
        print('Change the height of the plot.\n')
        choice = raw_input('Height of the plot >>>')
        self.height = choice
        self.menu_actions['10']()

    # ===========
    # MISC MENUS
    # ===========

    def credits(self):
        os.system('clear')
        print(self.colorize(data.header, 'pink'))

        print('Data : cryptocompare.com')
        print('Time is GMT.\n')
        print('Reader made by Antonin Paillet (github.com/antoninpa/CryptoPiReader)')
        print('Version : 0.1')
        print('Licence : CC/By-NC-SA\n')

        print(self.colorize('9. Back to menu', 'green'))
        print(self.colorize('10. Back to reader', 'green'))
        print(self.colorize('0. Quit', 'red'))
        choice = raw_input("  >>  ")
        self.exec_menu(choice)

    # Back to main menu
    def back(self):
        self.menu_actions['main_menu']()

    # Exit program
    def exit(self):
        sys.exit()


# Main Program
if __name__ == "__main__":
    CryptoCoinReader().reader()

