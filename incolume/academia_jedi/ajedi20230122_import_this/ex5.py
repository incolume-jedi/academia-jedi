import codecs

# ruff: noqa: D100, D103


def run():
    import this

    return codecs.encode(this.s, 'rot13')


if __name__ == '__main__':
    print(run())
