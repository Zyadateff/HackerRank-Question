if __name__ == '__main__':
    while True:
        n = int(input())
        arr = list(map(int, input().split()))

        if len(arr) == n:
            unique_scores = set(arr)
            unique_scores.remove(max(unique_scores))
            runner_up = max(unique_scores)
            print(runner_up)  
            break             
        else:
            print("Please, number of elements must equal n")
            continue
