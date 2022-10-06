import csv
import re

class FetchRecord():

    FILE_NAME = ""
    
    def __init__(self,file_name = "Records.csv"):
        self.FILE_NAME = file_name

    def fetch_all_records(self,file_name=FILE_NAME):
        """This method fetches all records in the source file"""
        headers = ()
        with open(file=self.FILE_NAME,mode="r") as file:
            read_object = csv.DictReader(file)
            fieldnames = read_object.fieldnames
            dict_row = list(read_object)
            # for row in dict_row:
            #     print(row)
        return (dict_row,fieldnames)

    def fetch_by_birthday(self,day,month):
        """This method fetches records with matching DoB and returns a list of dictionaries"""
        out_record = []
        search_string = "{:02d}-{:02d}".format(day,month)
        all_records= self.fetch_all_records()[0]
        for record in all_records:
            if search_string in record["DoB"]:
                print(search_string + " matched with " + record["DoB"]) 
                out_record.append(record)
        return out_record

    def fetch_by_fieldname(self,fieldname,value,ignore_case = True):
        """This method fetches records with matching header value and returns a list of dictionaries"""
        out_record = []

        print("Searching for {} in column {}".format(value,fieldname))

        all_records,fieldnames = self.fetch_all_records()
        if fieldname not in fieldnames:
            raise ValueError("Result: Fieldname must be one of these: {}".format(fieldnames))
        if ignore_case : value = value.lower()
        for record in all_records:
            if ignore_case and record[fieldname].lower() == value:
                out_record.append(record)
            if not ignore_case and record[fieldname] == value:
                out_record.append(record)
        
        return out_record

def main():
    record_object = FetchRecord()
    all_records = record_object.fetch_all_records()
    print(all_records)

if __name__ == "__main__":
    print("This script fetches records from source CSV file")
    main()







