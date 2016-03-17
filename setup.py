from distutils.core import setup, Extension
extension_mod = Extension("primes", ["primesmodule.c"])
setup(name="primes", ext_modules=[extension_mod])
