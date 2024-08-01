from groq import Groq
import xml.etree.ElementTree as ET
import shortuuid
import os

class News:
    def __init__(self, title, prompt, length, content):
        self.title = title
        self.prompt = prompt
        self.content = content
        self.length = length

def parse_news():
    news = []

    for i, file in enumerate(os.listdir('documents')):
        tree = ET.parse(f"documents/{file}")
        root = tree.getroot()

        doc = dict(title=root[0].text, prompt=root[1].text, 
                   length=root[2].text, content=root[3].text, 
                   days=root[4].text, uuid=root[5].text, 
                   author=root[6].text, tag=root[7].text, short=(root[3].text)[0:150])
        news.append(doc)

    news = sorted(news, key=lambda story:int(story['days']))
    return news

def create_story(title: str, content: str, prompt: str="none", length: str="none", days: str="0", author: str="Julia Herald", tag: str="Technology"):
    root = ET.Element("document")
    tit = ET.SubElement(root, "title") 
    tit.text = title

    prom = ET.SubElement(root, "prompt") 
    prom.text = prompt

    len = ET.SubElement(root, "length") 
    len.text = length

    cont = ET.SubElement(root, "content") 
    cont.text = content

    da = ET.SubElement(root, "days") 
    da.text = days

    ui = ET.SubElement(root, "uuid") 
    ui.text = shortuuid.uuid()

    auth = ET.SubElement(root, "author") 
    auth.text = author

    t = ET.SubElement(root, "tag") 
    t.text = tag

    tree = ET.ElementTree(root) 

    with open(f"documents/story_{ui.text}.xml", "wb") as f:
        tree.write(f)
 