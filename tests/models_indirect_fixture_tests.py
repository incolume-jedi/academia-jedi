import pytest


@pytest.fixture()
def fixture_name(request):
    return request.param


@pytest.mark.parametrize(
    'fixture_name',
    [
        'foo',
        'bar',
    ],
    indirect=True,
)
def test_indirect(fixture_name):
    assert fixture_name == 'baz'
