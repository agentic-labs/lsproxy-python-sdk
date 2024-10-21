# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .position_param import PositionParam

__all__ = ["FilePostionParam"]


class FilePostionParam(TypedDict, total=False):
    path: Required[str]

    position: Required[PositionParam]
