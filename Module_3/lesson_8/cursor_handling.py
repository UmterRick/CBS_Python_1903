import io


def check_cursor_position():
    with open("example.txt", 'r') as file:
        current_cursor_position = file.tell()
        print(f"Current position at : {current_cursor_position}")
        line = file.readline()
        print(line)
        current_cursor_position = file.tell()
        print(f"Current position at : {current_cursor_position}")
        line = file.readline()
        print(line)
        current_cursor_position = file.tell()
        print(f"Current position at : {current_cursor_position}")
        line = file.readline()
        print(line)


# for i in range(10):
#     with open(f"example_{i}.txt", 'r') as f:
#         print(f)


with open("example.txt", "rb") as f:
    f.seek(2)
    line = f.read(10)
    print(line)
    # f.seek(20)
    line = f.read(10)
    print(line)

    print("------------")
    print(f.tell())
    f.seek(4, io.SEEK_CUR)  # f.seek(curr_pos + 4) only in binary mode
    print(f.tell())

    f.seek(0, io.SEEK_END)
    print(f.tell())

