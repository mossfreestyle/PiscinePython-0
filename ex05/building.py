#!/usr/bin/env python3

import sys
import string


def count_cat(text: str) -> dict[str, int]:

    count = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }
    punctuation_set = set(string.punctuation)

    for ch in text:
        if ch.isupper():
            count["upper"] += 1
        elif ch.islower():
            count["lower"] += 1
        elif ch.isdigit():
            count["digits"] += 1
        elif ch.isspace():
            count["spaces"] += 1
        elif ch in punctuation_set:
            count["punctuation"] += 1
        else:
            pass

    return count


def prompt_text() -> str:

    print("What is the text to count?")
    line = sys.stdin.readline()
    if line == "":
        return ""
    return line


def text_argv(argv: list[str]) -> str | None:

    if len(argv) > 2:
        raise AssertionError("more than one argument provided")
    if len(argv) == 2:
        arg = argv[1]
        if arg.lower() == "none":
            return None
        return arg
    return None


def display_count(text: str) -> None:

    count = count_cat(text)
    total = len(text)

    print(f"The text contain {total} charactere:")
    print(f"{count['upper']} upper letters")
    print(f"{count['lower']} lower letters")
    print(f"{count['punctuation']} punctuation letters")
    print(f"{count['spaces']} spaces")
    print(f"{count['digits']} digits")


def main() -> None:

    try:
        text = text_argv(sys.argv)
        if text is None:
            text = prompt_text()
        display_count(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
