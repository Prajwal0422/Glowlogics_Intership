all_lines = []

with open("E:\\sample.txt", "r") as f2:
    data = f2.readlines()

    for x in data:
        all_lines.append(x.split())

print(all_lines)