pdffeed
============
A simple pdf hyper links extractor based on pdfminer.Parses pdf file and returns all the hyperlinks as an array.
The technique to check if the input path is URL or local file is adopted from pdfx.

Example Usage
------------
For globally accessing pdffeed module, copy the pdffeed.py file to ``your-python-path/site-packages``.
```
 >>> import pdffeed
 >>> links = pdffeed.feeder(['http://pavansoundara.com/files/PavanSoundara-Resume.pdf'])
```
