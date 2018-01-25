IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Users')
CREATE TABLE Privileges (
    id INTEGER IDENTITY(1, 1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Users')
CREATE TABLE  Users (
    id INTEGER IDENTITY(1, 1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL U   NIQUE,
    admin TINYINT NOT NULL
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Events')
CREATE TABLE  Events (
    id INTEGER IDENTITY(1, 1) PRIMARY KEY,
    year INTEGER NOT NULL,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,

    name VARCHAR(255) NOT NULL UNIQUE,
    FOREIGN KEY (year) REFERENCES Seasons(year)
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Teams')
CREATE TABLE  Teams (
    team_number INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Seasons')
CREATE TABLE  Seasons (
    year INTEGER PRIMARY KEY,
    json_schema VARCHAR(MAX) NOT NULL
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Scorekeepers')
CREATE TABLE  Scorekeepers (
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    level_id TINYINT NOT NULL,

    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (event_id) REFERENCES Events(id),
    PRIMARY KEY (user_id, event_id)
);

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Enrollments')
CREATE TABLE  Enrollments (
    team_number INTEGER NOT NULL,
    event_id INTEGER NOT NULL,

    practice_data VARCHAR(MAX),
    match1_data VARCHAR(MAX),
    match2_data VARCHAR(MAX),
    match3_data VARCHAR(MAX),
    
    practice_noshow TINYINT,
    match1_noshow TINYINT,
    match2_noshow TINYINT,
    match3_noshow TINYINT,

    FOREIGN KEY (team_number) REFERENCES Teams(team_number),
    FOREIGN KEY (event_id) REFERENCES Events(id),
    PRIMARY KEY (team_number, event_id)
);

IF NOT EXISTS (SELECT * FROM Privileges WHERE name = 'admin')
    INSERT INTO Privileges (name) VALUES ('admin')

IF NOT EXISTS (SELECT * FROM Privileges WHERE name = 'editor')
    INSERT INTO Privileges (name) VALUES ('editor')