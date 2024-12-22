path = 'books/frankenstein.txt'

def main():
  with open(path , 'r') as f:
    file_contents = full_text(path)
    word_count = count_words(file_contents)
    dup_chars = char_duplicates(file_contents)

def full_text(path):
  with open(path) as f:
      return f.read()

def count_words(file_contents):
  words = file_contents.split()
  print(len(words))

def char_duplicates(file_contents):
  file_contents = file_contents.lower()
  count = {}
  for c in file_contents:
    if c not in count:
      count[c] = 1
    else:
      count[c] += 1
  return count

if __name__ == '__main__':
  main()
