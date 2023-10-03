def run():
    import this

    s = ''.join([this.d.get(c, c) for c in this.s])
    return s


if __name__ == '__main__':
    print(run())
