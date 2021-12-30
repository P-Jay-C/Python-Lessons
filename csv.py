import csv

with open('data.csv', 'r') as csv_file:

    csv_reader  = csv.DictReader(csv_file)
    '''
    for line in csv_reader:
        print(line['Responder_id'])
    '''         

    fieldnames = ['Responder_id','LanguagesWorkedWith']
    with open('new_data.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames ,delimiter =',')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
 