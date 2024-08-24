# Programmatically run as if "nosetests" on command line
# NOTE: run this from the top level pyopenxr folder, *NOT* from this "tests" folder.

# workaround for python 3.10 and nose
import collections.abc
collections.Callable = collections.abc.Callable
import nose

nose.main()
