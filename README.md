# Password Vault

## Description
A program that stores each user's passwords.

## Installation
Log in or create an account after launching the application. Each account will have their own password storage.

Enter your password and its corresponding site, then save it. You can also check the other passwords the user has saved and how many times the entered password has been leaked.

# Complited functionality and approximate grades from your perception
- After executing the selected function, the program does not terminate but returns to the menu to choose another function. Exiting is only done after a specific command.
- All the functions apart the main are on the separate files
- "logs.log" - Uses an external file to save data such as .txt, .csv, .json, images, sounds or any other types of data.
  - "data.db" - Your external file is an actual SQL or NoSQL database
- "test_utils" - Make pytest or unittest for any 3 main functions of your project.
- "check_pwned" - Uses external API
- Use 2 Classes
- Error handling with 
  - try … except …
  - "utils.py" - Data validation with Regex
- Decomposition principals 
  - No code outside of the functions, follows decompositions principles
  - No more than 10 functions and 300 lines of code in a single file (use modules to store functions in a separate file.py)
  - Functions documentation
- All users interaction, along with restarting of an app, happense inside of the app, without hardreseting
- Logging

## Project Structure
password_vault/
├── .git/                 
├── README.md   
├── requirements.txt
├── main.py 
├── src/
  ├── utils.py
  ├── logic.py
  ├── db.py
  └── gui.py
└── tests/                
    └── test_utils.py        

## Team Members
- GitHub: [@hbspyana](https://github.com/hbspyana)
- Email: tatiananamoco@gmail.com
