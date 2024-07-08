import logging
from typing import Sequence

logger = logging.getLogger(__name__)


def perform_check(filenames: Sequence[str]) -> bool:
    errors = False
    for filename in filenames:
        if filename.endswith(".py"):
            with open(filename, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if "print(" in line and "ignore-print" not in line:
                        logging.warning(
                            "Print statement found in line %s of file %s. "
                            "Try using a logger instead, "
                            "or ignore this warning by including `ignore-print` on this line.",
                            i + 1,
                            filename,
                        )
                        errors = True
    return errors
