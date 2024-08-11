import typing
from _typeshed import Incomplete

re: typing.Any

def quote(s): ...
def parse_data_types_from_doc_ref(api, doc, namespace_context, ignore_missing_entries: bool = False): ...
def parse_route_name_and_version(route_repr): ...
def parse_data_types_and_routes_from_doc_ref(api, doc, namespace_context, ignore_missing_entries: bool = False): ...

doc_ref_re: Incomplete
doc_ref_val_re: Incomplete
BUILTIN_ANNOTATION_CLASS_BY_STRING: Incomplete

class Environment(dict[str, type]):
    namespace_name: str | None

class IRGenerator:
    data_types: Incomplete
    default_env: Incomplete
    api: Incomplete
    def __init__(self, partial_asts, version, debug: bool = False, route_whitelist_filter: Incomplete | None = None) -> None: ...
    def generate_IR(self): ...
