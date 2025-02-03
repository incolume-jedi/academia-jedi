"""Use Control."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import threading
import time

import flet as ft

"""
Theory: User control provides life-cycle "hook" methods

1) did_mount() - called after the UserControl added to a page.
2) will_unmount() - called before the UserControl is removed from a page.

Theory: Daemon

1) In multitasking computer OS, a daemon is a computer program
    that runs as background process, rather than being under the
    direct control of an interactive user.
"""


class Countdown(ft.UserControl):
    """Countdown."""

    def __init__(self, seconds):
        """Init."""
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        """DId Mount."""
        self.running = True
        self.myThread = threading.Thread(
            target=self.update_timer,
            args=(),
            daemon=True,
        )
        self.myThread.start()

    def will_unmount(self):
        """Will Unmount."""
        self.running = False

    def update_timer(self):
        """Update timer."""
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = f'{mins:02d}:{secs:02d}'
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        """Build."""
        self.countdown = ft.Text()
        return self.countdown


def main(page: ft.Page) -> None:
    """Main."""
    page.add(Countdown(120), Countdown(60))


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
