CREATE TABLE IF NOT EXISTS tasks (
    ID SERIAL PRIMARY KEY, 
    title VARCHAR(100), 
    description TEXT, 
    status_id INTEGER, 
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) 
        ON DELETE CASCADE 
        ON UPDATE cascade
    )