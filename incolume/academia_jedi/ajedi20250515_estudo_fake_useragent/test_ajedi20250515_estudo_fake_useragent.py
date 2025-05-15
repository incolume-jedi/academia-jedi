"""Estudo com biblioteca fake_useragent."""

import pytest
import incolume.academia_jedi.ajedi20250515_estudo_fake_useragent as pkg


class TestCase:
    """Casos de testes para estudo com fake-useragent."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('Google', 'GSA'),
            pytest.param('Chrome', 'Chrome'),
            pytest.param('Firefox', 'Firefox'),
            pytest.param('Edge', 'Edg'),
            pytest.param('Opera', 'OPR'),
            pytest.param('Safari', 'Safari'),
            # pytest.param('Android', ''),
            pytest.param('Yandex Browser', 'YaBrowser'),
            pytest.param('Samsung Internet', ''),
            pytest.param('Opera Mobile', ''),
            pytest.param('Mobile Safari', ''),
            pytest.param('Firefox Mobile', ''),
            pytest.param('Firefox iOS', ''),
            pytest.param('Chrome Mobile', ''),
            pytest.param('Chrome Mobile iOS', ''),
            pytest.param('Mobile Safari UI/WKWebView', ''),
            pytest.param('Edge Mobile', ''),
            pytest.param('DuckDuckGo Mobile', ''),
            # pytest.param('MiuiBrowser', ''),
            # pytest.param('Whale', ''),
            pytest.param('Twitter', ''),
            pytest.param('Facebook', ''),
            pytest.param('Amazon Silk', ''),
        ],
    )
    def test_user_agent_browser(self, entrance, expected):
        """Unitest."""
        ua = pkg.UserAgent(browsers=[entrance])
        assert expected in ua.random

