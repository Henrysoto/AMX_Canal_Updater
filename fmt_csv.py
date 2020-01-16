import os
import csv


class CSVFormatter:
    def __init__(self, version, provider):
        self.version = version
        self.provider = str(provider)
    
    def get_provider_dir(self):
        return os.path.join('.', 'channels', self.provider.capitalize(), '')
    
    def get_provider_file(self):
        path = self.get_provider_dir()
        return f"{path}{self.provider.lower()}_{self.version}"
    
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
        
        return csvf
    
