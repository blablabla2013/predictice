
from document import Document
from annotation import Annotation

'''
constants declaration
'''

SENTENCE_BEGIN = '<p>'
SENTENCE_END = '</p>'
WORD_BEGIN = '<span>'
WORD_END = '</span>'
SENTENCE = 'sentence'
WORD = 'word'

'''
Description: get annotated text of the given document
Input: a Document object
Output: a String object
Specification:
 - the text of document is not empty
 - annotation is not empty
 - no overlap between wordspair, sentences pair and word-sentence pair
 - call a exception when annotation is out of range or do not cover all text
 Optimize:
 - add function to check overlap for annotations
'''
def get_annotated(document):
    
    dict_positions = get_position_tags_dict(document.annotations)        
    
    # get ordered position list from tags position dictionary
    ordered_position = sorted(dict_positions)
    
    # exception when annotation is out of range of text or no cover all text
    try:
        if (ordered_position[0] < 0 or ordered_position[-1] != len(document.text)):
            raise Exception(MSG_RANGE_ERROR)
    except Exception as excpt:
            print(excpt.args)
            
    # create output text
    str_tagged = ''
    last_pos = 0
    for pos in ordered_position:
        # add text
        if pos > last_pos:
            str_tagged += document.text[last_pos:pos] if len(document.text[last_pos:pos].strip()) > 0 else ''
        # add tags
        for tag in dict_positions[pos]:
            str_tagged += tag
        last_pos = pos
            
    return str_tagged


'''
Description: return a tags position dictionary to store begin and end positions of each tag
  i.e.: {"position1":[sentence_begin, word_begin], "position2":[word_end], ...}
Input: a List of Annotation objects
Output: a Dictionary
'''
def get_position_tags_dict(lst_annotations):
    dict_positions = {}
    for annotation in lst_annotations:
        if annotation.begin not in dict_positions:
            dict_positions[annotation.begin] = []
        if annotation.end not in dict_positions:
            dict_positions[annotation.end] = [] 
        if annotation.type == SENTENCE :
            dict_positions[annotation.begin].append(SENTENCE_BEGIN)
            dict_positions[annotation.end].append(SENTENCE_END)
        else:
            dict_positions[annotation.begin].append(WORD_BEGIN)
            dict_positions[annotation.end].append(WORD_END)
    
    return dict_positions


import unittest

class DocumentAnnotationTestCase(unittest.TestCase):    
    
    def test_get_annotated(self):
        
        text = 'Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt.'
        tagged_text = '<p><span>Lorem</span> ipsum dolor sit <span>amet</span>.</p><p>Consectetur adipiscing <span>elit</span>.</p><p>Sed do eiusmod tempor <span>incididunt</span>.</p>'
        lst_annotations = [
            Annotation('sentence', 0, 27),
            Annotation('sentence', 28, 56),
            Annotation('sentence', 57, 90),
            Annotation('word', 22, 26),
            Annotation('word', 51, 55),
            Annotation('word', 79, 89),
            Annotation('word', 0, 5)
        ]
        
        tagged_text_test = get_annotated(Document(text, 'test', lst_annotations))
        self.assertEqual(tagged_text_test, tagged_text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
