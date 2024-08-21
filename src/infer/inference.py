from abc import ABCMeta, abstractmethod


class Inference(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def infer(self, texts: str | list[str]) -> list[float | list[float]]:
        raise NotImplementedError
