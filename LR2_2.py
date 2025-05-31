def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            lines = [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        print("File not found.")
        return

    while True:
        print(f"\nThe file has {len(lines)} lines.")
        try:
            line_num = int(input(f"Enter a line number (1-{len(lines)}) or 0 to quit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if line_num == 0:
            print("Goodbye!")
            break
        elif 1 <= line_num <= len(lines):
            print(lines[line_num - 1])
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    main()