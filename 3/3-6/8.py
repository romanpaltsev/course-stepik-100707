title = input()
author = input()
number_pages = int(input())
price = float(input())
book = [title, author, number_pages, price]
del book[2]
book[1] = "Пушкин"
book[2] = book[2] * 2
print(book)