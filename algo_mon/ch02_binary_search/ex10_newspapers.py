
def newspapers_read(newspapers: List[int], coworkers: int, max_time: int) -> bool:
    coworkers_required = 1
    time_taken = 0
    i = 0
    
    while i < len(newspapers):
        if newspapers[i] + time_taken > max_time:
            coworkers_required += 1
            time_taken = 0
        else:
            time_taken += newspapers[i]
            i += 1
    
    return coworkers_required <= coworkers
        

def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    min_time = max(newspapers)
    max_time = sum(newspapers)
    boundary_time = max_time
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        if newspapers_read(newspapers, coworkers, mid):
            boundary_time = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
            
            
    return boundary_time
        