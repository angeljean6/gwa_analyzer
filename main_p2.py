from student_grade_analyzer import StudentAnalyzer

def run_analysis():

    analyzer = StudentAnalyzer("students.txt")

    print("Analyzing student records...")
    analyzer.find_top_student()

if __name__ == "__main__":
    run_analysis()