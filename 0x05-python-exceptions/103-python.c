#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

void print_python_list(PyObject *p)
{
    long int size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}
void print_python_bytes(PyObject *p)
{
    long int size, i;
    char *trying_str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    trying_str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", trying_str);
    printf("  first %ld bytes: ", size + 1 < 10 ? size + 1 : 10);

    for (i = 0; i < size + 1 && i < 10; i++)
        printf("%02hhx ", (unsigned char) *(trying_str + i));
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %f\n", value);
}
