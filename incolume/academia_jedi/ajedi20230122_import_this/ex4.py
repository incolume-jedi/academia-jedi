def run():
    import this

    return ''.join([this.d.get(c, c) for c in this.s])


if __name__ == '__main__':
    print(run())
