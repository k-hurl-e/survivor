import matplotlib.pyplot as plt
from queries import query_db, get_db, DATABASE, num_seasons
from PIL import Image

class visualmaker:
    def makecroppedpie2(file_name, label1='Women', label2='Men', value1=0, value2=0, color1='cyan', color2='blue'):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['text.color'] = 'white'
        labels = label1, label2
        sizes = [value1, value2]
        explode = (0, 0)  # tells which slice to "explode
        colors_list = [color1, color2]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90, colors = colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True)
        imgPath = 'static/' + file_name + '.png'
        img = Image.open(imgPath)
        box = (70, 60, 570, 420)
        croppedImage = img.crop(box)
        croppedImage.save('static/' + file_name + '_cropped.png')

    def makeagepie(file_name, label1='20-29', label2='30-39', label3='40-49', label4='50+', value1=0, value2=0, value3=0, value4=0, color1='cyan', color2='blue', color3='red', color4='orange'):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['text.color'] = 'white'
        labels = label1, label2, label3, label4
        sizes = [value1, value2, value3, value4]
        explode = (0, 0, 0, 0)  # tells which slice to "explode
        colors_list = [color1, color2, color3, color4]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90, colors = colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True)
        imgPath = 'static/' + file_name + '.png'
        img = Image.open(imgPath)
        box = (70, 40, 570, 420)
        croppedImage = img.crop(box)
        croppedImage.save('static/' + file_name + '_cropped.png')
