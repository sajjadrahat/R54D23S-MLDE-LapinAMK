celeb_list = ['DiCaprio', 'Johansson', 'Pitt', 'Streep', 'Smith', 'Lawrence', 'Clooney', 'Winslet', 'Damon', 'Roberts']
new_celeb_list = []

for celeb in celeb_list:
    flag = False
    # Making all lower chracters in celeb name
    celeb_lower = celeb.lower()
    # Making a list of chracters in a celeb name
    celeb_name_letters = [ letters for letters in celeb]
    if "s" not in celeb_name_letters:
        if "e" not in celeb_name_letters:
            if len(celeb_name_letters)<=8:
                # First using lambda, map function to get True, False result in a list
                # Using Sum to count the True in function
                vowel_count = sum(list(map(lambda x: x in "aeiou", celeb_name_letters)))
                if vowel_count <=2:
                    flag= True
    
    if flag:
        new_celeb_list.append(celeb)

# Printin in one line using a comma seperator and astersisk for unpacking the data
print(*new_celeb_list, sep=', ')