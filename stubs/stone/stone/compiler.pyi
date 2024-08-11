from _typeshed import Incomplete

class BackendException(Exception):
    backend_name: Incomplete
    traceback: Incomplete
    def __init__(self, backend_name, tb) -> None: ...

class Compiler:
    backend_extension: str
    api: Incomplete
    backend_module: Incomplete
    backend_args: Incomplete
    build_path: Incomplete
    def __init__(self, api, backend_module, backend_args, build_path, clean_build: bool = False) -> None: ...
    def build(self) -> None: ...
    @classmethod
    def is_stone_backend(cls, path): ...
