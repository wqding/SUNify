from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

paths = response.download({
    'keywords': 'cloudy buildings',   
    'limit': 5000,
    'color_type': 'full-color',
    'type': 'photo',
    'thumbnail_only': True,
    'chromedriver': 'C:/Users/Adam/Desktop/chromedriver.exe',
    # 'usage_rights': 'labeled-for-reuse'
})



