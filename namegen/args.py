import sys
import argparse
from argparse import Namespace
from namegen.generators.generator_registry import GeneratorRegistry


def parse_args(argv) -> Namespace:
    parser = create_argument_parser()
    if len(argv) < 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args(argv)
    exit_on_bad_args(args)
    return args


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description="%(prog)s - application to help you generate names"
    )

    choices = list(GeneratorRegistry.registry)
    parser.add_argument(
        "-G",
        "--generator",
        help="generator to use",
        choices=choices,
        default=choices[0],
    )
    parser.add_argument(
        "-n",
        "--count",
        help="desired number of names to be generated (default: 10)",
        type=int,
        default=10,
    )
    parser.add_argument("keyword", help="keyword(s) to use", nargs="+")

    return parser


def exit_on_bad_args(args: Namespace):
    if args.count < 1:
        sys.exit("ERROR in --count: invalid value specified")
