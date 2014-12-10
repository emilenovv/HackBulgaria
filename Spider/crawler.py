from urllib import parse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from page import Page
import pythonwhois
from datetime import date


class Crawler:
    def __init__(self, domain, session):
        self.domain = domain
        self.scanned_urls = []
        self.url_to_scan = []
        self.__session = session

    def is_outgoing(self, url):
        o = urlparse(url)
        if o.netloc == self.domain:
            return False
        return True

    def href_to_url(self, url, href):
        return parse.urljoin(url, href)

    def scan_page(self, url):
        if url in self.scanned_urls:
            return
        #print(url)
        self.scanned_urls.append(url)
        website = requests.get(url)
        html_doc = website.text
        soup = BeautifulSoup(html_doc)
        # try:
        #     self.save_soup(soup, url)
        # except Exception as e:
        #     print(e)

        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            next_page = self.href_to_url(url, href)
            if next_page not in self.scanned_urls and not self.is_outgoing(next_page):# and '#' not in next_page:
                self.url_to_scan.append(next_page)

    def scan_site(self):
        while len(self.url_to_scan) != 0:
            print(len(self.url_to_scan))
            self.scan_page(self.url_to_scan.pop())

    def scan_website(self):
        url = 'http://' + self.domain
        self.scan_page(url)
        self.scan_site()

    def rate_by_date_created(self):
        year_created_string = pythonwhois.get_whois(self.domain)['creation_date'][0].strftime("%Y")
        year_created_int = int(year_created_string)
        current_year = date.today().year
        year_difference = current_year - year_created_int
        if year_difference >= 10:
            rating = 10
        else:
            rating = year_difference
        return rating

    def save_soup(self, soup, url):
        try:
            description = soup.find(attrs={"property": "og:description"}).get("content")
        except Exception as e:
            description = ""
        new_page = Page(
            title=soup.title.string,
            description=description,
            url=url,
            )
        self.__session.add(new_page)
        self.__session.commit()
        return new_page


if __name__ == '__main__':
    main()
