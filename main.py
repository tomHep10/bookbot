path = 'books/frankenstein.txt'

def main():
  with open(path , 'r') as f:
    file_contents = full_text(path)
    word_count = count_words(file_contents)
    print(word_count)

def full_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_contents):
  with open(path) as f:
    words = file_contents.split()
    print(len(words))

if __name__ == '__main__':
  main()
