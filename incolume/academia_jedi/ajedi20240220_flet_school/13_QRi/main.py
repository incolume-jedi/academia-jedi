"""Main."""

import datetime
from logging import info

import cv2
import flet as ft
import qrcode
from clear_qrs import clear_qr_codes


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'QR Code Scanner and Generator'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 550
    page.window_width = 750
    page.theme_mode = 'light'
    page.scroll = 'always'
    page.bgcolor = '#ffffff'
    page.window_bgcolor = '#522125'

    qr_to_show = ft.Image(width=200)

    dlg = ft.AlertDialog(
        title=ft.Text('Scan QR Code', text_align='center'),
        content=qr_to_show,
    )

    def open_dlg(e: ft.ControlEvent) -> None:
        page.dialog = dlg
        dlg.open = True
        info('%s', e)
        info('%s', e)
        page.update()

    def generate_qrcode(e: ft.ControlEvent) -> None:
        clear_qr_codes()
        img = qrcode.make(str(user_content.value))
        current_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        global timestamp
        timestamp = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
        img.save(f'assets/qr/qrCode_{timestamp}.jpg')
        qr_to_show.src = f'qr/qrCode_{timestamp}.jpg'
        open_dlg(e)
        info('%s', e)
        page.update()

    def scan_qrcode(e: ft.ControlEvent) -> None:
        global timestamp
        img = str(f'assets/qr/qrCode_{timestamp}.jpg')
        detector = cv2.QRCodeDetector()
        value, _, _ = detector.detectAndDecode(cv2.imread(img))
        show_qr_content.value = value
        info('%s', e)
        page.update()

    user_content = ft.TextField(
        hint_text='please put the content to encrypt',
        border_radius=40,
        border_color='#522125',
        color='#522125',
    )
    generate_button = ft.ElevatedButton(
        'Generate',
        on_click=generate_qrcode,
        bgcolor='#522125',
        color=ft.colors.WHITE,
    )

    show_qr_content = ft.Text(text_align='center')
    scan_button = ft.ElevatedButton(
        'Scan QR',
        on_click=scan_qrcode,
        bgcolor='#522125',
        color=ft.colors.WHITE,
    )

    page.add(
        ft.Row(
            [
                ft.Column(
                    [ft.Image(src='qrCodeCover.png', height=500)],
                    horizontal_alignment='center',
                    alignment='center',
                ),
                ft.Container(width=30),
                ft.Column(
                    [
                        ft.Image(src='logo/appLogo.png', width=150),
                        ft.Container(height=20),
                        user_content,
                        generate_button,
                        ft.Row([show_qr_content], alignment='center'),
                        scan_button,
                        ft.Container(height=20),
                        ft.Text(
                            value='Made by: Kumar Anurag',
                            color='#522125',
                            weight='bold',
                        ),
                    ],
                    horizontal_alignment='center',
                    alignment='center',
                ),
            ],
            vertical_alignment='center',
            alignment='center',
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, assets_dir='assets')
