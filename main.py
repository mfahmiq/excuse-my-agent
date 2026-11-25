#!/usr/bin/env python3
"""Entry for 'The Excuse My Agent Gave Me' (make.fun).

Writes the single-line excuse to /output/entry.txt.
"""

import os

ENTRY = "Sorry — I hallucinated a calendar where your deadline was next month, and it looked more confident than the real one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
