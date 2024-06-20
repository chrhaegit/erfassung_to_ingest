import sys
import shutil
from openpyxl import load_workbook
from pathlib import Path

class ExcelMapping:
    def __init__(self, inputfile, destinationfile):
        self.wb_input = load_workbook(inputfile, data_only=True)
        self.ws_input = self.wb_input["data sheet"]

        self.ingest_path = destinationfile
        self.wb_ingest = load_workbook(destinationfile)
        self.ws_ingest = self.wb_ingest["data sheet"]

    def colindex_bycolname(self, currworksheet, colname):
        retcolindex = 0

        for colindex in range(1, 50):
            header_name = currworksheet.cell(row=1, column=colindex).value
            if header_name == colname:
                retcolindex = colindex
                break
        return retcolindex

    def do_mappings(self, test_mappings):
        success = True
        for src_colname, src_rownr, dest_colname, dest_rownr in test_mappings:
            src_colind = self.colindex_bycolname(self.ws_input, src_colname)
            if not src_colind:
                print(f"Error: No source header[{src_colname}] found in the input.xlsx")
                success = False
                break

            source_cell_value = self.ws_input.cell(src_rownr, src_colind).value
            dest_colind = self.colindex_bycolname(self.ws_ingest, dest_colname)            
            if not dest_colind:
                print(f"Error: No destination header[{dest_colname}] found in the ingest-template")
                success = False
                break

            self.ws_ingest.cell(dest_rownr, dest_colind).value = source_cell_value
        if success:
            self.wb_ingest.save(self.ingest_path)
        return success

def test_mappings():
    # Define mappings of header names from inputfile.xlsx to ingest.xlsx
    return [
        ('Name', 2, 'Name', 4),
        ('Name', 2, 'Name2', 4),
        ('Vorname', 2, 'Vorname', 4)
    ]

def filehandling(template_path, ingest_path):
    if ingest_path.exists():
        ingest_path.unlink()
    
    if not template_path.exists():
        print("Error: templates.xlsx file not found.")
        return
    
    shutil.copy(template_path, ingest_path)
    print(f"Copied {template_path} to {ingest_path}")

def main(inputfile):
    print("*" *20, "  START  ", "*" *20)
    filehandling(Path('./data/templates.xlsx'), Path('./ingest.xlsx'))
    
    mapping = ExcelMapping(inputfile, Path('./ingest.xlsx'))
    if mapping.do_mappings(test_mappings()):
        print(f"sucessfully created ingest-excel!")
    print("*" *20, "  ENDE  ", "*" *20)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <inputfile>")
        sys.exit(1)

    inputfile = sys.argv[1]
    main(inputfile)