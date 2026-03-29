from flask import Flask, request
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    display = ""
    result = ""

    if request.method == "POST":
        display = request.form.get("display", "")
        btn = request.form.get("btn")

        try:
            if btn in "0123456789.+-*/":
                display += btn

            elif btn == "C":
                display = ""

            elif btn == "=":
                # SAFE EVALUATION
                result = eval(display, {"__builtins__": None}, {})
                display = str(result)

            # Scientific functions
            elif btn == "sin":
                result = math.sin(math.radians(float(display)))
                display = str(result)

            elif btn == "cos":
                result = math.cos(math.radians(float(display)))
                display = str(result)

            elif btn == "tan":
                result = math.tan(math.radians(float(display)))
                display = str(result)

            elif btn == "log":
                result = math.log10(float(display))
                display = str(result)

            elif btn == "ln":
                result = math.log(float(display))
                display = str(result)

            elif btn == "sqrt":
                result = math.sqrt(float(display))
                display = str(result)

        except:
            display = ""
            result = "Error"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Scientific Calculator</title>
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
                text-align: center;
            }}

            input {{
                width: 90%;
                padding: 10px;
                margin-bottom: 10px;
                font-size: 18px;
                text-align: right;
                border-radius: 5px;
                border: none;
            }}

            .btns button {{
                width: 60px;
                height: 40px;
                margin: 3px;
                border: none;
                border-radius: 5px;
                color: white;
                cursor: pointer;
            }}

            .result {{
                margin-top: 20px;
                font-size: 22px;
                color: cyan;
            }}
            
            .num {{ background: #334155; }}
            .op {{ background: #f59e0b; }}
            .eq {{ background: #22c55e; }}
            .func {{ background: #3b82f6; }}
            .clear {{ background: #ef4444; }}

        </style>
    </head>

    <body>
        <div class="box">
            <h2>Scientific Calculator</h2>

            <form method="POST">
                <input type="text" name="display" value="{display}" readonly>

                <div class="btns">

                    <!-- Numbers -->
                    <button name="btn" value="7" class="num">7</button>
                    <button name="btn" value="8" class="num">8</button>
                    <button name="btn" value="9" class="num">9</button>
                    <button name="btn" value="/" class="op">/</button>

                    <button name="btn" value="4" class="num">4</button>
                    <button name="btn" value="5" class="num">5</button>
                    <button name="btn" value="6" class="num">6</button>
                    <button name="btn" value="*" class="op">*</button>

                    <button name="btn" value="1" class="num">1</button>
                    <button name="btn" value="2" class="num">2</button>
                    <button name="btn" value="3" class="num">3</button>
                    <button name="btn" value="-" class="op">-</button>

                    <button name="btn" value="0" class="num">0</button>
                    <button name="btn" value="." class="num">.</button>
                    <button name="btn" value="=" class="eq">=</button>
                    <button name="btn" value="+" class="op">+</button>

                    <!-- Scientific -->
                    <button name="btn" value="sin" class="func">sin</button>
                    <button name="btn" value="cos" class="func">cos</button>
                    <button name="btn" value="tan" class="func">tan</button>

                    <button name="btn" value="log" class="func">log</button>
                    <button name="btn" value="ln" class="func">ln</button>
                    <button name="btn" value="sqrt" class="func">√</button>

                    <button name="btn" value="C" class="clear">C</button>
                </div>
            </form>

            <div class="result">{result}</div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
