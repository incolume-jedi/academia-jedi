"""Tests for module."""

# ruff: noqa: SLF001
from __future__ import annotations
from http import HTTPStatus
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.generic import ServerContainer
from testcontainers.core.image import DockerImage
from testcontainers.redis import RedisContainer

import httpx
import pytest


class TestCase:
    """TestCase class."""

    def test_0(self):
        """Unittest."""
        with DockerContainer('hello-world') as container:
            delay = wait_for_logs(container, 'Hello from Docker!')

            assert delay

    def test_generic(self):
        """Test generic."""
        with (
            DockerImage(
                path='./modules/generic/tests/samples/python_server',
                tag='test-srv:latest',
            ) as image,
            ServerContainer(port=9000, image=image) as srv,
        ):
            url = srv._create_connection_url()
            response = httpx.get(f'{url}', timeout=5)
            assert response.status_code == HTTPStatus.OK, (
                'Response status code is not 200'
            )
            delay = wait_for_logs(srv, 'GET / HTTP/1.1')

    def test_fastapi(self):
        """Test for container fastapi."""
        with (
            DockerImage(
                path='./modules/generic/tests/samples/fastapi',
                tag='fastapi-test:latest',
            ) as image,
            ServerContainer(port=80, image=image) as fastapi_server,
        ):
            delay = wait_for_logs(
                fastapi_server,
                'Uvicorn running on http://0.0.0.0:80',
            )
            fastapi_server.get_api_url = (
                lambda: fastapi_server._create_connection_url() + '/api/v1/'
            )
            client = fastapi_server.get_client()
            response = client.get('/')
            assert response.status_code == HTTPStatus.OK
            assert response.json() == {'Status': 'Working'}

    def test_redis(self):
        """Test for container redis."""
        with RedisContainer() as redis_container:
            redis_client = redis_container.get_client()

    @pytest.mark.skip(reason='Failing')
    def test_redis_access(self):
        """Test for contiainer redis."""
        with RedisContainer(image='redis:8-alpine3.21') as redis_:
            redis_container_port = redis_.port
            redis_container_ip_address = redis_.get_docker_client().bridge_ip(
                redis_._container.id,
            )

            with DockerImage(
                path='./modules/generic/tests/samples/advance_1',
                tag='advance-1:latest',
            ) as image:
                web_server = ServerContainer(port=80, image=image)
                web_server.with_env(
                    key='REDIS_HOST',
                    value=redis_container_ip_address,
                )
                web_server.with_env(
                    key='REDIS_PORT',
                    value=redis_container_port,
                )

                with web_server:
                    web_server.get_api_url = (
                        lambda: web_server._create_connection_url()
                    )
                    client = web_server.get_client()

                    response = client.get('/')
                    assert response.status_code == HTTPStatus.OK, (
                        'Server request failed'
                    )
                    assert response.json() == {'Status': 'ok'}

                    test_data = {'key': 'test_key', 'value': 'test_value'}
                    response = client.post('/set', params=test_data)
                    assert response.status_code == HTTPStatus.OK, (
                        'Failed to set data'
                    )

                    response = client.get(f'/get/{test_data["key"]}')
                    assert response.status_code == HTTPStatus.OK, (
                        'Failed to get data'
                    )
                    assert response.json() == {
                        'key': test_data['key'],
                        'value': test_data['value'],
                    }
