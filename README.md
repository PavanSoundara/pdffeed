# pdffeed

A simple pdf hyper links extractor based on pdfminer. Parses pdf file and returns all the hyperlinks as an array. The technique to check if the input path is URL or local file is adopted from pdfx.

### Prerequisites
For this module to work, it needs PDFMiner installed.

* PDFMiner.six - https://github.com/pdfminer/pdfminer.six
* PDFMiner - https://github.com/euske/pdfminer


### Example Usage
pdffeed works with both local files and urls.For globally accessing pdffeed module, copy the pdffeed.py file to ``your-python-path/site-packages``.
```
import pdffeed
links = pdffeed.feeder(['http://pavansoundara.com/files/PavanSoundara-Resume.pdf'])
file_links = pdffeed.feeder(['sample.pdf'])
```
