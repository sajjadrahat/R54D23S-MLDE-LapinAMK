import random
def random_proverb_generator():
    print("Today's proverb:")
    with open('wisewords.txt', 'r') as file:
        # Proverb in a list
        proverb_contents= file.readlines()

        # Max number of lines to generate random nums
        max_lines_index = len(proverb_contents)-1
        random_num = random.randint(0,max_lines_index)
        print(proverb_contents[random_num])


random_proverb_generator()