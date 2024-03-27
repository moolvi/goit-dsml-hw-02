SELECT title, description FROM tasks WHERE user_id = 11
SELECT title, description FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'completed') WHERE id = 15
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('bneQr-7081977', 'Нове завдання', 1, 1)
SELECT * FROM tasks WHERE status_id <> (SELECT id FROM status WHERE name = 'completed')
DELETE FROM tasks WHERE id = 50
SELECT * FROM users WHERE email LIKE '%ol%'
UPDATE users SET fullname = 'Нове ім''я' WHERE id = 21
SELECT COUNT(*) FROM tasks GROUP BY status_id
SELECT * FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@equeri.cet'
SELECT * FROM tasks WHERE description IS NULL OR description = ''
SELECT * FROM users INNER JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress')
SELECT COUNT(*), users.fullname  FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname