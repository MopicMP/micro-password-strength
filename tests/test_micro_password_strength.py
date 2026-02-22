"""Tests for micro-password-strength."""

import pytest
from micro_password_strength import strength


class TestStrength:
    """Test suite for strength."""

    def test_basic(self):
        """Test basic usage."""
        result = strength("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            strength("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = strength(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
