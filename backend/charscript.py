import sys

if len(sys.argv) != 3:
    print("Too few or too many arguments")
    print("Usage : python charscript.py inputfile outputfile")
else:
    with open(sys.argv[1], encoding="utf-8") as infile:
        with open(sys.argv[2], "w", encoding="utf-8") as outfile:
            outfile.write("BEGIN;")
            game = ""
            for line in infile:
                line = line.strip()
                if line.startswith("#"):
                    if(game != ""):
                        outfile.write(";\n\n")
                    game = line[1:]
                    outfile.write("INSERT INTO games (name) VALUES ('{}');\n".format(game))
                    outfile.write("INSERT INTO chars (name, game_id) VALUES")
                    outfile.write("('General', (SELECT id from games where name = '{}'))\n".format(game))
                else:
                    outfile.write(",('{}', (SELECT id from games where name = '{}'))\n".format(line,game))
            outfile.write(";\n")
            outfile.write("COMMIT;")