"""
Module: `print`-related helper functions

Public Functions:
    clear_print          : Clear line and print
    clear_print_clearable: Clear line and print clearable
    progress_str         : Generate progress string
    progress_percent     : Generate progress percentage
    shrink_str           : Shrink string to fit on console
"""

from __future__ import annotations

from shutil import get_terminal_size
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


def clear_print(
    value: str,
    *,
    sep: Optional[str] = None,
    end: Optional[str] = None,
    file: Optional[SupportsWrite[str]] = None,
    flush: bool = False,
) -> None:
    """
    Clear line and print
    """
    print(f"\r\x1b[K{value}", sep=sep, end=end, file=file, flush=flush)


def clear_print_clearable(
    value: str,
    *,
    sep: Optional[str] = None,
    file: Optional[SupportsWrite[str]] = None,
    flush: bool = False,
) -> None:
    """
    Clear line and print clearable
    """
    clear_print(value.translate(_CHAR_TRANS), sep=sep, end="", file=file, flush=flush)


def progress_full(current: int, total: int) -> str:
    """
    Full progress indicator:  80.000% [ 8/10]

    Args:
        current (int): ID of current element
        total   (int): Number of total elements

    Returns:
        {str}: Progress string:  80.000% [ 8/10]
    """
    return f"{progress_percent(current, total)} [{progress_str(current, total)}]"


def progress_str(current: int, total: int) -> str:
    """
    Generate progress string:  8/10

    Args:
        current (int): ID of current element
        total   (int): Number of total elements

    Returns:
        (str): Progress string:  8/10
    """
    count_str = str(total)
    return f"{current:>{len(count_str)}}/{count_str}"


def progress_percent(current: int, total: int) -> str:
    """
    Generate progress percentage:  80.000%

    Args:
        current (int): ID of current element
        total   (int): Number of total elements

    Returns:
        {str}: Progress percent string:  80.000%
    """
    return f"{current/total:8.3%}"


def shrink_str(shrink: str, *, prefix: str = "", postfix: str = "") -> str:
    """
    Shrink string to fit on console

    Args:
        shrink  (str): String to be shrinked
        prefix  (str): Stuff before the string that can't be shrinked
        postfix (str): Stuff after the string that can't be shrinked

    Returns:
        (str): Full string
    """
    max_len = get_terminal_size().columns - len(prefix) - len(postfix) - 4
    shrinked = ""
    counter = 0
    orig_str_iter = iter(shrink)
    while counter < max_len:
        try:
            char = next(orig_str_iter)
        except StopIteration:
            break
        counter += 1 if char.isascii() else 2
        shrinked += char
    if shrinked != shrink:
        shrink = shrinked[:-3] + "..."
    return f"{prefix} {shrink} {postfix}"


_CHAR_TRANS = str.maketrans(
    {
        "\n": " ",
        "\x84": "\\x84",
    }
)
