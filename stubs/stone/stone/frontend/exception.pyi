from _typeshed import Incomplete

class InvalidSpec(Exception):
    msg: Incomplete
    lineno: Incomplete
    path: Incomplete
    def __init__(self, msg, lineno, path: Incomplete | None = None) -> None: ...
