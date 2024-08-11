import typing
from _typeshed import Incomplete

from stone.backend import CodeBackend

argparse: typing.Any
base: str
doc_sub_tag_re: Incomplete
DOCSTRING_CLOSE_RESPONSE: str

class PythonClientBackend(CodeBackend):
    cmdline_parser: Incomplete
    supported_auth_types: Incomplete
    def generate(self, api) -> None: ...
