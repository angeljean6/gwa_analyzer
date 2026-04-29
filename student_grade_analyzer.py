class StudentAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def find_top_student(self):
        """Identifies the student with the lowest GWA (highest achievement)."""
        best_student = ""
        best_gwa = float('inf')

