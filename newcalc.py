import datetime
import math
import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
class App(ctk.CTk):
    def __init__(self, *args):
        super().__init__(*args)
        self.title("Advanced Calculator")
        self.geometry("420x320")
        self.resizable(False, False)

        # Entry for displaying the input expression or result
        self.inputlabel = ctk.CTkEntry(self, placeholder_text="Enter Something to Calculate")
        self.inputlabel.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 0), ('.', 4, 2), ('+', 5, 0),
            ('-', 5, 2), ('*', 6, 0), ('/', 6, 1),
            ('%', 6, 2), ('C', 4, 1), ('=', 7, 0)
        ]

        # Create the number and operator buttons dynamically
        for (text, row, col) in buttons:
            if text == "C":
                # For the "C" button, make it span across two rows
                button = ctk.CTkButton(self, text=text, width=60, fg_color="grey", height=70,command=self.clear_input)
                button.grid(row=row, column=col,padx=5,pady=5,sticky="ew",rowspan=2)
            elif text == "=":
                # For the "=" button, make it span across five columns
                button = ctk.CTkButton(self, text=text, width=60, fg_color="#ff0066", command=self.calc)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="ew", columnspan=5)
            else:
                # For other buttons, no need to use rowspan/columnspan
                button = ctk.CTkButton(self, text=text, width=60, fg_color="#660066", command=lambda t=text: self.button_click(t))
                button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

        # Other function buttons
        self.weight = ctk.CTkButton(self, text="Weight", width=60, fg_color="#ff3399", command=weightcalc)
        self.weight.grid(row=1, column=4, padx=5, pady=5, sticky="ew")
        self.Scientific = ctk.CTkButton(self, text="Scientific", width=60, fg_color="#ff3399", command=sciencecalc)
        self.Scientific.grid(row=2, column=4, padx=5, pady=5, sticky="ew")
        self.data = ctk.CTkButton(self, text="Data", width=60, fg_color="#ff3399", command=datacalc)
        self.data.grid(row=3, column=4, padx=5, pady=5, sticky="ew")
        self.length = ctk.CTkButton(self, text="Length", width=60, fg_color="#ff3399", command=lengthcalc)
        self.length.grid(row=4, column=4, padx=5, pady=5, sticky="ew")
        self.age = ctk.CTkButton(self, text="Age", width=60, fg_color="#ff3399", command=agecalc)
        self.age.grid(row=5, column=4, padx=5, pady=5, sticky="ew")
        self.area = ctk.CTkButton(self, text="Area", width=60, fg_color="#ff3399", command=areacalc)
        self.area.grid(row=6, column=4, padx=5, pady=5, sticky="ew")
        self.bmi = ctk.CTkButton(self, text="BMI", width=60, fg_color="#ff3399", command=bmicalc)
        self.bmi.grid(row=6, column=4, padx=5, pady=5, sticky="ew")
        self.numeral = ctk.CTkButton(self, text="Numeral System", width=60, fg_color="#ff3399", command=numeralcalc)
        self.numeral.grid(row=1, column=5, padx=5, pady=5, sticky="ew")
        self.tempreture = ctk.CTkButton(self, text="Temperature", width=60, fg_color="#ff3399", command=temprcalc)
        self.tempreture.grid(row=2, column=5, padx=5, pady=5, sticky="ew")
        self.date = ctk.CTkButton(self, text="Date", width=60, fg_color="#ff3399", command=datecalc)
        self.date.grid(row=3, column=5, padx=5, pady=5, sticky="ew")
        self.discount = ctk.CTkButton(self, text="Discount", width=60, fg_color="#ff3399", command=discountcalc)
        self.discount.grid(row=4, column=5, padx=5, pady=5, sticky="ew")
        self.mass = ctk.CTkButton(self, text="Mass", width=60, fg_color="#ff3399", command=masscalc)
        self.mass.grid(row=5, column=5, padx=5, pady=5, sticky="ew")
        self.speed = ctk.CTkButton(self, text="Speed", width=60, fg_color="#ff3399", command=speedcalc)
        self.speed.grid(row=6, column=5, padx=5, pady=5, sticky="ew")
        self.volume = ctk.CTkButton(self, text="Volume", width=60, fg_color="#ff3399", command=volumecalc)
        self.volume.grid(row=7, column=5, padx=5, pady=5, sticky="ew")

    def button_click(self, value):
        """Handles number/operator button click and updates the input field."""
        current = self.inputlabel.get()
        self.inputlabel.delete(0, ctk.END)
        self.inputlabel.insert(0, current + value)

    def clear_input(self):
        """Clears the input field."""
        self.inputlabel.delete(0, ctk.END)

    def calc(self):
        """Evaluates the expression entered in the input field."""
        try:
            expression = self.inputlabel.get()

            result = eval(expression)

            self.inputlabel.delete(0, ctk.END) 
            self.inputlabel.insert(0, str(result)) 
        except Exception as e:
            # In case of error, show "Error"
            self.inputlabel.delete(0, ctk.END) 
            self.inputlabel.insert(0, "Error")
            
