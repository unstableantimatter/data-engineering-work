import csv
with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
#  print(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])
    
    
import csv
with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
    
    
import csv
with open('books.csv', newline='') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])
    print(row['ISBN'])
    
# Concat csvs into formatted CSV 
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
    
# JSON Object read/write
import json
with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
  
# Turning Python objects to JSON  files
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}]
import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
  

#  Hacker Project

import csv
import json

compromised_users = []
with open('passwords.csv', 'r') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user + '\n')

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 

'''
    new_passwords_obj.write(slash_null_sig)
