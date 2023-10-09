def initialize_seating() -> list:
    return [[0] * 8 for _ in range(5)]


def print_seating(seating: list) -> None:
    for row in seating:
        print(row)


def book_seat(seating: list, row: int, seat: int) -> None:
    if seating[row][seat] == 0:
        seating[row][seat] = 1
        print("Seat booked successfully!")
    else:
        print("Seat is already booked.")


def book_back_row(seating: list) -> None:
    row = 4
    for i in range(8):
        if seating[row][i] == 0:
            seating[row][i] = 1
            print(f"Seat {i + 1} in the back row has been booked.")
            return
    print("No available seats in the back row.")


def book_multiple_seats(seating: list, row: int, num_seats: int) -> None:
    if row < 0 or row >= 5:
        print("Invalid row number.")
        return

    for i in range(9 - num_seats):
        is_available = True
        for j in range(num_seats):
            if seating[row][i + j] != 0:
                is_available = False
                break
        if is_available:
            for j in range(num_seats):
                seating[row][i + j] = 1
            print(f"{num_seats} seats booked in row {row + 1} starting from seat {i + 1}.")
            return
    print(f"No available {num_seats} seats together in row {row + 1}.")


def main():
    seating = initialize_seating()

    while True:
        print("\n--- Movie Theatre Booking System ---")
        print("1. Book a seat by row/column")
        print("2. Book seat in back row")
        print("3. Book multiple seats in a given row")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            row = int(input("Enter the row number (1-5): ")) - 1
            seat = int(input("Enter the seat number (1-8): ")) - 1
            book_seat(seating, row, seat)
            print_seating(seating)
        elif choice == "2":
            book_back_row(seating)
            print_seating(seating)
        elif choice == "3":
            row = int(input("Enter the row number (1-5): ")) - 1
            num_seats = int(input("Enter the number of seats to book: "))
            book_multiple_seats(seating, row, num_seats)
            print_seating(seating)
        elif choice == "4":
            print("Thank you for using the booking system. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
