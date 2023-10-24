from PIL import Image

def crop_and_save_image(input_image_path, output_image_path, left, top, right, bottom):

    image = Image.open(input_image_path)

    cropped_image = image.crop((left, top, right, bottom))

    cropped_image.save(output_image_path, 'JPEG')

input_image_path = 'pic.jpg'
output_image_path = 'cropped_image.jpg'
left = 100
top = 200
right = 500
bottom = 600

crop_and_save_image(input_image_path, output_image_path, left, top, right, bottom)
