import cv2
import numpy


def frame_to_text_image(frame, density, size, ascii_values):
    gray = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (int(size[0] / density), int(size[1] / density)), interpolation=cv2.INTER_AREA)

    resized = numpy.round(numpy.asarray(gray, dtype=float) / 255, 1)

    display_matrix = numpy.vectorize(ascii_values.get)(resized)

    display_matrix = numpy.repeat(display_matrix, 2, axis=1)

    string_list = [''.join(map(str, line)) for line in display_matrix]
    text = '\n'.join(map(str, string_list))

    return text


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

video = cv2.VideoCapture('This is a Bucket Long.mp4')
success, video_frame = video.read()

video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
how_many_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
character_density = 5
frame_skip = 5  # więcej niż 1 i mniej niż how_many_frames
fps = video.get(cv2.CAP_PROP_FPS) / frame_skip

success_count = 1
conversion_count = 1

file = open('This is a Bucket Long.txt', 'x')

while success:
    if success_count % frame_skip == 0:
        file.write(frame_to_text_image(video_frame, character_density, (video_width, video_height), ascii_codes))
        file.write('\n\n')
        print('Lasting frames: ', round(how_many_frames/frame_skip)-conversion_count, flush=True)
        conversion_count += 1

    success, video_frame = video.read()
    success_count += 1

file.close()
cv2.destroyAllWindows()
video.release()
