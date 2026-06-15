"""Example module — replace with real domain code."""

from __future__ import annotations

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

    Examples
    --------
    >>> import numpy as np
    >>> from {{cookiecutter.package_name}}.core.example import identity
    >>> identity(np.array([1.0, 2.0]))
    array([1., 2.])
    """
    return x
