from fastapi import FastAPI

app = FastAPI()
@app.get("/{num1}/{op}/{num2}/")
def calc(num1: int, op: str, num2: int):
    """Возможные операции:
    * сложение +
    * вычитание -
    * умножение *
    * возведение в степень ^
    * деление :"""
    if op == '+':
        return {num1 + num2}
    elif op == '-':
        return {num1 - num2}
    elif op == '*':
        return {num1 * num2}
    elif op == '^':
        return {num1 ** num2}
    elif (op == ':') and (num2 != 0):
        return {num1 / num2}
    elif (op == ':') and (num2 == 0):
        return {"Извините, но на 0 делить нельзя ;)"}