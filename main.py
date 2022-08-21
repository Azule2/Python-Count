count = int(input('Pls Enter your number: '))

if count == count:
	print('Your Count Running ')
	if count <= 10:
		print('your count is small',range(count))

	elif count <= 100:
		print('Your count is Mediam', range(count))

	elif count <= 10000:
		print('Your count is Large', range(count))

	elif count > 10000:
		print('Your count is Larger', range(count))
	else:
		print('Not Found')
else:
	print('sorry you can\'t use symbole and string ')
