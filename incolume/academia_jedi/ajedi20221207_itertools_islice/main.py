from itertools import islice


lines = [
    "line1",
    "line2",
    "line3",
    "line4",
    "line5",
    "line6",
    "line7",
    "line8",
    "line9",
    "line10",
]

# Sem islice
for i, line in enumerate(lines):
    if i >= 5:
        break
    print(line)


print()
# islice + stop
for line in islice(lines, 5):
    print(line)

print()
# islice + start + stop
for line in islice(lines, 1, 5):
    print(line)

print()
# islice + start + stop + step
for line in islice(lines, 1, 5, 2):
    print(line)
