# Movie-Theatre-Booking-System
Movie Theatre Booking System
Description:

Developed a Python program for a Movie Theatre Booking System, allowing users to book seats, including options for individual seat booking, back row booking, and booking multiple seats in a specific row. The program maintains the theatre's seating arrangement, ensuring a seamless booking experience for customers.
Key Features:

    Seat Initialization: Implemented a function to initialize the theatre seating, creating a 2D list representing available (0) and booked (1) seats.

    Individual Seat Booking: Users can book individual seats by specifying the row and seat numbers. The program checks seat availability and confirms successful bookings.

    Back Row Booking: Provided a feature to automatically book seats in the back row if available, enhancing the user experience for those preferring rear seating.

    Multiple Seat Booking: Implemented functionality for users to book multiple seats together in a specific row. The program validates seat availability for the requested number of seats and reserves them if available.

Functions:

    initialize_seating() -> list:
        Initializes the theatre seating grid with rows and seats.

    print_seating(seating: list) -> None:
        Displays the current seating arrangement.

    book_seat(seating: list, row: int, seat: int) -> None:
        Books an individual seat based on user input, considering seat availability.

    book_back_row(seating: list) -> None:
        Books a seat in the back row if available, providing a convenient option for users.

    book_multiple_seats(seating: list, row: int, num_seats: int) -> None:
        Allows users to book multiple seats in a specified row, ensuring consecutive seat availability.

    main():
        Main function handling user interaction, displaying menu options, and calling appropriate functions based on user choices.

Technologies Used:

    Programming Language: Python 3
    Development Environment: Python IDLE (or any Python-compatible editor)

Achievements:

    Designed and implemented a functional movie theatre booking system, enhancing user experience through intuitive seat booking options.
    Demonstrated proficiency in Python programming, utilizing loops, conditionals, and 2D lists for efficient seat management.
    Improved problem-solving skills by implementing seat availability checks and booking logic, ensuring a smooth booking process.

Learning Outcomes:

    Applied fundamental programming concepts to create a real-world application, reinforcing programming skills and problem-solving abilities.
    Enhanced user interaction understanding by developing a console-based interactive application, demonstrating user-driven program flow.
    Developed a modular program structure, promoting code organization and readability for easier maintenance and future enhancements.
