import dataclasses
from dataclasses import field 
import datetime

def positive_int_validator(value):
    if value <= 0:
        raise ValueError("Value must be a positive integer")

@dataclasses.dataclass
class Agent:
    agentType: str
    constraintID: int
    currentEstimatorID: int
    currentPolicyID: int
    gamesPlayed: int
    wins: int
    losses: int
    eloRating: int
    glickoRating: int
    ratingsDeviation: float

    def __post_init__(self):
        if self.constraintID <= 0:
            raise ValueError("constraintID must be a positive integer")
        if self.gamesPlayed <= 0:
            raise ValueError("gamesPlayed must be a positive integer")

@dataclasses.dataclass
class Game:
    event: str
    site: str
    white: int # Foreign Key?
    black: int # Foreign Key?
    result: bool # White winner
    UTCDate: datetime.date
    UTCTime: datetime.time
    #WhiteElo: "1639"
    #BlackElo: "1403"
    whiteRatingDiff: int
    blackRatingDiff: int
    ECO: str
    opening: str
    #TimeControl: "600+8" # Probably unnecessary; its unlikely that machines would take this long
    termination: str
    board: str

    def __post_init__(self):
        if not isinstance(self.black,int) or not isinstance(self.white,int):
            raise ValueError("Player labels should be foreign keys")
        
