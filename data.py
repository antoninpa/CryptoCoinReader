header = "\
   ______                 __        ______      _          ____                 __          \n\
  / ____/______  ______  / /_____  / ____/___  (_)___     / __ \___  ____ _____/ /__  _____ \n\
 / /   / ___/ / / / __ \/ __/ __ \/ /   / __ \/ / __ \   / /_/ / _ \/ __ `/ __  / _ \/ ___/ \n\
/ /___/ /  / /_/ / /_/ / /_/ /_/ / /___/ /_/ / / / / /  / _, _/  __/ /_/ / /_/ /  __/ /     \n\
\____/_/   \__, / .___/\__/\____/\____/\____/_/_/ /_/  /_/ |_|\___/\__,_/\__,_/\___/_/      \n\
          /____/_/                                                                          \n"

currencies = [
    'BTC',
    'ETH',
    'EOS',
    'LTC',
    'XRP',
    'BCH',
    'XMR',
    'QTUM',
    'ZEC',
    'NEO',
    'USD'
]

colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'default': '\033[99m',
    'green': '\033[92m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'red': '\033[91m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
}

time = {
    '1': ['histominute', '1440', '%H:%M', 60, 'Last 24h'],
    '2': ['histominute', '4320', '%d/%m\\n%H:%M', 60, 'Last 72h'],
    '3': ['histohour', '168', '%d/%m', 3600, 'Last 7 days'],
    '4': ['histohour', '720', '%d/%m', 3600, 'Last month'],
    '5': ['histoday', '180', '%d/%m', 3600, 'Last 6 months'],
    '6': ['histoday', '365', '%d/%m', 86400, 'Last year']
}
