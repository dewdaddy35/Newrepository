
CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
    name,
    summary,
    description
) VALUES (
    "Wash Clothes",
    "Feed son",
    "Feed Fish"
),
(
    "walk 1 hour",
    "workout 3 hours",
    "Study More"
),
(
    "eat a salad a day",
    "eat less bread",
    "be more active"
);