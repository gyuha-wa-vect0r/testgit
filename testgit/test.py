def add(x, y):
    """두 숫자의 합을 계산합니다."""
    return x + y

def subtract(x, y):
    """두 숫자의 차를 계산합니다."""
    return x - y

def multiply(x, y):
    """두 숫자의 곱을 계산합니다."""
    return x * y

def divide(x, y):
    """두 숫자의 나눗셈을 계산합니다. (0으로 나누는 경우는 처리하지 않습니다.)"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y


