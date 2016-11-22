# PURPOSE: Download repository of animal sounds in different languages (MP3 files) from ESL-Languages Website. 
# REFERENCE: https://www.esl-languages.com/en/study-abroad/coffee-time/animal-sounds/index.htm

import urllib

# Base URL for Animal Sound MP3's (determined via network calls)
base_url = 'https://www.esl-languages.com/assets/data/animal-sounds'

# Define List of Animals
animals = [
	'cockerel',
	'cat',
	'dog',
	'bee',
	'donkey',
	'pig',
	'cow',
	'owl',
	'bird'
]

# Define List of Languages
languages = [
	'arabic',
	'german',
	'english',
	'syrian',
	'japanese',
	'belgian',
	'spanish_basque',
	'taiwanese',
	'korean'
]

# Loop through Animals & Languages...
for animal in animals:
	for language in languages:

		# Create MP3 Filename
		filename = animal + '_' + language + '.mp3'

		# Create URL
		url = base_url + '/' + filename

		# Create Download Path
		path = 'downloads' + '/' + filename
		print 'Downloading: ' + url + '...'

		# Copy File from URL to Download Path
		urllib.urlretrieve(url, path)