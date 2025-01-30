"""Validator module."""

import locale


class Validator:
    """Validator class."""

    def format_to_int(self, value: float | str) -> int | None:
        """Format."""
        try:
            return int(value)
        except ValueError:
            return None

    def format_to_float(self, value):
        """Format."""
        value = value.replace('.', '')
        value = value.replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return None

    def format_to_currency(self, value: float) -> str:
        """Format it."""
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
        return locale.currency(value, symbol=False, grouping=True)
