import uuid
colorsFile = open('./colors.txt', "x")


colorsFile.write("[")
for i in range(0, 256, 15):
    for j in range(0, 256, 15):
        for k in range(0, 256, 15):
            x = "rgb({},{},{})".format(i, j, k)
            y = uuid.uuid4().hex
            z = {
                "id": y,
                "color": x
            }
            outputData = '{},'.format(z)
            colorsFile.write(outputData)
colorsFile.write("]")
