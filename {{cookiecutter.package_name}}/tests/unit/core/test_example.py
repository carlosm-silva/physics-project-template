"""Unit tests for core.example."""

from __future__ import annotations

import numpy as np

from {{cookiecutter.package_name}}.core.example import identity


def test_identity_returns_same_array() -> None:
    """Output is the same object as the input."""
    x = np.array([1.0, 2.0, 3.0])
    assert identity(x) is x


def test_identity_preserves_values(rng: np.random.Generator) -> None:
    """Values are unchanged for a random input."""
    x = rng.standard_normal(100)
    np.testing.assert_array_equal(identity(x), x)


def test_identity_preserves_shape() -> None:
    """Shape is unchanged for a 2-D input."""
    x = np.zeros((4, 5))
    assert identity(x).shape == (4, 5)
