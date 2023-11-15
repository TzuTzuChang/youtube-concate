from youtube_concate.pipline.steps.step import StepException


class Pipline:
    def __init__(self, steps):
        self.steps = steps
        pass

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(inputs)
            except StepException as e:
                print('Exception happened:', e)
                break
