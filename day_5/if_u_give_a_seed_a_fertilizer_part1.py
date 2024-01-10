seeds, *blocks = open("test.txt").read().split("\n\n")
seeds = list(map(int, seeds.split(":")[1].split()))
mapping = seeds
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new_mapping = []
    for val in mapping:
        for destination, source, range_len in ranges:
            if source <= val < (source + range_len):
                new_mapping.append(destination + val - source)
                break
        else:
            new_mapping.append(val)
    mapping = new_mapping
print(min(mapping))

