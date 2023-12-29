from typing import List



def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 3, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

# the bug in parse_music is that it doesn't handle the case when the music string is empty
# we need to add a check for an empty string and return an empty list
# here is the corrected implementation