from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class PlatformType(bb.Union):
    web: Incomplete
    desktop: Incomplete
    mobile_ios: Incomplete
    mobile_android: Incomplete
    api: Incomplete
    unknown: Incomplete
    mobile: Incomplete
    other: Incomplete
    def is_web(self): ...
    def is_desktop(self): ...
    def is_mobile_ios(self): ...
    def is_mobile_android(self): ...
    def is_api(self): ...
    def is_unknown(self): ...
    def is_mobile(self): ...
    def is_other(self): ...

PlatformType_validator: Incomplete
ROUTES: Incomplete
