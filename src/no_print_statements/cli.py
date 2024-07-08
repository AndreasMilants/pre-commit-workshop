import argparse
from typing import Sequence, Optional

from no_print_statements.run_checks import perform_check


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="no-print", description="Check for print statements in Python files."
    )
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames to process.",
    )

    args = parser.parse_args(argv)

    failures = perform_check(args.filenames)  # run check(s) on `args.filenames`
    return 1 if failures else 0  # must be 0 or 1 this time
