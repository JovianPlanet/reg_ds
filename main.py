import os
import argparse
from config import get_parameters
from transforms import flip, registrate, reg_T1toT2FLAIR
from plots import plots

def main(config):

    if config['mode'] == 'reg':

        #registrate(config)
        reg_T1toT2FLAIR(config)

    elif config['mode'] == 'flip':

        flip(config)

    elif config['mode'] == 'plot':

        plots(config)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Registrar, reorientar o plotear MRI')
    parser.add_argument('-m', 
                        '--mode', 
                        choices=['reg', 'flip', 'plot'],
                        default='reg',
                        help="Modo de operacion del programa.\n \
                        Las opciones son: \
                        'reg', 'flip' y 'plot'.\n \
                        La opcion por defecto es 'reg'"
    )

    args = parser.parse_args()
    config = get_parameters(args.mode, 'lab')
    main(config)
