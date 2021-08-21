from main import Annonce, Scrapper

test_url = "https://affairespc.com/annonce/pc-gamer-nitro-5-25613"

annonce: Annonce = Scrapper.get_this_page(test_url)

if annonce.title == "Pc gamer nitro 5":
    print("Title                    [OK]")
else:
    print("Title                    [NO]")

if annonce.price == 500:
    print("Price                    [OK]")
else:
    print("Price                    [NO]")

if annonce.email == "dadi94230@hotmail.fr":
    print("Email                    [OK]")
else:
    print("Email                    [NO]")

if annonce.phone_number == "06 99 83 02 21":
    print("Phone                    [OK]")
else:
    print("Phone                    [NO]")

if annonce.url == test_url:
    print("Url                      [OK]")
else:
    print("Url                      [NO]")