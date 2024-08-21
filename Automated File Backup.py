import os
import shutil
import datetime
import schedule
import time

source_dir = "E:/Downloads/Fireshot"
destination_dir = "E:/Downloads/Fireshot_backup"


def copy_folder_to_directory(source, destination):
    today = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
    destination_dir = os.path.join(destination, today)

    try:
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")


schedule.every().day.at("10:30").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
