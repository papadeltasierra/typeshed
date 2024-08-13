import typing
from _typeshed import Incomplete
from collections.abc import Generator

from stone.backends.swift import SwiftBaseBackend

argparse: typing.Any

class SwiftTypesBackend(SwiftBaseBackend):
    cmdline_parser: Incomplete
    def generate(self, api) -> None: ...
    def serializer_block(self, data_type) -> Generator[None, None, None]: ...
    def serializer_func(self, data_type) -> Generator[None, None, None]: ...
    def deserializer_func(self, data_type) -> Generator[None, None, None]: ...
