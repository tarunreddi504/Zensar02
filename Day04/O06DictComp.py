
squares = {x :x ** 2 for x in range(1, 11)}
print(f'squares :{squares}')
print("-" * 40)

players = {
    'sachin':{290, 350, 460, 401, 380},
    'rahul':{230, 410, 185, 275, 370},
    'sehwag':{340, 430, 485, 390, 350},
    'sourav':{140, 190, 385, 430, 320},
    'yuvraj':{160, 230, 380, 120, 185}
}
print(f"players :{players}")

print("-" * 40)

print(sum(players['sachin']))

print("-" * 40)
scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
scores = {k: (lambda scores: sum(scores) / len(scores))(v)
            for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
def avgScr(score):
    return sum(score) / len(score)

scores = {k: avgScr(v) for k,v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
basic1 = [{x: (lambda par: "Mr." + par)("sachin {}".format(x))}
          for x in range(1, 6)]
print(basic1)

print("-" * 40)

players = {
    'sachin':[290, 350, 460, 401, 380],
    'rahul':[230, 410, 185, 275, 370],
    'sehwag':[340, 430, 485, 390, 350],
    'sourav':[140, 190, 385, 430, 320],
    'yuvraj':[160, 230, 380, 120, 185]
}

ply1 = [ply1_score for ply1_score in players]
print(f"ply1 :{ply1}")

print("-" * 40)
ply1 = [ply1_score for ply1_score in players.values()]
print(f"ply1 :{ply1}")

print("-" * 40)
ply1 = [x for ply1_score in players.values() for x in ply1_score]
print(f"ply1 :{ply1}")

print("-" * 40)
ply1 = [x for ply1_score in players.values() for x in ply1_score if x > 200]
print(f"ply1 :{ply1}")

print("-" * 40)
runsGT200 = {name: [scr for scr in score if scr > 200]
              for name, score in players.items()}
print(f"runsGT200 :{runsGT200}")
