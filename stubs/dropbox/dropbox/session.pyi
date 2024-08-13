from _typeshed import Incomplete

from requests.adapters import HTTPAdapter

API_DOMAIN: Incomplete
WEB_DOMAIN: Incomplete
HOST_API: str
HOST_CONTENT: str
HOST_NOTIFY: str
HOST_WWW: str
API_HOST: Incomplete
API_CONTENT_HOST: Incomplete
API_NOTIFICATION_HOST: Incomplete
WEB_HOST: Incomplete
DEFAULT_TIMEOUT: int

class _SSLAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs) -> None: ...
    poolmanager: Incomplete
    def init_poolmanager(self, connections, maxsize, block: bool = False, **_) -> None: ...

def pinned_session(pool_maxsize: int = 8, ca_certs: Incomplete | None = None): ...

SSLError: Incomplete
