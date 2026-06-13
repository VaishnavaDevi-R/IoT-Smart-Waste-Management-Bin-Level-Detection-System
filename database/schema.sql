CREATE TABLE IF NOT EXISTS bin_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    bin_id TEXT,
    distance REAL,
    fill_percentage REAL,
    temperature REAL,
    humidity REAL,
    gas_level REAL,
    status TEXT,
    alert TEXT
);