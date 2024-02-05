#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)

if __name__ == "__main__":
    try:
        raise_exception_msg("An error occurred")
    except NameError as e:
        print(e)
