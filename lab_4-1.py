# Author MRS 12/16/20

rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan", "Phil", "Eman", "Alex", "Nicholas"], ["Matt", "Francesco"], ["Patrick", "Nico", "Trevayne"]]

for row in rows:
    for index, name in enumerate(row):
        if name[-1] == "s":
            row[index] = name + "'"
        else:
            row[index] = name + "'s"

print(rows)
