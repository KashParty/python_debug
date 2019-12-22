import sys


def test_function(a, b):
    x = a + b
    x -= 1
    y = x * 2
    y += a * b


def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "test_function":
        return trace_lines
    return


def trace_lines(frame, event, arg):
    with open("output.txt", "a") as f:
        f.write(f"[{frame.f_lineno}, {frame.f_locals}]\n")


open("output.txt", "w").close() #clear file contents
sys.settrace(trace_calls)
test_function(2, 3)

with open("output.txt", "r") as f:
    log = f.read().splitlines()

for i, line in enumerate(log):
    log[i] = eval(line)

for i in range(0, len(log)):
    for var in log[i][1].keys():
        if i == 0 or var not in log[i - 1][1].keys():
            print(f"Line {log[i][0] - 1}: New variable {var} = {log[i][1][var]}")
        elif log[i][1][var] != log[i - 1][1][var]:
            print(f"Line {log[i][0]}: Variable {var} changed from {log[i - 1][1][var]} to {log[i][1][var]}")
