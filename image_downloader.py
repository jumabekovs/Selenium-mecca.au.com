import os
import requests
from bs4 import BeautifulSoup

url = [
    "https://www.mecca.com.au/mecca-cosmetica/to-save-sensitive-body-spf50-superscreen/V-050458.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/original-coffee-scrub/V-025591.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/isle-of-paradise/self-tanning-mousse/V-035817.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/sol-de-janeiro/brazilian-bum-bum-cream/V-033306.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/smoothing-aha-body-lotion/I-050282.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/sol-de-janeiro/bom-dia-bright-cream/V-048673.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/isle-of-paradise/self-tanning-drops/V-035820.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/drunk-elephant/tlc-glycolic-body-lotion/I-050793.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/bangn-body/firming-lotion/I-045366.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/sugar-crush-body-scrub/I-016166.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/mario-badescu/aha-botanical-body-soap/I-004669.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/in-shower-moisturiser/I-049320.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/flake-away-spa-body-polish/V-846466.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/coconut-coffee-scrub/V-025592.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/mecca-cosmetica/mecca-athletica-skin-perfecting-body-wash/I-044901.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/sol-de-janeiro/brazilian-4play-moisturising-shower-cream-gel/V-047350.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/in-your-dreams-sleep-scrub-and-soak/V-813878.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/glide-n-go-body-oil-stick/I-050281.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/a-clean-body-wash-scented/I-048986.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/sol-de-janeiro/bum-bum-body-scrub/I-044739.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/the-righteous-butter/V-008914.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/booty-drops-firming-body-oil/I-043513.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/hand-food-hydrating-hand-cream/V-008918.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/clean-on-me-body-wash/I-052116.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/scrub-gloves/I-011282.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/gem/whitening-pen/I-050526.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/drunk-elephant/sili-body-lotion/I-042676.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/mecca-cosmetica/nourishing-hand-cream/V-038945.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/scrub-squad/I-048130.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/goop/gtox-ultimate-dry-brush/I-047491.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/soap-glory/call-of-fruity-body-wash/I-052129.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/frank-body/express-o-scrub/I-040315.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/luna-bronze/glow-gradual-tanning-moisturiser/V-030836.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/kosas/chemistry-aha-serum-deodorant/V-814470.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/glow-recipe/watermelon-glow-pink-dream-body-cream/I-049400.html?cgpath=bodypersonalcare",
    "https://www.mecca.com.au/bangn-body/illuminating-firming-lotion/I-045369.html?cgpath=bodypersonalcare",
]


def get_img(url):
    try:
        os.mkdir(os.path.join(os.getcwd()))
    except:
        pass

    os.chdir(os.path.join(os.getcwd()))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = img = soup.find_all('img')[31]

    with open(img['alt'].replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
        im = requests.get(img['src'])
        f.write(im.content)
        print('Writing: ', img['alt'])


for i in url:
    get_img(i)
