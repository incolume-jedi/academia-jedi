"""module template elements."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from logging import debug
from pathlib import Path
from typing import Final

import flet as ft

BLUE: Final = '#0060B5'
IMAGES: Final[list[Path]] = [
    Path('images', 'drawable-port-xhdpi-screen.png'),
    Path('images', 'background.jpg'),
    Path('images', 'Brasao-01.png'),
]
ICONS: Final[list[Path]] = [
    Path('images', 'icons', 'drawable-hdpi-icon.png'),
    Path('images', 'icons', 'drawable-ldpi-icon.png'),
    Path('images', 'icons', 'drawable-mdpi-icon.png'),
    Path('images', 'icons', 'drawable-xhdpi-icon.png'),
    Path('images', 'icons', 'drawable-xxhdpi-icon.png'),
    Path('images', 'icons', 'drawable-xxxhdpi-icon.png'),
    Path('images', 'icons', 'icon-1024.png'),
    Path('images', 'icons', 'icon-nobg-1024.png'),
]


# capa
class Cover(ft.UserControl):
    """Capa."""

    def __init__(self):
        """Init it."""
        super().__init__()

    def build(self):
        """Build it."""
        return ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src=Path(
                            'images',
                            'drawable-port-xhdpi-screen.png',
                        ).as_posix(),
                        width=400,
                    ),
                ],
            ),
        )


# appbar
class Appbar(ft.UserControl):
    """Appbar class."""

    def __init__(self, title: str) -> None:
        """Init of class."""
        super().__init__()
        self.title = title

    def build(self):
        """Build Appbar."""
        return ft.AppBar(
            title=ft.Text(
                self.title,
                weight=ft.FontWeight.BOLD,
                color='white',
            ),
            bgcolor='#3b65ad',
            center_title=True,
            actions=[
                ft.IconButton(
                    ft.icons.MENU,
                    tooltip='Menu',
                    icon_color='white',
                ),
            ],
        )


# menubar


# Navibar
class MyNavbar(ft.UserControl):
    """Navbar."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)

    def build(self):
        """Build."""
        return ft.Container(
            ft.NavigationBar(
                bgcolor=ft.colors.PRIMARY,
                shadow_color=ft.colors.PINK_50,
                indicator_color=ft.colors.WHITE70,
                selected_index=1,
                destinations=[
                    ft.NavigationDestination(
                        icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                        tooltip='Resenha diária',
                        label='RESENHA',
                    ),
                    ft.NavigationDestination(
                        icon=ft.icons.SEARCH,
                        tooltip='Busca avançada',
                        label='BUSCA',
                    ),
                    ft.NavigationDestination(
                        icon=ft.icons.STAR_PURPLE500_OUTLINED,
                        tooltip='Atos Favoritos',
                        label='FAVORITOS',
                    ),
                    ft.NavigationDestination(
                        icon=ft.icons.HELP,
                        label='AJUDA',
                    ),
                ],
            ),
        )


# page


class Layout(ft.View):
    """Layout Class."""

    def __init__(self, *args, **kwargs):
        """Init class."""
        super().__init__(*args, **kwargs)
        self.container = ft.Container()

    def web_view(self):
        """Web view."""
        return ft.WebView(
            'https://flet.dev',
            expand=True,
            on_page_started=lambda _: debug('Page started'),
            on_page_ended=lambda _: debug('Page ended'),
            on_web_resource_error=lambda e: debug('Page error: %s', e.data),
        )

    def build(self):
        """Build class."""
        self.container.content = ft.Column(
            controls=[
                Cover(),
            ],
        )
        return self.container


class TemplatePage(ft.Page):
    """."""

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)
        self.page.window_always_on_top = kwargs.get('is_topped')
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.title = kwargs.get('title', 'Planalto Legis')
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.window_width = 450
        self.page.window_height = 750
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window_bgcolor = ft.colors.BLACK

        self.main_page()

    def main_page(self):
        """Build main page."""
        self.add(
            ft.Container(
                image_src='images/backgrond.jpg',
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Control(),
            ),
        )


# Run
def main(page: ft.Page) -> None:
    """Run this app."""
    page.add()


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=TemplatePage)
