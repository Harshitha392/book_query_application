# refer : https://www.youtube.com/watch?v=_PRxiZk1ZJY

book_name = input()
query_book = book_name.lower()
query_book= query_book.replace(' ','+')

import requests
resp = requests.get(f"http://openlibrary.org/search.json?title={query_book}")
info = resp.json()
author_name=info['docs'][0]['author_name'][0]
publishing_year=info['docs'][0]['first_publish_year']

print(f"author of {book_name} is {author_name}. It was first published in the year {publishing_year}")

def get_subject(book_name):
  query_book = book_name.lower()
  query_book= query_book.replace(' ','+')
  resp = requests.get(f"http://openlibrary.org/search.json?title={query_book}")
  info = resp.json()
  subject=info['docs'][0]['subject']
  return subject

book1 = input()
book2 = input()

subj1 = get_subject(book1)
subj2 = get_subject(book2)

s1 = set(subj1)
s2 = set(subj2)

common = s1&s2
common = list(common)
common.sort()
print("common subjects are:",end= ' ')
for subject in common:
  print(subject,end=' ')

print()