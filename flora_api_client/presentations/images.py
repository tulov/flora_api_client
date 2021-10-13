from dataclasses import dataclass, field
from typing import Optional
from marshmallow.validate import OneOf

from .base import BaseDataclass, SuccessResponse
from .enums import ImageTarget


@dataclass(frozen=True)
class Image(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    position: int = field(metadata={
        "strict": True,
    })
    path: str = field()
    url: str = field()
    obj_id: Optional[int] = field(metadata={
        "strict": True,
    })
    obj_type: Optional[str] = field(
        metadata={
            'validate': OneOf([r.value for r in ImageTarget]),
        }
    )

    def build_url(self, *, width: int, height: int):
        return f'/display?path={self.path}&w={width}&h={height}&op=resize'

    @property
    def mime_type(self):
        if self.path.endswith('.png'):
            return "image/png"
        if self.path.endswith('.jpeg'):
            return "image/jpeg"
        raise RuntimeError("Not supported file type")

    @property
    def extension(self):
        m = self.mime_type
        return m.split('/')[1]


@dataclass(frozen=True)
class ImageResponse(SuccessResponse):
    result: Image = field()


@dataclass(frozen=True)
class ImageUploadRequest(BaseDataclass):
    position: int = field(metadata={
        "strict": True,
    })
    file: str = field()
