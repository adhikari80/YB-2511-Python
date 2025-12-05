class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def display_file(self):
        
        try:
            file = open(self.filename, "r", errors="ignore")  
            lines = file.readlines()
            file.close()  
            print("\n--- File Content ---")
            for line in lines:
                print(line, end="") 
            return lines
        except FileNotFoundError:
            print("Error: File not found at:", self.filename)
            return []

    def count_star(self):
        
        lines = self.display_file()  
        return sum(line.count("*") for line in lines)
    
    def append(self):
        f=open(self.filename, "a")
        f.write("\nEnd of file.")
        print("\nText appended to the file.")
        f.close()
    


# main program
if __name__ == "__main__":
    filepath = r"C:\Users\adhik\Downloads\demo_file.txt" 

    reader = FileReader(filepath)

    reader.append()
    star_count = reader.count_star()
    print("\nTotal '*' characters found:", star_count)
