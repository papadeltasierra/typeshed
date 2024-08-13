from stone.ir import ApiNamespace, DataType

MYPY: bool
OverrideDefaultTypesDict: str

def map_stone_type_to_python_type(ns: ApiNamespace, data_type: DataType, override_dict: object | None = None) -> str: ...
