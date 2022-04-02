num_soliders, num_vests,\
                lower_bound, upper_bound = list(map(int, input().split()))
solider_sizes = list(map(int, input().split()))
vest_sizes = list(map(int, input().split()))
 
vest_pointer = 0
solider_pointer = 0
results = []
while (vest_pointer < num_vests) and (solider_pointer < num_soliders):
    smallest_size = solider_sizes[solider_pointer] - lower_bound
    biggest_size = solider_sizes[solider_pointer] + upper_bound
    if vest_sizes[vest_pointer] >= smallest_size\
        and vest_sizes[vest_pointer] <= biggest_size:
        results.append((solider_pointer + 1, vest_pointer + 1))
        vest_pointer += 1
        solider_pointer += 1
    elif biggest_size < vest_sizes[vest_pointer]:
        solider_pointer += 1
    elif smallest_size > vest_sizes[vest_pointer]:
        vest_pointer += 1
 
print(len(results))
for result in results:
    print(result[0], result[1])