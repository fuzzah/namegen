from typing import Dict, Callable

from namegen.common.registry import Registry
from .base_generator import BaseGenerator


class GeneratorRegistry(Registry):
    registry: Dict[str, BaseGenerator] = {}
