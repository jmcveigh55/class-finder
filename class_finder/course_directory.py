import os
import glob
from typing import Optional


class Course:
    def __init__(self, course_path: str):
        self.course_path = course_path
        self.quarter_path = os.path.abspath(os.path.dirname(self.course_path))
        self.course_name = os.path.basename(os.path.normpath(self.course_path))
        self.quarter = os.path.basename(os.path.normpath(self.quarter_path))

    def __repr__(self) -> str:
        return (f'{type(self).__name__}({self.course_name=},{self.quarter=})'
                .replace('self.', ''))


class CourseDirectory:
    def __init__(self, quarters_path: str):
        self.quarters_path = quarters_path

    def search_for_class(self, course_name: str) -> Optional[Course]:
        all_items = glob.glob(f'{self.quarters_path}/*/*')
        classes = map(Course, filter(lambda f: os.path.isdir(f), all_items))
        for c in set(classes):
            if c.course_name == course_name:
                return c
