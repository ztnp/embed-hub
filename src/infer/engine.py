from infer.inference import Inference
from infer.st_inference import STInference


class Engine(Inference):

    def __init__(self, model_filepath):
        super().__init__()
        self.engine = STInference(model_filepath)

    def infer(self, texts: str | list[str]) -> list[float | list[float]]:
        return self.engine.infer(texts)
