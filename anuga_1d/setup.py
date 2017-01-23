from __future__ import division, print_function, absolute_import

import sys


def configuration(parent_package='',top_path=None):

    from numpy.distutils.misc_util import Configuration

    config = Configuration('anuga_1d',parent_package,top_path)
    config.add_subpackage('base')
    config.add_subpackage('channel')
    config.add_subpackage('sqpipe')
    config.add_subpackage('utilities')

    
    config.make_config_py()
    
    return config

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')

