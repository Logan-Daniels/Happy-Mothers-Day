from PIL import Image

countries = {
    'canada': 'ca',
    'korea_south': 'kr',
    'japan': 'jp',
    'united_states_of_america': 'us',
    'trinidad_and_tobago': 'tt',
    'cayman_islands': 'ky',
    'cuba': 'cu',
    'india': 'in',
    'russia': 'ru',
    'united_arab_emirates': 'ae',
    'china': 'cn',
    'united_kingdom': 'uk',
    'israel': 'il',
    'south_africa': 'za',
    'greece': 'gr',
    'france': 'fr',
    'zimbabwe': 'zi',
    'antarctica': 'aq',
    'argentina': 'ar',
    }
for country, code in countries.items():
    img = Image.open(f"original_marker_images/{country}_640.png")
    left = 188
    right = img.width - 204
    top = 20
    bottom = img.height - 45
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(f"cropped_marker_images/{code}.png")