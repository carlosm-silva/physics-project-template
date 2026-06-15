"""Example module — replace with real domain code."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


def identity(x: np.ndarray) -> np.ndarray:
    r"""Return the input array unchanged.

    A placeholder that confirms the package is importable
    and the quality gate is wired correctly.

    Parameters
    ----------
    x : np.ndarray
        Any array.

    Returns
    -------
    np.ndarray
        The same array, unmodified.
    """
    return x
