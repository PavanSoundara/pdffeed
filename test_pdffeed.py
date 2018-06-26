import sys
import unittest
import pdffeed
from pdfminer.pdfdocument import PDFSyntaxError

IS_PY2 = sys.version_info < (3, 0)

if IS_PY2:
    # Python 2
    from urllib2 import URLError, HTTPError
else:
    # Python 3
    from urllib.request import URLError, HTTPError

class TestPdfFeed(unittest.TestCase):

    def test_dumping(self):
        #Downloaded from http://gahp.net/wp-content/uploads/2017/09/sample.pdf
        #Test local file
        self.assertEqual(pdffeed.feeder(['sample.pdf']),
        ["ftp://ftp.mimuw.edu.pl/pub/Mirrors/Linux/redhat-5.2/",
        "http://www.adobe.com/",
        "ftp://ftp.task.gda.pl/pub/linux/redhat-contrib/",
        "http://www.mimuw.edu.pl/"])

        #Test remote file via URL
        self.assertEqual(pdffeed.feeder(['http://pavansoundara.com/files/PavanSoundara-Resume.pdf']), 
        ["http://pavansoundara.com",
        "mailto:pavansoundara@gmail.com",
        "https://github.com/pavansoundara",
        "https://www.linkedin.com/in/pavansoundara",
        "http://web.archive.org/web/20150618014223/http://www.beclasses.com:80/",
        "http://pavansoundara.com/lp.jpg",
        "https://sharemyworks.com",
        "https://github.com/PavanSoundara/Facial-expression-recognition",
        "https://github.com/teamvaps/Intelligent-Help-Desk",
        "http://pavansoundara.com/folio/flyer-landscape.png",
        "http://pavansoundara.com/team-landing-page/",
        "http://pavansoundara.com/folio/poster3hd.jpg",
        "http://pavansoundara.com/folio/phpbb-theme.jpg"])

        #Test pdf file with no links
        self.assertEqual(pdffeed.feeder(['http://www.africau.edu/images/default/sample.pdf']),[])

        #Test doc file
        self.assertRaises(PDFSyntaxError,pdffeed.feeder, ['sample.doc'])

        #Test non working url
        self.assertRaises(URLError,pdffeed.feeder, ['http://pavnsoundara.com'])

        #Test wrong file name
        self.assertRaises(IOError,pdffeed.feeder, ['sampl.pdf'])
        self.assertRaises(IOError,pdffeed.feeder, ['rteafsaa'])

        #Test file not found on server
        self.assertRaises(HTTPError,pdffeed.feeder, ['http://pavansoundara.com/files/PavanSoundara-Resume.pd'])

if __name__ == '__main__':
    unittest.main()