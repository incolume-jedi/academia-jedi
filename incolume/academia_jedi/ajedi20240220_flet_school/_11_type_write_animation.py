"""Type Write Animation."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import time
from logging import info

import flet as ft


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
