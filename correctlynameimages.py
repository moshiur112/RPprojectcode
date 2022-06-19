import os
xx
def main():
    # number_of_images = 256
    directory_name = 'SatelliteImages'
    currentType = "SI"

    for count, filename in enumerate(os.listdir(directory_name)):
        dst = "{currcount}_{currtype}.jpg".format(currcount = str(count + 1), currtype = currentType)
        src = f"{directory_name}/{filename}"
        dst = f"{directory_name}/{dst}"

        os.rename(src, dst)
        # if count > number_of_images:
        #     raise Exception("The folder contains more than {numimage} images".format(numimage=number_of_images))

if __name__ == '__main__':
    main()