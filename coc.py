import uuid
import json
from datetime import datetime as dt
import os
import sys
import hashlib
import logging
from collections import Counter
import shutil
import getpass
from datetime import datetime

author_details = {
        "Name": "Adam Doukani",
        "Location": "Malaysia",
        "Country": "Algeria"
}

author_name = author_details["Name"]
author_location = author_details["Location"]
author_country = author_details["Country"]

print("*" * 40)
print("\t   By {}".format(author_name))
print("*" * 40)
print("\tChain of Custody Report")
print("*" * 40)
def create_ev_file():
    try:
        add_name = {
        "Agency_Name": str(input("AgencyName: ")),
        "Item_Number": str(input("Item Number: ")),
        "Case_Number": str(input("Case Number: ")),
        "Date_of_Collection": str(input("Date of Collection: ")),
        "Time_of_Collection": str(input("Time of Collection: ")),
        "Collected_By": str(input("Collected By: ")),
        "Description": str(input("Description of Evidence: ")),
        "Location": str(input("Location of Evidence: ")),
        "Type_of_Offense": str(input("Type of Offense: ")),
        "Victim": str(input("Victim: ")),
        "Suspect": str(input("Suspect: ")),
        }
        agency_name = add_name["Agency_Name"]
        item_number = add_name["Item_Number"]
        case_number = add_name["Case_Number"]
        date_of_collection = add_name["Date_of_Collection"]
        time_of_collection = add_name["Time_of_Collection"]
        collected_by = add_name["Collected_By"]
        description = add_name["Description"]
        location = add_name["Location"]
        type_of_offense = add_name["Type_of_Offense"]
        victim = add_name["Victim"]
        suspect = add_name["Suspect"]

        random_id = uuid.uuid1()
        on_usage = True
        my_file_name = str(random_id.node)
        file = open(my_file_name + ".pdf", "x")
        file.write("Agency Name: \t\t" + agency_name + "\n")
        file.write("Item Number: \t\t" + item_number + "\n")
        file.write("Case Number: \t\t" + case_number + "\n")
        file.write("Date of Collection: \t\t" + date_of_collection + "\n")
        file.write("Time of Collection: \t\t" + time_of_collection + "\n")
        file.write("Collected By: \t\t" + collected_by + "\n")
        file.write("Description of Evidence: \t" + description + "\n")
        file.write("Location of Evidence: \t\t" + location + "\n")
        file.write("Type of Offense: \t\t" + type_of_offense + "\n")
        file.write("Victim: \t\t\t" + victim + "\n")
        file.close()
    except:
        print("Error While Writing to File ..")

    while on_usage:
        try:
            available_algorithms = {
                "sha1": hashlib.sha1,
                "sha256": hashlib.sha256,
                "sha512": hashlib.sha512
            }

            input_file = my_file_name + ".pdf"
            hash_alg = input("Specify hashing algorithm: sha1 | sha256 | sha521: ")
            file_name = available_algorithms[hash_alg]()
            abs_path = os.path.abspath(input_file)
            file_name.update(abs_path.encode())
            file_content = available_algorithms[hash_alg]()
            my_hash = file_content.hexdigest()
            now = datetime.now()
            x = getpass.getuser()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            file = open(my_hash + ".pdf", "a+")
            file.write("\nCreated By {}\nOn {} \n{} hash is: {} \nfor {}\n\n".format(x, dt_string, hash_alg , my_hash, input_file))
            print("Evidence Created Successfully")
            print("Report Generated Successfully")
            file.close()
            on_usage = False
        except:
            print("That was not an option, please choose again")

create_ev_file()
