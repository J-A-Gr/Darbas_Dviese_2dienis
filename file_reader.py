import pickle

class FileReader:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)
            
    @staticmethod
    def read_from_file(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)