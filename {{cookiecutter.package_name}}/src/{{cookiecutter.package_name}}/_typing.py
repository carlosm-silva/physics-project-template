"""Shared type aliases for {{cookiecutter.project_name}}.

Import exclusively under TYPE_CHECKING to avoid runtime cost.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    from numpy.typing import ArrayLike, NDArray

__all__: list[str] = []
