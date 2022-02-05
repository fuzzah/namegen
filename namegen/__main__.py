import sys

from namegen.args import parse_args
from namegen.generators.generator_registry import GeneratorRegistry


def main(argv=None):
    argv = argv or sys.argv[1:]
    args = parse_args(argv)

    generator = GeneratorRegistry.create(args.generator)
    generator.add_words(args.keyword)

    print("Keywords:", ", ".join(args.keyword), file=sys.stderr)
    print(f"Will generate up to {args.count} names\n", file=sys.stderr)
    names = generator.create_names(args.count)
    print("\n".join(names))

    return 0
