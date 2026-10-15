# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

# formula1 = ["mclaren", "ferrari", "redbull", 2, 3, 1, ["lewis Hamilton", 2]]
# print(formula1)
# formula1.append("mandalika")
# print(formula1)
# formula1.extend(["max", "carlos"])
# formula1.insert(3, "mercedes")
# print(formula1)
# formula1[1] = "alpine"
# print(formula1)
# formula1[0:2] = ["monza", "silverstone"]
# print(formula1)
# del formula1[2]
# formula1.remove("mclaren")
# ambil_formula1 =formula1.pop(0)
# print(ambil_formula1)
# print(formula1[0:6:2])

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# print(juara)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# for i in line_up:
#     for j in i:
#         print(j)
# print(line_up[1][1:2])

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# print(chara[3])
# listchara = list(chara)
# listchara.insert(3, 19)
# # listchara.append("yui")
# chara = tuple(listchara)
# print(chara[1:5])

chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, Genshin, DrStone) = chara
(Persona, Oregairu, *Genshin) = chara
print(Persona)
print(Oregairu) 
print(Genshin)
