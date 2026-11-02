def url_length(url):
    return len(url)

urls = ["google.com", "github.com", "free-gift-card.win"]

for u in urls:
    if url_length(u) > 12:
        print(u, "is long")
    else:
        print(u, "is short")