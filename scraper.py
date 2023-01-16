import requests
from bs4 import BeautifulSoup


def soup(url):
    page = requests.get("https://" + url)
    soup_ = BeautifulSoup(page.content, 'html.parser')
    return soup_


def get_citations_needed_count(url):
    soup_ = soup(url)
    count = len(soup_.find_all("sup", class_="noprint Inline-Template Template-Fact"))
    print("\x1B[3m" + "number of missing citations: " + "\x1B[0m" + str(count))


def get_citations_needed_report(url):
    soup_ = soup(url)
    report = soup_.find_all("sup", class_="noprint Inline-Template Template-Fact")
    string = ""
    for x in report:
        string += ("\x1B[3m" + "Section:\n" + "\x1B[0m" + x.find_previous("h3").get_text()
                   + ":\n" + "\x1B[3m" + "Entry: \n" + "\x1B[0m" + x.parent.get_text() + "\n")
    string = string.replace("[edit]:", "")
    print(string)


if __name__ == '__main__':
    url = input('> URL: ')
    get_citations_needed_count(url)
    get_citations_needed_report(url)
