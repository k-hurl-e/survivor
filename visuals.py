import matplotlib.pyplot as plt
from queries import query_db, get_db, DATABASE, num_seasons
from PIL import Image

def makecroppedpie2(file_name, title, label1='label1', label2='label2', value1=0, value2=0, color1='cyan', color2='blue'):
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
    plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
    plt.savefig('static/' + file_name + '.png', transparent=True)
    imgPath = 'static/' + file_name + '.png'
    img = Image.open(imgPath)
    box = (70, 20, 570, 420)
    croppedImage = img.crop(box)
    croppedImage.save('static/' + file_name + '_cropped.png')

makecroppedpie2('gender_pie_players', 'Players by Gender', 'Women', 'Men', 354, 356)
makecroppedpie2('gender_pie_winners', 'Winners by Gender', 'Women', 'Men', 15, 25)
