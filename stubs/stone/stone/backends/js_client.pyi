import typing
from _typeshed import Incomplete

from stone.backend import CodeBackend
from stone.ir import ApiNamespace

argparse: typing.Any

class JavascriptClientBackend(CodeBackend):
    cmdline_parser: Incomplete
    cur_namespace: ApiNamespace | None
    preserve_aliases: bool
    def generate(self, api) -> None: ...
