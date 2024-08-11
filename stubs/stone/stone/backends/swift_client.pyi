import typing
from _typeshed import Incomplete

from stone.backends.swift import SwiftBaseBackend

argparse: typing.Any

class SwiftBackend(SwiftBaseBackend):
    cmdline_parser: Incomplete
    def generate(self, api) -> None: ...
