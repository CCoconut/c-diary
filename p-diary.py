#/!/usr/bin/env python
import os, datetime, textwrap;

# Version 0.3.2: p-diary now supports multiple diaries. Each one is its own directory. Also asks for confirmation before sending an entry.

directory = os.path.join(os.path.expanduser('~'),'p-diary');
program_open = 1;

if os.path.exists(directory) == True:
	print("\nWelcome!");
else:
	print("\nWelcome to p-diary! You have no diaries, so type 'new' in the next prompt!");
	os.mkdir(directory);

# This function creates a new diary.
def create_directory():
	new_diary = input("\nName your diary (type 'cancel' to go back): \n");
	if new_diary == "cancel":
		print("\nOkay.");
	elif new_diary == "new" or new_diary == "exit" or new_diary == "quit" or new_diary == "help" or new_diary == "diaries":
		print("\nThat is not a valid name! That is reserved for a command!");
	else:
		os.mkdir(os.path.join(directory,new_diary));
		new_diary_log = open(os.path.join(directory, "Diaries"), "a");
		new_diary_log.write(new_diary + "\n");
		new_diary_log.close();

def Diaries():
	see_diaries = open(os.path.join(directory, "Diaries"), "r");
	print("\n" + see_diaries.read());

# This function writes an entry date to a file that can be called up as a reminder
def diary_log():
	diary_log = open(os.path.join(set_directory, "Entry Dates"), "a");
	diary_log.write(str(date) + "\n");
	diary_log.close();

# This function writes input data to a text file with today's date as a filename and header
def diary_write():
	global diary_entry;
	diary_entry = open(os.path.join(set_directory, str(date)), "w");
	global dream;
	dream = input("\nWrite your entry here (type 'cancel' and press enter to go back): \n");
	if dream == 'cancel':
		diary_entry.close();
		os.remove(os.path.join(set_directory, str(date)));
	else:
		diary_write_confirm();

# This function is for confirmation of writing an entry
def diary_write_confirm():
	confirm = input("\nDo you want to write this entry? (y/n): ");
	if confirm.lower()[0] == 'y':
		diary_entry.write("(" + str(date) + ")" + "\n");
		diary_entry.write(dream);
		diary_entry.close();
		diary_log();
	elif confirm.lower()[0] == 'n':
		diary_entry.close();
		os.remove(os.path.join(set_directory, str(date)));
	else:
		print("\nPlease use 'y' or 'n'.");
		diary_write_confirm();

# This function lets you read the entry dates file to see which dates have entries
def diary_entries():
	entry_dates = open(os.path.join(set_directory, "Entry Dates"), "r");
	print("\n" + entry_dates.read());

# This function reads text file contents and prints it for the user to read. Need to find a way to make it
# only able to read files with YYYY-MM-DD as a filename format. (does not yet do regex)
def diary_read():
	while answer2 == 'read':
		read_entry_yes = input("\nWhat is the date of the entry? (Type 'help' to see other commands): ");
		if read_entry_yes == "exit":
			break
		elif read_entry_yes == "entries":
			diary_entries();
		elif read_entry_yes == "help":
			print("\nValid commands are: " + "\n'help' (display this menu)" + "\n'entries' (see what dates have entries)" + "\n'today' (read today's entry)" + "\n'exit' (stop reading entries)" + "\nInput an entry date to read it");
		elif read_entry_yes == "today" and os.path.lexists(os.path.join(set_directory, str(datetime.date.today()))) == True:
			diary_read_today = open(os.path.join(set_directory, str(datetime.date.today())), "r");
			print("\n" + textwrap.fill(diary_read_today.read(), 80));
			diary_read_today.close();
		elif os.path.lexists(os.path.join(set_directory, read_entry_yes)) == False:
			print("\nYou didn't write an entry that day (or you typed an invalid command!)");
		else:
			diary_read = open(os.path.join(set_directory, read_entry_yes), "r");
			print("\n" + textwrap.fill(diary_read.read(), 80));
			diary_read.close();

# Main body of program. Asks for which diary to look at then gives the option to read, see entries, and write)
while program_open == 1:
	answer1 = input("\nWhich diary do you want to look at? (type 'help' for commands): ");
	if answer1 == "new":
		create_directory();
	elif answer1 == "help":
		print("\nValid commands are: " + "\n'new' (create a new diary)" + "\n'diaries' (see a list of your diaries)" + "\n'help' (display this menu)" + "\n'exit' (exit)" + "\nWrite the name of the diary you want to look at");
	elif answer1 == "diaries":
		Diaries();
	elif answer1 == "quit" or answer1 =="exit":
		break
	else:
		global set_directory;
		set_directory = os.path.join(directory,answer1);
		if os.path.exists(set_directory) == False:
			print("\nThat diary doesn't exist!");
		else:
			while os.path.exists(set_directory) == True:
				answer2 = input("\nWhat do you want to do? (Type 'help' for a list of commands): ");
				if answer2 == 'write':
					date = datetime.date.today();
					if os.path.lexists(os.path.join(set_directory, str(date))) == True:
						print("\nYou already wrote an entry in this diary today!");
					else:
						diary_write();
				elif answer2 == 'read':
					diary_read();
				elif answer2 == 'help':
					print("\nValid commands are: " + "\n'write' (write an entry)" + "\n'read' (read entries)" + "\n'help' (display this menu)" + "\n'entries' (see what dates have entries)" + "\n'exit'");
				elif answer2 == 'entries':
					diary_entries();
				elif answer2 == 'quit' or answer2 == 'exit':
					break
				else:
					print("\nThat is not a valid command.");
print("\nHave a nice day!\n");

# List of bugs or changes I need to implement:
# Confirmation doesn't take you back to edit your entry. I want to figure out a way to do this.
# Better entry management - right now you can only access files by typing in their date or 'today'. I'd like to implement entry numbers to make it easier.
# Calendars
