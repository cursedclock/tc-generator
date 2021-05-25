from subprocess import Popen, PIPE
from config import number_of_testcases, path_to_solution, generate_input


for i in range(1, number_of_testcases+1):
    name = str(i)+".txt"

    # generate input string
    inp_str = generate_input()
    # write input to file
    inp_file = open("in/input"+name, "w+")
    inp_file.write(inp_str)
    inp_file.close()

    # generate output string
    p = Popen([path_to_solution], stdout=PIPE, stdin=PIPE)
    p.stdin.write(bytes(inp_str, 'UTF-8'))
    p.stdin.flush()
    out_str = p.communicate()[0].decode("utf-8").replace("\r\n", "\n")
    # write output to file
    out_file = open("out/output"+name, "w+")
    out_file.write(out_str)
    out_file.close()
