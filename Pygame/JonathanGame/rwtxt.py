text_lines = [
    "Chapter 3\n",
    "Sample text data file\n",
    "This is the third line of text\n",
    "The fourth line looks like this\n",
    "Edit the file with any text editor\n"]

with open("data1.txt", "w") as file:
    file.writelines(text_lines)

with open("data1.txt", "r") as file:
    # all_data = file.read()
    # print(all_data)
    all_data = file.readlines()
    print("Lines: ", len(all_data))
    for line in all_data:
        print(line)
