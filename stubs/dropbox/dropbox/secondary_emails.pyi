from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class SecondaryEmail(bb.Struct):
    email: Incomplete
    is_verified: Incomplete
    def __init__(self, email: Incomplete | None = None, is_verified: Incomplete | None = None) -> None: ...

SecondaryEmail_validator: Incomplete
ROUTES: Incomplete
