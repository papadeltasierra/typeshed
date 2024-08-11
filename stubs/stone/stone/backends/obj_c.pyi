import abc
from _typeshed import Incomplete
from collections.abc import Generator

from stone.backend import CodeBackend

stone_warning: str
base_file_comment: Incomplete
undocumented: str
comment_prefix: str

class ObjCBaseBackend(CodeBackend, metaclass=abc.ABCMeta):
    def block_m(self, class_name) -> Generator[None, None, None]: ...
    def block_h_from_data_type(self, data_type, protocol: Incomplete | None = None) -> Generator[None, None, None]: ...
    def block_h(
        self,
        class_name,
        protocol: Incomplete | None = None,
        extensions: Incomplete | None = None,
        protected: Incomplete | None = None,
    ) -> Generator[None, None, None]: ...
    def block_init(self) -> Generator[None, None, None]: ...
    def block_func(
        self, func, args: Incomplete | None = None, return_type: str = "void", class_func: bool = False
    ) -> Generator[None, None, None]: ...
