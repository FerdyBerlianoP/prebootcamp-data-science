import requests
import json

# Replace YOUR_API_KEY with your actual API key
API_KEY = '0f4bec5a46694c0ab618ffa499e39210'

# Function to get top headlines for a category
def get_headlines(category):
    url = f'https://newsapi.org/v2/top-headlines?country=id&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return [article['title'] for article in data['articles'][:5]]

# Print welcome message
print("Selamat datang, mau tahu berita apa hari ini?")

# Print options
print("[1] Berita seputar teknologi")
print("[2] Berita seputar bisnis")
print("[3] Berita seputar olahraga")
print("[4] Berita seputar kesehatan")
print("[5] Berita seputar sains")

# Get user's choice
choice = int(input("Ketik pilihan Anda [1/2/3/4/5] : "))

# Print top headlines for chosen category
if choice == 1:
    category = 'technology'
    print("Berikut adalah top 5 berita Indonesia bidang technology :")
elif choice == 2:
    category = 'business'
    print("Berikut adalah top 5 berita Indonesia bidang business :")
elif choice == 3:
    category = 'sports'
    print("Berikut adalah top 5 berita Indonesia bidang sports :")
elif choice == 4:
    category = 'health'
    print("Berikut adalah top 5 berita Indonesia bidang health :")
elif choice == 5:
    category = 'science'
    print("Berikut adalah top 5 berita Indonesia bidang science :")

headlines = get_headlines(category)
for i, headline in enumerate(headlines):
    print(f'{i+1} - {headline}')
