# ETL, Analysis of User Behavior in HD Television Service

## Description:
This project aims to analyze the usage history of users who have terminated their contracts with the HD television service system. The dataset provided contains logs describing the usage history of these users. Using programming languages such as Java, Python, R, etc., the following tasks are to be performed:

# Tasks:
1: Parsing Logs to Determine Attributes:

Parse logs to identify the following attributes:
- MAC: userID
- SessionMainMenu: the time when the user starts using the service
- AppName: the type of app the user is using
- LogID: log ID
- Event: user action
- ItemID: ID of the program the user viewed
- RealTimePlaying: duration of user viewing.

Output: A new log set with a row-column format. Each row corresponds to a log entry, and each column corresponds to an attribute. Columns are separated by tab characters.

2: Combining user_info.txt and Parsed Data:

Combine the user_info.txt file with the parsed dataset to analyze the characteristic usage behaviors of these users.
3: Proposing a Solution for Predicting User Churn:

Based on the analysis results, propose a solution to predict user churn probability. Implement the solution if possible.
Requirements:

Candidates are required to submit the following documents: a report file (in PDF/Word/Slide format) and the source code.
README File:

Project Structure:

data: Directory containing the dataset files.
src: Directory containing the source code.
report: Directory containing the project report.
Instructions:

Clone the repository to your local machine.
Ensure that the required dataset files are placed in the "data" directory.
Run the appropriate scripts from the "src" directory to perform the tasks described in the project.
Dependencies:

Ensure that you have the necessary programming language and libraries installed to run the scripts. For Python scripts, common libraries such as pandas, numpy, etc., may be required.
Usage:

Execute the scripts in the "src" directory to perform the desired tasks. Follow the instructions provided within the scripts for usage guidelines.
Report:

Refer to the "report" directory for the project report, which includes detailed explanations of the tasks performed, analysis results, and proposed solutions.
Note:

For any inquiries or issues regarding the project, please contact [insert contact information].
