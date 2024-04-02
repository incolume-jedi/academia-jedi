"""Type Write Animation."""

import flet as ft
import time
from logging import info


class TypeWriterControl(ft.UserControl):
    """Writer Control."""

    def __init__(self, text_to_print):
        """Init."""
        super().__init__()
        self.text_to_print = text_to_print

    def effect(self, e):
        """Effect."""
        info('Event: %s', e)
        for i in range(len(self.text_to_print)):
            self.my_type_writter_text.value += self.text_to_print[i] + '_'
            self.my_type_writter_text.update()
            self.my_type_writter_text.value = self.my_type_writter_text.value[
                :-1
            ]
            time.sleep(0.02)

    def build(self):
        """Build."""
        self.my_type_writter_text = ft.Text(
            'My Typewriter Effect Will Happen Here!\n',
            no_wrap=False,
        )
        return ft.Column([
            self.my_type_writter_text,
            ft.ElevatedButton('start effect', on_click=self.effect),
        ])


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'TypeWriter Effect'
    page.window_width = 400
    page.window_height = 500
    page.bgcolor = '#333333'
    page.theme_mode = 'dark'
    page.window_center()
    page.scroll = 'always'
    page.update()

    some_text_to_type = """
    ChatGPT (Chat Generative Pre-trained Transformer)
     is a chatbot launched by OpenAI in November 2022.
    It is built on top of OpenAI's GPT-3 family of large
     language models, and is fine-tuned
     (an approach to transfer learning) with both
     supervised and reinforcement learning techniques.
    ChatGPT was launched as a prototype on November 30, 2022,
     and quickly garnered attention for
     its detailed responses and articulate answers across
     many domains of knowledge. Its uneven
     factual accuracy was identified as a significant drawback.
     Following the release of ChatGPT, OpenAI was valued at $29 billion.
    """

    page.add(TypeWriterControl(some_text_to_type))


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, assets_dir='assets')
