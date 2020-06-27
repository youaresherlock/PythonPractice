列表和元组的内部实现是怎样的?
列表:
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
}PyListObject;
ist 本质上是一个 over-allocate 的 array。其中，ob_item 是一个指针列表，
里面的每一个指针都指向列表的元素。而 allocated 则存储了这个列表已经被分配的空间大小。

元组:
typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
} PyTupleObject;
它和 list 相似，本质也是一个 array，但是空间大小固定。不同于一般 array，
Python 的 tuple 做了许多优化，来提升在程序中的效率。



















