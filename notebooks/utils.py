from tqdm import tqdm
import datasets
from typing import List, Callable, Any
import difflib
from constants import REFACT_PROMPT_TEMPLATE, REFACT_SYSTEM_PROMPT, CHECKER_CODE_TEMPLATE


def calculate_from_datasets(datasets_to_calculate_from: List[datasets.Dataset],
                            function: Callable[[datasets.Dataset], Any],
                            show_progress: bool = True) -> Any:
    """
    Calculates a function from each of the datasets for the list and returns the results

    :param datasets_to_calculate_from: A list of datasets to calculate a function from
    :param function: A function to calculate
    :param show_progress: A flag indicating, whether to show progress or not
    :return: A list of values calculated from the respective datasets
    """
    dataset_vals = []
    for dataset in (tqdm(datasets_to_calculate_from) if show_progress else datasets_to_calculate_from):
        dataset_vals.append(function(dataset))

    return dataset_vals


def get_changes_count(old_contents: str,
                      new_contents: str,
                      return_diff: bool = False):
    """
    A function that calculates the number of line changes. One change is either a deletion or an addition of a line.
    Hence, if the line is changed it counts as two changes: one addition and one deletion.

    :param old_contents: A string before changes
    :param new_contents: A string after changes
    :param return_diff: A flag indicating, whether to return the diff or not
    :return: If "return_diff" is True, then a tuple of (change_count, diff_string). Otherwise, just change_count.
    """
    old_lines = old_contents.splitlines(keepends=True)
    new_lines = new_contents.splitlines(keepends=True)

    diff = difflib.unified_diff(old_lines, new_lines, lineterm='')

    diff_list = list(diff)[2:]
    changes_count = sum(1 for line in diff_list if line.startswith('+') or line.startswith('-'))

    if return_diff:
        return changes_count, ''.join(diff_list)
    return changes_count


def get_fix_user_prompt(item: dict) -> str:
    """
    Returns a user prompt for a bug fixing task
    :param item: An item from HumanEvalPack dataset to generate the prompt for
    :return: A prompt
    """
    return f"\n{item['declaration']}{item['buggy_solution']}\n\n{item['test']}\n\nFix bugs in {item['entry_point']}"


def get_refact_prompt(item: dict) -> str:
    """
    Returns a prompt for bug fixing for Refact model
    :param item: An item from a HumanEvalPack dataset to generate a prompt for
    :return: A prompt for a model
    """
    return REFACT_PROMPT_TEMPLATE.format(system=REFACT_SYSTEM_PROMPT, user=get_fix_user_prompt(item))


def parse_refact_response(output: str) -> str:
    """
    Parses a response of the Refact model and returns the generated part
    :param output: A full output of a model
    :return: A generated output
    """
    generated_code = output.split("ASSISTANT")[1].strip().split("<empty_output>")[0].strip()
    first_attempt = "\ndef".join(generated_code.split("def")[:2])
    return first_attempt.strip()


def get_checke_code(item: dict) -> str:
    """
    Returns a string with python code of a checker script for an item from HumanEvalPack dataset
    :param item: An item from a dataset
    :return: A checker code string
    """
    return CHECKER_CODE_TEMPLATE.format(id=get_id(item), function=item['entry_point'],
                                        testcases=item['test'])


def get_id(item: dict) -> int:
    """
    Returns an id of an item from HumanEvalPack dataset
    :param item: An item from HumanEvalPack dataset
    :return: item's id
    """
    return int(item['task_id'].split('/')[1])