import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['C:\Project\Gen-AI\Dev\Ollama2\img\Sunrise_with_foreground_buildings.jpg']
		}
	]
)

print(res['message']['content'])
