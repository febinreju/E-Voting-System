# E-Voting System using Python (Tkinter)

This project is a simple **E-Voting System** built with Python using the `tkinter` library for the graphical user interface (GUI). The system allows voters to register, cast their votes for different candidates, and view election results in real-time. The goal of the project is to simulate a voting system that ensures each voter can cast their vote only once.

## Features

### 1. **Voter Registration**
   - The system allows users to register by entering a unique **Voter ID**.
   - If the **Voter ID** is already registered, the system will display an error message.
   - If the input is valid, a success message is shown, and the voter is registered.

### 2. **Voting for Candidates**
   - After registering, users can cast their vote by selecting a candidate from the list of available candidates.
   - The system ensures that voters can only vote once. If a voter tries to vote more than once, an error message is displayed.
   - The vote is registered for the selected candidate, and a success message confirms the vote.

### 3. **Viewing Election Results**
   - A **View Results** button allows users to see the current voting results.
   - The results show the total number of votes each candidate has received.
   - Results are updated in real-time as votes are cast.

## How It Works

### GUI Layout
- The application interface has three main sections:
  1. **Voter Registration**: Allows voters to input their Voter ID and register in the system.
  2. **Voting Section**: Registered voters can select a candidate and submit their vote.
  3. **Results Section**: Displays real-time election results when the "View Results" button is clicked.

### Candidate List
- The system includes three candidates by default:
  - CANDIDATE1
  - CANDIDATE2
  - CANDIDATE3
- You can add or modify the candidates by editing the `self.candidates` dictionary in the code.

### Voter Authentication
- A voter can only cast one vote. After voting, the system marks the voter's status as **True**, preventing them from voting again.

### Error Handling
- Proper error messages are displayed in cases such as:
  - Voter ID not registered.
  - Voter has already voted.
  - No candidate selected when attempting to vote.

## Prerequisites

- Python 3.x
- `tkinter` library (comes pre-installed with standard Python installations)

## How to Run the Project

1. Clone this repository or download the source code.
2. Navigate to the project folder in your terminal or command prompt.
3. Run the following command to start the application:

   ```bash
   python evoting_system.py
