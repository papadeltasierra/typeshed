from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class LaunchResultBase(bb.Union):
    @classmethod
    def async_job_id(cls, val): ...
    def is_async_job_id(self): ...
    def get_async_job_id(self): ...

LaunchResultBase_validator: Incomplete

class LaunchEmptyResult(LaunchResultBase):
    complete: Incomplete
    def is_complete(self): ...

LaunchEmptyResult_validator: Incomplete

class PollArg(bb.Struct):
    async_job_id: Incomplete
    def __init__(self, async_job_id: Incomplete | None = None) -> None: ...

PollArg_validator: Incomplete

class PollResultBase(bb.Union):
    in_progress: Incomplete
    def is_in_progress(self): ...

PollResultBase_validator: Incomplete

class PollEmptyResult(PollResultBase):
    complete: Incomplete
    def is_complete(self): ...

PollEmptyResult_validator: Incomplete

class PollError(bb.Union):
    invalid_async_job_id: Incomplete
    internal_error: Incomplete
    other: Incomplete
    def is_invalid_async_job_id(self): ...
    def is_internal_error(self): ...
    def is_other(self): ...

PollError_validator: Incomplete
AsyncJobId_validator: Incomplete
ROUTES: Incomplete
