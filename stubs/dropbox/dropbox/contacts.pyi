from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class DeleteManualContactsArg(bb.Struct):
    email_addresses: Incomplete
    def __init__(self, email_addresses: Incomplete | None = None) -> None: ...

DeleteManualContactsArg_validator: Incomplete

class DeleteManualContactsError(bb.Union):
    other: Incomplete
    @classmethod
    def contacts_not_found(cls, val): ...
    def is_contacts_not_found(self): ...
    def is_other(self): ...
    def get_contacts_not_found(self): ...

DeleteManualContactsError_validator: Incomplete
delete_manual_contacts: Incomplete
delete_manual_contacts_batch: Incomplete
ROUTES: Incomplete
