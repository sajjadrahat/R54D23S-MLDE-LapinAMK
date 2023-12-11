import functions
filename = 'artists.txt'

file_content_list = functions.read_file_contents(filename)

for lines in file_content_list:
    print(f"-> {lines}")
