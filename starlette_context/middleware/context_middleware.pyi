from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request as Request
from starlette.responses import Response as Response
from starlette_context.plugins import Plugin
from typing import Any, Optional, Sequence

class ContextMiddleware(BaseHTTPMiddleware):
    plugins: Optional[Sequence[Plugin]]
    def __init__(
        self,
        plugins: Optional[Sequence[Plugin]] = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    async def set_context(self, request: Request) -> dict: ...
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response: ...
