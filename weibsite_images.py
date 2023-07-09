import requests
import ssl
from bs4 import BeautifulSoup
import urllib.parse
import os

def download_images(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    response = requests.get(url,verify=False)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        img_tags = soup.find_all('img')
        
        base_url = urllib.parse.urljoin(url, '/')
        
        for img_tag in img_tags:
            if 'src' in img_tag.attrs:
                img_url = img_tag['src']
                
                download_image(base_url, img_url)
            
        print("All pictures are downloaded!")
    else:
        print("Unable to fetch web page content!")

def download_image(base_url, img_url):
    if not img_url.startswith('https'):
        img_url = urllib.parse.urljoin(base_url, img_url)
    
    img_filename = img_url.split("/")[-1]
    
    save_directory = os.path.join(os.path.dirname(__file__), "your_images_save_path")
    os.makedirs(save_directory, exist_ok=True)
    save_filepath = os.path.join(save_directory, img_filename)
    
    try:
        response = requests.get(img_url)
        
        if response.status_code == 200:
            with open(save_filepath, 'wb') as f:
                f.write(response.content)
                print("Image downloaded:", save_filepath)
        else:
            print("Unable to download image:", img_url)
    except requests.exceptions.RequestException as e:
        print("An error occurred while downloading the image:", str(e))

url = "your_website"

download_images(url)
