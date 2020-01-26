from PIL import Image,ImageDraw,ImageFont
import glob
 
# Create the frames
def stringToImage():
    number = 0
    while number < 3:
        num = str(number)
        texto = input("Enter text: ")
        image = Image.new('RGB',(255,255), color =(0,0,0))
        fontsize = 1

        img_fraction = 0.5

        font = ImageFont.truetype('/Users/Debora/Desktop/videoFerramenta/fonts/Roboto-Regular.ttf',fontsize)
        while font.getsize(texto)[0] <img_fraction*image.size[0]:
            fontsize +=1
            font = ImageFont.truetype('/Users/Debora/Desktop/videoFerramenta/fonts/Roboto-Regular.ttf',fontsize) 

        fontsize -= 1
        draw = ImageDraw.Draw(image)
        draw.text((10,10), texto, font = ImageFont.truetype('/Users/Debora/Desktop/videoFerramenta/fonts/Roboto-Regular.ttf',fontsize) , fill=(255,255,255)) 
        image.save(num+'.jpg')
        number+=1

def imageToGif():
    frames = []
    imgs = glob.glob("*.jpg")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    frames[0].save('png_to_gif.mp4', format='mp4',
                append_images=frames[1:],
                save_all=True,
                duration=2000, loop=0)

numero = int(input("Escrever 1:  Criar GIF 2:  sair 0: "))

while numero != 0:
    if numero == 1:
        stringToImage()
        numero = int(input("Escrever 1:  Criar GIF 2:  sair 0: "))

    elif numero == 2:
        imageToGif() 
        numero = int(input("Escrever 1:  Criar GIF 2:  sair 0: "))   
