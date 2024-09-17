


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

product_names = [
    'POUF WITH FILLER', 'CUSHION WITH FILLER', "MEN'S FULL SLEEVE SHIRT", 'TUFTED THROW', 'COTTON THROW', 'BEADED SOCKS',
    'BEADED VELVET SOCKS', 'BATH MAT', 'EMBROIDERED RUNNER', 'FLOOR LAMP WITH SHADE SET', 'TABLE LAMP WITH SHADE',
    'LADIES MAXI DRESS', 'LADIES MIDI DRESS', 'LADIES DRESS', 'LADIES SMOCKED DRESS', 'LADIES SCHIFFLI MAXI DRESS',
    'LADIES OFF SHOULDER DRESS', "MEN'S SHORT SLEEVE SHIRT", "MEN'S BEACH PANT", "MEN'S BEACH ELASTICATED WAIST SHORTS",
    'JUTE BASKET', 'HAIRON LEATHER PHOTOFRAME', 'HAIRON LEATHER BOX', 'BONE PHOTOF RAME', 'DECORATIVE BOX',
    'DECORATIVE PIECES', 'WOODEN BOX WITH LID', 'BONE CONE', 'WALL HANGING', 'TUFTED CUSHION WITH FILLER',
    'TUFTED CUSHION', 'BABY GIRL PANT', 'BABIES JUMPSUIT', 'BABY GIRL DRESS', 'BABIES ROMPER', 'BABIES SHORTS',
    'COTTON POUF', 'BABIES HOODED T-SHIRT', 'FLOOR CUSHION WITH FILLER', 'SOAP DISPENSER', 'PUMP SOAP DISPENSER',
    'WOODEN TRAY', 'COTTON BASKET', 'TUFTED BATH MAT', 'LADIES SHORT SLEEVE BLOUSE', 'LADIES SKIRT', 'LADIES TOP',
    'LADIES SHIRT', 'LADIES RUFFLE SLEEVE MIDI DRESS', 'LADIES SLEEVELESS BLOUSE', 'LADIES SHORTS', 'BATH TUMBLER',
    'COTTON PLACEMAT', 'COTTON LUREX RUNNER', 'TABLE NAPKIN', 'TABLE CLOTH', 'KIDS CARPET', 'CHARGER PLATE',
    'COTTON BOX', 'WOODEN TUMBLER', 'COTTON CARPET', 'FLOOR CARPET', 'BABY GIRL SLEEVELESS TOP', 'MOP PLACE MAT',
    'BEADED PLACE MAT', 'JUTE PLACE MAT', 'COTTON NAPKIN', 'FLOWER EMBOIDERY PLACE MAT', 'BEADED BOX', 'CUTLERY SET',
    'DECORATIVE PINEAPPLE', 'TABLE LAMP', 'EMBROIDERY STOOL', 'CAKE STAND', 'BEADED COASTERS', 'NAPKIN RING', 'TEA BOX',
    'MDF COASTER', 'SERVING TRAY', 'DRINKING GLASS', 'CHRISTMAS GARLAND', 'GARDEN PLANTER', 'DECORATIVE VASE',
    'METAL PLANTER', 'WATERING CAN', 'BABY BOY SWEATSHIRT', 'BABIES LONG SLEEVE SHIRT', 'BABIES JACKET', 'BABIES HOODIE',
    'BABIES SWEATER', 'BABIES SWEATSHIRT', 'BABY BOY SWEATER', 'BABIES T-SHIRT', 'BABIES KNITTED TOP', 'BABY GIRLS SWEATER',
    'BABY GIRL SKIRT', 'BABIES JUMPER', 'BABIES BLOUSE', 'COTTON RUG', 'JUTE RUG', 'DECORATIVE PIECE', 'CHRISTMAS ORNAMENT',
    'CHRISTMAS STOCKING', 'CHRISTMAS TREE', 'WOODEN TREE COLLAR', 'BEADED RUNNER', 'CRYSTAL ORNAMENT', 'BEADED SNOW FLAKE',
    'TABLE TREE', 'TREE COLLAR', 'TREE SKIRT', 'BEADED TREE SKIRT', 'WOODEN REINDEER', 'BEADED TREE TOPPER',
    'EMBROIDERED TREE SKIRT', '3PC BEACHWEAR SET', 'WOODEN PHOTO FRAME', 'MDF PHOTO FRAME', 'RESIN PHOTO FRAME',
    'WOODEN SCULPTURE', 'MANGO WOOD SCULPTURE', 'LADIES BLOUSE', 'GLASS VASE', 'ALUMINIUM VASE', 'STEEL VASE',
    'X&O GAME DECOR PIECE', 'STEEL LANTERN', 'LADIES RUFFLED SWEATER', 'METAL SCULPTURE', 'TABLE CLOCK', 'DECORATIVE APPLE',
    'BABY BOY CARDIGAN', 'LADIES VEST', 'LADIES JACKET', 'MIRROR', 'DINING TABLE', 'CONSOLE TABLE', 'MEDIA TV UNIT',
    'SIDE BOARD TABLE', 'WOODEN CHAIR', 'WOODEN BENCH', 'COFFEE TABLE', 'COUNTER TABLE', "MEN'S VEST", "MEN'S JOGGERS",
    "MEN'S ZIPPER JACKET", "MEN'S JACKET", "MEN'S HOODED JACKET", "MEN'S SWEATSHIRT", 'BABIES SHIRT', 'BEADED COASTER',
    '4 PC BEDSHEET SET', 'BABIES PYJAMA SET', 'RATAN POT', 'RATAN COASTER', 'DECORATIVE PUMPKIN', 'JEWELLERY BOX',
    'BATH TOWEL SET OF 6', 'HAND TOWEL', 'FACIAL TOWEL', 'MANGO WOOD BOX', 'JEWELLERY TRAY', 'LADIES CARDIGAN',
    'LADIES LOUNGWEAR', 'LADIES SWEATER', 'MENS LONG SLEEVE SWEATER', "MEN'S SWEATER", 'NAPKIN HOLDER', 'SALT & PEPPER SHAKER',
    'MARBLE COASTER', 'STORAGE BASKET', 'WOODEN COASTER', 'SERVING SPOON', 'DECORATIVE BOWL', 'COTTON RUNNER',
    'LADIES HANDBAG', "WOMEN'S BUCKET BAG", 'LADIES BAG', 'LADIES SLING BAG', 'LAZY SUSAN', 'COTTON COASTER',
    'MARBLE CHEESE SET', 'LADIES UTILITY BAG', 'SALT & PEPPER POT', 'LADIES HANDBAG', 'MARBLE PINCH POT',
    'GLASS TUMBLER', 'RESIN TUMBLER', 'HAIRPIN LEG BENCH', 'BEADED PHOTO FRAME', 'COTTON PLACE MAT', 'CANDLE STAND',
    'MULTICOLOR PLACE MAT', 'MULTICOLORED RUNNER', 'CHINDI RUG', 'TUFTED CARPET', 'ROUND CARPET', 'JUTE CARPET',
    'TABLE PLACE MAT', 'WOODEN LANTERNS', 'T-LIGHT HOLDER', 'WOODEN BOX', 'TABLE RUNNER', 'FABRIC PLACE MAT',
    'TOY SMALL FISHING', 'SILK SOLID DYED', 'LADIES JUTE BAG', 'MAGNIFYING GLASS', 'WALL CLOCK', 'BAR STOOL',
    'ROUND DINING TABLE', 'WOODEN COFFEE TABLE', 'WOODEN SIDE TABLE', 'ROUND SIDE TABLE', 'RATAN BASKET',
    'ACETATE PRINTED FABRICS', 'GIRLS SKIRT', 'POLYESTER PRINTED FABRICS', 'PROJECTION TOY GUN', 'KIDS TORCH',
    'WOODEN SOAP DISPENSER', 'TOY MIKE PROJECTOR', 'OMBRE CHIFFON SOLID DYED', "MEN'S PANT", 'ORGANZA SOLID DYED',
    'VISCOSE BLEND PRINTED FABRICS', 'TOY GUN', 'SILK PRINTED FABRICS', 'TOY LAPTOP', 'BOYS SHORT', 'TOY RING TOSS',
    'LINEN PRINTED FABRICS', 'HOVER BALL', 'BLAZE STROM', 'VISCOSE PRINTED FABRICS', 'PLASTIC TOY CUBE',
    'COTTON PRINTED FABRICS', 'LADIES PANT', 'SATIN SOLID DYED', "MEN'S SHIRT", 'BLAST GUN',
    'COTTON BLEND PRINTED FABRICS', 'TULLE SOLID DYED', 'POLYURETHANE PRINTED FABRICS', 'ACETATE SATIN SOLID DYED',
    'TOY ROLL BALL', 'ACETATE BLEND PRINTED FABRICS', 'DRUM PIANO', 'TOY TOM CAT', 'FLASH DRUM',
    'ELASTIC SILK LIKE SATIN SOLID DYED', 'STUDY TABLE', 'TABLE BENCH', 'GLASS BEADS CONE', 'MARBLE BOWL',
    'LADIES CLUTCH BAG', 'COTTON PRINTED BASKET', 'FORMAL TROUSERS', 'SOLID COTTON PANT', 'COTTON SOFT TOY',
    'COTTON CUSHION', 'COTTON PLAYMAT', 'COTTON THROW', 'BABY CRIB', 'LONG SLEEVE COVERALLS', "MEN'S STRETCH CAP",
    'HI VIZ JACKET', 'LADIES CROPPED PANT', "MEN'S T-SHIRT", 'LEATHER GLOVES', 'SAFETY GLOVES', 'LODGE CAP',
    'MENS CAP', "MEN'S CARGO PANT", 'CARGO PANT', 'FLEXFIT CAP', "MEN'S INSULATED JACKET", 'PERFORMANCE JACKET',
    'WATER PROOF JACKET'
]


