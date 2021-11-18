
def write_to_file(file_path, lines):
    with open(file_path, 'w+') as f:
        for line in lines:
            f.write(f"{line}")


if __name__ == "__main__":
    print("Test write")
    write_file("test.txt", [[1,2,3],[4,5,6]])

