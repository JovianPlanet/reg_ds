import os
from config import get_parameters
from transforms import flip, registrate

def main(config):

    if config['mode'] == 'reg':

        registrate(config)

    elif config['mode'] == 'flip':

        flip(config)

    elif config['mode'] == 'plot':

        plots(config)

if __name__ == '__main__':
    config = get_parameters('home')
    main(config)
