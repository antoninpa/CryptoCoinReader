# CryptoCoinReader
Generate crypto currencies ascii price charts in a terminal.

![Chart illustration](/static/ccr_reader.png)

## Description

CryptoCoinReader (CCR) is a python script which outputs in the terminal a historical diagram of multiple cryptocurrencies' price.

By default it outputs a BTC to USD price chart over the last 3 days but you can customize it:
 * Choose which coin to compare to another coin as you wish
 * Choose the time range of the plot (1D/3D/7D/1M/6M/1Y)
 * Set the plot's height and width.

Just press [Enter] to enter the main menu.

## About the script

Python 3 is supported out of the box. Python 2 should be supported as long as `raw_input()` is changed into `input()`.

CCR requires a few python packages not included in Python, namely [requests](http://docs.python-requests.org/en/master/), [numpy](https://www.numpy.org/) and [gnuplotlib](https://github.com/dkogan/gnuplotlib).

## Author

Antonin Paillet `antonin@paillet.fr`

## License and copyright

This program is free software; you can redistribute it and/or modify it under the terms of the Creative Commons Attributions Share Alike Internationnal Public Licence v4.0

See : https://creativecommons.org/licenses/by-sa/4.0/legalcode
