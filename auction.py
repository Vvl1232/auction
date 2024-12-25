import random as rd
import streamlit as st

# List of IPL players
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

# Function to determine the highest bidder
def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder, amount in bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner, highest_bid

# Streamlit app setup
st.title("🎉MEGA-AUCTION🎉")
st.title("💥 IPL Player Bidding Platform 💥")
st.write("Welcome to the IPL Player Bidding Platform! 🏏 Place your bids and see who wins the player! 🚀")

# Select a random player
if "player_to_bid" not in st.session_state:
    st.session_state.player_to_bid = rd.choice(ipl_players)

st.subheader(f"✨ Player for Bidding: {st.session_state.player_to_bid} ✨")

# Initialize bids
if "bids" not in st.session_state:
    st.session_state.bids = {}
if "show_bids" not in st.session_state:
    st.session_state.show_bids = False

# Bidding form
with st.form("bidding_form"):
    team_name = st.text_input("🏆 Enter your team name:", key="team_name")
    bid_amount = st.number_input("💵 Enter your bid amount ($):", min_value=100, step=50, key="bid_amount")
    submit_bid = st.form_submit_button("Place Bid 🔥")

if submit_bid:
    if team_name and bid_amount > 0:
        st.session_state.bids[team_name] = bid_amount
        st.success(f"🎯 Bid placed successfully for {team_name}!")
    else:
        st.error("⚠️ Please enter a valid team name and bid amount.")

# End bidding and determine winner
if st.button("🎉 End Bidding 🎉"):
    if st.session_state.bids:
        st.session_state.show_bids = True
        winner, highest_bid = highest_bidder(st.session_state.bids)
        st.success(f"🏆 The highest bidder is {winner} with a bid of ${highest_bid}! 🏅")
        st.balloons()  # Balloons effect when the winner is announced
        st.info("🎉 Congratulations! The player joins your team. 🏏")
        st.session_state.bids.clear()
        st.session_state.player_to_bid = rd.choice(ipl_players)
    else:
        st.error("⚠️ No bids placed yet!")

# Display current bids if bidding has ended
if st.session_state.show_bids:
    st.write("💬 Current Bids:")
    for team, bid in st.session_state.bids.items():
        st.write(f"📢 Team {team}: ${bid} 💸")
