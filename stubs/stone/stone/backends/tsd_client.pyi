import typing
from _typeshed import Incomplete

from stone.backend import CodeBackend

argparse: typing.Any

class TSDClientBackend(CodeBackend):
    cmdline_parser: Incomplete
    preserve_aliases: bool
    def generate(self, api) -> None: ...
