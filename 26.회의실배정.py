n = int(input())
meeting = []

for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

# print(meeting)

meeting.sort(key=lambda x: (x[1], x[0]))
# print(meeting)

endtime = 0
count = 0
for start, end in meeting:
    if start >= endtime:
        endtime = end
        count += 1

print(count)
