from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class BaseDataclass:
    def as_dict(self):
        return asdict(self)
