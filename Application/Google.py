from google_images_download import google_images_download


class Google:
    __query = ''
    __response = ''

    def __init__(self):
        pass

    def __init__(self, search_param):
        self.__query = search_param
        self.__response = google_images_download.googleimagesdownload()
        self.download_image()

    def download_image(self):
        # keywords is the search query
        # format is the image file format
        # limit is the number of images to be downloaded
        # print urs is to print the image file url
        # size is the image size which can
        # be specified manually ("large, medium, icon")
        # aspect ratio denotes the height width ratio
        # of images to download. ("tall, square, wide, panoramic")
        arguments = {"keywords": self.__query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": True,
                     "size": "medium"}
        try:
            self.__response.download(arguments)
        # Not found
        except FileNotFoundError:
            print("DID NOT DOWNLOAD!!!")
            pass
