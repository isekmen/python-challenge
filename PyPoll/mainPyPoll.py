import os
import csv


def list_of_candidate_names(vote_data):

    candidates = []
    for row in vote_data:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    return candidates


def sum_votes_for_each_candidate(vote_data, candidate_names):

    votes_per_candidate = {} 

    for candidate in candidate_names:
        vote_count = 0
        for row in vote_data:
            if candidate in row[2]:
                vote_count += 1
        votes_per_candidate[candidate] = vote_count

    return votes_per_candidate


def create_title(votes_per_candidate):

    total_votes = sum(votes_per_candidate.values())
    title = f"\nElection Results \n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"

    return title


def create_body(votes_per_candidate):
   
    total_votes = sum(votes_per_candidate.values())
    highest_vote_count = max(votes_per_candidate.values())
    body = []


    for candidate, vote_count in votes_per_candidate.items():
        percentage_of_total_votes = (vote_count / total_votes) * 100
        body.append((f"{candidate}: {round(percentage_of_total_votes, 3)}% ({vote_count})\n"))

    return body


def create_winner(votes_per_candidate):

    vote_counts = list(votes_per_candidate.values())
    candidate_names = list(votes_per_candidate.keys())
    index_of_highest_vote_count = vote_counts.index(max(vote_counts))
    winner = candidate_names[index_of_highest_vote_count]
    winner = f"-------------------------\n Winner: {winner}\n-------------------------\n"

    return winner


    
def create_txt_file(title, body, winner):

    newbody = "\n".join(body) 
    output = title + newbody + winner

    f = open('PyPoll/analysis/PyPoll_Export.txt','w')
    f.write(output)
    f.close()


def pypoll():
    
    csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        
        vote_data = list(csvreader)
        candidate_names = list_of_candidate_names(vote_data)
        votes_per_candidate = sum_votes_for_each_candidate(vote_data, candidate_names)

        title = create_title(votes_per_candidate)
        body = create_body(votes_per_candidate)
        winner = create_winner(votes_per_candidate)

        print(title, *body, winner) 

        create_txt_file(title, body, winner)


pypoll()