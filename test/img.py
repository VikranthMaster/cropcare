# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def fetch_image_url(prompt):
#     """
#     Fetches the first image URL from Bing's image search results page.
#     """
#     search_url = "https://www.bing.com/images/search"
#     params = {"q": prompt}  # Search query

#     try:
#         response = requests.get(search_url, params=params)
#         response.raise_for_status()

#         # Parse HTML content
#         soup = BeautifulSoup(response.text, "html.parser")
#         img_tag = soup.find("img", {"class": "mimg"})
#         if img_tag and img_tag.get("src"):
#             return urljoin(search_url, img_tag["src"])
#         else:
#             print("No image found!")
#             return None
#     except Exception as e:
#         print(f"Error occurred while fetching image URL: {e}")
#         return None

# def download_image(img_url, save_path):
#     """
#     Downloads an image from the given URL and saves it locally.
#     """
#     try:
#         print(f"Downloading image from {img_url}...")
#         response = requests.get(img_url, stream=True)
#         response.raise_for_status()

#         with open(save_path, "wb") as file:
#             for chunk in response.iter_content(1024):
#                 file.write(chunk)

#         print(f"Image saved at {save_path}")
#     except Exception as e:
#         print(f"Failed to download image: {e}")

# if __name__ == "__main__":
#     prompt = input("Enter a prompt for the image: ")
#     save_directory = "downloaded_images"

#     # Create directory if it doesn't exist
#     if not os.path.exists(save_directory):
#         os.makedirs(save_directory)

#     # Fetch image URL and download the image
#     img_url = fetch_image_url(prompt)
#     if img_url:
#         save_path = os.path.join(save_directory, "downloaded_image.jpg")
#         download_image(img_url, save_path)
#     else:
#         print("Could not retrieve an image for the given prompt.")



import requests
from PIL import Image
from io import BytesIO

# Replace 'image_url' with the URL of the image you want to download
image_url = "https://example.com/path/to/image.jpg"

# Send a GET request to fetch the image data
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the image using PIL
    image = Image.open(BytesIO(response.content))
    
    # Save the image to a local file
    image.save("downloaded_image.jpg")
    print("Image downloaded and saved as downloaded_image.jpg")
else:
    print("Failed to retrieve the image. Status code:", response.status_code)
