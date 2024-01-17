celeb = "Dicaprio"

count= sum(list(map(lambda x: x in "aiou", celeb)))
print(count)