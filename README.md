<h1>ASCIIconverter</h1>
<p>ASCIIconverter is a Python project that takes an image or video as input and converts it into ASCII art text or video.</p>

<p>The project includes two programs: image_to_txt.py and main.py. The image_to_txt.py program converts a video into a text document, and the main.py program converts a video into an ASCII video based on the text.</p>

<p>You can modify the parameters directly in the code, which include:<p>
<ul>
<li>character_density: the number of characters per frame of the video.</li>
<li>frame_skip: the number of frames to skip before rendering the processed image.</li>
<li>video = cv2.VideoCapture('ToConvert/nazwa_pliku_do_przetworzenia.mp4'): the name and location of the file to be processed.</li>
<li>converted_video = cv2.VideoWriter('Converted/przetworzony_plik.avi', 0, fps, (video_width, video_height)): the name and location of the processed file.</li>
<li>font = ImageFont.truetype('Fonts/nazwa_czcionki.ttf', density + 1): the name and location of the font to be used.</li>
<li>image = Image.new("RGB", (width, height), color='black'): the background color of the text document.</li>
<li>d.text((x * density + (density * 0.25), y * density), display_matrix[y][x], font=font, fill='white'): the color of the font.</li>
</ul>
<p><b>Please note that no file with the same name as the processed file can exist in the target directory for the programs to work properly.</b></p>

<h2>Requirements</h2>
<p>To run ASCIIconverter, you will need to install the following Python packages:</p>
<ul>
<li>OpenCV (cv2)</li>
<li>Pillow (PIL)</li>
</ul>

<p>You can install them using pip:</p>
`pip install opencv-python pillow`


<h2>Usage</h2>
<ol>
<li>Clone or download the ASCIIconverter repository.</li>
<li>Navigate to the project directory.</li>
<li>Place the video or image you want to convert in the ToConvert directory.</li>
<li>Modify the parameters in the code if necessary.</li>
<li>Run the appropriate program based on your desired output:</li>
</ol>

<p>To convert a video to ASCII text: `python image_to_txt.py`</p>
<p>To convert a video to an ASCII video: `python main.py`</p>

<p>The converted file will be saved in the Converted directory.</p>

<h2>Credits</h2>
<p>ASCIIconverter was created by Piotr Szamocki.<p>
