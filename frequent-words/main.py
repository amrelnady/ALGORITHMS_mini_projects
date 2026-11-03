from collections import Counter

# Get text from user
text = input("Enter your text: ")

# Get K value
k = int(input("Enter K: "))

# Convert text to lowercase
text = text.lower()

# Split text into words
words = text.split()

# Count word frequency
word_count = Counter(words)

# Get the K most frequent words
top_words = word_count.most_common(k)

# Display results
print("\nTop", k, "Frequent Words:")

for word, count in top_words:
    print(word, ":", count)