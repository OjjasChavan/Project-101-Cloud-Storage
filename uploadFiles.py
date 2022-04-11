import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open (local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'https://www.dropbox.com/sh/7oy1nnxkc3117k0/AACyHRrwpBO5317P-sqH96qka?dl=0'
    transfer = TransferData(access_token)
    file_from = str(input("Enter the folder path to transfer: "))
    file_to = str(input("Enter the full path to upload to dropbox: "))

    transfer.upload_file(file_from, file_to)
    print("Transfer complete!")

main()