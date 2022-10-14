Są dwa programy, image to txt.py iraz main.py.

Pierwszy zamienia film na dokument tekstowy, a drugi na filmik na podstawie tekstu.

Parametry można zmienić bezpośrednio w kodzie i są to:
-character_density (ilość znaków na klatkę filmu)
-frame_skip (co którą klatkę ma się renderować przetworzony obraz)
-video = cv2.VideoCapture('ToConvert/nazwa_pliku_do_przetworzenia.mp4') (nazwa i lokalizacja pliku do przetoworzenia)
-converted_video = cv2.VideoWriter('Converted/przetworzony_plik.avi', 0, fps, (video_width, video_height)) (nazwa i lokalizacja przetworzonego pliku)
-font = ImageFont.truetype('Fonts/nazwa_czcionki.ttf', density + 1) (nazwa i lokalizacja czcionki, pozwala zmienić czcionkę na dowolną inną)
-image = Image.new("RGB", (width, height), color='black') (parametr color='kolor' zmienia kolor tła)
-d.text((x * density + (density * 0.25), y * density), display_matrix[y][x], font=font, fill='white') (parametr fill='kolor' zmienia kolor czcionki)

By programy działały nie może być w docelowym katalogu stworzony żaden plik o tej samej nazwie co nazwa przetworzonego pliku.
