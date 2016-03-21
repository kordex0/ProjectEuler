
import sys, math

from primes import isPrime, primes, nprimes
from factors import primeFactorDict as primeFactorsDict
from factors import primeFactorList as primeFactorsList
from factors import primeFactorSet as primeFactorsSet
from divisors import divisors as factors
from divisors import properDivisors as properFactors

def _import_module(name):
    __import__(name)
    return sys.modules[name]

# make sure to always use the iterator range
def range(*args, **kwargs):
    if sys.version_info[0] == 2:
        module = _import_module("__builtin__")
        return getattr(module, "xrange")(*args,**kwargs)
    else:
        module = _import_module("builtins")
        return getattr(module, "range")(*args,**kwargs)  

