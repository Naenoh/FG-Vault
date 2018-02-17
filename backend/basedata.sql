INSERT INTO games (name) VALUES
  ('Guilty Gear Xrd: Rev2'),
  ('Tekken 7'),
  ('Dragonball FighterZ'),
  ('Blazblue: Central Fiction');

INSERT INTO chars (name, game_id) VALUES
    ('Answer',1),
    ('Axl',1),
    ('Baiken',1),
    ('Bedman',1),
    ('Chipp',1),
    ('Dizzy',1),
    ('Elphelt',1),
    ('Faust',1),
    ('I-No',1),
    ('Jack-O',1),
    ('Jam',1),
    ('Johnny',1),
    ('Kum',1),
    ('Ky',1),
    ('Leo',1),
    ('May',1),
    ('Millia',1),
    ('Potemkin',1),
    ('Ramlethal',1),
    ('Raven',1),
    ('Sin',1),
    ('Slayer',1),
    ('Sol',1),
    ('Venom',1),
    ('Zato-1',1);

INSERT INTO chars (name, game_id) VALUES
    ('Akuma',2),
    ('Alisa',2),
    ('Asuka',2),
    ('Bob',2),
    ('Claudio',2),
    ('Devil Jin',2),
    ('Dragunov',2),
    ('Eddy ',2),
    ('Eliza',2),
    ('Feng',2),
    ('Geese',2),
    ('Gigas',2),
    ('Heihachi',2),
    ('Hwoarang',2),
    ('Jack-7',2),
    ('Jin',2),
    ('Josie ',2),
    ('Katarina',2),
    ('King',2),
    ('Kazuya',2),
    ('Kazumi',2),
    ('Kuma',2),
    ('Lars',2),
    ('Lee',2),
    ('Lili ',2),
    ('Leo',2),
    ('Lucky Chloe',2),
    ('Law',2),
    ('Master Raven',2),
    ('Miguel',2),
    ('Nina',2),
    ('Paul',2),
    ('Panda ',2),
    ('Shaheen',2),
    ('Steve',2),
    ('Xiaoyu',2),
    ('Yoshimitsu ',2);

INSERT INTO chars (name, game_id) VALUES
    ('Android 16',3),
    ('Android 18',3),
    ('Android 21',3),
    ('Beerus',3),
    ('Captain Ginyu',3),
    ('Cell',3),
    ('Frieza',3),
    ('Gohan (Adult)',3),
    ('Gohan (Teen)',3),
    ('Goku (SSGSS)',3),
    ('Goku (Super Saiyan)',3),
    ('Goku Black',3),
    ('Gotenks',3),
    ('Hit',3),
    ('Piccolo',3),
    ('Kid Buu',3),
    ('Krillin',3),
    ('Majin Buu',3),
    ('Nappa',3),
    ('Tien',3),
    ('Trunks',3),
    ('Vegeta (SSGSS)',3),
    ('Vegeta (Super Saiyan)',3),
    ('Yamcha',3);

INSERT INTO chars (name, game_id) VALUES
    ('Amane',4),
    ('Arakune',4),
    ('Azrael',4),
    ('Bang',4),
    ('Bullet',4),
    ('Carl',4),
    ('Celica',4),
    ('Es',4),
    ('Hakumen',4),
    ('Hazama',4),
    ('Hibiki',4),
    ('Tager',4),
    ('Izanami',4),
    ('Izayoi',4),
    ('Jin',4),
    ('Jubei',4),
    ('Kagura',4),
    ('Kokonoe',4),
    ('Litchi',4),
    ('Mai',4),
    ('Makoto',4),
    ('Naoto',4),
    ('Nine',4),
    ('Noel',4),
    ('Platinum',4),
    ('Rachel',4),
    ('Ragna',4),
    ('Relius',4),
    ('Susanoo',4),
    ('Taokaka',4),
    ('Tsubaki',4),
    ('Valkenhayn',4),
    ('Yuuki',4),
    ('Λ-11',4),
    ('μ-12',4),
    ('ν-13',4);

INSERT INTO categories (name) VALUES
  ('Combo'),
  ('Okizeme'),
  ('Guide'),
  ('MU'),
  ('General'),
  ('Misc.');

INSERT INTO posts (title, game_id, char_id) VALUES
  ('Sol BNBs', 1, 23),
  ('Sol Framedata', 1, 23),
  ('Feng BNBs', 2, 35),
  ('Tsubaki BNBs', 4, 117);

INSERT INTO cats (post_id, category_id) VALUES
  (1,1),
  (2,6),
  (3,1),
  (4,1);

INSERT INTO links (url, post_id) VALUES
  ('http://www.dustloop.com/wiki/index.php/GGXRD/Sol_Badguy/Combos', 1),
  ('http://www.dustloop.com/wiki/index.php/GGXRD-R2/Sol_Badguy/Combos', 1),
  ('http://www.dustloop.com/wiki/index.php?title=GGXRD-R2/Sol_Badguy/Frame_Data', 2),
  ('http://alphabla.de/ggxrd/index.php?id=14',2),
  ('http://forums.tekkengamer.com/viewtopic.php?f=4&t=146',3),
  ('http://www.evernote.com/l/AZZj8QupdRNLWZayTqsNqTuLGfkyO1LWzA4/',4)