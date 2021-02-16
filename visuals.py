import matplotlib.pyplot as plt
from queries import query_db, get_db, DATABASE, num_seasons
from PIL import Image

color_1 = '#4e4376'
color_2 = '#E09D00'
color_3 = '#50A7C2'
color_4 = '#A1BE37'
color_5 = '#8F4311'

class visualmaker:
    def makecroppedpie2(file_name, label1='Women', label2='Men', value1=0, value2=0, color1=color_1, color2=color_2):
        plt.rcParams['font.family'] = 'monospace'
        plt.rcParams['text.color'] = 'white'
        labels = label1, label2
        sizes = [value1, value2]
        explode = (0, 0)  # tells which slice to "explode
        colors_list = [color1, color2]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors = colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True, dpi=300)
        imgPath = 'static/' + file_name + '.png'
        img = Image.open(imgPath)
        width, height = img.size
        box = ((width / 8 - width / 32), 60, (width - width / 8 + width / 32), (height - height / 8))
        croppedImage = img.crop(box)
        croppedImage.save('static/' + file_name + '_cropped.png')

    def makeagepie(file_name, label1='20-29', label2='30-39', label3='40-49', label4='50+', value1=0, value2=0, value3=0, value4=0, color1=color_1, color2=color_2, color3=color_3, color4=color_4):
        plt.rcParams['font.family'] = 'monospace'
        plt.rcParams['text.color'] = 'white'
        labels = label1, label2, label3, label4
        sizes = [value1, value2, value3, value4]
        explode = (0, 0, 0, 0)  # tells which slice to "explode
        colors_list = [color1, color2, color3, color4]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors = colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True, dpi=300)
        imgPath = 'static/' + file_name + '.png'
        img = Image.open(imgPath)
        width, height = img.size
        box = ((width / 8 - width / 32), (height / 12), (width - width / 8 + width / 32), (height - height / 8))
        croppedImage = img.crop(box)
        croppedImage.save('static/' + file_name + '_cropped.png')

    def makeregionpie(file_name, label1='Southern', label2='Mid-Atlantic', label3='New England', label4='Western', label5="Midwest", value1=0, value2=0, value3=0, value4=0, value5=0, color1=color_1, color2=color_2, color3=color_3, color4=color_4, color5=color_5):
        plt.rcParams['font.family'] = 'monospace'
        plt.rcParams['text.color'] = 'white'
        labels = label1, label2, label3, label4, label5
        sizes = [value1, value2, value3, value4, value5]
        explode = (0, 0, 0, 0, 0)  # tells which slice to "explode
        colors_list = [color1, color2, color3, color4, color5]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors = colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True, dpi=300)
        imgPath = 'static/' + file_name + '.png'
        img = Image.open(imgPath)
        width, height = img.size
        box = ((width / 8 - width / 32), (height / 12), (width - width / 8 + width / 32), (height - height / 24))
        croppedImage = img.crop(box)
        croppedImage.save('static/' + file_name + '_cropped.png')
        # 70 40 570 460
