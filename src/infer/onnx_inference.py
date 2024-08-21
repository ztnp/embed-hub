from infer.inference import Inference


class ONNXInference(Inference):

    def __init__(self, model_filepath: str):
        super().__init__()

    def infer(self, texts: str | list[str]) -> list[float | list[float]]:
        pass
