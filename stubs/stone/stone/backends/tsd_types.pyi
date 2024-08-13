import typing
from _typeshed import Incomplete

from stone.backend import CodeBackend
from stone.ir import ApiNamespace

argparse: typing.Any

class TSDTypesBackend(CodeBackend):
    cmdline_parser: Incomplete
    preserve_aliases: bool
    cur_namespace: ApiNamespace | None
    split_by_namespace: bool
    def generate(self, api) -> None: ...
