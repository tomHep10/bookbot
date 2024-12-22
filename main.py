def main():
  path = 'books/frankenstein.txt'

  with open(path , 'r') as f:
    file_contents = full_text(path)
    word_count = count_words(file_contents)
    dup_chars = char_duplicates(file_contents)
    report(word_count, dup_chars, path)

# Returns the contents of the file
def full_text(path):
  with open(path) as f:
      return f.read()

# Finds number of words
def count_words(file_contents):
  words = file_contents.split()
  return len(words)

# Counts number of duplicate/matching characters
def char_duplicates(file_contents):
  file_contents = file_contents.lower()
  count = {}
  for c in file_contents:
    if c not in count:
      count[c] = 1
    else:
      count[c] += 1
  return count

# Creates report by cleaning up the dictionary and sorting it by value
def report(word_count, dup_chars, path):
  dup_chars = {c: count for c, count in dup_chars.items() if c.isalpha()} # Makes dictionary only hold alpha char
  dup_chars = dict(sorted(dup_chars.items(), reverse=True, key=lambda item: item[1])) # Sorts dictionary by values from most->least

  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document\n")
  for c in dup_chars:
    print(f"The {c} character was found {dup_chars[c]} times")

  print("--- End report ---")

if __name__ == '__main__':
  main()
