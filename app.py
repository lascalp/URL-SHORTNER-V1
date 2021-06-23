import pyshorteners

link = input("Enter Link:")

shortener=pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)