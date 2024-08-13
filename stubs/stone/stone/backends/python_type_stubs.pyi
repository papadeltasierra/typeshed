from _typeshed import Incomplete

from stone.backend import CodeBackend
from stone.ir import Api, ApiNamespace, DataType

class ImportTracker:
    cur_namespace_typing_imports: Incomplete
    cur_namespace_adhoc_imports: Incomplete
    def __init__(self) -> None: ...
    def clear(self) -> None: ...

class PythonTypeStubsBackend(CodeBackend):
    cmdline_parser: Incomplete
    cur_namespace: Incomplete
    preserve_aliases: bool
    import_tracker: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def generate(self, api: Api) -> None: ...
    def map_stone_type_to_pep484_type(self, ns: ApiNamespace, data_type: DataType) -> str: ...
