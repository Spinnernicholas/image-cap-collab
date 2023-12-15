from abc import ABC, abstractmethod
from typing import Any

class BaseDatasetLoader(ABC):

    @abstractmethod
    def load_dataset(self, path: str) -> None:
        pass

    @abstractmethod
    def get_image(self, image_id: str) -> Any:
        pass
    