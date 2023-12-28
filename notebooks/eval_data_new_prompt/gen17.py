from typing import List



def parse_music(music_string: str) -> List[int]:
    """
    Parses a string representing a piece of music and returns a list of integers representing the notes played.
    The string can contain multiple notes separated by spaces. Each note can be a single character representing a note or a note followed by a duration.
    The duration can be represented by a single character, '.' representing a quarter note, '|' representing a half note, and '|' representing a whole note.
    The notes are represented by integers from 0 to 3, where 0 represents a rest and 1 to 3 represent the notes C, C#, D, D#, E, F, F#, G, and G#.
    """
    note_map = {'o': 3, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]