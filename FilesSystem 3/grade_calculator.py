class GradeCalculator:
    def determine_grade(avg_score):
        if avg_score > 89:
            return 'A'
        elif avg_score > 79:
            return 'B'
        elif avg_score > 69:
            return 'C'
        elif avg_score > 59:
            return 'D'
        elif avg_score > 49:
            return 'F'
        else:
            return 'F'
