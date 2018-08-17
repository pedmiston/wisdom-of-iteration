drop table if exists guesses;
create table guesses (
  id integer primary key autoincrement,
  question_id integer not null,
  guess text not null
);
