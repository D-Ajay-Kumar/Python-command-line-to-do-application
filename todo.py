import sys
from datetime import date
import os.path



todo_file_name = "todo.txt"
done_file_name = "done.txt"



# shows all the todos in reverse order when ls is passed
def show_all_todos_in_reverse():

	if os.path.isfile(todo_file_name):
	    todo_file_read = open(todo_file_name, 'r')
	    todo_file_data = todo_file_read.readlines()
	    todo_count = len(todo_file_data)
	    todo_string = ""

	    for todo in todo_file_data:
	    	todo_string += '[{}] {}'.format(todo_count , todo)
	    	todo_count -= 1

	    todo_utf8 = todo_string.encode('utf8')
	    sys.stdout.buffer.write(todo_utf8)

	else:
	    print ("There are no pending todos!") 
		


# shows the report
def show_report():

	pending_todo_count = 0
	done_todo_count = 0
	if os.path.isfile(todo_file_name):
	    todo_file_read = open(todo_file_name,'r')
	    todo_file_data = todo_file_read.readlines()
	    pending_todo_count = len(todo_file_data)
	if os.path.isfile(done_file_name):
	    done_file_read = open(done_file_name,'r')
	    done_file_data = done_file_read.readlines()
	    done_todo_count = len(done_file_data)
	todo_string =  str(date.today()) + " Pending : {} Completed : {}".format(pending_todo_count, done_todo_count)
	
	todo_string_utf8 = todo_string.encode('utf8')
	sys.stdout.buffer.write(todo_string_utf8)



# delete the todo whose number is passed as argument
def delete_todo_from_file(todo_num):

	if os.path.isfile(todo_file_name):
	    todo_file_read = open(todo_file_name,'r')
	    todo_file_data = todo_file_read.readlines()
	    todo_count = len(todo_file_data)

		# if invalid todo number is passed in arguments
	    if todo_num > todo_count or todo_num <= 0:
	    	print(f"Error: todo #" + str(todo_num) + " does not exist. Nothing deleted.")

		# if valid number is passed
	    else:
	    	todo_file_write = open(todo_file_name,'w')
	    	for todo in todo_file_data:
	    		if todo_count != todo_num:
	    			todo_file_write.write(todo)
	    		todo_count -= 1
	    	print("Deleted todo #" + str(todo_num))

	else:
	    print("Error: todo #" + str(todo_num) + " does not exist. Nothing deleted.")


# shows help catalogue with all valid functions when no arg is passed or when help is passed
def show_help():

	catalogue = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""

	# prints the above catalogue in utf8 encoding as normal print() wasn't working
	catalogue_utf8 = catalogue.encode('utf8')
	sys.stdout.buffer.write(catalogue_utf8)


	
# adds new todo to the todo.txt file
def add_todo_to_file(todo_string):
	
	# if todo.txt exists then append new todo at top
	if os.path.isfile(todo_file_name):					
	    todo_read_file = open(todo_file_name,'r')
	    todo_file_data  =  todo_read_file.read()

	    todo_file_write = open(todo_file_name,'w')
	    todo_file_write.write(todo_string + '\n' + todo_file_data)

	# if todo.txt doesn't exist then create it and then add new todo
	else:
	    todo_file_write = open(todo_file_name,'w')
	    todo_file_write.write(todo_string + '\n')

	print('Added todo: "' + todo_string + '"')



# removes finished todo from todo.txt and adds it to done.txt file
def mark_todo_as_done(todo_num):

	if os.path.isfile(todo_file_name):
	    todo_file_read = open(todo_file_name,'r')
	    todo_file_data = todo_file_read.readlines()
	    todo_count = len(todo_file_data)
	    if todo_num > todo_count or todo_num  <= 0:
	    	print("Error: todo #" + str(todo_num) + " does not exist.")
	    else:
	    	with open(todo_file_name,'w') as todo_file_write:
	    		if os.path.isfile(done_file_name):						
	    			with open(done_file_name,'r') as done_file_read:
				    	done_file_data = done_file_read.read()
			    	with open(done_file_name,'w') as done_file_write:
			    		for todo in todo_file_data:
			    			if todo_count == todo_num:
			    				done_file_write.write("x " + str(date.today()) + " " + todo)
			    			else:
			    				todo_file_write.write(todo)
			    			todo_count -= 1
			    		done_file_write.write(done_file_data)
		    	else:
		    		with open(done_file_name,'w') as done_file_write:
			    		for todo in todo_file_data:
			    			if todo_count == todo_num:
			    				done_file_write.write("x " + str(date.today()) + " " + todo)
			    			else:
			    				todo_file_write.write(todo)
			    			todo_count -= 1

	    	print("Marked todo #" + str(todo_num) + " as done.")

	else:
	    print("Error: todo #" + str(todo_num) + " does not exist.")



# this main function is called in the very beginning
def main(): 

	# no arg is passed then show help by default 
	if ( len(sys.argv) == 1 ):
		show_help()


	# when help arg is passed then show help
	elif ( sys.argv[1] == 'help' ): 
		show_help()


	# when list of todos is asked
	elif ( sys.argv[1] == 'ls' ): 
		show_all_todos_in_reverse()


	# when new todo is added
	elif ( sys.argv[1] == 'add' ):
		# if todo is given
		if ( len(sys.argv) > 2 ): 
			add_todo_to_file(sys.argv[2])
		
		# if todo is missing
		else: 
			print("Error: Missing todo string. Nothing added!")


	# for deleting a todo
	elif ( sys.argv[1] == 'del' ):
		# when todo number is specified
		if ( len(sys.argv) > 2 ):
			delete_todo_from_file(int(sys.argv[2]))

		# when todo number is not specified throw error
		else:
			print("Error: Missing NUMBER for deleting todo.")


	# to mark a todo as done and 
	elif ( sys.argv[1] == 'done' ):
		# when todo number is specified
		if ( len(sys.argv) > 2 ):
			mark_todo_as_done(int(sys.argv[2]))

		# when todo number is not specified throw error
		else:
			print("Error: Missing NUMBER for marking todo as done.")

	
	# to show report
	elif ( sys.argv[1] == 'report' ):
		show_report()


	# when invalid arg is passed
	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')


# driver code
if __name__  ==  "__main__": 
    main()