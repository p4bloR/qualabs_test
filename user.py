class User:

    def __init__(self, name, provider, filepath = None):
        self.id = None
        self.name = name
        self.provider = provider
        self.filepath = filepath

    def get_data(self):
        return self.name, self.provider

    def get_provider(self):
      return self.provider

    def get_filepath(self):
      return self.filepath