import hashlib
import string
import bcrypt

challenge_words: list[str] = []
with open('./ctfchallenge.txt', 'r') as challenge_file:
    for each_word in challenge_file:
        challenge_words.append(each_word)


x = string.ascii_lowercase + string.ascii_uppercase + ' ' + string.punctuation
encoded_letters = {}

for each_letter in x:
    encoded_letter = hashlib.sha256(bytes(each_letter, 'utf-8')).hexdigest()
    encoded_letters[encoded_letter] = each_letter

key = ''
for each_entry in challenge_words:
    if each_entry.strip() in encoded_letters.keys():
        key += encoded_letters[each_entry.strip()]
print(key)

pass_ = input('enter password:\t')

salted_pass = hashlib.sha256(bytes(pass_ + str(bcrypt.gensalt()))).hexdigest()
