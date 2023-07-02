import requests

# '/version/scheme/zoom/col/row/resolution/format'
version = "newest"
scheme = "satellite.day"
zoom = 1
col = 0
row = 0
resolution = 256
Format = "jpg"

resolution = str(resolution)
# url = 'https://1.aerial.maps.ls.hereapi.com/maptile/2.1/maptile/newest/satellite.day/1/0/1/256/jpg?apiKey=aRrXMN6rNeDunujbIgCqESvkttKlk4Pp2j5N7xTp4Ek'

err = 0
while True:
    url = 'https://1.aerial.maps.ls.hereapi.com/maptile/2.1/maptile/'+version+'/'+scheme+'/'+str(zoom)+'/'+str(col)+'/'+str(row)+'/'+resolution+'/'+Format+'?apiKey=aRrXMN6rNeDunujbIgCqESvkttKlk4Pp2j5N7xTp4Ek'

    response = requests.get(url)

    if response.status_code == 200:
        with open(str(zoom)+"x"+str(col)+"x"+str(row)+'.jpg', 'wb') as file:
            file.write(response.content)
        print(str(zoom)+"x"+str(col)+"x"+str(row)+'Image saved successfully.')
        col += 1
    elif response.status_code == 400:
        print(str(zoom)+"x"+str(col)+"x"+str(row)+'Failed to retrieve the image.')
        row += 1
        col = 0

        err += 1
        # print(err)
        if err > col+1:
            zoom += 1
            col = 0
            row = 0
            err = 0
            #break
