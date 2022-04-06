from object_creator import JsonObjCreator
from user import User
from set_cover import SetCover

## FIRST PART OF THE TEST STARTS HERE ##
print("---------- Part 1 ----------")

# I use * to select all files in the json_files folder
# The method itself takes care of only selection .json files
report, users = JsonObjCreator.create_objects_from_folder(User, "json_files/*")

modules = {}

for user in users:
    providers = user.get_provider()
    for prov in providers.keys():
      if prov not in modules.keys():
        modules[prov] = {}

      if providers[prov] not in modules[prov]:
          modules[prov][providers[prov]] = []
          modules[prov][providers[prov]].append(user.get_filepath())
      else:
          modules[prov][providers[prov]].append(user.get_filepath())

print(modules)
## FIRST PART OF THE TEST ENDS HERE ##

## SECOND PART OF THE TEST STARTS HERE ##
print("---------- Part 2 ----------")
universe = []

[universe.append(k) for key in modules.keys() for k in modules[key].keys()]

subsets = []

for user in users:
  subsets.append(list(user.get_provider().values()))

indexes = SetCover.set_cover(universe, subsets)
test_group = [users[i].get_filepath() for i in indexes]

print(test_group)

## SECOND PART OF THE TEST ENDS HERE ##
