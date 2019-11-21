import utils

def run(string, entities):
	"""Leon tells you about other personal assistants"""

	string = string.lower()

	assistants = [
		'friends',
		'sister',
		'girlfriend',
		'office'
	]

	for assistant in assistants:
		if string.find(assistant) != -1:
			return utils.output('end', 'success', utils.translate(assistant.replace(' ', '_')))

	return utils.output('end', 'unknown', utils.translate('unknown'))