def weightcalc():
    weightcalcwindow = ctk.CTkToplevel(app)
    weightcalcwindow.title("Weight Calculator") 
    weightcalcwindow.geometry("400x400")
    weightcalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(weightcalcwindow, text="WEIGHT CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="ew")

    weight_option = ctk.CTkOptionMenu(weightcalcwindow, values=["Kilograms", "Pounds"], width=150)
    weight_option.grid(row=1, column=0, padx=20, pady=10)

    weight_entry = ctk.CTkEntry(weightcalcwindow, placeholder_text="Enter Weight", width=150)
    weight_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(weightcalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_weight():
        try:
            weight = float(weight_entry.get())  
            unit = weight_option.get() 

            if unit == "Kilograms":
                # Convert to Pounds
                result = weight * 2.20462
                result_label.configure(text=f"Result: {result:.2f} Pounds")
            elif unit == "Pounds":
                # Convert to Kilograms
                result = weight * 0.453592
                result_label.configure(text=f"Result: {result:.2f} Kilograms")
        except ValueError:
            result_label.configure(text="Please enter a valid number.")

    convert_button = ctk.CTkButton(weightcalcwindow, text="Convert", width=150, fg_color="#660066", command=convert_weight)
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    weightcalcwindow.mainloop()


def sciencecalc():
    sciencecalcwindow = ctk.CTkToplevel(app)
    sciencecalcwindow.title("Science Calculator") 
    sciencecalcwindow.geometry("400x400")
    sciencecalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(sciencecalcwindow, text="SCIENCE CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    # Option menu to choose the type of science (Physics, Chemistry, Biology)
    science_option = ctk.CTkOptionMenu(sciencecalcwindow, values=["Physics", "Chemistry", "Biology"], width=150)
    science_option.grid(row=1, column=0, padx=20, pady=10)

    # Entry field to enter data (weight, height, or chemical formula)
    science_entry = ctk.CTkEntry(sciencecalcwindow, placeholder_text="Enter Data", width=150)
    science_entry.grid(row=1, column=1, padx=20, pady=10)

    # Label to show the result
    result_label = ctk.CTkLabel(sciencecalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Function to handle the calculation based on the selected science field
    def calculate_science():
        selected_option = science_option.get()
        input_data = science_entry.get()
        
        try:
            if selected_option == "Physics":
                # Physics: Force = Mass * Acceleration
                mass, acceleration = map(float, input_data.split(","))
                result = mass * acceleration
                result_label.configure(text=f"Result: {result:.2f} N (Newtons)")

            elif selected_option == "Chemistry":
                # Chemistry: (Simple Molar Mass Calculator for a compound)
                # Assuming the input is in the form of "H2O" or "NaCl"
                molar_masses = {"H": 1.008, "O": 15.999, "Na": 22.990, "Cl": 35.45}
                result = 0
                i = 0
                while i < len(input_data):
                    element = input_data[i]
                    if i + 1 < len(input_data) and input_data[i + 1].isdigit():
                        count = int(input_data[i + 1])
                        result += molar_masses[element] * count
                        i += 2
                    else:
                        result += molar_masses[element]
                        i += 1
                result_label.configure(text=f"Result: {result:.2f} g/mol")

            elif selected_option == "Biology":
                # Biology: Body Mass Index (BMI) = Weight(kg) / Height(m)^2
                weight, height = map(float, input_data.split(","))
                bmi = weight / (height ** 2)
                result_label.configure(text=f"Result: {bmi:.2f} BMI")

        except ValueError:
            result_label.configure(text="Please enter valid data.")

    # Calculate button to trigger the calculation
    calculate_button = ctk.CTkButton(sciencecalcwindow, text="Calculate", width=150, fg_color="#660066", command=calculate_science)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    sciencecalcwindow.mainloop()



def datacalc():
    datacalcwindow = ctk.CTkToplevel(app)
    datacalcwindow.title("Calculate Data")
    datacalcwindow.geometry("400x400")
    datacalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(datacalcwindow, text="DATA CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    # Labels and Inputs for Value and Units
    value_label = ctk.CTkLabel(datacalcwindow, text="Enter Value:", text_color="black")
    value_label.grid(row=1, column=0, padx=20, pady=10)
    
    value_entry = ctk.CTkEntry(datacalcwindow, placeholder_text="Value", width=150)
    value_entry.grid(row=1, column=1, padx=20, pady=10)

    # Unit Options for Conversion
    from_unit = ctk.CTkOptionMenu(datacalcwindow, values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes"], width=150)
    from_unit.grid(row=2, column=0, padx=20, pady=10)
    
    to_unit = ctk.CTkOptionMenu(datacalcwindow, values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes"], width=150)
    to_unit.grid(row=2, column=1, padx=20, pady=10)

    # Convert Button
    convert_button = ctk.CTkButton(datacalcwindow, text="Convert", width=150, fg_color="#660066", command=lambda: convert_data(value_entry.get(), from_unit.get(), to_unit.get(), result_label))
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Result Label
    result_label = ctk.CTkLabel(datacalcwindow, text="Converted Value: ", text_color="black")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    datacalcwindow.mainloop()

# Data conversion logic
def convert_data(value, from_unit, to_unit, result_label):
    try:
        value = float(value)

        # Conversion factors
        units = {
            "Bytes": 1,
            "Kilobytes": 1024,
            "Megabytes": 1024**2,
            "Gigabytes": 1024**3
        }

        # Convert value to bytes first
        value_in_bytes = value * units[from_unit]

        # Then convert bytes to the target unit
        result = value_in_bytes / units[to_unit]

        # Display the result
        result_label.configure(text=f"Converted Value: {result} {to_unit}")
    except ValueError:
        result_label.configure(text="Invalid Input. Please try again.")

def weightcalc():
    weightcalcwindow = ctk.CTkToplevel(app)
    weightcalcwindow.title("Weight Calculator") 
    weightcalcwindow.geometry("400x400")
    weightcalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(weightcalcwindow, text="WEIGHT CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    # Dropdown menu to choose between Kilograms and Pounds
    weight_option = ctk.CTkOptionMenu(weightcalcwindow, values=["Kilograms", "Pounds"], width=150)
    weight_option.grid(row=1, column=0, padx=20, pady=10)

    # Entry to input weight
    weight_entry = ctk.CTkEntry(weightcalcwindow, placeholder_text="Enter Weight", width=150)
    weight_entry.grid(row=1, column=1, padx=20, pady=10)

    # Function to perform the conversion
    def convert_weight():
        try:
            weight = float(weight_entry.get())
            selected_unit = weight_option.get()
            
            if selected_unit == "Kilograms":
                # Convert kilograms to pounds
                result = weight * 2.20462
                result_label.configure(text=f"Result: {result:.2f} Pounds")
            elif selected_unit == "Pounds":
                # Convert pounds to kilograms
                result = weight / 2.20462
                result_label.configure(text=f"Result: {result:.2f} Kilograms")
        except ValueError:
            result_label.configure(text="Please enter a valid number.")

    # Convert button to trigger the conversion
    convert_button = ctk.CTkButton(weightcalcwindow, text="Convert", width=150, fg_color="#660066", command=convert_weight)
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Label to display the result
    result_label = ctk.CTkLabel(weightcalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    weightcalcwindow.mainloop()


def sciencecalc():
    def calculate_result():
        try:
            # Get the expression from the entry
            expression = entry.get()

            # Try to evaluate the expression
            result = eval(expression)

            # Display the result
            result_label.configure(text=f"Result: {result:.5f}")
        except Exception as e:
            result_label.configure(text="Error in calculation")

    sciencecalcwindow = ctk.CTkToplevel(app)
    sciencecalcwindow.title("Scientific Calculator")
    sciencecalcwindow.geometry("400x600")
    sciencecalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(sciencecalcwindow, text="SCIENCE CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=4, pady=10)

    # Entry field for the user to input the expression
    entry = ctk.CTkEntry(sciencecalcwindow, placeholder_text="Enter Expression", width=300)
    entry.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

    # Function buttons for the calculator
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
        ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
        ('log', 7, 0), ('ln', 7, 1), ('exp', 7, 2), ('pi', 7, 3)
    ]

    # Function to insert the button value into the entry field
    def insert_to_entry(value):
        current = entry.get()
        entry.delete(0, ctk.END)  # Clear entry
        entry.insert(0, current + value)

    # Create buttons dynamically
    for (text, row, col) in buttons:
        button = ctk.CTkButton(sciencecalcwindow, text=text, width=60, height=40, command=lambda t=text: insert_to_entry(t) if t != '=' else calculate_result())
        button.grid(row=row, column=col, padx=10, pady=10)

    # Result label to show the calculation result
    result_label = ctk.CTkLabel(sciencecalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=8, column=0, columnspan=4, pady=20)

    sciencecalcwindow.mainloop()


def lengthcalc():
    def convert_length():
        try:
            # Get the value from the entry and the selected unit
            length_value = float(length_entry.get())
            selected_unit = length_option.get()

            # Conversion logic based on selected unit
            if selected_unit == "Meters":
                kilometers = length_value / 1000
                miles = length_value * 39.3701
                result = f"{length_value} Meters = {kilometers:.3f} Kilometers = {miles:.3f} Miles"
            elif selected_unit == "Kilometers":
                meters = length_value * 1000
                miles = length_value * 0.621371
                result = f"{length_value} Kilometers = {meters:.3f} Meters = {miles:.3f} Miles"
            elif selected_unit == "Miles":
                meters = length_value * 1609.34
                kilometers = length_value / 0.621371
                result = f"{length_value} Miles = {meters:.3f} Meters = {kilometers:.3f} Kilometers"
            else:
                result = "Invalid unit selected."

            # Update the result label
            result_label.configure(text=f"Result: {result}")
        except ValueError:
            # If input is not a valid number
            result_label.configure(text="Error: Please enter a valid number")

    # Create the window for the length calculator
    lengthcalcwindow = ctk.CTkToplevel(app)
    lengthcalcwindow.title("Length Calculator")
    lengthcalcwindow.geometry("400x400")
    lengthcalcwindow.resizable(False, False)

    # Header label
    headlabel = ctk.CTkLabel(lengthcalcwindow, text="LENGTH CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    # Option menu for length unit selection
    length_option = ctk.CTkOptionMenu(lengthcalcwindow, values=["Meters", "Kilometers", "Miles"], width=150)
    length_option.grid(row=1, column=0, padx=20, pady=10)

    # Entry for user to input length
    length_entry = ctk.CTkEntry(lengthcalcwindow, placeholder_text="Enter Length", width=150)
    length_entry.grid(row=1, column=1, padx=20, pady=10)

    # Result label to display conversion result
    result_label = ctk.CTkLabel(lengthcalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Convert button
    convert_button = ctk.CTkButton(lengthcalcwindow, text="Convert", width=150, fg_color="#660066", command=convert_length)
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Start the main loop for the window
    lengthcalcwindow.mainloop()
    
    
def calculate_age(day, month, year, result_label):
    try:
        # Getting today's date
        today = datetime.datetime.today()

        # Parsing the entered date
        birth_date = datetime.datetime(year=int(year), month=int(month), day=int(day))

        # Calculate the difference in years, months, and days
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day

        # Adjust months and years if necessary
        if age_months < 0:
            age_months += 12
            age_years -= 1

        # Adjust days if necessary
        if age_days < 0:
            # Subtract one from the month and add the days from the previous month
            previous_month = today.month - 1 if today.month > 1 else 12
            previous_month_days = (datetime.datetime(today.year, previous_month, 1) - datetime.timedelta(days=1)).day
            age_days += previous_month_days
            age_months -= 1

        # If months are negative, we subtract a year and correct the months.
        if age_months < 0:
            age_months += 12
            age_years -= 1

        # Display the result
        result_label.configure(text=f"Your Age: {age_years} years, {age_months} months, {age_days} days")
    except ValueError:
        result_label.configure(text="Invalid Date. Please try again.")

def agecalc():
    agecalcwindow = ctk.CTkToplevel(app)
    agecalcwindow.title("Calculate Age")
    agecalcwindow.geometry("400x400")
    agecalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(agecalcwindow, text="AGE CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    # Date of Birth Input (Using Entry fields for day, month, and year)
    dob_label = ctk.CTkLabel(agecalcwindow, text="Enter Your Date of Birth:", text_color="black")
    dob_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    # Year, Month, Day input fields
    day_entry = ctk.CTkEntry(agecalcwindow, placeholder_text="Day", width=80)
    day_entry.grid(row=2, column=0, padx=20, pady=10)
    month_entry = ctk.CTkEntry(agecalcwindow, placeholder_text="Month", width=80)
    month_entry.grid(row=2, column=1, padx=20, pady=10)
    year_entry = ctk.CTkEntry(agecalcwindow, placeholder_text="Year", width=80)
    year_entry.grid(row=2, column=2, padx=20, pady=10)

    # Calculate Button
    calculate_button = ctk.CTkButton(agecalcwindow, text="Calculate Age", width=150, fg_color="#660066", command=lambda: calculate_age(day_entry.get(), month_entry.get(), year_entry.get(), result_label))
    calculate_button.grid(row=3, column=0, columnspan=3, pady=10)

    # Result Label
    result_label = ctk.CTkLabel(agecalcwindow, text="Your Age: ", text_color="black")
    result_label.grid(row=4, column=0, columnspan=3, pady=10)

    agecalcwindow.mainloop()

def areacalc():
    areacalcwindow = ctk.CTkToplevel(app)
    areacalcwindow.title("Area Calculator") 
    areacalcwindow.geometry("400x400")
    areacalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(areacalcwindow, text="AREA CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    shape_option = ctk.CTkOptionMenu(areacalcwindow, values=["Circle", "Rectangle", "Triangle"], width=150)
    shape_option.grid(row=1, column=0, padx=20, pady=10)

    dimension_entry = ctk.CTkEntry(areacalcwindow, placeholder_text="Enter Dimensions", width=150)
    dimension_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(areacalcwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    calculate_button = ctk.CTkButton(areacalcwindow, text="Calculate", width=150, fg_color="#660066",
                                      command=lambda: calculate_area(shape_option.get(), dimension_entry.get(), result_label))
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    areacalcwindow.mainloop()

def calculate_area(shape, dimensions, result_label):
    try:
        dims = list(map(float, dimensions.split()))
        
        if shape == "Circle":
            if len(dims) == 1:
                radius = dims[0]
                area = math.pi * (radius ** 2)
                result_label.configure(text=f"Result: {area:.2f} square units")
            else:
                result_label.configure(text="Error: Please enter 1 dimension for Circle.")
        
        elif shape == "Rectangle":
            if len(dims) == 2:  # Two dimensions for length and width
                length, width = dims
                area = length * width
                result_label.configure(text=f"Result: {area:.2f} square units")
            else:
                result_label.configure(text="Error: Please enter 2 dimensions for Rectangle.")
        
        elif shape == "Triangle":
            if len(dims) == 2:  # Two dimensions for base and height
                base, height = dims
                area = 0.5 * base * height
                result_label.configure(text=f"Result: {area:.2f} square units")
            else:
                result_label.configure(text="Error: Please enter 2 dimensions for Triangle.")
        
        else:
            result_label.configure(text="Error: Invalid shape selected.")
    
    except ValueError:
        result_label.configure(text="Error: Please enter valid numeric dimensions.")

def bmicalc():
    bmicalcwindow = ctk.CTkToplevel(app)
    bmicalcwindow.title("Calculate BMI") 
    bmicalcwindow.geometry("400x400")
    bmicalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(bmicalcwindow, text="BMI CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Weight input fields
    weight_option = ctk.CTkOptionMenu(bmicalcwindow, values=['Kilograms', 'Pounds'], width=100)
    weight_option.grid(row=1, column=0, padx=10, pady=10)
    weight_entry = ctk.CTkEntry(bmicalcwindow, placeholder_text="Enter Weight")
    weight_entry.grid(row=2, column=0, padx=10, pady=10)

    # Height input fields
    height_option = ctk.CTkOptionMenu(bmicalcwindow, values=['Centimeters', 'Meters', 'Feet', 'Inches'], width=100)
    height_option.grid(row=1, column=1, padx=10, pady=10)
    height_entry = ctk.CTkEntry(bmicalcwindow, placeholder_text="Enter Height")
    height_entry.grid(row=2, column=1, padx=10, pady=10)

    # Result label
    result_label = ctk.CTkLabel(bmicalcwindow, text="BMI: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Calculate Button
    calculate_button = ctk.CTkButton(bmicalcwindow, text="Calculate BMI", width=150, fg_color="#660066", 
                                     command=lambda: calculate_bmi(float(weight_entry.get()), weight_option.get(),
                                                                  float(height_entry.get()), height_option.get(), result_label))
    calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    bmicalcwindow.mainloop()
    
    
def convert_weight(weight_value, weight_unit):
    if weight_unit == 'Pounds':
        return weight_value * 0.453592  # Pounds to Kilograms
    return weight_value  # Kilograms

def convert_height(height_value, height_unit):
    if height_unit == 'Centimeters':
        return height_value / 100  # Centimeters to Meters
    elif height_unit == 'Feet':
        return height_value * 0.3048  # Feet to Meters
    elif height_unit == 'Inches':
        return height_value * 0.0254  # Inches to Meters
    return height_value  # Meters

# BMI Calculation Function
def calculate_bmi(weight, weight_unit, height, height_unit, result_label):
    try:
        # Convert weight and height to standard units
        weight_kg = convert_weight(weight, weight_unit)
        height_m = convert_height(height, height_unit)

        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        
        # BMI Categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.configure(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        result_label.configure(text="Error: Please enter valid numbers")

def decimal_to_binary(decimal_value):
    return bin(decimal_value)[2:]

def decimal_to_hexadecimal(decimal_value):
    return hex(decimal_value)[2:].upper()

def decimal_to_roman(decimal_value):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while decimal_value > 0:
        for _ in range(decimal_value // val[i]):
            roman_num += syb[i]
            decimal_value -= val[i]
        i += 1
    return roman_num


def numeralcalc():
    numeralcalcwindow = ctk.CTkToplevel(app)
    numeralcalcwindow.title("Calculate Numerals") 
    numeralcalcwindow.geometry("400x400")
    numeralcalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(numeralcalcwindow, text="NUMERAL CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    from_option = ctk.CTkOptionMenu(numeralcalcwindow, values=["Decimal", "Binary", "Hexadecimal", "Roman"], width=150)
    from_option.grid(row=1, column=0, padx=20, pady=10)

    to_option = ctk.CTkOptionMenu(numeralcalcwindow, values=["Decimal", "Binary", "Hexadecimal", "Roman"], width=150)
    to_option.grid(row=1, column=1, padx=20, pady=10)

    input_entry = ctk.CTkEntry(numeralcalcwindow, placeholder_text="Enter Number", width=150)
    input_entry.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    # Result label
    result_label = ctk.CTkLabel(numeralcalcwindow, text="Converted Value: ", text_color="black")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Convert Button
    convert_button = ctk.CTkButton(numeralcalcwindow, text="Convert", width=150, fg_color="#660066", 
                                    command=lambda: handle_conversion(input_entry.get(), from_option.get(), to_option.get(), result_label))
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    numeralcalcwindow.mainloop()
    
    
def binary_to_decimal(binary_value):
    return int(binary_value, 2)

def hexadecimal_to_decimal(hex_value):
    return int(hex_value, 16)

def roman_to_decimal(roman_value):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    prev_value = 0
    for symbol in reversed(roman_value):
        value = roman_dict[symbol]
        if value < prev_value:
            decimal_value -= value
        else:
            decimal_value += value
        prev_value = value
    return decimal_value

# Handle conversion based on the selected options
def handle_conversion(input_value, from_system, to_system, result_label):
    try:
        # Convert the input number based on the "from" system
        if from_system == "Decimal":
            decimal_value = int(input_value)
        elif from_system == "Binary":
            decimal_value = binary_to_decimal(input_value)
        elif from_system == "Hexadecimal":
            decimal_value = hexadecimal_to_decimal(input_value)
        elif from_system == "Roman":
            decimal_value = roman_to_decimal(input_value)
        else:
            result_label.configure(text="Invalid input system")
            return

        # Convert the decimal value to the target system
        if to_system == "Decimal":
            result = str(decimal_value)
        elif to_system == "Binary":
            result = decimal_to_binary(decimal_value)
        elif to_system == "Hexadecimal":
            result = decimal_to_hexadecimal(decimal_value)
        elif to_system == "Roman":
            result = decimal_to_roman(decimal_value)
        else:
            result_label.configure(text="Invalid output system")
            return

        result_label.configure(text=f"Converted Value: {result}")
    except ValueError:
        result_label.configure(text="Error: Invalid number")

def temprcalc():
    tempwindow = ctk.CTkToplevel(app)
    tempwindow.title("Temperature Calculator") 
    tempwindow.geometry("400x400")
    tempwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(tempwindow, text="TEMPERATURE CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    temp_option = ctk.CTkOptionMenu(tempwindow, values=["Celsius", "Fahrenheit", "Kelvin"], width=150)
    temp_option.grid(row=1, column=0, padx=20, pady=10)

    temp_entry = ctk.CTkEntry(tempwindow, placeholder_text="Enter Temperature", width=150)
    temp_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(tempwindow, text="Result: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Convert Button
    convert_button = ctk.CTkButton(tempwindow, text="Convert", width=150, fg_color="#660066", 
                                    command=lambda: handle_temperature_conversion(temp_entry.get(), temp_option.get(), result_label))
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    tempwindow.mainloop()
    
def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9/5) + 32

def celsius_to_kelvin(celsius_value):
    return celsius_value + 273.15

def fahrenheit_to_celsius(fahrenheit_value):
    return (fahrenheit_value - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit_value):
    return (fahrenheit_value - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin_value):
    return kelvin_value - 273.15

def kelvin_to_fahrenheit(kelvin_value):
    return (kelvin_value - 273.15) * 9/5 + 32

# Function to Handle Temperature Conversion
def handle_temperature_conversion(temp_value, selected_unit, result_label):
    try:
        temp_value = float(temp_value)  # Convert input to float

        if selected_unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result = f"{temp_value} Celsius = {fahrenheit:.2f} Fahrenheit = {kelvin:.2f} Kelvin"
        elif selected_unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result = f"{temp_value} Fahrenheit = {celsius:.2f} Celsius = {kelvin:.2f} Kelvin"
        elif selected_unit == "Kelvin":
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result = f"{temp_value} Kelvin = {celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit"
        else:
            result_label.configure(text="Invalid unit selected.")
            return
        
        result_label.configure(text=f"Result: {result}")
    except ValueError:
        result_label.configure(text="Error: Please enter a valid number")



def calculate_day_of_week(date_value, result_label):
    try:
        # Parse the date value entered by the user (format: YYYY-MM-DD)
        date_obj = datetime.datetime.strptime(date_value, "%Y-%m-%d")
        # Get the day of the week
        day_of_week = date_obj.strftime("%A")
        result_label.configure(text=f"Day of the Week: {day_of_week}")
    except ValueError:
        result_label.configure(text="Error: Invalid date format. Please use YYYY-MM-DD")

# Main Date Calculator window
def datecalc():
    datecalcwindow = ctk.CTkToplevel(app)
    datecalcwindow.title("Date Calculator") 
    datecalcwindow.geometry("400x400")
    datecalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(datecalcwindow, text="DATE CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    date_entry = ctk.CTkEntry(datecalcwindow, placeholder_text="Enter Date (YYYY-MM-DD)", width=150)
    date_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    result_label = ctk.CTkLabel(datecalcwindow, text="Day of the Week: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    calculate_button = ctk.CTkButton(datecalcwindow, text="Calculate Day", width=150, fg_color="#660066", 
                                    command=lambda: calculate_day_of_week(date_entry.get(), result_label))
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    datecalcwindow.mainloop()
    
# Function for Discount Calculator
def calculate_discount(original_price, discount_percentage, result_label):
    try:
        original_price = float(original_price)
        discount_percentage = float(discount_percentage)
        discount_amount = (original_price * discount_percentage) / 100
        discounted_price = original_price - discount_amount
        result_label.configure(text=f"Discounted Price: {discounted_price:.2f}")
    except ValueError:
        result_label.configure(text="Error: Please enter valid numbers")

# Main Discount Calculator window
def discountcalc():
    discountcalcwindow = ctk.CTkToplevel(app)
    discountcalcwindow.title("Discount Calculator") 
    discountcalcwindow.geometry("400x400")
    discountcalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(discountcalcwindow, text="DISCOUNT CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    price_entry = ctk.CTkEntry(discountcalcwindow, placeholder_text="Enter Original Price", width=150)
    price_entry.grid(row=1, column=0, padx=20, pady=10)

    discount_entry = ctk.CTkEntry(discountcalcwindow, placeholder_text="Enter Discount Percentage", width=150)
    discount_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(discountcalcwindow, text="Discounted Price: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    calculate_button = ctk.CTkButton(discountcalcwindow, text="Calculate Discount", width=150, fg_color="#660066", 
                                    command=lambda: calculate_discount(price_entry.get(), discount_entry.get(), result_label))
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    discountcalcwindow.mainloop()


# Conversion Functions for Mass
def convert_kg(mass_value):
    pounds = mass_value * 2.20462
    grams = mass_value * 1000
    return f"{mass_value} kg = {pounds:.2f} lbs = {grams:.2f} g"

def convert_pounds(mass_value):
    kg = mass_value / 2.20462
    grams = mass_value * 453.592
    return f"{mass_value} lbs = {kg:.2f} kg = {grams:.2f} g"

def convert_grams(mass_value):
    kg = mass_value / 1000
    pounds = mass_value / 453.592
    return f"{mass_value} g = {kg:.2f} kg = {pounds:.2f} lbs"

# Function to Handle Mass Conversion
def handle_mass_conversion(mass_value, selected_unit, result_label):
    try:
        mass_value = float(mass_value)
        if selected_unit == "Kilograms":
            result = convert_kg(mass_value)
        elif selected_unit == "Pounds":
            result = convert_pounds(mass_value)
        elif selected_unit == "Grams":
            result = convert_grams(mass_value)
        else:
            result = "Invalid unit selected."
        result_label.configure(text=f"Converted Mass: {result}")
    except ValueError:
        result_label.configure(text="Error: Please enter a valid number")

# Main Mass Converter window
def masscalc():
    masscalcwindow = ctk.CTkToplevel(app)
    masscalcwindow.title("Mass Calculator") 
    masscalcwindow.geometry("400x400")
    masscalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(masscalcwindow, text="MASS CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    mass_option = ctk.CTkOptionMenu(masscalcwindow, values=["Kilograms", "Pounds", "Grams"], width=150)
    mass_option.grid(row=1, column=0, padx=20, pady=10)

    mass_entry = ctk.CTkEntry(masscalcwindow, placeholder_text="Enter Mass", width=150)
    mass_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(masscalcwindow, text="Converted Mass: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = ctk.CTkButton(masscalcwindow, text="Convert", width=150, fg_color="#660066", 
                                    command=lambda: handle_mass_conversion(mass_entry.get(), mass_option.get(), result_label))
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    masscalcwindow.mainloop()


# Conversion Functions for Speed
def convert_mps(speed_value):
    kmph = speed_value * 3.6
    mph = speed_value * 2.23694
    return f"{speed_value} m/s = {kmph:.2f} km/h = {mph:.2f} mph"

def convert_kmph(speed_value):
    mps = speed_value / 3.6
    mph = speed_value / 1.60934
    return f"{speed_value} km/h = {mps:.2f} m/s = {mph:.2f} mph"

def convert_mph(speed_value):
    mps = speed_value / 2.23694
    kmph = speed_value * 1.60934
    return f"{speed_value} mph = {mps:.2f} m/s = {kmph:.2f} km/h"

# Function to Handle Speed Conversion
def handle_speed_conversion(speed_value, selected_unit, result_label):
    try:
        speed_value = float(speed_value)
        if selected_unit == "m/s":
            result = convert_mps(speed_value)
        elif selected_unit == "km/h":
            result = convert_kmph(speed_value)
        elif selected_unit == "mph":
            result = convert_mph(speed_value)
        else:
            result = "Invalid unit selected."
        result_label.configure(text=f"Converted Speed: {result}")
    except ValueError:
        result_label.configure(text="Error: Please enter a valid number")

# Main Speed Converter window
def speedcalc():
    speedcalcwindow = ctk.CTkToplevel(app)
    speedcalcwindow.title("Speed Calculator") 
    speedcalcwindow.geometry("400x400")
    speedcalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(speedcalcwindow, text="SPEED CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    speed_option = ctk.CTkOptionMenu(speedcalcwindow, values=["m/s", "km/h", "mph"], width=150)
    speed_option.grid(row=1, column=0, padx=20, pady=10)

    speed_entry = ctk.CTkEntry(speedcalcwindow, placeholder_text="Enter Speed", width=150)
    speed_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(speedcalcwindow, text="Converted Speed: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = ctk.CTkButton(speedcalcwindow, text="Convert", width=150, fg_color="#660066", 
                                    command=lambda: handle_speed_conversion(speed_entry.get(), speed_option.get(), result_label))
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    speedcalcwindow.mainloop()


# Conversion Functions for Volume
def convert_cubic_meters(volume_value):
    liters = volume_value * 1000
    cubic_feet = volume_value * 35.3147
    return f"{volume_value} m³ = {liters:.2f} L = {cubic_feet:.2f} ft³"

def convert_liters(volume_value):
    cubic_meters = volume_value / 1000
    cubic_feet = volume_value / 28.3168
    return f"{volume_value} L = {cubic_meters:.2f} m³ = {cubic_feet:.2f} ft³"

def convert_cubic_feet(volume_value):
    cubic_meters = volume_value / 35.3147
    liters = volume_value * 28.3168
    return f"{volume_value} ft³ = {cubic_meters:.2f} m³ = {liters:.2f} L"

# Function to Handle Volume Conversion
def handle_volume_conversion(volume_value, selected_unit, result_label):
    try:
        volume_value = float(volume_value)
        if selected_unit == "Cubic Meters":
            result = convert_cubic_meters(volume_value)
        elif selected_unit == "Liters":
            result = convert_liters(volume_value)
        elif selected_unit == "Cubic Feet":
            result = convert_cubic_feet(volume_value)
        else:
            result = "Invalid unit selected."
        result_label.configure(text=f"Converted Volume: {result}")
    except ValueError:
        result_label.configure(text="Error: Please enter a valid number")

# Main Volume Converter window
def volumecalc():
    volumecalcwindow = ctk.CTkToplevel(app)
    volumecalcwindow.title("Volume Calculator") 
    volumecalcwindow.geometry("400x400")
    volumecalcwindow.resizable(False, False)

    headlabel = ctk.CTkLabel(volumecalcwindow, text="VOLUME CALCULATOR", fg_color="#660066", text_color="white")
    headlabel.grid(row=0, column=0, columnspan=2, pady=10)

    volume_option = ctk.CTkOptionMenu(volumecalcwindow, values=["Cubic Meters", "Liters", "Cubic Feet"], width=150)
    volume_option.grid(row=1, column=0, padx=20, pady=10)

    volume_entry = ctk.CTkEntry(volumecalcwindow, placeholder_text="Enter Volume", width=150)
    volume_entry.grid(row=1, column=1, padx=20, pady=10)

    result_label = ctk.CTkLabel(volumecalcwindow, text="Converted Volume: ", text_color="black")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = ctk.CTkButton(volumecalcwindow, text="Convert", width=150, fg_color="#660066", 
                                    command=lambda: handle_volume_conversion(volume_entry.get(), volume_option.get(), result_label))
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    volumecalcwindow.mainloop()


    
if __name__=="__main__":
    app=App()
    app.mainloop()
