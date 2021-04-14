#   Name: project.py
#   Author: Patrik Richard Szilagyi
#   Description: SOFT6018 Project 2020 - BLACKWATER ANNUAL CONCERT

# Main menu
MENU = "Blackwater Annual Music Concert\n" \
       "-------------------------------\n" \
       "1. Adding Performers\n" \
       "2. Generate Concert Details\n" \
       "3. Quit"
print(MENU)

# Start of infinite while loop
while True:
    try:
        # Ask user for input
        selected = int(input("==> "))

        # Code to execute when 1st option is selected
        if selected == 1:
            # Open performer.txt file to append to it
            performance_file = open("performer.txt", "a")

            # Option 1 Heading
            print("\n(1) Adding Performers")
            print("-" * 22)

            # Try to get a valid input for the number of performers, otherwise display an error and ask for input again
            while True:
                try:
                    num_of_performers = int(input("How many performers are you adding? "))
                    break
                except ValueError:
                    num_of_performers = 0
                    print("[ERR1] INVALID INPUT! Use integers to add the amount of performers.\n")
            # End of while loop

            # Code to execute when the number of performers are greater than 0 (valid input is provided)
            if num_of_performers > 0:
                # Accumulators and counters
                performance_details = ""
                num_of_musicians = 0
                num_of_singers = 0
                num_of_dancers = 0
                total_time = 0
                hours = 0
                minutes = 0
                longest_performance = 0
                longest_act = ""

                # Keep getting input from user for the performers
                for i in range(num_of_performers):
                    # Iterate i
                    i += 1

                    print(f"3\nBooking {i}/{num_of_performers}:")
                    # Start of inputs
                    firstname = input("Enter your name: ")
                    surname = input("Enter your surname: ")
                    # Keep looping until valid input is given by user for the performance type
                    while True:
                        try:
                            performance_type_num = int(input("Type of Performance:\n"
                                                             "\t1. Musical\n"
                                                             "\t2. Singer\n"
                                                             "\t3. Dance\n"
                                                             "==> "))
                            # Get the type of performance
                            if performance_type_num == 1:
                                performance_type = "Musician"
                                num_of_musicians += 1
                                break
                            elif performance_type_num == 2:
                                performance_type = "Singer"
                                num_of_singers += 1
                                break
                            elif performance_type_num == 3:
                                performance_type = "Dancer"
                                num_of_dancers += 1
                                break
                            else:
                                performance_type = ""
                                print("[ERR2] INVALID INPUT! Please select from a valid option (1-3).\n")
                            # End of if-else statement
                        except ValueError:
                            print("[ERR3] INVALID INPUT! Use integers to select from a valid option (1-3).\n")
                    # End of while loop
                    # Keep looping until valid input is given by user for the performance length
                    while True:
                        try:
                            # Keep looping until time slot entered by user is more than 0
                            while True:
                                perf_length = int(input("Time slot required (mins): "))
                                if perf_length > 0:
                                    performance_length = perf_length
                                    break
                                else:
                                    performance_length = 0
                                    print("[ERR4] INVALID INPUT! Value for time on stage must be greater than 0.\n")
                                # End of if-else statement
                            # End of while loop
                            break
                        except ValueError:
                            print("[ERR5] INVALID INPUT! Use integers to set time in minutes.\n")
                    # End of while loop
                    # End of inputs

                    # Get the total time
                    total_time += performance_length
                    hours = total_time // 60
                    minutes = total_time % 60

                    # Get the longest act
                    if performance_length > longest_performance:
                        longest_performance = performance_length
                        longest_act = f"{firstname} {surname} ({performance_type}) {longest_performance} minutes"

                    # Add performers to performance details
                    performer = f"{surname}, {firstname}\t\t{performance_type:10}\t{performance_length:4} minutes"
                    performance_details += f"\n{i}. {performer}"

                    # Add performer details to performer.txt file
                    print(f"{surname} {firstname} {performance_type} {performance_length}", file=performance_file)
                # End of for loop

                # Close performance.txt file
                performance_file.close()

                # Output of option 1
                print(f"\nThe following information has been added."
                      f"\n{performance_details}\n"
                      f"\nSummary Notes:\n"
                      f"--------------\n"
                      f"{num_of_musicians} Musician(s)\n"
                      f"{num_of_singers} Singer(s)\n"
                      f"{num_of_dancers} Dancer(s)\n"
                      f"Total time required: {hours} hour(s), {minutes} min(s)\n"
                      f"The longest act added is {longest_act}.\n"
                      f"\n{MENU}")

            # Code to execute when no valid input is given for number of performers (<0)
            else:
                print(f"{MENU}")
            # End of if-else statement
        # End of option 1

        # Code to execute when 2nd option is selected
        elif selected == 2:
            # Option 2 Heading
            print("\n(2) Concert Details")
            print("-" * 20)

            # Open performer.txt to read
            with open("performer.txt") as concert_details:
                # Iterator
                i = 0

                # Keep looping the lines in the file
                for line in concert_details:
                    # Increment iterator
                    i += 1

                    # Get the data from performer.txt
                    performer_data = line.rstrip().split(" ")
                    perform_surname = performer_data[0]
                    perform_firstname = performer_data[1]
                    perform_type = performer_data[2]
                    perform_length = int(performer_data[3])

                    # If the length of a performance > 15 then display an asterisk as an indicator
                    if perform_length > 15:
                        indicator = "*"
                    else:
                        indicator = ""
                    # End of if-else statement

                    # Output of option 2
                    print(
                        f"{i}: {perform_firstname} {perform_surname}{indicator}\t\t({perform_type})\t{perform_length} minutes")
                # End of for loop
            # End of file operations

            # Close performance.txt file
            concert_details.close()

            # Print main menu
            print(f"\n{MENU}")
        # End of option 2

        # Code to execute when 3rd option is selected (quit program)
        elif selected == 3:
            break
        # End of option 3

        # Code to execute when no valid option is selected (ask the user for input again)
        else:
            print("[ERR6] INVALID INPUT! Please select from a valid option (1-3).\n"
                  f"\n{MENU}")
        # End of elif statements

    # When an error is detected ask the user for input again
    except ValueError:
        print("[ERR7] INVALID INPUT! Use integers to select from a valid option (1-3).\n"
              f"\n{MENU}")
# End of infinite while loop
