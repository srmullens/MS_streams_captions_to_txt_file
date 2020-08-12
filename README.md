# dms_to_txt
Convert closed captioned .dms files (for example, used on Microsoft Streams) to .txt files.

## Example case: Course lectures
As a college lecturer, I make videos for my class. My university has purchased access to the Microsoft Office suite of software, which includes Microsoft Streams. To make my videos accessible to students with hearing disabilities, I allow Streams to auto-generate a closed caption file for my video. Like all closed-captions generated automatically by software, it's not perfect and I need to manually revise and edit the file. 

To make my lectures accessible to those with poor or no internet connection, I transfer these closed captions, which are now transcriptions of what I said in the lecture, back to PowerPoint. By placing what I said in the notes section of each slide, you can go into the print settings and set it to the Notes view of the slides. This generates pages that have the slide on the top, and your notes section (which is now your transcription) below the slide. Instead of printing, you can use the menu typically at the bottom of the print settings to "Save as PDF." That PDF can be placed next to your video in your Course Management System (Canvas, Moodle, etc.). 

But how do you get your transcriptions to the notes section easily? On Streams, you can do a lot of work to manually copy and past each individual line. That's no good. You can download the captioned file, with its .dms file extension, but you are still required to do a lot of manual work to format that text into the paragraphs you want. And although you edited the file in the beginning, you can miss things.

## Code features
So, I wrote this code to automatically process the .dms files and turn it into a text file with one long paragraph. With this, the simpler task is to divide your transcript into meaningful paragraphs. It's now easier to copy and paste the paragraphs into PowerPoint to produce the PDFs you desire. 

In addition, the code outputs things for you to check out and manually find and replace in a more targeted way. In 2020, Streams appears to favor British spellings, which is inappropriate for a manual audience. It often splits hyphenated words between lines. It suggests the word 'tored' instead of "toward," which I haven't found is an actual word. So these issues are either changed for you (e.g. tored) or flagged for you to edit as you please (e.g. colour, metre). 

Just for fun, simple statistics are provided, including total words, the number of unique words, and the ten most common words. No, I have not filtered out words like 'to' or 'and'. This is my code, and I'm having fun. 

Finally, the resulting text is output in a text file. The name of the text file is modified to remove the extra formatting Streams applies to the .dms file. Instead of 'Modified_AutoTranscript_captions_1.dms,' you now have just 'captions.txt'.

## Plea for help.
I would love for this code to be more accessible to folks who don't work with Python, UNIX, and terminals regularly. But I don't know how to turn this into an application, much less one that is easy to use. So somebody please help turn this into an application that works on Mac and Windows, so this can be distributed to colleagues more freely. Thanks.
