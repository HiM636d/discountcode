
from django.core import management
from django.test import TestCase
from django.core.management import call_command
import json
from io import StringIO

class CommandTestCase(TestCase):
    def test_mkvoucher(self):
        out=StringIO()
        call_command('mkvouchers','10 agenctva',stdout=out)
        set.assertEqual(out.getvalue(),'the file must have 10 codes and 1 groups.')
        

