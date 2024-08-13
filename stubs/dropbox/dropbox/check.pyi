from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class EchoArg(bb.Struct):
    query: Incomplete
    def __init__(self, query: Incomplete | None = None) -> None: ...

EchoArg_validator: Incomplete

class EchoResult(bb.Struct):
    result: Incomplete
    def __init__(self, result: Incomplete | None = None) -> None: ...

EchoResult_validator: Incomplete
app: Incomplete
user: Incomplete
ROUTES: Incomplete
