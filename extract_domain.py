from urllib.parse import urlparse

# Input URL
url = input("Enter a URL: ")

# Parsing domain
parsed_url = urlparse(url)
domain = parsed_url.netloc

# Menampilkan hasil
print(f"Domain: {domain}")