from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

# Make a simple API call
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Hello! What is AI?"}
]
)

# Print the response
print(completion.choices[0].message.content)