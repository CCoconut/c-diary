#!/usr/bin/env python
import os.path
import datetime

program_open = 1

# This function writes input data to a text file with today's date as a filename and header
def diary_write():
	diary_entry = open(str(date), "w");
	diary_entry.write(str(date) + "\n");
	dream = input("Write your entry here: \n");
	diary_entry.write(dream);
	diary_entry.close();

def diary_log():
	diary_log = open("Entry Dates", "a");
	diary_log.write(str(date) + "\n");
	diary_log.close();

# This function reads text file contents and prints it for the user to read. Need to find a way to make it
# only able to read files with YYYY-MM-DD as a filename format.
def diary_read():
	while answer == 'read':
		read_entry_yes = input("\nWhat is the date of the entry? (yyyy-mm-dd) If you want to stop reading, type stop: ");
		if read_entry_yes == "stop":
			break
		elif os.path.lexists(read_entry_yes) == False:
			print("\nYou didn't write an entry that day.");
			continue
		else:
			diary_read = open(read_entry_yes, "r");
			print("\n" + diary_read.read());
			diary_read.close();
			continue

# Version 0.2.1: Now asks for a command instead of if the user dreamt. This is to make it more general than
# just a dream journal (can be used as any kind of diary now). The while loop ensures that it will always
# go back to 'What do you want to do?' before the program quits. Also logs dates that have entries.
while program_open == 1:
	answer = input("\nWhat do you want to do? (Type 'help' for a list of commands): ");
	if answer == 'write':
		date = datetime.date.today();
		if os.path.lexists(str(date)) == True:
			print("\nYou already wrote an entry for today!");
		else:
			diary_write();
			diary_log();
	elif answer == 'read':
		diary_read();
	elif answer == 'help':
		print("\nValid commands are: " + "\n'write' (write an entry)" + "\n'read' (read entries)" + "\n'help' (display this menu)" + "\n'entries' (see what dates have entries)" + "\n'quit'");
	elif answer == 'entries':
		entry_dates = open("Entry Dates", "r");
		print("\n" + entry_dates.read());
	elif answer == 'quit' or 'exit':
		break
	else:
		print("\nThat is not a valid command.");
print("\nHave a nice day!\n");
