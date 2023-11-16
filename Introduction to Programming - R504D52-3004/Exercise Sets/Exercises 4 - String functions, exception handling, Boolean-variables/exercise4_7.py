#writing 2 function for Word to Number and Number to Words
def num_to_words(user_input, nums_words):
    user_input = str(user_input)
    output = [nums_words[d] for d in user_input]
    print(" ".join(output))

def words_to_num(user_input, words_nums):
    user_input = user_input.split(" ")
    output = [words_nums[d] for d in user_input]
    print("".join(output))

user_input = input("Enter a number or words to convert: \n")

nums_words={'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
words_nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if user_input.isdigit() and len(user_input) <= 5:
    num_to_words (user_input, nums_words)
else:
    try:
        words_to_num(user_input, words_nums)
    except:
        print("Invalid input")