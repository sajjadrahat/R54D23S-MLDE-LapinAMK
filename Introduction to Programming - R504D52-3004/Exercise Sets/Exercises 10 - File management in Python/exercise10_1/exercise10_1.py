def read_file_contents(filename):
    with open(filename, "r") as file_handle:
            content_str = file_handle.read()
            content_list = content_str.split("\n")
            return content_list

filename = 'artists.txt'

file_content_list = read_file_contents(filename)

for lines in file_content_list:
    print(f"-> {lines}")
