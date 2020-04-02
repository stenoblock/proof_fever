import random

# Declare input files here.
nouns = "./vs_substantive.txt"
verbs = "./vs_verben.txt"
pradvectives = "./vs_pradvektive.txt"

def make_poetry():
    """Print phrase of 3 random SU words and where to find them."""
    with open(nouns) as n:
        nlines = n.readlines()
        noun = random.choice(nlines).split("§")
    with open(verbs) as v:
        vlines = v.readlines()
        verb = random.choice(vlines).split("§")
    with open(pradvectives) as p:
        plines = p.readlines()
        pradvective = random.choice(plines).split("§")
    print(noun[0] + pradvective[0] + verb[0][:-1] + ".", 
          "(§" + noun[1][:-1] + ", §" + pradvective[1][:-1]
          + ", §" + verb[1][:-1] + ")", end = " "
    )

print("\nFür neue Phrase ENTER drücken, beliebige Eingabe zum Beenden.\n")
motivated = True
while motivated:
    motivated = False
    make_poetry()
    if input() == "":
        motivated = True
    else:
        raise SystemExit
