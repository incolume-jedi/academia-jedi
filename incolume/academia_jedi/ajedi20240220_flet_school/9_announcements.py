"""In this section, we will build a simple announcement app."""

import flet as ft
from logging import info


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Make Announcements'

    # subscribe to broadcase announcements
    def on_announcement(message):
        announcements.controls.append(ft.Text(message))
        page.update()

    page.pubsub.subscribe(on_announcement)

    def send_click(e: ft.ControlEvent) -> None:
        page.pubsub.send_all(f'{user.value}: {announcement.value}')
        # cleaning up the form
        announcement.value = ''
        info('%s', e)
        page.update()

    announcements = ft.Column()
    user = ft.TextField(hint_text='author name...', width=150)
    announcement = ft.TextField(hint_text='announcement...', expand=True)
    send = ft.ElevatedButton('Send', on_click=send_click)
    page.add(
        announcements,
        ft.Row(
            controls=[
                user,
                announcement,
                send,
            ],
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.WEB_BROWSER)
