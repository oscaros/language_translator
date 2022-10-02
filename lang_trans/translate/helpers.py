

import csv

from .models import LanguagesModel



def load_languages():
    with open("/home/godwin/Desktop/cit/group assignment/language_translator/lang.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = LanguagesModel.objects.get_or_create(
                name=row[1],
                iso_code=row[2],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created