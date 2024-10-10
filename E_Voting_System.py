import tkinter as tk
from tkinter import messagebox


class EVotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Voting System")
        self.root.geometry("400x400")

        # Voter Data
        self.voters = {}
        self.candidates = {'CANDIDATE1': 0, 'CANDIDATE2': 0, 'CANDIDATE3': 0}

        # GUI Layout
        self.create_gui()

    def create_gui(self):
        # Title Label
        title_label = tk.Label(self.root, text="E-Voting System", font=("Arial", 20))
        title_label.pack(pady=10)

        # Register Voter Frame
        register_frame = tk.Frame(self.root)
        register_frame.pack(pady=10)

        tk.Label(register_frame, text="Enter Voter ID:", font=("Arial", 14)).grid(row=0, column=0)
        self.voter_id_entry = tk.Entry(register_frame, font=("Arial", 14))
        self.voter_id_entry.grid(row=0, column=1)

        register_button = tk.Button(register_frame, text="Register Voter", font=("Arial", 14),
                                    command=self.register_voter)
        register_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Voting Frame
        voting_frame = tk.Frame(self.root)
        voting_frame.pack(pady=10)

        tk.Label(voting_frame, text="Vote for a Candidate:", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        self.selected_candidate = tk.StringVar()
        for idx, candidate in enumerate(self.candidates.keys()):
            tk.Radiobutton(voting_frame, text=candidate, variable=self.selected_candidate, value=candidate,
                           font=("Arial", 12)).grid(row=1 + idx, column=0, columnspan=2, sticky="w")

        vote_button = tk.Button(voting_frame, text="Submit Vote", font=("Arial", 14), command=self.cast_vote)
        vote_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Results Frame
        results_button = tk.Button(self.root, text="View Results", font=("Arial", 14), command=self.display_results)
        results_button.pack(pady=10)

    def register_voter(self):
        voter_id = self.voter_id_entry.get().strip()
        if voter_id in self.voters:
            messagebox.showerror("Error", "Voter ID already registered!")
        elif voter_id == "":
            messagebox.showerror("Error", "Voter ID cannot be empty!")
        else:
            self.voters[voter_id] = False
            messagebox.showinfo("Success", f"Voter ID {voter_id} has been successfully registered!")
            self.voter_id_entry.delete(0, tk.END)

    def cast_vote(self):
        voter_id = self.voter_id_entry.get().strip()
        candidate = self.selected_candidate.get()

        if voter_id == "":
            messagebox.showerror("Error", "Please enter your Voter ID!")
        elif voter_id not in self.voters:
            messagebox.showerror("Error", "Voter ID not registered!")
        elif self.voters[voter_id]:
            messagebox.showerror("Error", "You have already voted!")
        elif candidate == "":
            messagebox.showerror("Error", "Please select a candidate!")
        else:
            self.candidates[candidate] += 1
            self.voters[voter_id] = True
            messagebox.showinfo("Success", f"Thank you for voting for {candidate}!")
            self.voter_id_entry.delete(0, tk.END)
            self.selected_candidate.set("")

    def display_results(self):
        results = "\n".join([f"{candidate}: {votes} votes" for candidate, votes in self.candidates.items()])
        messagebox.showinfo("Election Results", results)


# Main function to run the app
def main():
    root = tk.Tk()
    app = EVotingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
