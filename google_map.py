import requests
from PIL import Image


class google_map:

    def __init__(self):
        self.api_key = "AIzaSyDo0YRz-RhdclLdMA1UXCM2FpnNHbOOT8M"
        self.url = "http://maps.googleapis.com/maps/api/staticmap?"

    def map_region(self, loc):
        center = loc
        zoom = 15
        r = requests.get(self.url+"center="+center+"&zoom="+str(zoom) +"&size=1024x768&key="+self.api_key)
        print(self.url+"center="+center+"&zoom="+str(zoom)+"&size=1024x768&key="+self.api_key)
        f = open('a.png', 'wb')
        f.write(r.content)
        f.close()
        img = Image.open('a.png')
        img.show()

    def map_city(self, loc):
        center = loc
        zoom = 10
        r = requests.get(self.url+"center="+center+"&zoom="+str(zoom) +"&size=1024x768&key="+self.api_key)
        print(self.url+"center="+center+"&zoom="+str(zoom)+"&size=1024x768&key="+self.api_key)
        f = open('a.png', 'wb')
        f.write(r.content)
        f.close()
        img = Image.open('a.png')
        img.show()
# City
# zoom = 10

# if __name__ == '__main__':
#     gm = google_map()
#     gm.map_region("Walmart,Mayaguez")
#     gm.map_city("Walmart,Mayaguez")




# print(url+"center="+center+"&zoom="+str(zoom)+"&size=1024x768&key="+api_key)

