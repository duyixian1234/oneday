import pytest
from oneday import Component
from oneday.exceptions import NotAddedError


@pytest.fixture
def A():
    class _A:
        pass

    yield _A


def test_component(A):
    a = A()
    Component.add(a)
    assert Component.get(A) is a

    with pytest.raises(NotAddedError) as error:
        Component.get(str)

    assert 'not added' in str(error)
