print ("Поддерживает ссылки формата: https://www.youtube.com/watch?v=")
Video_YouTube = str(input("Вставьте ссылку для скачивания обложки: "))
replace_block = '?v='
replace = Video_YouTube.split(replace_block, 1)[1]

Y_max = 'https://img.youtube.com/vi/'

print("Скачать обложку - ", Y_max + replace + '/maxresdefault.jpg')
