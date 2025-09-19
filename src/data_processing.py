import os
import csv

# Set the path to your image folder and CSV file
image_folder = r'C:\Users\muham\OneDrive\Desktop\yolo_dataset\Brazil\files'
csv_file = r'C:\Users\muham\OneDrive\Desktop\yolo_dataset\Brazil\labels\Brazil_domain1_p1_samples.csv'

# Get the list of image names in the folder
image_names = os.listdir(image_folder)

# Open the CSV file and read its contents
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Sort the CSV data based on the image names
sorted_data = sorted(data, key=lambda x: image_names.index(x[0]) if x[0] != '' else -1)

# Write the sorted data to a new CSV file
with open('sorted_' + csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sorted_data)
