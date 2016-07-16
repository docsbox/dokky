import time
import dokky
import unittest


class DokkyTestCase(unittest.TestCase):

    def setUp(self):
        self.docsbox = dokky.Docsbox()

    def test_basic(self):
        document = self.docsbox.process(open("tests/samples/easychair.docx", "rb"), formats=["txt"])
        self.assertTrue(document.id)
        self.assertEqual(document.status, "queued")
        while True: # wait for result
            self.assertIn(document.get_status(), ["queued", "started", "finished"])
            if document.status in ("queued", "started"):
                time.sleep(1)
            elif document.status == "finished":
                break
            else:
                raise ValueError(document)
        result = document.get_result()
        with result.open("txt") as text:
            body = text.read().decode("utf-8")
            self.assertIn("chair", body)
