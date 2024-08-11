from _typeshed import Incomplete

from stone.backend import CodeBackend
from stone.ir import ApiNamespace

doc_sub_tag_re: Incomplete

class PythonTypesBackend(CodeBackend):
    cmdline_parser: Incomplete
    cur_namespace: ApiNamespace | None
    preserve_aliases: bool
    def generate(self, api) -> None: ...

def generate_validator_constructor(ns, data_type): ...
def generate_func_call(name, args: Incomplete | None = None, kwargs: Incomplete | None = None): ...