chromedriver_path = r"C:\Users\91701\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object
service = Service(chromedriver_path)

# Create Chrome options
chrome_options = Options()

# If you need to specify the Chrome binary location
chrome_binary_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.binary_location = chrome_binary_path

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

for product_name in product_names:
    data = []
    driver.get('https://www.amazon.in')

    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.clear()
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Allow time for search results to load

    for page in range(10):
        print(f'Scraping page {page + 1}')

        # Extract product details
        titles = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
        ratings = driver.find_elements(By.XPATH, "//i[@data-cy='reviews-ratings-slot']/span[@class='a-icon-alt']")

        print(f'Found {len(titles)} products on this page.')

        for index in range(len(titles)):
            title = titles[index].text if index < len(titles) else 'N/A'
            price = prices[index].text if index < len(prices) else 'N/A'
            rating = ratings[index].text if index < len(ratings) else 'N/A'

            data.append({
                'Title': title,
                'Price': price,
                'Rating': rating
            })

        # Click the next page button if it exists
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
            next_button.click()
            time.sleep(1)  # Allow time for the next page to load
        except:
            print('No more pages or next button not found.')
            break

    # Save data to CSV
    df = pd.DataFrame(data)
    file_name = f'{product_name}.csv'
    df.to_csv(file_name, index=False)
    print(f'Data for "{product_name}" saved to CSV: {file_name}')

driver.quit()
