import csv
import os
from fmt import Fmt


class CSVFormatter(Fmt):
    def parse_file(self):
        csvf = f"{self.get_provider_file()}.csv"
        txtf = f"{self.get_provider_file()}.txt"
        if not os.path.isfile(csvf):
            with open(csvf, 'w', newline='') as f:
                w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                with open(txtf) as ftxt:
                    for line in ftxt:
                        line = line.rstrip('\n').split('-')
                        w.writerow(line)
            return os.path.realpath(csvf)
        else:
            return os.path.realpath(csvf)

