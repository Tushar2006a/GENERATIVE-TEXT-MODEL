from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

print("=== Generative Text Model ===")
print("Type a prompt and get generated text.")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("Enter your prompt: ")

    if prompt.lower() == "exit":
        print("Program stopped.")
        break

    result = generator(
        prompt,
        max_length=120,
        do_sample=True
    )

    print("\nGenerated Text:\n")
    print(result[0]["generated_text"])
    print("\n" + "-" * 50 + "\n")
