from dataclasses import dataclass, field
from .base import BaseDataclass, SuccessResponse


@dataclass(frozen=True)
class Image(BaseDataclass):
    filename: str = field()
    path: str = field()
    url: str = field()


@dataclass(frozen=True)
class ImageResponse(SuccessResponse):
    result: Image = field()


@dataclass(frozen=True)
class ImageUploadRequest(BaseDataclass):
    file: str = field()
