from typing import Callable, Dict

import logging

log = logging.getLogger(__name__)


class Registry:

    registry: Dict[str, Callable] = {}

    @classmethod
    def register(cls, name: str) -> Callable:
        def wrapper(wrapped: Callable) -> Callable:
            if name in cls.registry:
                log.warning("Overwriting '%s' in class registry", name)
            cls.registry[name] = wrapped
            return wrapped

        return wrapper

    @classmethod
    def create(cls, name: str) -> Callable:
        if name not in cls.registry:
            raise ValueError(f"class with name {name} is not registered")

        return cls.registry[name]()
