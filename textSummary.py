import ollama

f = open("maths_learning.txt", "r", encoding="utf-8")
text = f.read()

messages = [
    {
        "role": "user",
        "content": "I'm going to upload some text. Give me a summary of the text, including the main points, something surprising about the text and potential applications to everyday life based on the main points"
    }
]
response = ollama.chat(model="llama3.2", messages = [
    {
        "role": "user",
        "content": "I'm going to upload some text. Give me a summary of the text, including the main points, something surprising about the text and potential applications to everyday life based on the main points"
    },
    {
        "role": "user",
        "content": text
    }
])
print(response['message']['content'])