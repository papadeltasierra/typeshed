from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class OpenIdError(bb.Union):
    incorrect_openid_scopes: Incomplete
    other: Incomplete
    def is_incorrect_openid_scopes(self): ...
    def is_other(self): ...

OpenIdError_validator: Incomplete

class UserInfoArgs(bb.Struct):
    def __init__(self) -> None: ...

UserInfoArgs_validator: Incomplete

class UserInfoError(bb.Union):
    other: Incomplete
    @classmethod
    def openid_error(cls, val): ...
    def is_openid_error(self): ...
    def is_other(self): ...
    def get_openid_error(self): ...

UserInfoError_validator: Incomplete

class UserInfoResult(bb.Struct):
    family_name: Incomplete
    given_name: Incomplete
    email: Incomplete
    email_verified: Incomplete
    iss: Incomplete
    sub: Incomplete
    def __init__(
        self,
        family_name: Incomplete | None = None,
        given_name: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        iss: Incomplete | None = None,
        sub: Incomplete | None = None,
    ) -> None: ...

UserInfoResult_validator: Incomplete
userinfo: Incomplete
ROUTES: Incomplete
