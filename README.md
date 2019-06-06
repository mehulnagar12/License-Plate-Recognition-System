# LICENSE PLATE RECOGNITION SYSTEM
--------------------------------------

## Module Used:
1. Open-CV East Text Detection: EAST is an Efficient and Accurate Scene Text detection pipeline. 
	In summary, EAST detects text in an image (or video) and provides geometry and confidence 
	scores for each block of text it detects.
2. Used MySql Database to store the value of the License plate that is detected and if the plate detected is present
   int the database, then the amount is deducted from the corresponding person's account.

Video will be captured using the camera which is converted into the frame, from which the text is extracted and stored
in the database.

**VideoToFrame.ipynb** converts each frame of the video into image.
**TextRecognizerFinal.ipynb** Detects the text from that frame and compares the value into the database and performs the
required operations
