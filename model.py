import requests
import os

def generate_image_api(male_path, female_path):
    # Pastikan Anda sudah mendapatkan API key dari DeepAI
    api_key = 'e2a50274-7efd-4aa3-b493-94987bbf1711'
    
    response = requests.post(
        "https://api.deepai.org/api/cartoon",
        files={
            'male': open(male_path, 'rb'),
            'female': open(female_path, 'rb'),
        },
        headers={'api-key': api_key}
    )
    
    if response.status_code == 200:
        image_url = response.json()['output_url']
        # Simpan gambar dari URL ke folder uploads
        image_response = requests.get(image_url)
        output_image_path = os.path.join('static/uploads', 'generated_image.png')
        with open(output_image_path, 'wb') as f:
            f.write(image_response.content)
        return output_image_path
    else:
        return None

def generate_image(male_path, female_path):
    return generate_image_api(male_path, female_path)
