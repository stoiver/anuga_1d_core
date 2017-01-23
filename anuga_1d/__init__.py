""" ANUGA_1D models Shallow water flow in 1D


"""

#-----------------------------------------------------
# Make selected classes available directly
#-----------------------------------------------------


__version__ = '0.5'

__svn_revision__ = filter(str.isdigit, "$Revision: 9740 $")

__svn_revision_date__ = "$Date: 2017-01-23 16:44:46 +1100 (Mon, 23 Jan 2017) $"[7:-1]


# We first need to detect if we're being called as part of the anuga_1d setup
# procedure itself in a reliable manner.
try:
    __ANUGA_1D_SETUP__
except NameError:
    __ANUGA_1D_SETUP__ = False
    
    
if __ANUGA_1D_SETUP__:
    import sys as _sys
    _sys.stderr.write('Running from anuga_1d source directory.\n')
    del _sys
else:

    try:
        from anuga_1d.__config__ import show as show_config
    except ImportError:
        msg = """Error importing anuga1d: you should not try to import anuga from
        its source directory; please exit the anuga_1d source tree, and relaunch
        your python interpreter from there."""
        raise ImportError(msg)
    
    
    #---------------------------------
    # Setup the nose tester from numpy
    #---------------------------------
    from numpy.testing import Tester
    test = Tester().test

