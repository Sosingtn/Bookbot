def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents    
   

def count_words(content):
    counted_words = len(content.split())
    return f"{counted_words} words found in the document"




def main():
    print(count_words(get_book_text("books/frankenstein.txt")))



main()
