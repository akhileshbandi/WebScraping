from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request,urlopen
import re
def tag_visible(element):

    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def get_text(raw_url):
        req = Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page,'lxml')
        links_with_text = []
        for a in soup.find_all('a', href=True):
            if a.text:
                    links_with_text.append(a['href'])
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts) + u" ".join(" "+ t.strip() + " " for t in links_with_text)

def main():
    print("Enter the URL")
    url=(input())
    text = get_text(url)
    url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
    email_regex = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    print("All the links in : ", url)
    for i in re.findall(url_extract_pattern,text):
        print(i)
    print("All the emails in : ", url)
    for i in re.findall(email_regex,text):
        print(i)

if __name__=="__main__":

    main()
