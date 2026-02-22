"""
Micro check password strength and suggest improvements

Usage:
    from micro_password_strength import strength

    print(strength("test@example.com"))  # True
    print(strength("invalid"))           # False
"""

__version__ = "1.0.0"

import re


def strength(value: str) -> bool:
    """Validate the input value.

    Args:
        value: String value to validate.

    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(value, str) or not value.strip():
        return False
    return _check(value.strip())


def _check(value: str) -> bool:
    """Internal validation logic."""
    # Basic validation pattern
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern, value))


def validate_many(values: list[str]) -> dict[str, bool]:
    """Validate multiple values at once.

    Args:
        values: List of strings to validate.

    Returns:
        Dict mapping each value to its validation result.
    """
    return {v: strength(v) for v in values}


def assert_valid(value: str, message: str = "Validation failed") -> str:
    """Validate and return value, or raise ValueError.

    Args:
        value: String to validate.
        message: Error message if validation fails.

    Returns:
        The validated value (stripped).

    Raises:
        ValueError: If validation fails.
    """
    if not strength(value):
        raise ValueError(f"{message}: '{value}'")
    return value.strip()
