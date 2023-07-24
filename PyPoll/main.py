import csv
import os

# Commands to load election_data.csv file and to create a location to output an analysis text file
electioncsv = os.path.join("Resources", "election_data.csv")
analysis_output = os.path.join("analysis", "election_analysis.txt")

# Commands for total votes and candidate vote counters, candidate choice list 
total_votes_cast = 0
candidate_choices = []
candidate_votes = {}

# Creating tracker for winning candidate and winning count
winning_candidate = ""
winning_count = 0

# Commands to read the csv file, convert it into list of dictionaries and clarify the character that separates \n
# the columns 
with open(electioncsv) as voter_data:
    filereader = csv.reader(voter_data, delimiter=',')
    fileheader = next(filereader)

    for row in filereader:
        # Adds to the total vote counts
        total_votes_cast = total_votes_cast + 1

        # Extracts Candidate Name from each row and compares it with the listing in candidate_choices list
        candidate_name = row[2]
        if candidate_name not in candidate_choices:

            # Add candidate name to list of candidates running
            candidate_choices.append(candidate_name)

            # Start tracking new candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate's count already on the list
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(analysis_output, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"\n"
        f"----------------------------------\n"
        f"\n"
        f"Total Votes:  {total_votes_cast:0,.0f}\n"
        f"\n"
        f"----------------------------------\n")
    
    print(election_results, end="")
    txt_file.write(election_results)
    
    # Commands to determine election winner
    for candidate in candidate_votes:
        # Get vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes_cast) * 100

        # Determinw winning candidate  and vote count
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage to screen
        voter_output = f"{candidate}:  {vote_percentage:.3f}% ({votes:0,.0f})\n"
        print(voter_output, end="")
        
        # Print & save candidate's voter count and percentage to text file
        txt_file.write(voter_output)
    
        winning_candidate_summary = (
        f"---------------------------------------\n"
        f"\n"
        f"Election Winner:  {winning_candidate}! \n"
        f"\n"
        f"--------------------------------------\n"  
         )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
