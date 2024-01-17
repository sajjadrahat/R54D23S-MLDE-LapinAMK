user_input= input("Give a word: \n")
chr_place_shift = int(input("Give a number to shift the alphabets: \n"))
new_word=""

for chracters in user_input:
    # Getting the ord of old charcter using ord() function
    # Adding Charcater shift number with the old chracter ord.
    # Generate new chracter from that using chr() function
    new_chracter = chr(ord(chracters)+chr_place_shift)
    # Concating new charcters everytime
    new_word+=new_chracter

print(f"New Word: {new_word}")