from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class AccountType(bb.Union):
    basic: Incomplete
    pro: Incomplete
    business: Incomplete
    def is_basic(self): ...
    def is_pro(self): ...
    def is_business(self): ...

AccountType_validator: Incomplete
AccountId_validator: Incomplete
ROUTES: Incomplete
