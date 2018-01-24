INSERT TABLE IF NOT EXISTS Users (
    INTEGER id,
    VARCHAR name,
    VARCHAR email,
    TINYINT admin
);

INSERT TABLE IF NOT EXISTS Events (
    INTEGER id,
    DATE date_start,
    DATE date_end,
    VARCHAR name
);

INSERT TABLE IF NOT EXISTS Teams (
    INTEGER team_number,
    VARCHAR name
);

INSERT TABLE IF NOT EXISTS Seasons (
    INTEGER year,
    VARCHAR schema
);

INSERT TABLE IF NOT EXISTS Scorekeepers (

);

INSERT TABLE IF NOT EXISTS Enrollments (
    INTEGER team_number,
    INTEGER event_id,

    VARCHAR practice_data,
    VARCHAR match1_data,
    VARCHAR match2_data,
    VARCHAR match3_data,
    
    TINYINT practice_noshow,
    TINYINT match1_noshow,
    TINYINT match2_noshow,
    TINYINT match3_noshow
);