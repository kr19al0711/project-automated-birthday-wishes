import unittest
from fetch_records import FetchRecord

class TestRearrange(unittest.TestCase):

    def test_fetch_all_records1(self):
        all_records_list = [{'Name': 'Kripal', 'DoB': '07-11-1998', 'Relation': 'Me', 'Email': 'kripalparsekar@gmail.com'}, {'Name': 'Suyan', 'DoB': '25-11-1997', 'Relation': 'Friend', 'Email': 'suyanbelurkar@gmail.com '}, {'Name': 'Bhargavi', 'DoB': '03-12-1997', 'Relation': 'Friend', 'Email': 'bhargavi.tilve@gmail.com '}, {'Name': 'Shriyan', 'DoB': '05-06-1997', 'Relation': 'Friend', 'Email': 'snarolkar@gmail.com '}, {'Name': 'Barood', 'DoB': '07-11-2022', 'Relation': 'Friend', 'Email': 'kripalparsekar.it@gmail.com'}]
        test_fieldnames = ['Name', 'DoB', 'Relation', 'Email']
        fetch_object = FetchRecord()
        all_records,fieldnames = fetch_object.fetch_all_records()
        self.assertEqual(all_records,all_records_list)
        self.assertEqual(fieldnames,test_fieldnames)

    def test_fetch_by_birthday1(self):
        test_record = [{'Name': 'Kripal', 'DoB': '07-11-1998', 'Relation': 'Me', 'Email': 'kripalparsekar@gmail.com'},{'Name': 'Barood', 'DoB': '07-11-2022', 'Relation': 'Friend', 'Email': 'kripalparsekar.it@gmail.com'}]
        fetch_object = FetchRecord()
        self.assertEqual(fetch_object.fetch_by_birthday(7,11),test_record)

    


if __name__ == "__main__":
    print("Running unit test for fetch_records.py")
    unittest.main()