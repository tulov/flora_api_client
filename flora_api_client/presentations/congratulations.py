from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse


@dataclass
class Congratulation(BaseDataclass):
    text: str = field(metadata={"validate": Length(max=1500, min=1)})
    occasion_id: int = field(metadata={"strict": True})
    id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    enabled: bool = field(default=False)


@dataclass
class Occasion(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150, min=1)})
    id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    enabled: bool = field(default=False)
    congratulations: list[Congratulation] = field(default_factory=list)


@dataclass
class OccasionResponse(SuccessResponse):
    result: Occasion = field()


@dataclass
class OccasionsResponse(PagedResponse):
    result: list[Occasion] = field(default_factory=list, metadata={"required": True})


@dataclass
class CongratulationResponse(SuccessResponse):
    result: Congratulation = field()
