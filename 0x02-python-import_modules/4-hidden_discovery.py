#!/usr/bin/python3
import hidden_4 as h4_module

if __name__ == "__main__":
    defined_names = dir(h4_module)
    for single_name in sorted(defined_names):
        if not single_name.startswith('__'):
            print(single_name)
