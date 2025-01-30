"""Module fixture."""

import pytest


@pytest.fixture()
def fixture_name(request):
    """Fixture."""
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
    """Unitest."""
    assert fixture_name == 'baz'
