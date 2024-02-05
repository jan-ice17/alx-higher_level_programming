#include <Python.h>

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
