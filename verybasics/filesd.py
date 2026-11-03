def read_file(filename):
    with open(filename, "r") as f:
        print(f.read())

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

read_file("sample.txt")
