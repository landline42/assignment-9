class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        "Adds a friend to the person's friend list."

        #Check if the people are already added
        if friend not in self.friends:
            self.friends.append(friend)
            return 0
        else:
            print(f"{self.name} has already added {friend.name}.")
            return 1

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """ Adds a new person to the network. """
        #Check for invalid data types
        if type(name) != str:
            print("Error: invalid data type.")
            return

        #Check if the person is already in the network
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} is already in the network.")


    def add_friendship(self, person1_name, person2_name):
        """ Creates a friendship between two people. """
        #Check for invalid data types
        if type(person1_name) != str or type(person2_name) != str:
            print("Error: invalid data type.")
            return

        #Make sure both people are not the same
        if person1_name == person2_name:
            print(f"Error: cannot add {person1_name} to their own friend list.")
            return

        #Confirm both people are in the social network
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            added = person1.add_friend(person2)
            if added == 0:  #Only run the add_friend function again if it ran successfully before
                person2.add_friend(person1)
        else:
            print(f"Error: one or both people do not exist.")

    def print_network(self):
        """ Prints the names of all people and their friends. """
        print("\n----------------")
        print("Current network:")
        print("----------------")

        for person in self.people:
            
            #Check for an empty friend list
            if len(self.people[person].friends) == 0:
                print(f"{person} has no friends.")

            else:
                print(f"{person} is friends with: ", end="")  #Print the current person's name
                
                for friend in self.people[person].friends:
                    if friend is self.people[person].friends[-1]:  #If the current friend is the last in the list, leave out the comma and allow a new line
                        print(f"{friend.name}")
                    else:
                        print(f"{friend.name}, ", end="")
        
        print()  #Add new line once network is done printing

# Test your code here
network = SocialNetwork()

#Add people
network.add_person("Alex")
network.add_person("Jordan")

#Try adding someone who is already in the network
network.add_person("Alex")

#Add invalid data
network.add_person(1)

#Print current network - no friendships
network.print_network()

#Add some more people
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Ashley")  #Will not have any friends added

#Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")

#Try adding a person who doesn't exist (Johnny)
network.add_friendship("Jordan", "Johnny")

#Send invalid data to add_friendship
network.add_friendship("Alex", 4)

#Try adding someone to their own friend list
network.add_friendship("Alex", "Alex")

#Try adding a duplicate friendship
network.add_friendship("Alex", "Jordan")

#Add more legitimate friendships
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")

network.print_network()

network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()
