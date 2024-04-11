from PIL import Image

countries = ['canada', 'korea_south', 'japan', 'united_states_of_america']
for country in countries:
    img = Image.open(f"original_images/{country}_640.png")
    left = 188
    right = img.width - 204
    top = 20
    bottom = img.height - 45
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(f"cropped_images/{country}.png")