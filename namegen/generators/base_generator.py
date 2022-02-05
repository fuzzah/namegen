from typing import List, Set, Iterable

from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    def __init__(self):
        self.keywords: List[str] = []

    def add_words(self, words: Iterable) -> None:
        """Add multiple words from Iterable `words`"""
        self.keywords.extend(words)

    def create_names(self, count: int, components: int) -> List[str]:
        """Generate `count` names, return them as list of strings"""

        names: Set[str] = set()
        max_tries = count * 10

        for _ in range(max_tries):
            names.add(self.create_one_name(components))
            if len(names) == count:
                break

        return sorted(names)

    @abstractmethod
    def create_one_name(self, components: int) -> str:
        """Generate one name consisting of at most `components` parts"""
