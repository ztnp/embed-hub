from fastapi import FastAPI

from infer.engine import Engine
from server import config
from server.typings import EncodeRequest
from server.response import JsonResponse

app = FastAPI()

engine = Engine(config.model_filepath)


@app.post('/encode', response_class=JsonResponse)
async def encode(item: EncodeRequest) -> dict | None:
    embeddings = engine.infer(item.inputs)
    return {'embeddings': embeddings}
