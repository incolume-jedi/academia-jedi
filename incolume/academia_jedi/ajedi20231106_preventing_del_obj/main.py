class Foo:
    """Class Foo."""
    def __init__(self, name: str = 'Foo') -> None:
        """Self init."""
        self.name = name


class Bar:
    """Class Bar."""
    __all_foos = []

    def __init__(self, name: str = 'Bar'):
        self.name = name
        self.__all_foos.append(self)
