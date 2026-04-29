class StudentAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def find_top_student(self):
        """Identifies the student with the lowest GWA (highest achievement)."""
        best_student = ""
        best_gwa = float('inf')

        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        name = parts[0].strip()
                        gwa = float(parts[1].strip())

                        if gwa < best_gwa:
                            best_gwa = gwa
                            best_student = name

            if best_student:
                print(f"Top Student: {best_student}")
                print(f"Highest GWA: {best_gwa}")
            else:
                print("No valid student records found.")

        except FileNotFoundError:
            print(f"Error: '{self.data_file}' not found.")
        except ValueError:
            print("Error: Check if GWA values are formatted correctly as numbers.")