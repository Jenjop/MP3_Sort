Run MusicScriptPublic.py

- Automatically runs the rest
- I may update and simplify the process given time

Explanation:
MusicScriptPublic sorts mp3 files based on user classification
If song contains lyrics, Lyrics category may be used
	Songs with lyrics will be prompted to input name of song and url to lyrics
	Python Files are then run to create a HTML file containing alphabetically sorted links
		Process:
		Text file with a song name and url on each line
		Copied over to a temporary text file
		Songs sorted alphabetically and output to new text file
		Excel sheet created with cells for songs and urls based on sorted text file
		HTML of links created using Excel sheet
All Created Files will begin with "_"