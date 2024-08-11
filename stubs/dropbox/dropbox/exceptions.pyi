from _typeshed import Incomplete

class DropboxException(Exception):
    request_id: Incomplete
    def __init__(self, request_id, *args, **kwargs) -> None: ...

class ApiError(DropboxException):
    error: Incomplete
    user_message_text: Incomplete
    user_message_locale: Incomplete
    def __init__(self, request_id, error, user_message_text, user_message_locale) -> None: ...

class HttpError(DropboxException):
    status_code: Incomplete
    body: Incomplete
    def __init__(self, request_id, status_code, body) -> None: ...

class PathRootError(HttpError):
    error: Incomplete
    def __init__(self, request_id, error: Incomplete | None = None) -> None: ...

class BadInputError(HttpError):
    message: Incomplete
    def __init__(self, request_id, message) -> None: ...

class AuthError(HttpError):
    error: Incomplete
    def __init__(self, request_id, error) -> None: ...

class RateLimitError(HttpError):
    error: Incomplete
    backoff: Incomplete
    def __init__(self, request_id, error: Incomplete | None = None, backoff: Incomplete | None = None) -> None: ...

class InternalServerError(HttpError): ...
