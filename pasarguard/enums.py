# enums.py
from enum import Enum, StrEnum


class ShadowsocksMethod(StrEnum):
    AES_128_GCM = "aes-128-gcm"
    AES_256_GCM = "aes-256-gcm"
    CHACHA20_IETF_POLY1305 = "chacha20-ietf-poly1305"
    XCHACHA20_POLY1305 = "xchacha20-poly1305"


class FlowOption(StrEnum):
    NONE = ""
    XTLS_RPRX_VISION = "xtls-rprx-vision"


class UserDataLimitResetStrategy(str, Enum):
    no_reset = "no_reset"
    day = "day"
    week = "week"
    month = "month"
    year = "year"
