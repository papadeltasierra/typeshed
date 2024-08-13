from _typeshed import Incomplete
from typing import Any

from stone.backends.obj_c import ObjCBaseBackend

argparse: Any

class ObjCTypesBackend(ObjCBaseBackend):
    cmdline_parser: Incomplete
    obj_name_to_namespace: dict[str, str]
    namespace_to_has_route_auth_list: dict[Any, set[str]]
    def generate(self, api): ...
