#!/usr/bin/env python3

import argparse
import glob
import os

GIT_IGNORE_PATH = ".gitignore"

from collections import namedtuple

Pattern = namedtuple("Pattern", ["pattern", "config"])


def parse_lines(f):
    return f.read().splitlines()


def get_patterns():
    pattern_dir = os.path.join(os.path.dirname(__file__), "patterns")
    pattern_files = glob.glob(os.path.join(pattern_dir, "*.txt"))
    return [os.path.splitext(os.path.basename(f))[0] for f in pattern_files]


def read_patterns(pattern):
    pattern_file = os.path.join(os.path.dirname(__file__), "patterns", f"{pattern}.txt")
    if not os.path.exists(pattern_file):
        print(f"❌ Warning: Pattern file for {pattern} not found.")
        return []

    with open(pattern_file, "r") as file:
        return parse_lines(file)


def update_gitignore(patterns):
    if not os.path.exists(GIT_IGNORE_PATH):
        open(GIT_IGNORE_PATH, "a").close()
        print("✅ Created .gitignore file.")

    with open(GIT_IGNORE_PATH, "r") as file:
        existing_content = {line for line in parse_lines(file)}

    with open(GIT_IGNORE_PATH, "a") as file:
        for pattern, config in patterns:
            header = (
                f"{'\n' if existing_content else ""}## {pattern.capitalize()} Config"
            )
            if header not in existing_content:
                file.write(header + "\n")
            for line in config:
                if line not in existing_content:
                    file.write(line + "\n")

    print("✅ Updated .gitignore with specified patterns.")


def main():
    available_patterns = get_patterns()

    parser = argparse.ArgumentParser(
        description="Update .gitignore with common patterns."
    )
    for pattern in available_patterns:
        parser.add_argument(
            f"--{pattern}",
            action="store_true",
            help=f"Add {pattern} patterns",
        )
    args = parser.parse_args()

    if not any(vars(args).values()):
        args.python = True

    patterns = [
        Pattern(pattern, read_patterns(pattern))
        for pattern in available_patterns
        if getattr(args, pattern)
    ]

    update_gitignore(patterns)


if __name__ == "__main__":
    main()
