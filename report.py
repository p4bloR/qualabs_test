class Report:

    def __init__(self, errors = None, warnings = None, successes = None):
      
        self.errors = errors
        if errors is None:
          self.errors = []
          
        self.warnings = warnings
        if warnings is None:
          self.warnings = []
          
        self.successes = successes
        if successes is None:
          self.successes = []
            
    def __str__(self):
        return str(self.get_summary())

    def get_data(self):
        return self.errors, self.warnings, self.successes

    def get_summary(self):
        summary = "Errors: " + str(len(self.errors)), "Warnings: " + str(len(self.warnings)), "Successes: " + str(len(self.successes))
        return summary

    def get_errors(self):
        return self.errors

    def get_warnings(self):
        return self.warnings  

    def get_successes(self):
        return self.successes  

    def print_errors(self):
        print("Errors: ")
        if len(self.errors) > 0:
            for item in self.errors:
                print(item)
        else:
          print("None")

    def print_warnings(self):
        print("Warnings: ")
        if len(self.warnings) > 0:
            for item in self.warnings:
                print(item)
        else:
          print("None")

    def print_successes(self):
        print("Successes: ")
        if len(self.successes) > 0:
            for item in self.successes:
                print(item)
        else:
          print("None")

    def add_errors(self, error):
        self.errors.append(str(error))

    def add_warnings(self, warning):
        self.warnings.append(str(warning))

    def add_successes(self, success):
        self.successes.append(str(success))      

    def append_data(self, internal_report):
      
        if len(internal_report.get_errors()) > 0:
            self.add_errors(internal_report.get_errors)

        if len(internal_report.get_warnings()) > 0:
            self.add_warnings(internal_report.get_warnings)
            
        if len(internal_report.get_successes()) > 0:
            self.add_successes(internal_report.get_successes)
