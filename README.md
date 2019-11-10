# swapi
Additional library installation
1. Go to script folder within python repository
2. Execute command "pip install pyinstaller --upgrade"
3. Execute command "pip install pyinstaller pywin32"
4. Execute command "pip install bs4"


To get list of Star Wars Characters follow steps:
1. Create an instance X of class ApiHelper. 
2. Using instance X call function star_wars_characters. This function accepts only one parameter i.e link of api. e.g. "https://swapi.co/api/people" 
3. You will get list of all Start Wars Characters in class variable star_wars_details
4. To write same details to CSV file use function append_to_file. this function accepts 4 parameters 
	a. Path of CSV file
	b. name, height, gender.
