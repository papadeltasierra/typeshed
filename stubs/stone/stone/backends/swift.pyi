import abc
from _typeshed import Incomplete
from collections.abc import Generator

from stone.backend import CodeBackend

stone_warning: str
base: Incomplete
undocumented: str

class SwiftBaseBackend(CodeBackend, metaclass=abc.ABCMeta):
    def function_block(self, func, args, return_type: Incomplete | None = None) -> Generator[None, None, None]: ...
    def class_block(self, thing, protocols: Incomplete | None = None) -> Generator[None, None, None]: ...

def fmt_serial_type(data_type): ...
def fmt_serial_obj(data_type): ...
