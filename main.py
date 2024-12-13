def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_book_characters(text)
    characters_list = [{'char': k, 'count': v} for k, v in characters.items()]
    characters_list.sort(reverse=True, key=lambda x: x["count"])
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for char in characters_list:
        print(f"The {char['char']} character was found {char['count']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            low_char = char.lower()
            if low_char not in char_count:
                char_count[low_char] = 1
            else: 
                char_count[low_char] += 1
    return char_count

main()
