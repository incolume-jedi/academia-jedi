"""Use Control."""

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
