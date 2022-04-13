
FL = open("data.txt", "rb")         #  rb  - read and binary

fl_pos = FL.seek(100, 0)

print(fl_pos)

fl_pos = FL.seek(50, 1)

print(fl_pos)

# FL.seek(-50, 0)
fl_pos = FL.seek(0, 2)

print(fl_pos)

FL.close()
