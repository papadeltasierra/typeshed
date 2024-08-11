from _typeshed import Incomplete
from typing_extensions import TypeAlias

from stone.ir import ApiNamespace, DataType

MYPY: bool
DataTypeCls: TypeAlias = type[DataType]
Callback: Incomplete
OverrideDefaultTypesDict: TypeAlias = dict[DataTypeCls, Callback]

def map_stone_type_to_python_type(
    ns: ApiNamespace, data_type: DataType, override_dict: OverrideDefaultTypesDict | None = None
) -> str: ...
