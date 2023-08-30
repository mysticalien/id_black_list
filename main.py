from collections import Counter

n, k = map(int, input().split())
black_list = set()
end_list = []
middles = []
used_addresses = set()
filter_entries = []
minimum = 0
flag = 1

for i in range(0, n):
    line = input()
    black_list.add(line)
    parts = line.split('.')
    ending = parts[-1]
    middle = parts[-2]
    end_list.append(ending)
    middles.append(middle)

counter = 0
new_counter = 0
hehe = 0

duplicates = [item for item, count in sorted(Counter(middles).items(), key=lambda x: x[1], reverse=True) if count > 1]

for i in range(0, len(middles)):
    for duplicate in duplicates:
        if duplicate == middles[i]:
            counter += 1

if duplicates and (counter == len(end_list) or k >= len(duplicates) + 1):
    for duplicate in duplicates:
        if k < len(middles):
            entry = f"100.200.{duplicate}.0/24"
            filter_entries.append(entry)
            end_list = [end_list[i] for i in range(0, len(end_list)) if middles[i] != duplicate]
            middles = [mid for mid in middles if mid != duplicate]
            k -= 1
            new_counter += 1
if len(middles) <= k:
    filter_entries.extend([f"100.200.{mid}.{end}" for mid, end in zip(middles, end_list)])
else:
    filter_entries = []
    filter_entries.append("100.200.0.0/16")

for entry in filter_entries:
    if flag == 1 and entry.endswith('/16'):
        minimum = (65536 - n)
        flag = 0
    elif entry.endswith('/24') and flag == 1:
        minimum = (256 * new_counter - (n - len(middles)))
        flag = 0

print(minimum)
print(len(filter_entries))
for entry in filter_entries:
    print(entry)

