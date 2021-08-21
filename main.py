from bs4 import BeautifulSoup
import requests

class Annonce:
    def __init__(self, title: str, description: str, price: float, etat: str, shipping: bool, category: str, likes: str, images: str, phone_number: str, email: str, location: str, publied_at: str, url: str):
        self.title = title
        self.description = description
        self.price = price
        self.etat = etat
        self.shipping = shipping
        self.category = category
        self.likes = likes
        self.images = images
        self.phone_number = phone_number
        self.email = email
        self.location = location
        self.publied_at = publied_at
        self.url = url

class Scrapper:
    @staticmethod
    def search_by_title (title: str) -> list[Annonce]:
        pass
    
    @staticmethod
    def search_by_url (url: str) -> list[Annonce]:
        pass

    @staticmethod
    def get_this_page (url: str) -> Annonce:  
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.find("h1", {"class": "main-title h3"}).text
        

        description = soup.find("div", {"class": "col-12 p-1 text-left"}).find('p').text
        

        price = float(soup.find("div", {"class": "mb-1 h2 text-primary"}).text.replace("€ ", "").replace(",", "."))
        

        info = soup.find("div", {"class": "col-12 p-1 text-center"}).findAll("div")

        category = info[0].text
        

        publied_at = info[1].text
        

        etat = info[2].text
        

        likes = int(info[3].text)
        

        shipping = "Envoi" in soup.find("div", {"class": "mb-1 d-inline-block"}).text
        

        images_scraped = soup.find("div", {"class": "carousel-inner"}).findAll("div")
        images = []
        for i in images_scraped:
            images.append(str(i).replace('<div class="carousel-item active" style="height:500px;background-image:url(', "").replace('<div class="carousel-item" style="height:500px;background-image:url(', "").replace(');background-size: contain;background-repeat: no-repeat;background-position: center;"></div>', "").replace("'", ""))
        

        location = soup.find("div", {"class": "mb-1 d-inline-block mr-2"}).text
        

        contact = soup.find("div", {"class": "col-12 col-md-4 p-1 text-center"}).findAll("button")

        email = str(contact[0]).replace('<button class="btn btn-outline-primary btn-xs btn-block shadow-sm" id="btn_view_email" onclick="display_text(this,', "").replace(');add_clic_annonce(25613);">Voir l', "").replace('email</button>', "").replace("'", "")
        

        phone_number = str(contact[1]).replace('<button class="btn btn-outline-primary btn-xs btn-block shadow-sm" id="btn_view_phone" onclick="display_text(this,', "").replace(');add_clic_annonce(25613);">Voir le numéro</button>', "").replace("'", "")
        

        return Annonce(title, description, price, etat, shipping, category, likes, images, phone_number, email, location, publied_at, url)

annonce = Scrapper.get_this_page("http://affairespc.com/annonce/pc-gamer-nitro-5-25613")

print(annonce.title)