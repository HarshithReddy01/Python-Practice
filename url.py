url = input('Enter your URL: ')
protocol = url[ : url.find(':')]
x1 = url.find('.')
x2 = url.find('.', x1+1)

domain = url[x1+1 : x2]

page = url[url.find('/', x2) :]


