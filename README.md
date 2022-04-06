# Overview:

The system consists of four modules and five classes. The ObjectCreator can create instances of a desired class using a class method. JsonObjCreator inherits this capability and is able to receive and process json data in order to create the desired objects. After finishing the creation process, the class returns a report summarizing the successes or errors involved in the process. With the users created, the SetCover class is used to select the minimum number of users necessary to cover all the provider options. 

# In order to run solution

Requirements:

1. Have python 3.x installed

Steps:

1. Download/clone this repo

2. Run the main.py file

3. That's it :)

# More detailed information the classes involved

## User

The user class has 4 properties: id, name, provider, and filepath.

I included the id propery because it's most likely necessary in any real life scenario, but I set it to None, leaving the door open for future implementation.

The name, provider, and filepath properties can be assigned when creating an instance, the latter having a default value of None. The idea is that if a User instance is created from data contained in a file, the filepath can be included in the User object. If that is not the case, the property can simply be ignored.

## Report

The report class has 3 properties: errors, warnings, and successes.

The reasoning behind this class was the following: when creating hundreds or thousands of objects automatically, it becomes necessary to have a summary of any problems that might occur (I totally stole this idea from a Salesforce API I used last week). 

All the properties are, by default, empty lists. The flexible thing about them is that these lists can contain anything. I simply used them to contain strings stating messages, but it would be perfectly possible to pass an object without needing any type of modification. So if an Error class was created in the future, there would be no problem integrating it. 

Every property has a corresponding get, add, and print function. There's also a the function get_summary that returns  a summary stating how many errors, warnings, and successes are included in the report.

The append_data function allows you to append data from another report object, basically merging the info from both into the current instance. This feature is especially handy when creating batches of objects with the ObjectCreator classes.

## ObjectCreator and JsonObjCreator

The ObjectCreator has a class method that, after receiving a class type and the necessary arguments, can create an instance of said class. The JsonObjCreator inherits this method and builds on top of it by making it possible to use json data to create these instances. 

JsonObjCreator has four class methods of its own, all of which work in a similar way. Using either json.load or json.loads to parse the necessary data and returning a report object followed by either the desired objects (in case it was successful) or an empty list or null result (in case the operation fails). All methods also use exception catching, so an unsuccessful operation won't crash the script. Right now, all methods act the same without taking into consideration any specific exceptions. This is an aspect that can and should be improved, since certain exceptions will always be more frequent than others.

Let's see some more details and a few examples of the existing methods.

Examples can be accessed here: https://replit.com/@PabloRios2/StableYummyTelecommunications#main.py

**create_object_from_string()**

Receives accepts a json string containing a dictionary the data necessary to create a single object.

Usage example:

Example create_object_from_string

json_string = '{"name": "User 1", "provider": {"content_module": "authz.provider_4", "auth_module": "authn.provider_2"}}'

report, user  = JsonObjCreator.create_object_from_string(User, json_string)

print(user.name)

Output in console:

User 1

**create_object_from_list()**

Receives accepts a json list containing a list of dictionaries with record data.

Usage example:

Example create_object_from_list

json_list = '[{"name": "User 2", "provider": {"content_module": "authz.provider_4", "auth_module": "authn.provider_2"}}, {"name": "User 3", "provider": {"content_module": "authz.provider_4", "auth_module": "authn.provider_2"}}, {"name": "User 4", "provider": {"content_module": "authz.provider_4", "auth_module": "authn.provider_2"}}]'

report, user_list  = JsonObjCreator.create_object_from_list(User, json_list)

for u in user_list:

  print(u.name)

Output in console:

User 2

User 3

User 4

**create_object_from_file()**

It receives a class and a filepath, then opens the json file in reading mode and uses json.load to parse the file. An important detail is that this method imports the filepath into the json data after parsing it. Making sure that all objects created from an object can know where their data comes from. An important limitation is that this function assumes files contain information about a single record. This is a **severe** weakness in the system that should be worked on. 

This method has no example since it is used in the main.py file already.

**create_objects_from_folder**

