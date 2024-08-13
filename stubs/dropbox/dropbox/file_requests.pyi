from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class GeneralFileRequestsError(bb.Union):
    disabled_for_team: Incomplete
    other: Incomplete
    def is_disabled_for_team(self): ...
    def is_other(self): ...

GeneralFileRequestsError_validator: Incomplete

class CountFileRequestsError(GeneralFileRequestsError): ...

CountFileRequestsError_validator: Incomplete

class CountFileRequestsResult(bb.Struct):
    file_request_count: Incomplete
    def __init__(self, file_request_count: Incomplete | None = None) -> None: ...

CountFileRequestsResult_validator: Incomplete

class CreateFileRequestArgs(bb.Struct):
    title: Incomplete
    destination: Incomplete
    deadline: Incomplete
    open: Incomplete
    description: Incomplete
    def __init__(
        self,
        title: Incomplete | None = None,
        destination: Incomplete | None = None,
        deadline: Incomplete | None = None,
        open: Incomplete | None = None,
        description: Incomplete | None = None,
    ) -> None: ...

CreateFileRequestArgs_validator: Incomplete

class FileRequestError(GeneralFileRequestsError):
    not_found: Incomplete
    not_a_folder: Incomplete
    app_lacks_access: Incomplete
    no_permission: Incomplete
    email_unverified: Incomplete
    validation_error: Incomplete
    def is_not_found(self): ...
    def is_not_a_folder(self): ...
    def is_app_lacks_access(self): ...
    def is_no_permission(self): ...
    def is_email_unverified(self): ...
    def is_validation_error(self): ...

FileRequestError_validator: Incomplete

class CreateFileRequestError(FileRequestError):
    invalid_location: Incomplete
    rate_limit: Incomplete
    def is_invalid_location(self): ...
    def is_rate_limit(self): ...

CreateFileRequestError_validator: Incomplete

class DeleteAllClosedFileRequestsError(FileRequestError): ...

DeleteAllClosedFileRequestsError_validator: Incomplete

class DeleteAllClosedFileRequestsResult(bb.Struct):
    file_requests: Incomplete
    def __init__(self, file_requests: Incomplete | None = None) -> None: ...

DeleteAllClosedFileRequestsResult_validator: Incomplete

class DeleteFileRequestArgs(bb.Struct):
    ids: Incomplete
    def __init__(self, ids: Incomplete | None = None) -> None: ...

DeleteFileRequestArgs_validator: Incomplete

class DeleteFileRequestError(FileRequestError):
    file_request_open: Incomplete
    def is_file_request_open(self): ...

DeleteFileRequestError_validator: Incomplete

class DeleteFileRequestsResult(bb.Struct):
    file_requests: Incomplete
    def __init__(self, file_requests: Incomplete | None = None) -> None: ...

DeleteFileRequestsResult_validator: Incomplete

class FileRequest(bb.Struct):
    id: Incomplete
    url: Incomplete
    title: Incomplete
    destination: Incomplete
    created: Incomplete
    deadline: Incomplete
    is_open: Incomplete
    file_count: Incomplete
    description: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        url: Incomplete | None = None,
        title: Incomplete | None = None,
        created: Incomplete | None = None,
        is_open: Incomplete | None = None,
        file_count: Incomplete | None = None,
        destination: Incomplete | None = None,
        deadline: Incomplete | None = None,
        description: Incomplete | None = None,
    ) -> None: ...

FileRequest_validator: Incomplete

class FileRequestDeadline(bb.Struct):
    deadline: Incomplete
    allow_late_uploads: Incomplete
    def __init__(self, deadline: Incomplete | None = None, allow_late_uploads: Incomplete | None = None) -> None: ...

FileRequestDeadline_validator: Incomplete

class GetFileRequestArgs(bb.Struct):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...

GetFileRequestArgs_validator: Incomplete

class GetFileRequestError(FileRequestError): ...

GetFileRequestError_validator: Incomplete

class GracePeriod(bb.Union):
    one_day: Incomplete
    two_days: Incomplete
    seven_days: Incomplete
    thirty_days: Incomplete
    always: Incomplete
    other: Incomplete
    def is_one_day(self): ...
    def is_two_days(self): ...
    def is_seven_days(self): ...
    def is_thirty_days(self): ...
    def is_always(self): ...
    def is_other(self): ...

GracePeriod_validator: Incomplete

class ListFileRequestsArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

ListFileRequestsArg_validator: Incomplete

class ListFileRequestsContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFileRequestsContinueArg_validator: Incomplete

class ListFileRequestsContinueError(GeneralFileRequestsError):
    invalid_cursor: Incomplete
    def is_invalid_cursor(self): ...

ListFileRequestsContinueError_validator: Incomplete

class ListFileRequestsError(GeneralFileRequestsError): ...

ListFileRequestsError_validator: Incomplete

class ListFileRequestsResult(bb.Struct):
    file_requests: Incomplete
    def __init__(self, file_requests: Incomplete | None = None) -> None: ...

ListFileRequestsResult_validator: Incomplete

class ListFileRequestsV2Result(bb.Struct):
    file_requests: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, file_requests: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

ListFileRequestsV2Result_validator: Incomplete

class UpdateFileRequestArgs(bb.Struct):
    id: Incomplete
    title: Incomplete
    destination: Incomplete
    deadline: Incomplete
    open: Incomplete
    description: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        title: Incomplete | None = None,
        destination: Incomplete | None = None,
        deadline: Incomplete | None = None,
        open: Incomplete | None = None,
        description: Incomplete | None = None,
    ) -> None: ...

UpdateFileRequestArgs_validator: Incomplete

class UpdateFileRequestDeadline(bb.Union):
    no_update: Incomplete
    other: Incomplete
    @classmethod
    def update(cls, val): ...
    def is_no_update(self): ...
    def is_update(self): ...
    def is_other(self): ...
    def get_update(self): ...

UpdateFileRequestDeadline_validator: Incomplete

class UpdateFileRequestError(FileRequestError): ...

UpdateFileRequestError_validator: Incomplete
FileRequestId_validator: Incomplete
FileRequestValidationError_validator: Incomplete
count: Incomplete
create: Incomplete
delete: Incomplete
delete_all_closed: Incomplete
get: Incomplete
list_v2: Incomplete
list: Incomplete
list_continue: Incomplete
update: Incomplete
ROUTES: Incomplete
