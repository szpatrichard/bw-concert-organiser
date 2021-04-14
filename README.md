<img src="https://socsportal.cit.ie/assets/images/logowhite.jpg" alt="CIT Logo" width="25%" />

#### Cork Institute of Technology

##### CR106 - BSc Honours Software Development

##### 2020-21 Academic Year (Year 1 Semester 1)

---

# SOFT6018 - Programming Fundamentals Project

Worth: 30%

**Due Date:**: Sunday 13th December @ 23:59

## Blackwater Annual Concert

Write a program that helps organise the Blackwater Annual Concert.

The main menu allows the user add performers to the concert and eventually it is used to generate a
schedule for the concert based on all the information entered and stored in a file performers.txt

Write a program that offers two choices to the user:

1. Add performers to the show
2. Generate concert details

### 1 - Adding performers

The program allows the user add a list of performers. For each performer entered they must give

-   their first name and last name
-   the type of performance
-   the duration in minutes for their performance.

The performers information entered is stored to a file called performers.txt. After performers are added
a summary of the performers just added is given.

This shows the details for each performer and some statistics:

-   the number of musicians, singers and dancers
-   the longest act
-   the total time required for all performances

**A sample run:**

```
Blackwater Annual Music Concert
-------------------------------
1. Adding Performers
2. Generate Concert Details
3. Quit
==> 1

(1) Adding Performers
---------------------
How many performers are you adding: 3

Booking 1/3:
Enter your name: Fred
Enter your surname: Walsh
Type of Performance
1. Musical
2. Singer
3. Dance
==>: 1
Time slot required(mins): 15

Booking 2/3:
Enter your name: Harry
Enter your surname: Ford
Type of Performance
1. Musical
2. Singer
3. Dance
==>:3
Time slot required(mins): 25

Booking 3/3:
Enter your name: Sam
Enter your surname: Murphy
Type of Performance
1. Musical
2. Singer
3. Dance
==>:1
Time slot required(mins)? 20

The following information has been added.

1. Walsh,Fred Musician 15 minutes
2. Ford,Harry Dancer 25 minutes
3. Murphy,Sam Musician 20 minutes

Summary Notes:
-------------
2 Musicians
0 Singers
1 Dancer
Total time required: 1 hour(s), 0 min(s)
The longest act added is Harry Ford(Dancer) 25 minutes.

Blackwater Annual Music Concert
-------------------------------
1. Adding performers
2. Generate Concert Details
3. Quit
==> 1
How many performers are you adding: 1

Booking 1/1:
Enter your name: Mary
Enter your surname: Murphy
Type of Performance
1. Musical
2. Singer
3. Dance
==>: 3
Time slot required(mins): 19

The following information has been added.

1. Murphy, Mary Dancer 19 minutes

Summary Notes:
-------------
0 Musicians
0 Singers
1 Dancer
Total time required: 0 hours, 19 mins
The longest act added is Mary Murphy(Dancer) 19 minutes.

Blackwater Annual Music Concert
-------------------------------
1. Adding performers
2. Generate Concert Details
3. Quit
==> 3
```

And **performers.txt** becomes

```
Walsh Fred Musician 15
Ford Harry Dancer 25
Murphy Sam Musician 20
Murphy Mary Dancer 19
```

### 2 - Generate Concert Details

The program will read performers.txt and display the details of the concert on the screen.

An asterisk should be placed after each performer's name whose act is longer than 15 minutes.

**Sample Run**

```
Blackwater Annual Music Concert
--------------------------------
1. Adding performers
2. Generate Concert Schedule
3. Quit
==> 2

1: Fred Walsh (Musician) 15 minutes
2: Ford Harry* (Dancer) 25 minutes
3: Sam Murphy* (Musician) 20 minutes
4: Mary Murphy* (Dancer) 19 minutes

Blackwater Annual Music Concert
--------------------------------
1. Adding performers
2. Generate Concert Schedule
3. Quit
==> 3
```

## Project Development Guidelines

### 1. Implementing the Menu

**Step 1.1**

-   Create a string for the menu showing 3 options
-   Get the users choice as an int and print a message for each option(if statement)
-   Test and Run

**Step 1.2**

-   Add a while loop so that the user can exit loop on choosing `3`
-   Hint: Easiest way is forever loop + if statement + break
-   Test and Run

### 2. Implementing Option 1 Adding Performers

**Step 2.1**

-   Get the number of performers to be addded from the user
-   Add a counting loop for this ie. printing `1/3`, `2/3`, `3/3` if they type in `3`.
-   Test and Run

**Step 2.2**

-   Add code to get information about each performer that needs to be added
-   Get the first name and surname
-   Get the type of performance - as a number
-   Get the length of the performance - as a number
-   Add an if statement to initialise a string for `performance_type` to be `Dancer`/`Singer`/`Musician`.
-   Create a variable using f-string containing the details for a performer. ie `Ann Ford Musician 20 minutes`
-   Print this variable in the loop for testing.
-   Test and Run

**Step 2.3**

-   Create a string accumulator variable for all the performers details.
-   In your loop add the line of information about each performer to this variable
-   Modify the program so there is a single print statement that shows the information for all performers once all the data for this set of performers has been added

**Step 2.4**

-   Add counters for
    -   no. of musicians
    -   no. of singers
    -   no. of dancers
    -   total time
-   Set these variables to `0` before the loop and bump up when appropriate ( you may need to add if statements)
-   print these outside the loop. ie once all of this set of performers have been added
-   convert the total minutes to hours and minutes

**Step 2.5**

-   Create an empty file `performer.txt` in the same directory as your program in pycharm.
-   At the start of “Add Performers” open the file to append to the file.
-   Add 1 line to the file for each performer: create a line of data that matches the format of the data stored in the file
-   Once a set of performers have been added close the file
-   Test and Run

### Implementing Option 2 Generating Concert Schedule

**Step 3.1**
• Open the file for reading
• Read each line of the file and print to screen
• Number each line shown
• Close the file

**Step 3.2**
• Extract the details of each line into an array
• Print all the elements of the array to the screen

**Step 3.2**
• Modify so the duration of a performance is stored as an int
• Add an if statement so a \* appears after the name if duration > 15

---

#### SOFT6018 - Programming Fundamentals

##### Patrik Richard Szilagyi, 2020
