"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

import calendar
from datetime import datetime
from typing import NoReturn

import flet as ft
from config import settings

cal = calendar.Calendar()

# pre-defined calendar maps ...
date_class: dict[int, str] = {
    0: 'Mo',
    1: 'Tu',
    2: 'We',
    3: 'Th',
    4: 'Fr',
    5: 'Sa',
    6: 'Su',
}

month_class: dict[int, str] = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}


# Date class to handle calendar logic ...
class Settings:
    """In this class we'll use datetime module to handle dates."""

    timestamp = datetime.now(tz=settings.TZ)
    year: int = timestamp.year
    month: int = timestamp.month

    @staticmethod
    def get_year() -> int:
        """Static method to return the !year."""
        return Settings.year

    @staticmethod
    def get_month() -> int:
        """Static method to return the !month."""
        return Settings.month

    @staticmethod
    def get_date(delta: int) -> NoReturn:
        """Static method to calculate month changes (user event).

        the following logic handles changes in the month
         if user triggers back, we check the limit of 1 to see ifi t's been
         passed and handle it accordingly. Same goes ith next trigger...

        """
        if delta == 1:
            if Settings.month + delta > len(month_class):
                Settings.month = 1
                Settings.year += 1
            else:
                Settings.month += 1

        if delta == -1:
            if Settings.month + delta < 1:
                Settings.month = 12
                Settings.year -= 1
            else:
                Settings.month -= 1


# Custom Container class to display days ...
date_box_style = {
    'width': 30,
    'height': 30,
    'alignment': ft.alignment.center,
    'shape': ft.BoxShape('rectangle'),
    'animate': ft.Animation(400, 'ease'),
    'border_radius': 5,
}


class DateBox(ft.Container):
    """Class DateBox."""

    def __init__(  # noqa: PLR0913
        self,
        day: int,
        date: str = '',
        date_instnace: ft.Column = None,
        task_instance: ft.Column = None,
        opacity_: float = 0,
    ):
        """Init class."""
        super().__init__(
            **date_box_style,
            data=date,
            opacity=opacity_,
            # add a on_click trigger to select days
            on_click=self.selected,
        )

        self.day = day
        self.date_instance = date_instnace
        self.task_instance = task_instance

        self.content = ft.Text(self.day, text_align='center')

    def selected(self, e: ft.TapEvent) -> NoReturn:
        """Because each BoxDay has the !grid instance.

        we can loop over the rows and check to see which
        day is being clicked and update the UI...
        """
        if self.date_instance:  # to bypass any errors
            # [1:] becuase we skip over the weekday row
            for row in self.date_instance.controls[1:]:
                for date in row.controls:
                    date.bgcolor = '#20303e' if date == e.control else None
                    date.border = (
                        ft.border.all(0.5, '#4fadf9')
                        if date == e.control
                        else None
                    )
                    # we can add one more line of code to display
                    # the clicked date into the text field

                    if date == e.control:
                        # recall that we passed in a formatted date,
                        # under the method called !format_date
                        self.task_instance.date.value = e.control.data

            self.date_instance.update()
            self.task_instance.update()


class DateGrid(ft.Column):
    """Calendar class that sets up UI for year/month/day...

    data grid takes in !year and !month as well as the task manager instance
    """

    def __init__(self, year: int, month: int, task_instance: object):
        """Init class."""
        super().__init__()

        self.year = year
        self.month = month
        self.task_manager = task_instance

        self.date = ft.Text(f'{month_class[self.month]} {self.year}')

        self.year_and_month = ft.Container(
            bgcolor='#20303e',
            border_radius=ft.border_radius.only(top_left=10, top_right=10),
            content=ft.Row(
                alignment='center',
                controls=[
                    ft.IconButton(
                        'chevron_left',
                        on_click=lambda e: self.update_date_grid(e, -1),
                    ),
                    ft.Container(
                        width=150,
                        content=self.date,
                        alignment=ft.alignment.center,
                    ),
                    ft.IconButton(
                        'chevron_right',
                        on_click=lambda e: self.update_date_grid(e, 1),
                    ),
                ],
            ),
        )

        self.controls.insert(1, self.year_and_month)

        week_days = ft.Row(
            alignment='spaceEvenly',
            controls=[
                DateBox(day=date_class[index], opacity_=0.7)
                for index in range(7)
            ],
        )

        self.controls.insert(1, week_days)
        self.populate_date_grid(self.year, self.month)

    #
    def populate_date_grid(self, year: int, month: int) -> NoReturn:
        """This method adds the days of each week accordingly...

        delete all controls after the list of days of the week row
        """
        del self.controls[2:]

        for week in cal.monthdayscalendar(year, month):
            row = ft.Row(alignment='spaceEvenly')
            for day in week:
                if day != 0:
                    row.controls.append(
                        DateBox(
                            day,
                            self.format_date(day),
                            self,
                            self.task_manager,
                        ),
                    )

                else:
                    row.controls.append(DateBox(' '))

            self.controls.append(row)

    #
    def update_date_grid(self, _: ft.TapEvent, delta: int) -> NoReturn:
        """We need a method to update the UI.

         when user triggers back or next for !month
        we need to pass delta (either 1 or -1) to settings
         and get current year and month changes...
        The logic is set up, we can trigger the method first ...
        """
        Settings.get_date(delta)  # make sure to pass in delta...

        self.update_year_and_month(
            Settings.get_year(),
            Settings.get_month(),
        )

        self.populate_date_grid(
            Settings.get_year(),
            Settings.get_month(),
        )

        self.update()

    #
    def update_year_and_month(self, year: int, month: int) -> NoReturn:
        """Another helper method to insert the changes post-event trigger."""
        self.year = year
        self.month = month
        self.date.value = f'{month_class[self.month]} {self.year}'

    def format_date(self, day: int) -> str:
        """A helper method to format and return the day..."""
        return f'{month_class[self.month]} {day}, {self.year}'


def input_style(height: int) -> dict[str, str | int]:
    """Some stylign for the inputs we will use ..."""
    return {
        'height': height,
        'focused_border_color': 'blue',
        'border_radius': 5,
        'cursor_height': 16,
        'cursor_color': 'white',
        'content_padding': 10,
        'border_width': 1.5,
        'text_size': 12,
    }


# Task manager class to handle tasks (if app is a to-do app)
class TaskManager(ft.Column):
    """Class TaskManager."""

    def __init__(self):
        """Init class."""
        super().__init__()

        self.date = ft.TextField(
            label='Date',
            read_only=True,
            value=' ',
            **input_style(38),
        )

        self.controls = [self.date]


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    # page settings ...
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#1f2128'

    task_manager = TaskManager()

    # first instance, we need to pass current month and year...
    grid = DateGrid(
        year=Settings.get_year(),
        month=Settings.get_month(),
        task_instance=task_manager,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    height=350,
                    border=ft.border.all(0.75, '#4fadf9'),
                    border_radius=10,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    content=grid,
                ),
                ft.Divider(color='transparent', height=20),
                task_manager,
            ],
        ),
    )

    page.update()


if __name__ == '__main__':  # pragma: no cover
    ft.app(main)
