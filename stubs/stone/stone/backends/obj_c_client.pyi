import typing
from _typeshed import Incomplete

from stone.backends.obj_c import ObjCBaseBackend

argparse: typing.Any

class ObjCBackend(ObjCBaseBackend):
    cmdline_parser: Incomplete
    obj_name_to_namespace: dict[str, int]
    namespace_to_has_routes: dict[typing.Any, bool]
    def generate(self, api) -> None: ...
