oneday
======

A Python DI/component project.

Example
-------

>>> from import Component, Service
>>> class A:
            pass
>>> a = A()
>>> Component.add(a)
>>> Component.get(A) is a
True
>>> @Service.register
     class B:
        def __init__(self, a: A):
            self.a = a
>>> b = Service.create(B)
>>> b.a is a
True

Install
-------

.. code-block:: shell
pip install oneday

Author
------
Yixian Du (duyixian1234@qq.com)