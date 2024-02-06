from dataclasses import dataclass
from justcard.models import Card


@dataclass
class GameState:
    deck: list[Card]
    players: list[list[Card]]
