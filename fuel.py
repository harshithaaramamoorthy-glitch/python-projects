def min_cost(n, distances):
    total_distance = sum(distances)
    fuel_adjustment = abs(total_distance)
    return fuel_adjustment

def main():
    try:
        n = int(input().strip())
        distances = list(map(int, input().strip().split()))
        print(min_cost(n, distances))
    except Exception as e:
        # In a real application, you'd log this error
        pass
if __name__ == "__main__":
    main()