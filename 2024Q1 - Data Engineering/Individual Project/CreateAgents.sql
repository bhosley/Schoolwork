CREATE TABLE Agents (
    agentType VARCHAR(255),
    constraintID INT,
    currentEstimatorID INT,
    currentPolicyID INT,
    currentRating INT,
    ratingsDeviation FLOAT,
    gamesPlayed INT,
    wins INT,
    losses INT
);

INSERT INTO Agents (agentType, constraintID, currentEstimatorID, currentPolicyID, currentRating, ratingsDeviation, gamesPlayed, wins, losses)
VALUES
    ('Agent1', 1, 101, 201, 1500, 30.0, 50, 30, 20),
    ('Agent2', 2, 102, 202, 1600, 25.5, 45, 25, 20),
    ('Agent3', 3, 103, 203, 1400, 35.2, 60, 40, 20),
    ('Agent4', 4, 104, 204, 1700, 20.1, 55, 35, 20),
    ('Agent5', 5, 105, 205, 1550, 28.6, 65, 45, 20);