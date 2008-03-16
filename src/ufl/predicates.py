#!/usr/bin/env python

"""
Functions to check properties of forms and integrals.
"""

__authors__ = "Martin Sandve Alnes"
__date__ = "2008-14-03 -- 2008-16-03"

from output import *
from integral import *
from form import *


def is_multilinear(a):
    """Checks if a form is multilinear. Returns True/False."""
    ufl_assert(isinstance(o, Form), "Assuming a Form.")
    ufl_warning("is_multilinear is not implemented.")
    return True

