from __future__ import annotations

from enum import IntEnum, StrEnum


class AdminAccountStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"


class AdminStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    LIMITED = "limited"


class PermissionScope(IntEnum):
    NONE = 0
    OWN = 1
    ALL = 2


__all__ = ("AdminAccountStatus", "AdminStatus", "PermissionScope")
