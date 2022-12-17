from PIL import Image
import os, sys

from torchvision import transforms

def rand_crop(img_pil, denom=2):
    h = int(img_pil.size[0]/denom)
    w = int(img_pil.size[1]/denom)

    return transforms.RandomCrop((h,w)).forward(img_pil)

def five_crop(img_pil, denom=2):
    h = int(img_pil.size[0]/denom)
    w = int(img_pil.size[1]/denom)

    return transforms.FiveCrop((h,w)).forward(img_pil)

def get_image(path):
    with open(os.path.abspath(path), 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB') 

def get_crops(img_path, crop, denom, rand_number):
    img_pil = get_image(img_path)
    crops = []

    if crop == 'five':
        crops = five_crop(img_pil, denom)
    elif crop == 'grid':
        print('not yet implemented')
    else:
        crops = [rand_crop(img_pil, denom) for i in range(rand_number)]
    

    return crops
        
def save_crops(crops, img_name, parent_dir):
    new_dir = os.path.join(parent_dir, img_name)
    os.mkdir(new_dir)
    for i, crop in enumerate(crops):
        crop.save(os.path.join(parent_dir, img_name, f'{img_name}_{i}.png'))

def main(img_path, crop='five', denom=2, rand_number=10, parent_dir=''):
    crops = get_crops(img_path, crop, denom, rand_number)

    img_name = os.path.basename(img_path).split('.')[0]
    save_crops(crops, img_name, parent_dir)


if __name__ == '__main__':
    img_path = sys.argv[1]
    main(img_path)