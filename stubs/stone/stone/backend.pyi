import abc
import argparse
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable, Iterator, Sequence
from typing import Tuple, TypeVar  # noqa: Y022

import six
from stone.ir import Api

# TypeAlias is not available pre Python 3.10.
# ruff: noqa: UP006
_DelimTuple = Tuple[str, str]  # noqa: Y026
_K = TypeVar("_K")
_V = TypeVar("_V")

def remove_aliases_from_api(api): ...

class Backend(metaclass=abc.ABCMeta):
    tabs_for_indents: bool
    cmdline_parser: argparse.ArgumentParser | None
    preserve_aliases: bool
    logger: Incomplete
    target_folder_path: Incomplete
    output: Incomplete
    lineno: int
    cur_indent: int
    positional_placeholders: Incomplete
    named_placeholders: Incomplete
    args: Incomplete
    def __init__(self, target_folder_path: str, args: Sequence[str] | None) -> None: ...
    @abstractmethod
    def generate(self, api: Api) -> None: ...
    def output_to_relative_path(self, relative_path: str, mode: str = "wb") -> Iterator[None]: ...
    def output_buffer_to_string(self) -> str: ...
    def clear_output_buffer(self) -> None: ...
    def indent_step(self) -> int: ...
    def indent(self, dent: int | None = None) -> Iterator[None]: ...
    def make_indent(self) -> str: ...
    def capture_emitted_output(self, output_buffer: six.StringIO) -> Iterator[None]: ...
    def emit_raw(self, s: str) -> None: ...
    def emit(self, s: str = "") -> None: ...
    def emit_wrapped_text(
        self,
        s: str,
        prefix: str = "",
        initial_prefix: str = "",
        subsequent_prefix: str = "",
        width: int = 80,
        break_long_words: bool = False,
        break_on_hyphens: bool = False,
    ) -> None: ...
    def emit_placeholder(self, s: str = "") -> None: ...
    def add_positional_placeholder(self, s: str) -> None: ...
    def add_named_placeholder(self, name: str, s: str) -> None: ...
    @classmethod
    def process_doc(cls, doc: str, handler: Callable[[str, str], str]) -> str: ...

class CodeBackend(Backend, metaclass=abc.ABCMeta):
    def filter_out_none_valued_keys(self, d: dict[_K, _V]) -> dict[_K, _V]: ...
    def generate_multiline_list(
        self,
        items: list[str],
        before: str = "",
        after: str = "",
        delim: _DelimTuple = ("(", ")"),
        compact: bool = True,
        sep: str = ",",
        skip_last_sep: bool = False,
    ) -> None: ...
    def block(
        self, before: str = "", after: str = "", delim: _DelimTuple = ("{", "}"), dent: int | None = None, allman: bool = False
    ) -> Iterator[None]: ...
