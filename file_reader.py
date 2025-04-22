class FileReader:
    @staticmethod
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


    @staticmethod
    def read_from_file(filename):
        """Read content from a .txt file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return ""
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""
