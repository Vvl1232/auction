import random as rd
ipl_players = [
    "Virat Kohli", "MS Dhoni", "Rohit Sharma", "AB de Villiers", "Chris Gayle",
    "David Warner", "Andre Russell", "Suresh Raina", "Ravindra Jadeja", "Shikhar Dhawan",
    "Lasith Malinga", "Jasprit Bumrah", "Sunil Narine", "KL Rahul", "Kieron Pollard",
    "Hardik Pandya", "Shane Watson", "Dwayne Bravo", "Faf du Plessis", "Rashid Khan",
    "Yuvraj Singh", "Gautam Gambhir", "Sanju Samson", "Ruturaj Gaikwad", "Trent Boult",
    "Mohammed Shami", "Bhuvneshwar Kumar", "Quinton de Kock", "Eoin Morgan", "Steve Smith",
    "Jos Buttler", "Pat Cummins", "Mohammed Siraj", "Axar Patel", "Shubman Gill",
    "Prithvi Shaw", "Ishan Kishan", "Rishabh Pant", "Moeen Ali", "Anil Kumble",
    "Rahul Tewatia", "Yuzvendra Chahal", "Kuldeep Yadav", "Imran Tahir", "Mitchell Starc",
    "Umesh Yadav", "Harbhajan Singh", "Irfan Pathan", "Shaun Marsh", "Adam Gilchrist",
    "Brendon McCullum", "Jacques Kallis", "Aaron Finch", "Kevin Pietersen", "Michael Hussey",
    "Matthew Hayden", "Albie Morkel", "Ajinkya Rahane", "Parthiv Patel", "Ambati Rayudu",
    "Siddarth Kaul", "Deepak Chahar", "Washington Sundar", "T Natarajan", "Kamlesh Nagarkoti",
    "Nitish Rana", "Venkatesh Iyer", "Sam Curran", "Ben Stokes", "Tim Southee",
    "Jason Holder", "Marcus Stoinis", "Daniel Sams", "Riley Meredith", "Mayank Agarwal",
    "Krishnappa Gowtham", "Rahul Chahar", "Varun Chakravarthy", "Navdeep Saini", "Arshdeep Singh",
    "Shardul Thakur", "Lungi Ngidi", "Chris Morris", "Mitchell Marsh", "Lockie Ferguson",
    "Nathan Coulter-Nile", "Kyle Jamieson", "Devdutt Padikkal", "Anrich Nortje", "Mustafizur Rahman",
    "Shivam Dube", "Riyan Parag", "Dewald Brevis", "Tilak Varma", "Abdul Samad",
    "Sandeep Sharma", "Jaydev Unadkat", "Piyush Chawla", "Ashok Dinda", "Manish Pandey",
    "Mandeep Singh", "Wriddhiman Saha", "Sarfaraz Khan", "Karun Nair", "Shahbaz Ahmed",
    "Priyam Garg", "Abhishek Sharma", "Rahul Tripathi", "Harshal Patel", "Mohit Sharma",
    "Ramesh Powar", "Darren Sammy", "Ricky Ponting", "Zaheer Khan", "Glenn Maxwell",
    "Paul Valthaty", "Andrew Tye", "James Faulkner", "Mitchell McClenaghan", "George Bailey",
    "Lendl Simmons", "Dale Steyn", "Chris Lynn", "Angelo Mathews", "Ryan ten Doeschate",
    "Mithun Manhas", "Hanuma Vihari", "Munaf Patel", "Doug Bollinger", "Shaun Tait",
    "Andrew Symonds", "Graeme Smith", "David Miller", "Shane Bond", "John Hastings",
    "Brad Hodge", "Clint McKay", "Cameron White", "Justin Langer", "Darren Lehmann",
    "Dirk Nannes", "Ravi Bishnoi", "Krunal Pandya", "Shreyas Iyer", "Tim David",
    "Evin Lewis", "Shimron Hetmyer", "Nicholas Pooran", "Dinesh Karthik", "Liam Livingstone",
    "Avesh Khan", "Mohammad Nabi", "Jason Roy", "Saqib Mahmood", "Rajat Patidar",
    "Obed McCoy", "Phil Salt", "Matthew Wade", "Tim Seifert", "Rilee Rossouw",
    "Fabian Allen", "Kyle Mayers", "Keemo Paul", "David Willey", "Reece Topley",
    "Ben Cutting", "Colin Munro", "Colin de Grandhomme", "Daniel Christian", "Shahbaz Nadeem",
    "Shreyas Gopal", "Kane Richardson", "Billy Stanlake", "Scott Kuggeleijn", "Mohammad Hafeez",
    "Brett Lee", "Zaheer Khan", "Ajit Agarkar", "RP Singh", "Pragyan Ojha",
    "Ishant Sharma", "Parvinder Awana", "Ashish Nehra", "Makhaya Ntini", "Sreesanth",
    "Joginder Sharma", "Manvinder Bisla", "Chandrakant Pandit", "Cheteshwar Pujara", "Tirumalasetti Suman",
    "Wriddhiman Saha", "Venugopal Rao", "Rajagopal Sathish", "Swapnil Asnodkar", "Abhishek Nayar",
    "Gurkeerat Singh Mann", "Sunny Singh", "Iqbal Abdulla", "Manan Vohra", "Arun Karthik",
    "Baba Aparajith", "Unmukt Chand", "Tanmay Srivastava", "Saurabh Tiwary", "Ankit Rajpoot"
]
player_to_bid=rd.choice(ipl_players)
print(player_to_bid)

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        amount = bids[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner, highest_bid

bids = {}
choice = "yes"
while choice == "yes":
    team_name = input("Bidder team name: ")
    bid = int(input("Bidding amount: $"))
    bids[team_name] = bid 
    choice = input("Are there any more bidders 'yes' or 'no': ").lower()
    if choice == "no":
        winner, highest_bid = highest_bidder(bids)
        print(f"The highest bidder was {winner} with a bid of ${highest_bid}")
        choice = "no"
