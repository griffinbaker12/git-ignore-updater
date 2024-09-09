#!/usr/bin/env python3

import argparse
import os

GIT_IGNORE_PATH = ".gitignore"


def main():
    lines_to_add = [
        # python specific
        "__pycache__/",
        # env vars and secrets
        ".env",
        # virtual environments
        "venv/",
    ]

    if not os.path.exists(GIT_IGNORE_PATH):
        open(GIT_IGNORE_PATH, "a").close()

    with open(GIT_IGNORE_PATH, "r") as file:
        existing_content = set(file.read())

    with open(GIT_IGNORE_PATH, "a") as file:
        for line in lines_to_add:
            if line not in existing_content:
                file.write(f"{line}\n")

    print(f"✅ Updated {GIT_IGNORE_PATH}")


def get_patterns():
    pattern_dir = os.path.join(os.path.dirname(__file__), "patterns")
    print(pattern_dir)


if __name__ == "__main__":
    main()
