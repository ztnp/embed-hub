from sentence_transformers import SentenceTransformer

from infer.inference import Inference


class STInference(Inference):

    def __init__(self, model_filepath):
        super().__init__()
        self.model = SentenceTransformer(model_filepath)

    def infer(self, texts: str | list[str]) -> list[float | list[float]]:
        return self.model.encode(texts).tolist()
