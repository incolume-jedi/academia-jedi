def run():
    # ruff: noqa: D100, D103
    import this

    s = this.s.decode('rot13')
    print(s)


if __name__ == '__main__':
    print(run())
