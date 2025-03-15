"""Submodule."""

import logging
import re

from icecream import ic


def convert_case(match_obj: re.Pattern) -> str | None:
    """Converter case."""
    """https://flexiple.com/python/python-regex-replace/."""
    if match_obj.group(1) is not None:
        return match_obj.group(1).lower()

    if match_obj.group(2) is not None:
        return match_obj.group(2).upper()
    return None


if __name__ == '__main__':
    s = 'jOE kIM mAx ABY lIzA'
    logging.info(ic(re.sub(r'([A-Z]+) | ([a-z]+)', convert_case, s)))
