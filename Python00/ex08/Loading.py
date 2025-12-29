import sys
import os
from typing import Generator, Any


def ft_tqdm(lst: range) -> Generator[Any, None, None]:
    total = len(lst)
    try:
        bar_len = max(20, os.get_terminal_size().columns - 42)
    except (OSError, AttributeError):
        bar_len = 50

    for i, elem in enumerate(lst, 1):
        percent = int(100 * i / total)
        filled = int(bar_len * i / total)
        if filled > 0:
            bar = '=' * (filled - 1) + '>'
        else:
            bar = ' '
        bar = bar.ljust(bar_len, '=')
        sys.stdout.write(f"\r{percent:3d}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()
        yield elem
