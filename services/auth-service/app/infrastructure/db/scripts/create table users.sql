CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(150) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  hashed_password TEXT NOT NULL
);

select * from users;