class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def display_file(self):
        """Reads the file, prints its content, and returns all lines."""
        try:
            with open(self.filename, "r", errors="ignore") as file:
                lines = file.readlines()
            print("\n--- File Content ---")
            for line in lines:
                print(line, end="")  # lines already include \n
            return lines
        except FileNotFoundError:
            print("Error: File not found at:", self.filename)
            return []

    def count_star(self):
        """Counts total '*' characters in the file."""
        lines = self.display_file()  # reuse display_file to read lines
        return sum(line.count("*") for line in lines)


# main program
if __name__ == "__main__":

    filepath = r"C:\Users\adhik\Downloads\demo_file.txt" 

    reader = FileReader(filepath)

    # Count '*' characters (also prints the file)
    star_count = reader.count_star()
    print("\nTotal '*' characters found:", star_count)


