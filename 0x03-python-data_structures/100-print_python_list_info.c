#include <Python.h>

void print_python_list_info(PyObject *py_list)
{
    Py_ssize_t list_size = PyList_Size(py_list);
    Py_ssize_t index;

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)py_list)->allocated);

    for (index = 0; index < list_size; index++) {
        printf("Element %ld: %s\n", index, Py_TYPE(PyList_GetItem(py_list, index))->tp_name);
    }
}