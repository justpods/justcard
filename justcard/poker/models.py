from dataclasses import dataclass
from justcard.models import Card
from strenum import StrEnum
from enum import Enum


@dataclass
class GameState:
    deck: list[Card]
    players: list[list[Card]]


class Action(StrEnum):
    FOLD = "fold"
    CALL = "call"
    RAISE = "raise"


class Stage(Enum):
    FLOP = 1
    TURN = 2
    RIVER = 3
