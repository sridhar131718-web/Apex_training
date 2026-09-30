players = ["virat", "dhoni", "rohit", "jadeja"]

players.append("bumrah")
print(players)


players.append("kl rahul")
print(players)


players.insert(2, "dravid")
print(players)


players.remove("rohit")
print(players)


players.pop(3)
print(players)

print(players.index("virat"))
players.append("dhoni")
print(players.count("dhoni"))

players2 = [18, 7, 19, 97, 1]

players2.sort()
print("Sorted list:", players2)

players2.reverse()
print("Reversed list:", players2)

players = ["virat", "dhoni", "rohit", "jadeja"]

players2 = players.copy()

print("Original list:", players)
print("Copied list:", players2)

players2 = [18, 7, 19, 97, 1]

print("List:", players2)

print("Maximum value:", max(players2))
print("Minimum value:", min(players2))
print("Number of elements:", len(players2))

players2.clear()

print("After clear():", players2)
