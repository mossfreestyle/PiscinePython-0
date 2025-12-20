#!/usr/bin/env python3

import sys
from ft_filter import ft_filter


def long_word(word: str, nb: int) -> bool:
    return len(word) > nb


def words_by_len(text: str, nb: int) -> bool:
    words = text.split()
    return ft_filter(lambda w: long_word(w, nb), words)


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        
        text = sys.argv[1]
        try:
            nb = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        
        result = words_by_len(text, nb)
        print(result)
    
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()