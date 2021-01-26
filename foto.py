import os
import piexif
import shutil

# Получаем список фотографий из указанной папки
# Папка должна лежать рядом с этим скриптом
directory = 'C:/Users/Skorix/Pictures/Foto/'
files = os.listdir(directory)
files2 = filter(lambda x: x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png') or x.endswith('.jpeg'), files) 
os.chdir('C:/Users/Skorix/Pictures/Foto/')

# Перебираем каждый файл из списка фото и вытаскиваем из его EXIF дату фотографирования
for x in files2:
    print(x)
    # Проверяем чтобы файл не был папкой
    if(os.path.isdir(x)==False):
        try:
            kartinka = piexif.load(x)
        except Exception:
            qq=None
        else:
            qq=None
        
            for i in ("0th", "Exif", "GPS", "1st"):
                for tag in kartinka[i]:
                    # Нам нужны EXIF теги DateTime и DateTimeOriginal
                    if((piexif.TAGS[i][tag]["name"]=="DateTime") or ((piexif.TAGS[i][tag]["name"]=="DateTimeOriginal"))):
                        qq=kartinka[i][tag]                
    
        if(qq==None):
            # Еcли в EXIF нет даты то имя папки будет 0000
            # В нее будут складываться фотки без даты в EXIF
            g = "0000-00-00"
        else:
            qq = qq.decode("utf-8")
            qq = qq[0:10]
            qq = qq.replace(":", "-")
            g = qq
    
        z = g[5:7] 

        # Заменяем цифры месяца на его название
        if(z=="01"):
            zz="январь"
        elif(z=="02"):
            zz="февраль"
        elif(z=="03"):
            zz="март"
        elif(z=="04"):
            zz="апрель"
        elif(z=="05"):
            zz="май"
        elif(z=="06"):
            zz="июнь"
        elif(z=="07"):
            zz="июль"
        elif(z=="08"):
            zz="август"
        elif(z=="09"):
            zz="сентябрь"
        elif(z=="10"):
            zz="октябрь"
        elif(z=="11"):
            zz="ноябрь"
        elif(z=="12"):
            zz="декабрь"
        else:
            zz="no"

        if (os.path.exists(g[0:4] + "/" + zz + '/' + g[8:10]) != True):
            os.makedirs(os.path.join(g[0:4], zz, g[8:10] ))
            
        # Копируем фотку в папку и удаляем оригинал 
        shutil.copyfile(x, g[0:4] + "/" + zz+ '/' + g[8:10] + '/' + x)
        os.remove(x)
