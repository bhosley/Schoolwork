
import pytest
import data_schema


def test_create_agent(func):
    # Create a sample agent
    agent = data_schema.Agent(
        agentType="Type1",
        constraintID=1,
        currentEstimatorID=101,
        currentPolicyID=201,
        gamesPlayed=50,
        wins=30,
        losses=20,
        eloRating=1500,
        glickoRating=1600,
        ratingsDeviation=30.0
    )
    func(agent)
    
    # Check if the agent is created successfully
    assert agent.agentType == "Type1"
    assert agent.constraintID == 1
    assert agent.currentEstimatorID == 101
    assert agent.currentPolicyID == 201
    assert agent.gamesPlayed == 50
    assert agent.wins == 30
    assert agent.losses == 20
    assert agent.eloRating == 1500
    assert agent.glickoRating == 1600
    assert agent.ratingsDeviation == 30.0


def test_create_agent_with_errors(func):
    # Attempt to create an agent with invalid attributes
    with pytest.raises(ValueError):
        agent = data_schema.Agent(
            agentType="Type1",
            constraintID=-1,  # Invalid constraint ID (negative value)
            currentEstimatorID=101,
            currentPolicyID=201,
            gamesPlayed=50,
            wins=30,
            losses=20,
            eloRating=1500,
            glickoRating=1600,
            ratingsDeviation=30.0
        )
        func(agent)
        
    with pytest.raises(ValueError):
        agent = data_schema.Agent(
            agentType="Type1",
            constraintID=1,
            currentEstimatorID=101,
            currentPolicyID=201,
            gamesPlayed=-5,  # Invalid gamesPlayed (negative value)
            wins=30,
            losses=20,
            eloRating=1500,
            glickoRating=1600,
            ratingsDeviation=30.0
        )
        func(agent)


def test_create_game(func):
    game = data_schema.Game(
        event="Chess Tournament",
        site="New York",
        white=1,
        black=4,
        result=True,
        UTCDate="2024.01.26",
        UTCTime="14:30:00",
        whiteRatingDiff=10,
        blackRatingDiff=-5,
        ECO="A40",
        opening="Queen's Pawn",
        termination="Time forfeit",
        board="1")
    func(game)


def test_create_game_with_errors(func):
    with pytest.raises(ValueError):
        game = data_schema.Game(
            event="Chess Tournament",
            site="New York",
            white="Magnus Carlsen", # Names should be IDs
            black="Fabiano Caruana", # Names should be IDs
            result=True,
            UTCDate="2024-01-26", # Incorrect date format
            UTCTime="14:30:00",
            whiteRatingDiff=10,
            blackRatingDiff=-5,
            ECO="A40",
            opening="Queen's Pawn",
            termination="Time forfeit",
            board="1")
        func(game)


def test_player_to_agent(func,conv,pgn):   
    with pytest.raises(AttributeError):
        func(pgn)
    game_c = conv(pgn)
    func(game_c)

def test_populate(func):
    func(10)
    