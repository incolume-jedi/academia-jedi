class Foo:
    """Class Foo."""

    __all_foos = []

    def __init__(self, name: str = 'Foo') -> None:
        """Self init."""
        self.__all_foos.append(self)
        self.name = name


class Bar:
    """Class Bar."""

    def __init__(self, name: str = 'Bar'):
        self.name = name
