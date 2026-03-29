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
                result = num1 + num2
            elif op == "sub":
                result = num1 - num2
            elif op == "mul":
                result = num1 * num2
            elif op == "div":
                result = "Error" if num2 == 0 else num1 / num2

        except:
            result = "Invalid Input"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Calculator v0.9</title>
        <style>
            body {{
                background: #0f172a;
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
            }}

            .box {{
                width: 320px;
                padding: 20px;
                background: #1e293b;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.5);
                text-align: center;
            }}

            h2 {{
                margin-bottom: 15px;
            }}

            input {{
                width: 90%;
                padding: 10px;
                margin: 8px 0;
                border: none;
                border-radius: 5px;
            }}

            .btns button {{
                width: 70px;
                padding: 10px;
                margin: 5px;
                border: none;
                border-radius: 5px;
                color: white;
                cursor: pointer;
            }}

            .add {{ background: #22c55e; }}
            .sub {{ background: #ef4444; }}
            .mul {{ background: #f59e0b; }}
            .div {{ background: #3b82f6; }}

            .result {{
                margin-top: 15px;
                font-size: 20px;
                color: cyan;
            }}
        </style>
    </head>

    <body>
        <div class="box">
            <h2>Calculator</h2>

            <form method="POST">
                <input type="number" step="any" name="num1" placeholder="First number" required>
                <input type="number" step="any" name="num2" placeholder="Second number" required>

                <div class="btns">
                    <button name="operation" value="add" class="add">+</button>
                    <button name="operation" value="sub" class="sub">-</button>
                    <button name="operation" value="mul" class="mul">×</button>
                    <button name="operation" value="div" class="div">÷</button>
                </div>
            </form>

            <div class="result">{result}</div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
