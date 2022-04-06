import json
import glob
from report import Report

class ObjectCreator:
    @classmethod
    def create_object(cls, klass, arguments):
        return klass(arguments)

class JsonObjCreator(ObjectCreator):
    @classmethod
    def create_object(cls, klass, arguments):
        super().create_object(klass, arguments)

    @classmethod
    def create_object_from_string(cls, klass, json_str):
        report = Report()
        try:
            json_dict = json.loads(json_str)
        except Exception as e:
            report.add_errors(e.__class__)
        else:
            report.add_successes(str(klass) + " Object created")
            return report, klass(**json_dict)          

    #creates objects from [, , ] lists
    @classmethod
    def create_object_from_list(cls, klass, json_list):
        report = Report()

        try: 
            output = []
            json_dict = json.loads(json_list)
            for json_item in json_dict:
                output.append(klass(**json_item))
                #output.append(ObjectCreator.create_object_from_string(klass, json_item))
        except Exception as e:
            report.add_errors(e.__class__)
            return report, output
        else:
            report.add_successes(str(klass) + " Object created")
            return report, output        

    #creates a single object per file
    @classmethod
    def create_object_from_file(cls, klass, json_file):
        report = Report()
      
        try: 
            with open(json_file, "r") as read_file:
                json_dict = json.load(read_file)
                #Injecting the filepath into the json data
                json_dict["filepath"] = json_file 
                output = klass(**json_dict)
        except Exception as e:
            report.add_errors(e.__class__)
            return report, output
        else:
            report.add_successes(str(klass) + " Object created")
            return report, output

    @classmethod
    def create_objects_from_folder(cls, klass, criteria):
        report = Report()
        output = []

        try:
            #criteria contains the filepath and the criteria used to select the files
            for file in glob.glob(criteria + ".json"):
                internal_report, obj = JsonObjCreator.create_object_from_file(klass, file)
                report.append_data(internal_report)
                output.append(obj)

        except Exception as e:
            print("An exception ocurred")
            report.add_errors(e.__class__)
            return report, output
        else:
            return report, output


