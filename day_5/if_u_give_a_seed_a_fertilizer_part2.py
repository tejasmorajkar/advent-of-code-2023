input_seeds, *blocks = open("input.txt").read().split("\n\n")
input_seeds = list(map(int, input_seeds.split(":")[1].split()))
seeds = []
for idx in range(0, len(input_seeds), 2):
    seeds.append((input_seeds[idx], input_seeds[idx] + input_seeds[idx + 1]))

mapping = seeds
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new_mapping = []
    while len(mapping) > 0:
        segment_start, segment_end = mapping.pop()
        for destination_start, source_start, range_len in ranges:
            overlap_start = max(segment_start, source_start)
            overlap_end = min(segment_end, source_start + range_len)
            if overlap_start < overlap_end:
                new_mapping.append((destination_start + overlap_start - source_start,
                                    destination_start + overlap_end - source_start))
                if overlap_start > segment_start:
                    mapping.append((segment_start, overlap_start))
                if segment_end > overlap_end:
                    mapping.append((overlap_end, segment_end))
                break
        else:
            new_mapping.append((segment_start, segment_end))
    mapping = new_mapping
print(min(mapping)[0])
