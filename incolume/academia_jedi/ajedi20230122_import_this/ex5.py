import codecs


def run():
    import this

    return codecs.encode(this.s, 'rot13')


if __name__ == '__main__':
    print(run())
