
from school_assessment import SchoolAssessmentSystem
from report_generator import ReportGenerator


def main():
    try:
        file = 'all_semester.csv'
        analyzer = SchoolAssessmentSystem(file)
                
        while True:
            student_name = input("Enter student name (or type 'exit' to quit): ")
            if student_name.lower() == 'exit':
                break
            
            analyzer.analyze_content(student_name)
            summary = ReportGenerator.generate_summary(analyzer.summary_data)
            print(summary)
            ReportGenerator.save_summary_to_file(summary, 'assessment_summary_report.txt')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
