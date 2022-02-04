import nltk
from nltk.corpus import wordnet

import random

from .generator_registry import GeneratorRegistry
from .base_generator import BaseGenerator


@GeneratorRegistry.register("nltk-synonym")
class NLTKSynonymGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        nltk.download("wordnet")
        nltk.download("omw-1.4")

    def create_one_name(self) -> str:
        n = min(2, len(self.keywords))
        words = random.sample(self.keywords, n)
        parts = []
        random.shuffle(words)
        for word in words:
            syn_sets = wordnet.synsets(word)
            if not syn_sets:
                continue
            syn_set = random.choice(syn_sets)
            max_tries = 10
            for _ in range(max_tries):
                part = random.choice(syn_set.lemmas()).name()
                if "_" not in part:
                    break
            if "_" in part:
                part = word
            parts.append(part)

        if not parts:
            return "_"

        return " ".join(parts)
