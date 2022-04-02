num_soliders, num_vests, lower, upper = list(map(int, input().split()))
soliders = list(map(int, input().split()))
vests = list(map(int, input().split()))

vest_pointer = 0
solider_pointer = 0

results = []

while (vest_pointer < num_vests) and (solider_pointer < num_soliders):
    smallest = soliders[solider_pointer] - lower
    biggest = soliders[solider_pointer + 1] + upper
    if vests[vest_pointer] >= smallest and vests[vest_pointer] <= biggest:
        results.append((solider_pointer + 1, vest_pointer + 1))
        vest_pointer += 1
        solider_pointer += 1
    elif vests[vest_pointer] < smallest:
        vest_pointer += 1
    elif vests[vest_pointer] > biggest:
        solider_pointer += 1
        
print(len(results))
for result in results:
    print(result[0], result[1])

