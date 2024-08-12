from _typeshed import Incomplete
from typing_extensions import TypeAlias
import typing

from stone.ir import ApiNamespace, DataType

MYPY: bool
OverrideDefaultTypesDict: str
_OverrideDefaultTypesDict = typing.TypeVar("_OverrideDefaultTypesDict")

def map_stone_type_to_python_type(
    ns: ApiNamespace, data_type: DataType, override_dict: _OverrideDefaultTypesDict | None = None
) -> str: ...
