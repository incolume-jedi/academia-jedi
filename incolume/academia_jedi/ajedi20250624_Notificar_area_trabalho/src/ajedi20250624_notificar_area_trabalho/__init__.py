"""Module for the ajedi20250624-notificar-area-trabalho package."""

from __future__ import annotations

import time

from icecream import ic
from plyer import notification


def main() -> None:
    """Main function for the ajedi20250624-notificar-area-trabalho package."""
    ic('Hello from ajedi20250624-notificar-area-trabalho!')
    while True:
        notification.notify(
            title='Notificação de Área de Trabalho',
            message='Esta é uma notificação de teste.',
            app_name='ajedi20250624-notificar-area-trabalho',
            timeout=10,  # Tempo em segundos
            app_icon=None,  # Caminho para um ícone personalizado
        )
        time.sleep(10)  # Intervalo de 10 segundos entre notificações


if __name__ == '__main__':
    main()
