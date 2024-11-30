from file_processor import FileProcessor
from report_generator import ReportGenerator
from grade_calculator import GradeCalculator


class SchoolAssessmentSystem:
    def __init__(self, file_path):
        self.data = FileProcessor.process_file(file_path)
        self.summary_data = []

    def analyze_content(self, student_name):
        try:
            subject_list = ['Mathematics', 'Science', 'English']
            student_data = self.data[self.data['Name'] == student_name]
            if not student_data.empty:
                student_summary = self._generate_student_summary(student_data, subject_list)
                self.summary_data.append(student_summary)
            else:
                print(f"Student '{student_name}' not found in data.")
        except Exception as e:
            print(f"An error occurred during content analysis: {e}")

    def _generate_student_summary(self, student_data, subject_list):
        try:
            semester = student_data['Semester'].iloc[0]
            id = student_data['Id'].iloc[0]
            email = student_data['URL'].iloc[0]
            avg_score = student_data[subject_list].mean(axis=1).mean()
            grade = GradeCalculator.determine_grade(avg_score)
            highest_scoring_subject = student_data[subject_list].idxmax(axis=1).iloc[0]
            highest_score = student_data[highest_scoring_subject].iloc[0]
            lowest_class = student_data[subject_list].mean().idxmin()
            lowest_score = student_data[subject_list].min().min()
            lowest_grade = GradeCalculator.determine_grade(lowest_score)
            notable_observations = student_data[subject_list].idxmax(axis=1).value_counts().idxmax()
            web_data_time = student_data['Time Spent'].str.extract(r'(\d+)m').astype(int).sum().values[0]
            subject_analysis = self._subject_analysis(student_data, subject_list)
            highest_score = student_data[subject_list].max().max()
            highest_grade = GradeCalculator.determine_grade(highest_score)

            return {
                'Name': student_data['Name'].iloc[0],
                'id': id,
                'email': email,
                'Semester': semester,
                'Average Score': avg_score,
                'Grade': grade,
                'Highest Score': highest_score,
                'Highest Score subject': highest_scoring_subject,
                'Highest Grade': highest_grade,
                'Lowest Score': lowest_score,
                'Lowest Class': lowest_class,
                'Lowest Grade': lowest_grade,
                'Notable Observation': notable_observations,
                'Online Participation': web_data_time,
                'Subject Analysis': subject_analysis
            }
        except Exception as e:
            print(f"An error occurred while generating the student summary: {e}")

    def _subject_analysis(self, student_data, subject_list):
        try:
            subject_grade = []
            for subject in subject_list:
                
                result = ""
                if student_data[subject].iloc[0] > student_data[subject].iloc[1]: 
                    result = f"Improved by {abs(student_data[subject].iloc[0] - student_data[subject].iloc[1])}% compared to the last assessment."
                elif student_data[subject].iloc[0] < student_data[subject].iloc[1]: 
                    result = f"Performed less by {abs(student_data[subject].iloc[0] - student_data[subject].iloc[1])}% compared to the last assessment."
                else: 
                    result = f"Consistent performance across all classes."
                subject_grade.append(f"   - {subject}: {result}")
                        

                # subject_grade.append(f"   - {subject}: Score: {score}, Grade: {sub_grade}")
                
            return '\n'.join(subject_grade)
        except Exception as e:
            print(f"An error occurred during subject analysis: {e}")
    
    # def _subject_analysis(self, student_data, subject_list):
    #     try:
    #         subject_grade = []
    #         for subject in subject_list:
    #             score = student_data[subject].iloc[0]
    #             sub_grade = GradeCalculator.determine_grade(score)
    #             subject_grade.append(f"   - {subject}: Score: {score}, Grade: {sub_grade}")
    #         return '\n'.join(subject_grade)
    #     except Exception as e:
    #         print(f"An error occurred during subject analysis: {e}")
            
    
    
