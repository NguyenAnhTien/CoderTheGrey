def assign_tasks(tasks, workers, pills, strength):
    def can_assign(tasks, workers, pills):
        while len(tasks) and len(workers):
            if workers[-1] >= tasks[-1]:
                workers.pop()
                tasks.pop()
            elif pills > 0: 
                pills -= 1
                position = bisect.bisect_left(workers, tasks[-1] - strength)
                if position >= len(workers):
                    return False
                workers.pop(position)
                tasks.pop()
            else:
                return False
        return True

    tasks.sort()
    workers.sort()
    low = 0
    high = min(len(tasks), len(workers))
    while low <= high:
        mid = (low + high) // 2
        if can_assign(tasks[:mid], workers[-mid:], pills):
            low = mid + 1
        else:
            high = mid - 1
    return high

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        return assign_tasks(tasks, workers, pills, strength)