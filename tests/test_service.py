import pytest
from oneday import Service, Component
from oneday.exceptions import NotRegisteredError


@pytest.fixture
def A():
    class _A:
        pass

    yield _A


def test_service(A):
    a = A()
    Component.add(a)

    @Service.register
    class B:
        def __init__(self, a: A):
            self.a = a

    b = Service.create(B)

    assert b.a is a

    with pytest.raises(NotRegisteredError) as error:
        Service.create(str)

    assert 'not registered' in str(error)
