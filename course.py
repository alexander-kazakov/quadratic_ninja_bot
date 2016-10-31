import config

def build_course():
    course = {}
    steps = list()

    config.add_course_steps(steps)

    for step in steps:
        course[step.name] = step

    return course
