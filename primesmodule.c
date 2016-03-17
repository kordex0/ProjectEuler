
#include <Python.h>
#include <stdbool.h>
#include <math.h>

static PyObject * primes_isPrime(PyObject *self, PyObject *args) {
    const int n;
    int i;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    if(n < 2)
        Py_RETURN_FALSE;
    if(n == 2 || n == 3)
        Py_RETURN_TRUE;
    if(n % 2 == 0)
        Py_RETURN_FALSE;
    if(n % 3 == 0)
        Py_RETURN_FALSE;
    const int nsqrt = sqrt(n);
    for(i=5; i <= nsqrt; i += 6){
        if(n % i == 0 || n % (i+2) == 0)
            Py_RETURN_FALSE;
    }
    Py_RETURN_TRUE;
}


static PyObject * primes_primesList(PyObject *self, PyObject *args) {
    const int n;
    int i, j, count;
    bool *primes;
    PyObject *pylist;
    PyObject *item;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    if(n < 2) {
        return PyList_New(0);
    }
    primes = malloc(sizeof(bool)*n);
    primes[0] = false;
    primes[1] = false;
    for(i=2; i < n; i++) {
        primes[i] = true;
    }
    for(j=4; j < n; j += 2) {
        primes[j] = false;
    }
    for(j=9; j < n; j += 3) {
        primes[j] = false;
    }
    
    const int nsqrt = sqrt(n);
    for(i=5; i <= nsqrt; i += 6){
        if(primes[i]) {
            for(j=i*i; j < n; j += i) {
                primes[j] = false;
            }
        }
        if(primes[i+2]) {
            for(j=(i+2)*(i+2); j < n; j += (i+2)) {
                primes[j] = false;
            }
        }
    }
    count = 0;
    for(i=0; i < n; i++) {
        if(primes[i]) {
            count++;
        }
    }
    
    pylist = PyList_New(count);
    j = 0;
    for(i=0; i < n; i++) {
        if(primes[i]) {
            item = PyInt_FromLong(i);
            PyList_SetItem(pylist, j++, item);
        }
    }
    
    return pylist;
}


static PyMethodDef PrimesMethods[] = {
    {"isPrime",  primes_isPrime, METH_VARARGS,
     "Checks if the given number is prime."},
    {"primesList",  primes_primesList, METH_VARARGS,
     "Returns list of primes less than given number."},
    {NULL, NULL, 0, NULL}
};

DL_EXPORT(void) initprimes(void)
{
  Py_InitModule("primes", PrimesMethods);
}

