def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes  # Return a list if multiple modes

def main():
    # Ask the user to input numbers separated by spaces
    numbers = input("Enter numbers separated by spaces: ").strip()
    if not numbers:
        number_list = []
    else:
        number_list = [int(num) for num in numbers.split()]
    avg = calculate_average(number_list)
    median = calculate_median(number_list)
    mode = calculate_mode(number_list)
    print("Average:", avg)
    print("Median:", median)
    print("Mode:", mode)

# The entry point for program execution
if __name__ == "__main__":
    main()
