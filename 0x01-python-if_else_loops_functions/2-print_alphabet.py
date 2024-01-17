#!/usr/bin/python3
print("".join(chr(b) for b in range(ord('a'), ord('z') + 1) if chr(b) != 'e' and chr(b) != 'q'))