import requests
import random

url = 'http://api.quotable.io'


def get_quote(tags=None):
    if tags == None:
        r = requests.get(url + '/random')
    else:
        r = requests.get(url + f'/random?tags={tags}')
    return r.json()


def find_author(slug):
    r = requests.get(url + f'/search/authors?query={slug}')
    return r.json()


def question(tags=None):
    quote = get_quote(tags)
    authors = [quote['author']]
    for i in range(3):
        authors.append(get_quote(tags)['author'])
    random.shuffle(authors)
    print(quote['content'])
    print(
        f'  (1) {authors[0]}\n  (2) {authors[1]}\n  (3) {authors[2]}\n  (4) {authors[3]}')
    print("Answer?")
    answer = int(input())
    if authors[answer-1] == quote['author']:
        print("CORRECT!")
    else:
        print(f'Wrong, it was {quote["author"]}')
    print(find_author(quote['author'])['results'][0]['bio'])


if __name__ == '__main__':
    question('famous-quotes')
