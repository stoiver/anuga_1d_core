from __future__ import division, print_function

import os
import sys

from os.path import join

def local_fun():
    pass


def configuration(parent_package='',top_path=None):
    
    from numpy.distutils.misc_util import Configuration

    
    config = Configuration('sqpipe', parent_package, top_path)

    config.add_data_dir('tests')

   
    util_dir = join('..','utilities') 
 
    
    config.add_extension('sqpipe_comp_flux',
                         sources=['sqpipe_comp_flux.c'],
                         include_dirs=[util_dir])        

        

    return config
    
if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(configuration=configuration)
