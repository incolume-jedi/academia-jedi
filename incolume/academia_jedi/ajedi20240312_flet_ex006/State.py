"""State."""


class GlobalState:
    """Global State."""

    def __init__(self):
        """Init."""
        self._state = {}

    def register_state(self, state):
        """Register State."""
        self._state[state.get_key()] = state

    def get_state_by_key(self, key: str) -> None:
        """Get State by Key."""
        return self._state.get(key)


global_state = GlobalState()


class State:
    """State."""

    def __init__(self, key: str, value: None):
        """Init."""
        self._global_state = global_state
        self._key = key
        self._value = value
        self.register_with_global()

    def register_with_global(self):
        """Register."""
        self._global_state.register_state(self)

    def get_key(self):
        """Get Key."""
        return self._key

    def get_state(self):
        """Get State."""
        return self._value
