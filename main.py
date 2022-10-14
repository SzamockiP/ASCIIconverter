import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy


def frame_to_text_image(frame, density, size, ascii_values):
    width = size[0]
    height = size[1]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # klatka na grayscale

    matrix = [[0.0 for i in range(width)] for j in range(height)]  # deklaracja tablicy na średną wartości RGB 0.0-1.0 zdjęcia

    for y in range(height):  # rzędy
        for x in range(width):  # kolumny
            matrix[y][x] = round(gray[y][x] / 255, 1)  # przypisanie wartości w.w.

    round_sum = 0.0

    display_matrix = [['' for i in range(int(width / density))] for j in range(int(height / density))]  # deklaracja tablicy ASCII
    for y in range(int(height / density)):
        for x in range(int(width / density)):
            for y_p in range(y * density, y * density + density):
                for x_p in range(x * density, x * density + density):
                    round_sum += matrix[y_p][x_p]
            display_matrix[y][x] = ascii_values[round(round_sum / density / density, 1)]  # to po prostu robi że robimy miejszą tablicę z uśrednionych wartości i wypełniamy ją literkami
            round_sum = 0

    image = Image.new("RGB", (width, height), color='black')

    d = ImageDraw.Draw(image)
    font = ImageFont.truetype('Fonts/consola.ttf', density + 1)

    for y in range(len(display_matrix)):
        for x in range(len(display_matrix[y])):
            d.text((x * density + (density * 0.25), y * density), display_matrix[y][x], font=font, fill='white')

    return image


video = cv2.VideoCapture('test.mp4')
success, video_frame = video.read()

ascii_codes = {
    0.0: ' ',
    0.1: '.',
    0.2: ':',
    0.3: '-',
    0.4: '=',
    0.5: '+',
    0.6: '*',
    0.7: '#',
    0.8: '%',
    0.9: '$',
    1.0: '@',
}

video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
how_many_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
character_density = 6
frame_skip = 5  # więcej niż 1 i mniej niż how_many_frames
fps = video.get(cv2.CAP_PROP_FPS) / frame_skip

frames = []
success_count = 1
conversion_count = 1

while success:
    if success_count % frame_skip == 0:
        frames.append(numpy.array(frame_to_text_image(video_frame, character_density, (video_width, video_height), ascii_codes)))
        print('lasting frames: ', round(how_many_frames/frame_skip)-conversion_count, flush=True)
        conversion_count += 1
        cv2.imshow('image', frames[-1])
    success, video_frame = video.read()
    success_count += 1

converted_video = cv2.VideoWriter('converted_video.avi', 0, fps, (video_width, video_height))

for list_frame in frames:
    converted_video.write(list_frame)

cv2.destroyAllWindows()
video.release()
