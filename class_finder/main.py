import re
import sys

from .course_directory import CourseDirectory
from .config import QUARTERS_PATH


def main() -> None:
    if len(sys.argv) == 1:
        print(f'Usage: main.py CLASS-NAME ...')
        return

    provided_courses = sys.argv[1:]
    course_directory = CourseDirectory(QUARTERS_PATH)
    for needle_course in provided_courses:
        result = course_directory.search_for_class(needle_course)
        if result:
            print(result.course_path)
        else:
            print(f'{needle_course} not found in course directory.')


if __name__ == '__main__':
    main()
