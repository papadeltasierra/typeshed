from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class PathRoot(bb.Union):
    home: Incomplete
    other: Incomplete
    @classmethod
    def root(cls, val): ...
    @classmethod
    def namespace_id(cls, val): ...
    def is_home(self): ...
    def is_root(self): ...
    def is_namespace_id(self): ...
    def is_other(self): ...
    def get_root(self): ...
    def get_namespace_id(self): ...

PathRoot_validator: Incomplete

class PathRootError(bb.Union):
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def invalid_root(cls, val): ...
    def is_invalid_root(self): ...
    def is_no_permission(self): ...
    def is_other(self): ...
    def get_invalid_root(self): ...

PathRootError_validator: Incomplete

class RootInfo(bb.Struct):
    root_namespace_id: Incomplete
    home_namespace_id: Incomplete
    def __init__(self, root_namespace_id: Incomplete | None = None, home_namespace_id: Incomplete | None = None) -> None: ...

RootInfo_validator: Incomplete

class TeamRootInfo(RootInfo):
    home_path: Incomplete
    def __init__(
        self,
        root_namespace_id: Incomplete | None = None,
        home_namespace_id: Incomplete | None = None,
        home_path: Incomplete | None = None,
    ) -> None: ...

TeamRootInfo_validator: Incomplete

class UserRootInfo(RootInfo):
    def __init__(self, root_namespace_id: Incomplete | None = None, home_namespace_id: Incomplete | None = None) -> None: ...

UserRootInfo_validator: Incomplete
Date_validator: Incomplete
DisplayName_validator: Incomplete
DisplayNameLegacy_validator: Incomplete
DropboxTimestamp_validator: Incomplete
EmailAddress_validator: Incomplete
LanguageCode_validator: Incomplete
NamePart_validator: Incomplete
NamespaceId_validator: Incomplete
OptionalNamePart_validator: Incomplete
SessionId_validator: Incomplete
SharedFolderId_validator = NamespaceId_validator
ROUTES: Incomplete