The protagonist! The method is used in the main.py file. This method receives a class and a string containing the filepath criteria, that criteria serves two functions: it indicates where the files are located and it indicates which json files are selected (the JsonObjCreator method ignores all the non .json files already). Thanks to the glob library, it's possible to use regular expressions to select the wanted files, making the method quite flexible. In my case I simply gave the directory location followed by an asterisk symbol, since I knew that folder contained only the wanted json files.

This method has no examples since it is used in the main.py file already.

## SetCover

A class containing class methods that can execute a (very inefficient) greedy set cover algorithm.

Don't know what a greedy set cover is? Read this: https://en.wikipedia.org/wiki/Set_cover_problem

(I mean, if you're reading this you probably work at Qualabs and you're evaluating me, so I'm pretty sure you know that algorithm. Buuuut this repo is public, so who knows who might end up reading this)

Ok, so bad things first: **this algorithm should use sets** instead of lists, and most importantly, **it should use generators**, since they're much more memory efficient. 

Sets make sure, by definition, that they do not contain duplicate elements, making them perfect for this task. The reason I used lists is that the only way I could think of making this algorithm work (while writing 100% of it myself) was by working with indexes. And sets don't have indexes, so I used lists.

Generators, on the other hand, only store one item at a time in memory , making it possible to examine huge sets without using that much memory. Why didn't I use them? Well, I tried and failed for too much time, so I decided to move on so I could get this test done within a decent time frame (I already had to ask for a few days to finish a bootcamp).

With those shameful confessions out of the way, let's dive into what I did.

The set_cover method receives a universe (i.e. a list of the elements I want to cover) and a group of subsets (a list of lists from which I want to use the minimum amount that's necessary to cover the elements of the universe). 

First, it makes sure to remove any duplicates from the universe list (using remove_duplicates()) and copies the universe list values to another list called to_cover.

Then it makes sure that the subsets cover the elements in universe.

After that, it proceeds to find the most valuable set in the subsets list (get_most_valuable_index method and get_subsets_scores), which is the one that contains the most elements in common with the universe. If more than one subset fulfills the max() operation, the first one read is the one used. After finding that subset, the elements it contains are removed from the to cover list and the operation is repeated until the to_cover list is empty.

The set_cover method works independently of the data types contained in universe and subset lists, and it also works if the subset contains more elements than the universe.

You can access an example that has strings, ints, booleans, and extra elements in the subsets by going to this link:

https://replit.com/@PabloRios2/SetCoverTest

# Main challenges and lessons learned

- **Assigning a list as a default value for the properties of the Report objects.**:

This caused report instances to share data involuntarily, since they shared the same list, which got bigger and bigger with every use. It is definitely a newbie mistake I am not proud of. 

- **Attempting to use an efficient greedy cover algorithm**:

An actually efficient greedy cover algorithm in Python should use sets and generators. The problem is, I never used generators before and actually learning how to implement them would take a little bit of time. I tried, but ended up just losing a lot of time, so I decided to move on and use a less efficient but more familiar method. On the bright side, since this functionality is loosely coupled, it would be easy to just edit the SetCover class without changing any other module.

- **Reusing json reading methods**:

I made methods for reading json from a string containing a single record, a string containing a list of records, a file, and a folder. Basically, incrementing the "size" with each method, the original idea was that the "bigger" methods would reuse the "smaller" ones. create_objects_from_folder would call create_object_from_file, which in turn would call create_object_from_list and finally create_object_from_string. This idea was abandoned when I remembered that to read a file it's necessary to use json.load() and to read strings it's necessary to use json.loads(). Not only that, but the way I made the create from list method didn't allow me to easily reuse the create from string method. However, I did end up reusing the create_object_from_file in the create_objects_from_folder method, which is the method I actually use in this solution. So I guess I was successful where it mattered the most :)

- **Ability to create different types of classes with the ObjectCreator classes**:

Implementing this wasn't particularly hard, but it is an aspect I'm proud of since it allows a lot of flexibility. Therefore, I believe it deserves a mention in this space.

- **Different json formats**:

As mentioned in the JsonObjCreator section, the current system has a huge weakness by assuming all json files contain only information about a single record. This is something that should be worked upon if given the chance. It turns out that checking if the json file contains a list or only a dictionary was trickier than I thought.
