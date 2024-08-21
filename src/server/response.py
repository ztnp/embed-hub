import json
import typing

from starlette.background import BackgroundTask
from starlette.responses import Response


class JsonResponse(Response):
    media_type = "application/json"

    def __init__(
            self,
            content: typing.Any,
            status_code: int = 200,
            headers: typing.Mapping[str, str] | None = None,
            media_type: str | None = None,
            background: BackgroundTask | None = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: typing.Any) -> bytes:
        response = {
            'code': self.status_code,
            'message': 'ok',
            'data': None
        }

        if not isinstance(content, dict):
            response['data'] = content if content else None
            return json.dumps(
                response,
                ensure_ascii=False,
                allow_nan=False,
                indent=None,
                separators=(",", ":"),
            ).encode("utf-8")

        response['message'] = content.pop('message', 'ok')
        response['data'] = content if content else None

        return json.dumps(
            response,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")
