from _typeshed import Incomplete

from dropbox.base import DropboxBase
from dropbox.base_team import DropboxTeamBase

__all__ = ["Dropbox", "DropboxTeam", "create_session"]

class RouteResult:
    obj_result: Incomplete
    http_resp: Incomplete
    def __init__(self, obj_result, http_resp: Incomplete | None = None) -> None: ...

class RouteErrorResult:
    request_id: Incomplete
    obj_result: Incomplete
    def __init__(self, request_id, obj_result) -> None: ...

def create_session(max_connections: int = 8, proxies: Incomplete | None = None, ca_certs: Incomplete | None = None): ...

class _DropboxTransport:
    def __init__(
        self,
        oauth2_access_token: Incomplete | None = None,
        max_retries_on_error: int = 4,
        max_retries_on_rate_limit: Incomplete | None = None,
        user_agent: Incomplete | None = None,
        session: Incomplete | None = None,
        headers: Incomplete | None = None,
        timeout=100,
        oauth2_refresh_token: Incomplete | None = None,
        oauth2_access_token_expiration: Incomplete | None = None,
        app_key: Incomplete | None = None,
        app_secret: Incomplete | None = None,
        scope: Incomplete | None = None,
        ca_certs: Incomplete | None = None,
    ) -> None: ...
    def clone(
        self,
        oauth2_access_token: Incomplete | None = None,
        max_retries_on_error: Incomplete | None = None,
        max_retries_on_rate_limit: Incomplete | None = None,
        user_agent: Incomplete | None = None,
        session: Incomplete | None = None,
        headers: Incomplete | None = None,
        timeout: Incomplete | None = None,
        oauth2_refresh_token: Incomplete | None = None,
        oauth2_access_token_expiration: Incomplete | None = None,
        app_key: Incomplete | None = None,
        app_secret: Incomplete | None = None,
        scope: Incomplete | None = None,
    ): ...
    # Ref: https://github.com/dropbox/dropbox-sdk-python/issues/511
    def request(self, route, namespace, request_arg, request_binary, timeout: Incomplete | None = None): ...
    def check_and_refresh_access_token(self) -> None: ...
    def refresh_access_token(self, host="api.dropboxapi.com", scope: Incomplete | None = None) -> None: ...
    def request_json_object(
        self, host, route_name, route_style, request_arg, auth_type, request_binary, timeout: Incomplete | None = None
    ): ...
    def request_json_string_with_retry(
        self, host, route_name, route_style, request_json_arg, auth_type, request_binary, timeout: Incomplete | None = None
    ): ...
    def request_json_string(
        self, host, func_name, route_style, request_json_arg, auth_type, request_binary, timeout: Incomplete | None = None
    ): ...
    def raise_dropbox_error_for_resp(self, res) -> None: ...
    def with_path_root(self, path_root): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

# Ref: https://github.com/dropbox/dropbox-sdk-python/issues/511
class Dropbox(_DropboxTransport, DropboxBase): ...  # type: ignore [misc]

# Ref: https://github.com/dropbox/dropbox-sdk-python/issues/511
class DropboxTeam(_DropboxTransport, DropboxTeamBase):  # type: ignore[misc]
    def as_admin(self, team_member_id): ...
    def as_user(self, team_member_id): ...

class BadInputException(Exception): ...
