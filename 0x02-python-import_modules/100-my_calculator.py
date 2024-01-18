#!/usr/bin/python3
import sys
import calculator_1 as calc_module


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <num1> <operator> <num2>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    operator_symbol = sys.argv[2]
    num2 = int(sys.argv[3])

    if operator_symbol == "+":
        result_value = calc_module.add(num1, num2)
    elif operator_symbol == "-":
        result_value = calc_module.sub(num1, num2)
    elif operator_symbol == "*":
        result_value = calc_module.mul(num1, num2)
    elif operator_symbol == "/":
        result_value = calc_module.div(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(num1, operator_symbol, num2, result_value))


if __name__ == "__main__":
    main()