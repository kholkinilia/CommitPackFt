from typing import List, Tuple



def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the closest pair of elements in a list of floats.

    Parameters:
    numbers (List[float]): The list of floats to search for the closest pair.

    Returns:
    Tuple[float, float]: The closest pair of elements as a tuple of two floats.
    """

    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx!= idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance > distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair