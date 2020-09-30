formatter = "{} {} {} {}"
#calls the format function:  displays the string on the console.
print(formatter.format(1, 2, 3, 4))
#calls the format funtion:  displays the string to the console.
print(formatter.format("one", "two", "three", "four"))
#calls the format function displays the contents of the function to the console.
print(formatter.format(True, False, False, True))
#calls the format function and concatenates the string assigned to the variable formatter on one line and displays on the console.
print(formatter.format(formatter, formatter, formatter, formatter))
#calls the format function and displays the string on one line and prints to the console.
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
	))
