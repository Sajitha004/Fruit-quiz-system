# Fruit-quiz-system
A Python project featuring a CLI admin tool and a GUI quiz application that manage and test knowledge of fruit nutritional data using JSON and Tkinter.

# Project Overview
This project contains two related Python programs: a **Command-Line Interface (CLI)** admin tool and a **Graphical User Interface (GUI)** quiz application. Together, they manage and use nutritional data for various fruits stored in a shared JSON file (`data.txt`).

The project demonstrates practical programming skills including:
- File handling using JSON
- Input validation and exception handling
- Use of loops, functions, and lists/dictionaries
- Object-Oriented Programming (OOP) and GUI design using `tkinter`

# Learning Objectives
This assignment was designed to strengthen programming fundamentals and introduce structured problem-solving techniques. Through this project, the following learning outcomes were achieved:
- Design and Implementation: Developed both CLI and GUI applications from a set of functional requirements.
- Data Management: Implemented JSON-based storage for persistent and structured data handling.
- Function Reusability: Created and used reusable functions (input_something(), input_float(), save_data()) for validation and modularity.
- Error Handling: Employed exception handling for invalid inputs and missing or corrupt files.
- GUI Programming: Designed an interactive quiz interface using the tkinter library.
- Object-Oriented Design: Applied class-based structure to manage GUI logic and state tracking effectively.

# Program Functionality
1. Admin Program (admin - final.py): A command-line interface that manages the fruit nutrition database.

Core Features:  
- Add Fruit: Prompts for fruit name and nutritional information per 100g (energy, fibre, sugar, potassium). Prevents duplicates and validates all inputs.  
- List Fruit: Displays all fruits in the database with numbered indices.  
- Search Fruit: Finds fruits containing a search term (case-insensitive) and lists results.  
- View Fruit: Displays full nutritional information of a selected fruit with units and labels.  
- Delete Fruit: Removes a fruit entry from the list and updates the data file.  
- Persistent Data Storage: All changes are saved to a data.txt file in JSON format.  

2. Fruit Quiz Program (fruit_quiz.py): A GUI-based quiz that loads the fruit data and tests the user’s knowledge interactively.

Core Features:  
- Automatic Data Loading: Reads fruit information from data.txt and validates the dataset.  
- Randomized Questions: Randomly selects two different fruits and one nutrient (energy, fibre, sugar, or potassium).  
- Interactive Quiz: Asks “Which fruit has more [nutrient]?” with clickable buttons.  
- Feedback and Scoring: Displays message boxes showing if the user was correct and the running score.  
- Continuous Play: Generates new questions until the user closes the window.

# Reflection
This project provided hands-on experience in building complete software systems that combine data management with interactive interfaces. Developing the admin tool emphasized clean logic flow, input validation, and data persistence, while creating the GUI quiz highlighted object-oriented design and event-driven programming. Overall, the project demonstrated the ability to translate requirements into working code, use modular and reusable structures, and design a user-friendly experience through both command-line and graphical interfaces.
