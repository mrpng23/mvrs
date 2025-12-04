Project 2: Book Recommendation System

GitHub Repository:
The source code for this project is available on GitHub:
https://github.com/mrpng23/mvrs

Identification:
Name: ROMIN MAKHSUTSHOEV
P-number: P475223
Course code: IY499 - Practical Programming Assignment

I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

Description of the Program:
This project implements a simple book recommendation system that demonstrates how collaborative filtering works at a basic level. The primary goal of the program is to compare a new user’s book ratings to existing users’ ratings and generate personalized recommendations based on similarity. This system was created to illustrate how recommendation engines function in real applications, such as online bookstores or streaming platforms.
The program loads all stored ratings from a JSON file, making the data easy to modify and easy to extend. The similarity() function was introduced to compare two users and calculate how many books they rated in common. The recommend() function uses this similarity score to identify the most similar existing user and then recommend books they rated highly. These functions demonstrate how algorithms can be split into small, reusable components with clear purposes.
User input is handled through a simple command-line interface with error checking to prevent invalid ratings. The program’s structure highlights core topics such as dictionaries, loops, searching through data, simple sorting logic, and file-based data storage.
To conclude, the system is a compact but fully functional example of a basic recommendation algorithm, designed to demonstrate both Python fundamentals and the logic behind similarity-based suggestions.

Libraries Used:
json (standard library)

Installation:
1. Install Python 3.
2. Download all project files.
3. No external libraries are required.

How to Run the Program:
python main.py