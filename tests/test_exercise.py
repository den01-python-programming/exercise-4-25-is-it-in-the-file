import pytest
import src.exercise
import os

def test_exercise():
    os.chdir('src')

    input_values = ["names.txt","Antti","names.txt","ada","nonsense.txt","ada",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Name of the file:","Search for:","Not found.",\
                      "Name of the file:","Search for:","Found!",\
                      "Name of the file:","Search for:","Reading the file nonsense.txt failed."]
