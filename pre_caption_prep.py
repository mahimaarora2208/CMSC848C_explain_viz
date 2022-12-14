from PIL import Image
import os, sys

from torchvision import transforms
from torchvision.transforms.functional import crop

def grid_crop(img_pil, denom):
    h, w = img_pil.size
    h_new = int(h/denom)
    w_new = int(w/denom)

    grid = []
    for i in range(0, h, h_new):
        for j in range(0, w, w_new):
            grid.append(crop(img_pil, i, j, h_new, w_new))
    
    return grid

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

    names = []
    for i, crop in enumerate(crops):
        saved_img = os.path.join(parent_dir, img_name, f'{img_name}_{i}.png')
        crop.save(saved_img)

        names.append(os.path.join('..',saved_img)) # .. prints out paths relative to Git2 dir
        #makes for easy pasting when running captioner

    return names

def main(img_path, crop='five', denom=2, rand_number=10, parent_dir=''):
    crops = get_crops(img_path, crop, denom, rand_number)

    img_name = os.path.basename(img_path).split('.')[0]
    return save_crops(crops, img_name, parent_dir)

if __name__ == '__main__':
    img_path = sys.argv[1]
    print(main(img_path))
