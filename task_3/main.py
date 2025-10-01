import heapq

def minimize_costs(cables: list) -> int:
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

def main():
    cables = [10, 8, 12, 6, 3, 2, 11, 5]
    print("Minimum total cost to connect all cables:", minimize_costs(cables))

if __name__ == "__main__":
    main()
