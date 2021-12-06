"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = get_subjects()
    show_subject(subjects)


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)

    input_file.close()
    return subjects


def show_subject(subjects):
    for subject in subjects:
        print(f"{subject[0]:13} is taught by {subject[1]:13} and has {subject[2]:13} students")


main()
