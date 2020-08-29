class InvalidGridSize(Exception):
    """Raised when a invalid grid size has been parsed."""
    pass

class InvalidMineCount(Exception):
    """Raised when a invalid number of mines has been parsed."""
    pass

class NoPresetGiven(Exception):
    """Raised when no preset has been parsed."""
    pass
