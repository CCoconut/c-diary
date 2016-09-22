#!/usr/bin/env python
import os.path;
import datetime;

# Version 0.2.2: P-Diary will now always write and read files to/from whatever directory the script is in.

program_open = 1;
directory = os.path.dirname(os.path.realpath(__file__));

# This function writes input data to a text file with today's date as a filename and header
def diary_write():
	diary_entry = open(os.path.join(directory, str(date)), "w");
	diary_entry.write(str(date) + "\n");
	dream = input("Write your entry here: \n");
	diary_entry.write(dream);
	diary_entry.close();

def diary_log():
	diary_log = open(os.path.join(directory, "Entry Dates"), "a");
	diary_log.write(str(date) + "\n");
	diary_log.close();

# This function reads text file contents and prints it for the user to read. Need to find a way to make it
# only able to read files with YYYY-MM-DD as a filename format.
def diary_read():
	while answer == 'read':
		read_entry_yes = input("\nWhat is the date of the entry? (yyyy-mm-dd) If you want to stop reading, type stop: ");
		if read_entry_yes == "stop":
			break
		elif os.path.lexists(os.path.join(directory, read_entry_yes)) == False:
			print("\nYou didn't write an entry that day.");
			continue
		else:
			diary_read = open(os.path.join(directory, read_entry_yes), "r");
			print("\n" + diary_read.read());
			diary_read.close();
			continue

# The while loop ensures that it always goes back to 'What do you want to do?' unless the user
# exits the program.
while program_open == 1:
	answer = input("\nWhat do you want to do? (Type 'help' for a list of commands): ");
	if answer == 'write':
		date = datetime.date.today();
		if os.path.lexists(os.path.join(directory, str(date))) == True:
			print("\nYou already wrote an entry for today!");
		else:
			diary_write();
			diary_log();
	elif answer == 'read':
		diary_read();
	elif answer == 'help':
		print("\nValid commands are: " + "\n'write' (write an entry)" + "\n'read' (read entries)" + "\n'help' (display this menu)" + "\n'entries' (see what dates have entries)" + "\n'quit'");
	elif answer == 'entries':
		entry_dates = open(os.path.join(directory, "Entry Dates"), "r");
		print("\n" + entry_dates.read());
	elif answer == 'quit' or answer == 'exit':
		break
	else:
		print("\nThat is not a valid command.");
print("\nHave a nice day!\n");
