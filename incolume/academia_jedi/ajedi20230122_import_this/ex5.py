import codecs


def run():
    import this

    zen_of_python = codecs.encode(this.s, "rot13")
    return zen_of_python


if __name__ == "__main__":
    print(run())
