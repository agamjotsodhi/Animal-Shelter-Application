DROP DATABASE IF EXISTS  animalshelter;

CREATE DATABASE animalshelter;

\c animalshelter

CREATE TABLE listofpets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO listofpets
  (name, species, photo_url, age, notes, available)
VALUES
  ('max', 'dog', 'https://www.what-dog.net/Images/faces2/scroll001.jpg', 3, 'Incredibly adorable.', 't'),
  ('woof', 'bird', 'http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', 4, 'Somewhat spiky!', 't'),
  ('Silly', 'cat', 'https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', null, null, 't'),
  ('Dr. evil', 'cat', null, null, null, 't');
