# Import the necessary module(s).
import tkinter, tkinter.messagebox, random, json



class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of fruit_quiz.py" section of the assignment brief.
        
        self.window = tkinter.Tk()
        self.window.title("Fruit Quiz")
        self.window.geometry("+0+0")

        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
                if len(self.data) < 2:
                    tkinter.messagebox.showerror("Error", "Not enough fruit in database (minimum 2 required)")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            tkinter.messagebox.showerror("Error", "Missing/Invalid file")
            return

        self.components = ["energy", "fibre", "sugar", "potassium"]
        self.questions_answered = 0
        self.correct_answers = 0

        tkinter.Label(self.window, text="Which fruit has more...").pack(pady=10)
        self.question_label = tkinter.Label(self.window, text="", font=("Arial", 12, "bold"))
        self.question_label.pack(pady=10)

        button_frame = tkinter.Frame(self.window)
        button_frame.pack(pady=20)
        
        self.left_button = tkinter.Button(button_frame, width=20, height=2, command=lambda: self.check_answer("left"))
        self.left_button.pack(side="left", padx=10)
        
        tkinter.Label(button_frame, text="or").pack(side="left", padx=10)
        
        self.right_button = tkinter.Button(button_frame, width=20, height=2, command=lambda: self.check_answer("right"))
        self.right_button.pack(side="left", padx=10)
        
        # Show first question and start main loop
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        # This method randomly selects two fruit and a nutritional component and displays them in the GUI.
        # See Point 1 of the "Methods in the GUI class of fruit_quiz.py" section of the assignment brief.

        # Selects two different random fruits and a random component.
        self.left_fruit, self.right_fruit = random.sample(self.data, 2)
        self.component = random.choice(self.components)


        self.question_label.config(text=self.component)
        self.left_button.config(text=self.left_fruit["name"])
        self.right_button.config(text=self.right_fruit["name"])



    def check_answer(self, choice):   
        # This method is responsible for determining whether the user clicked the correct button.
        # See Point 2 of the "Methods in the GUI class of fruit_quiz.py" section of the assignment brief.

        
        left_value = self.left_fruit[self.component]
        right_value = self.right_fruit[self.component]

        # This checks the answer is correct or not.
        if choice == "left":
            is_correct = left_value >= right_value
        else:
            is_correct = right_value >= left_value


        # This updates the score and shows the result.
        self.questions_answered += 1
        if is_correct:
            self.correct_answers += 1
            message = "You got it right."
        else:
            message = "You got it wrong."
        
        tkinter.messagebox.showinfo("Result", f"{message}\nScore: {self.correct_answers}/{self.questions_answered}")

        self.show_question()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

