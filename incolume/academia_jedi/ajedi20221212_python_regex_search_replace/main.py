import re


def convert_case(match_obj):
    """https://flexiple.com/python/python-regex-replace/."""
    if match_obj.group(1) is not None:
        return match_obj.group(1).lower()

    if match_obj.group(2) is not None:
        return match_obj.group(2).upper()
    return None


if __name__ == '__main__':
    str = 'jOE kIM mAx ABY lIzA'
    print(re.sub(r'([A-Z]+) | ([a-z]+)', convert_case, str))
