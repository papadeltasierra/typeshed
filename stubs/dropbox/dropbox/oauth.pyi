from _typeshed import Incomplete

__all__ = [
    "BadRequestException",
    "BadStateException",
    "CsrfException",
    "DropboxOAuth2Flow",
    "DropboxOAuth2FlowNoRedirect",
    "NotApprovedException",
    "OAuth2FlowNoRedirectResult",
    "OAuth2FlowResult",
    "ProviderException",
]

class OAuth2FlowNoRedirectResult:
    access_token: Incomplete
    expires_at: Incomplete
    refresh_token: Incomplete
    account_id: Incomplete
    user_id: Incomplete
    scope: Incomplete
    def __init__(self, access_token, account_id, user_id, refresh_token, expiration, scope) -> None: ...

class OAuth2FlowResult(OAuth2FlowNoRedirectResult):
    url_state: Incomplete
    def __init__(self, access_token, account_id, user_id, url_state, refresh_token, expires_in, scope) -> None: ...
    @classmethod
    def from_no_redirect_result(cls, result, url_state): ...

class DropboxOAuth2FlowBase:
    consumer_key: Incomplete
    consumer_secret: Incomplete
    locale: Incomplete
    token_access_type: Incomplete
    requests_session: Incomplete
    scope: Incomplete
    include_granted_scopes: Incomplete
    code_verifier: Incomplete
    code_challenge: Incomplete
    def __init__(
        self,
        consumer_key,
        consumer_secret: Incomplete | None = None,
        locale: Incomplete | None = None,
        token_access_type: Incomplete | None = None,
        scope: Incomplete | None = None,
        include_granted_scopes: Incomplete | None = None,
        use_pkce: bool = False,
        timeout=100,
        ca_certs: Incomplete | None = None,
    ) -> None: ...
    def build_path(self, target, params: Incomplete | None = None): ...
    def build_url(self, target, params: Incomplete | None = None, host="api.dropboxapi.com"): ...

class DropboxOAuth2FlowNoRedirect(DropboxOAuth2FlowBase):
    def __init__(
        self,
        consumer_key,
        consumer_secret: Incomplete | None = None,
        locale: Incomplete | None = None,
        token_access_type: Incomplete | None = None,
        scope: Incomplete | None = None,
        include_granted_scopes: Incomplete | None = None,
        use_pkce: bool = False,
        timeout=100,
        ca_certs: Incomplete | None = None,
    ) -> None: ...
    def start(self): ...
    def finish(self, code): ...

class DropboxOAuth2Flow(DropboxOAuth2FlowBase):
    redirect_uri: Incomplete
    session: Incomplete
    csrf_token_session_key: Incomplete
    def __init__(
        self,
        consumer_key,
        redirect_uri,
        session,
        csrf_token_session_key,
        consumer_secret: Incomplete | None = None,
        locale: Incomplete | None = None,
        token_access_type: Incomplete | None = None,
        scope: Incomplete | None = None,
        include_granted_scopes: Incomplete | None = None,
        use_pkce: bool = False,
        timeout=100,
        ca_certs: Incomplete | None = None,
    ) -> None: ...
    def start(self, url_state: Incomplete | None = None): ...
    def finish(self, query_params): ...

class BadRequestException(Exception): ...
class BadStateException(Exception): ...
class CsrfException(Exception): ...
class NotApprovedException(Exception): ...
class ProviderException(Exception): ...
class BadInputException(Exception): ...
