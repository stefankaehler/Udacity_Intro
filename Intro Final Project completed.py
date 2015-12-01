Intro Final Project completed

# Use this to try out anything you like. Use print to display your answer
# when you press the "Test Run" button.
# Use the "Reset" button to reset the screen 

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Jimbo is connected to ."

def create_lists(string_input):
    network = []
    start = 0
    if not string_input:
        return network
    else:
        inputs = string_input.count('.')
        n = 0
        while n < inputs:
            end = string_input.find('.', start)
            network.append(string_input[start:end])
            start = end + 1
            n = n + 1
    return network

def user_connections(network, user):
    connections = []
    for data in network:
        if user and 'connected' in data:
            if user in data[0:data.find('connected')]:
                data = data.replace(',','')
                data = data[data.find('connected'):]
                data = data.split()
                for word in data:
                    #word = word.replace(',','')
                    if word[0].isupper():
                        connections.append(word)
    return connections

def user_games_liked(network, user):
    likes = []
    for data in network:
        if user and 'likes' in data:
            if user in data[0:data.find('play')]:
                data = data[data.find('play')+5:]
                length = len(data)
                start = 0
                n = data.count(',') + 1
                i = 0
                while i < n:
                    i = i + 1
                    end = data.find(',')
                    if end == -1:
                        length = len(data)
                        end = length
                    likes.append(data[start:end])
                    data = data[end+1:]
    return likes

def create_data_structure(network):
    n_dict = {}
    network = create_lists(network)
    for entry in network:
        #print entry
        user = entry[0:entry.find(' ')]
        if user not in n_dict:
            n_dict[user] = {}
            n_dict[user]['connections'] = user_connections(network, user)
            n_dict[user]['likes'] = user_games_liked(network, user)
    return n_dict

def get_connections(network, user):
    n_dict = create_data_structure(network)
    if user in n_dict:
        return n_dict[user]['connections']
    else:
        return None
    
def get_games_liked(network, user):
    n_dict = create_data_structure(network)
    if user in n_dict:
        return n_dict[user]['likes']
    else:
        return None

def add_connection(network, user_A, user_B):
    n_dict = create_data_structure(network)
    if user_B not in n_dict:
        return False
    if user_A not in n_dict:
        return False
    if user_B not in n_dict[user_A]['connections']:
        n_dict[user_A]['connections'].append(user_B)
    return n_dict

def add_new_user(network, user, games):
    n_dict = create_data_structure(network)
    games = games
    if user in n_dict:
        return n_dict
    else:
        n_dict[user]={'likes':games}
    return n_dict

def get_secondary_connections(network, user):
    n_dict = create_data_structure(network)
    if user not in n_dict:
        return None
    else:
        first_connect = n_dict[user]['connections']
        final_connect = []
        for first_user in first_connect:
            second_connect = n_dict[first_user]['connections']
            for second_user in second_connect:
                if second_user not in final_connect:
                    final_connect.append(second_user)
        return final_connect
    
def connections_in_common(network, user_A, user_B):
    n_dict = create_data_structure(network)
    if user_A not in n_dict:
        return False
    if user_B not in n_dict:
        return False
    else:
        common = 0
        user_A_connects = get_connections(network, user_A)
        user_B_connects = get_connections(network, user_B)
        for connection in user_A_connects:
            if connection in user_B_connects:
                common = common + 1
        return common
    
def path_to_friend(network, user_A, user_B):
    n_dict = create_data_structure(network)
    current_connects = get_connections(network, user_A)
    #print "current connections for %s: %s" % (user_A, current_connects)
    for user in current_connects:
        #print "checking: %s" % user
        if user == user_B:
            #vertices = vertices + 1
            #print "found him!"
            return 1
        else:
            #current = user
            #print "going deeper!"
            return path_to_friend(network, user, user_B) + 1
        
# adding to dictionary values that indicate how many users are connected to user
            
def add_popularity(network):
    n_dict = create_data_structure(network)
    for user in n_dict:
        n_dict[user]['popularity'] = get_popularity(network, user)
    return n_dict

def get_popularity(network, user_A):
    n_dict = create_data_structure(network)
    #for user_A in n_dict:
    popularity = 0
    for user_B in n_dict:
        if user_A in n_dict[user_B]['connections']:
            popularity = popularity + 1
    return popularity

def get_most_popular(network):
    n_dict = add_popularity(network)
    top_banana = None
    for user in n_dict:
        if get_popularity(network, user) > get_popularity(network, top_banana):
            top_banana = user
    print 'And the top banana is:...'
    return top_banana

#print get_popularity(example_input, None)

#print get_most_popular(example_input)

#print add_popularity(example_input)
#print create_data_structure(example_input)    
#print path_to_friend(example_input,'Mercedes','John')
#print connections_in_common(example_input,'Olive','John')
#print get_secondary_connections(example_input, 'Jimbo')    
#print add_new_user(example_input, 'Freda', 'Starfleet')
#print create_data_structure(example_input)