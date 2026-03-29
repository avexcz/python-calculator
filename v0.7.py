from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import font
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator v0.6")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        # Variables
        self.current_expression = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")

        # Create UI
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#1e1e1e", pady=20, padx=20)
        display_frame.pack(fill=tk.BOTH, expand=False)

        # Display
        display = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            font=("Arial", 32, "bold"),
            background="#090909",
            fg="#ffffff",
            bd=0,
            justify=tk.RIGHT,
            state="readonly",
        )
        display.pack(fill=tk.BOTH, padx=20, pady=10, ipady=20)

    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Button layout
        buttons = [
            ["C", "⌫", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
            ["sin", "cos", "tan", "^"],
            ["(", ")", "!", "log"],
        ]

        # Button styling
        button_font = font.Font(family="Arial", size=18, weight="bold")

        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                # Determine button color
                if button_text in ["C", "⌫"]:
                    bg_color = "red"
                    fg_color = "#000000"
                elif button_text == "=":
                    bg_color = "#4ecdc4"
                    fg_color = "#1e1e1e"
                elif button_text in ["/", "*", "-", "+", "^"]:
                    bg_color = "#ff9f43"
                    fg_color = "#1e1e1e"
                elif button_text in ["√", "sin", "cos", "tan", "!", "log", "(", ")"]:
                    bg_color = "#5f27cd"
                    fg_color = "#1e1e1e"
                else:
                    bg_color = "#ffffff"
                    fg_color = "#1e1e1e"

                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=button_font,
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=bg_color,
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    command=lambda x=button_text: self.on_button_click(x),
                )
                btn.grid(
                    row=row_idx,
                    column=col_idx,
                    sticky="nsew",
                    padx=3,
                    pady=3,
                )

        # Configure grid weights for responsive layout
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):

        try:
            if char == "C":
                self.clear()
            elif char == "⌫":
                self.backspace()
            elif char == "=":
                self.calculate()
            elif char == "±":
                self.toggle_sign()
            elif char == "√":
                self.square_root()
            elif char == "sin":
                self.trigonometric("sin")
            elif char == "cos":
                self.trigonometric("cos")
            elif char == "tan":
                self.trigonometric("tan")
            elif char == "!":
                self.factorial()
            elif char == "log":
                self.logarithm()
            elif char == "^":
                self.append_to_expression("**")
            else:
                self.append_to_expression(char)
        except Exception as e:
            self.display_text.set("Error")
            self.current_expression = ""

    def append_to_expression(self, char):
        """Append character to expression"""
        if self.display_text.get() == "0" or self.display_text.get() == "Error":
            self.current_expression = char
        else:
            self.current_expression += char
        self.display_text.set(self.current_expression)

    def clear(self):
        """Clear the display"""
        self.current_expression = ""
        self.display_text.set("0")

    def backspace(self):
        """Remove last character"""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            if self.current_expression:
                self.display_text.set(self.current_expression)
            else:
                self.display_text.set("0")

    def calculate(self):
        """Evaluate the expression"""
        try:
            if self.current_expression:
                # Replace visual symbols with Python operators
                expression = self.current_expression.replace("×", "*").replace("÷", "/")
                result = eval(expression)

                # Format result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 10)

                self.display_text.set(str(result))
                self.current_expression = str(result)
        except ZeroDivisionError:
            self.display_text.set("Cannot divide by 0")
            self.current_expression = ""
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""

    def toggle_sign(self):
        """Toggle positive/negative sign"""
        try:
            if self.current_expression and self.current_expression != "0":
                if self.current_expression.startswith("-"):
                    self.current_expression = self.current_expression[1:]
                else:
                    self.current_expression = "-" + self.current_expression
                self.display_text.set(self.current_expression)
        except Exception:
            self.display_text.set("Error")

    def square_root(self):
        """Calculate square root"""
        try:
            if self.current_expression:
                value = float(eval(self.current_expression))
                if value < 0:
                    self.display_text.set("Error: Negative")
                    self.current_expression = ""
                else:
                    result = math.sqrt(value)
                    if result.is_integer():
                        result = int(result)
                    self.display_text.set(str(result))
                    self.current_expression = str(result)
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""

    def trigonometric(self, func):
        """Calculate trigonometric functions (in degrees)"""
        try:
            if self.current_expression:
                value = float(eval(self.current_expression))
                angle_rad = math.radians(value)

                if func == "sin":
                    result = math.sin(angle_rad)
                elif func == "cos":
                    result = math.cos(angle_rad)
                elif func == "tan":
                    result = math.tan(angle_rad)

                result = round(result, 10)
                self.display_text.set(str(result))
                self.current_expression = str(result)
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""

    def factorial(self):
        """Calculate factorial"""
        try:
            if self.current_expression:
                value = int(eval(self.current_expression))
                if value < 0:
                    self.display_text.set("Error: Negative")
                    self.current_expression = ""
                else:
                    result = math.factorial(value)
                    self.display_text.set(str(result))
                    self.current_expression = str(result)
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""

    def logarithm(self):
        """Calculate natural logarithm"""
        try:
            if self.current_expression:
                value = float(eval(self.current_expression))
                if value <= 0:
                    self.display_text.set("Error: Non-positive")
                    self.current_expression = ""
                else:
                    result = math.log(value)
                    result = round(result, 10)
                    self.display_text.set(str(result))
                    self.current_expression = str(result)
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
