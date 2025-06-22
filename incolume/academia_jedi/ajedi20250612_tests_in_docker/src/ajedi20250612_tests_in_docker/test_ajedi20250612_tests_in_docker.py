"""Tests for module."""

from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


class TestCase:
    """TestCase class."""

    def test_0(self):
        """Unittest."""
        with DockerContainer('hello-world') as container:
            delay = wait_for_logs(container, 'Hello from Docker!')
