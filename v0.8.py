from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            op = request.form.get("operation")

            if op == "add":
                result = f"Result: {num1 + num2}"
            elif op == "sub":
                result = f"Result: {num1 - num2}"
            elif op == "mul":
                result = f"Result: {num1 * num2}"
            elif op == "div":
                result = (
                    "Error: Division by zero" if num2 == 0 else f"Result: {num1 / num2}"
                )

        except:
            result = "Invalid input"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Calculator v0.8</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                background: #121212;
                color: white;
            }}
            .container {{
                margin-top: 50px;
            }}
            input, button {{
                padding: 10px;
                margin: 5px;
                font-size: 16px;
            }}
            .add {{ background: green; }}
            .sub {{ background: red; }}
            .mul {{ background: orange; }}
            .div {{ background: blue; }}
            button {{
                color: white;
                border: none;
                cursor: pointer;
            }}
            .result {{
                margin-top: 20px;
                font-size: 22px;
                color: cyan;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Python Web Calculator</h1>

            <form method="POST">
                <input type="number" step="any" name="num1" required>
                <input type="number" step="any" name="num2" required>
                <br>

                <button name="operation" value="add" class="add">Add</button>
                <button name="operation" value="sub" class="sub">Subtract</button>
                <button name="operation" value="mul" class="mul">Multiply</button>
                <button name="operation" value="div" class="div">Divide</button>
            </form>

            <div class="result">{result}</div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
