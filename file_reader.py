import pickle

class FileReader:
    @staticmethod
<<<<<<< HEAD
    def save_to_file(filename, content, mode='a'):
        """Save content to a .txt file. Accepts string or list of strings."""
        try:
            if isinstance(content, list):
                content = '\n'.join(str(item) for item in content)
            with open(filename, mode, encoding='utf-8') as file:
                file.write(content)
            print(f"Content saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving to file '{filename}': {e}")

=======
    def save_to_file(filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)
>>>>>>> origin/dev

    @staticmethod
    def read_from_file(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)