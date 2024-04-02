"""Module."""

__author__ = '@britodfbr'  # pragma: no cover
import flet as ft


class Filtro(ft.Container):
    """Filtro class."""
    def __init__(self, on_click=None, *args, **kwargs):
        """Init from filtro."""
        super().__init__(*args, **kwargs)
        self.width = 100
        self.height = 100
        self.content = ft.Column(
            controls=[
                ft.ElevatedButton(text=btn, on_click=on_click, data=btn)
                for btn in ['Adicionar', 'Excluir']
            ],
        )


class Layout(ft.ResponsiveRow):
    """Layout class."""
    def __init__(self, *args, **kwargs):
        """Init from layout."""
        super().__init__(*args, **kwargs)
        self.expand = True
        self.controls = [Filtro(on_click=self.eventos)]

    def eventos(self, e):
        """Events controls."""
        if e.control.data == 'Adicionar':
            self.controls.append(ft.Text('ELEMENTO ADICIONADO'))
        elif len(self.controls) > 1:
            self.controls.pop()
        self.update()


class App:
    """Principal class for app."""
    def __init__(self, page: ft.Page):
        """Init app."""
        self.page = page
        self.layout = Layout()
        self.page.add(self.layout)


if __name__ == '__main__':
    ft.app(target=App)
