from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lxml import html

driver = webdriver.Chrome()# Open the website
driver.get("https://www.streetfighter.com/6/en-us/character")
assert "STREET FIGHTER" in driver.title
#id ="CybotCookiebotDialogBodyButtonDecline"
roster_space = driver.find_element(By.CLASS_NAME, "select_character__select__list__bgBGl")
roster = roster_space.find_elements(By.XPATH,"ul//li//a")
roster_links = []
for x in roster:
    roster_links.append(x.get_attribute('href'))
#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#print(driver.page_source)
driver.close()

class Tag:
    def __init__(self, /, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        items = (f"{k}={v!r}\n" for k, v in self.__dict__.items())
        return "{}".format(''.join(items))

    def __eq__(self, other):
        if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
           return self.__dict__ == other.__dict__
        return NotImplemented

t = Tag(**{'type':'p','value':'hello'})


with open('guile.html','r') as f:
    file = f.read()

tree = html.fromstring(file)

#tags = tree.xpath('//*')

rows = [element for element in tree.iterfind('.//tr')]

def parse(element,xpath):
    elements = {}
    for element in element.iterfind(xpath):
        #print("%s - %s - %s" % (element.tag, element.text,element.))
        attrib = element.attrib
        try:
            clss = attrib.pop('class')
            if 'frame_fixed' in clss:
                clss = 'name'
            elements[clss] = element.text_content()
        except KeyError:
            pass
        #children = element.getchildren()
        #if len(children) > 0:
        #    for x in children:
        
        #print(str(element.attrib) + ' ' + str(element.text_content()))
    attack = Tag(**elements)
    return attack
attacks = []
for row in rows:
    attacks.append(parse(row,'./td'))

for x in attacks:
    print(x)
    print('---')