A Document is defined by a name, a text, and a sequence of annotations. name and text are strings, the field for annotations is a container for annotation instances. 

An Annotation is defined by a begin (the char position within the text), an end, a type – a string that specifies the type of annotation, this case only sentence and word – and metadata (a map key-value).

Annotations can be compared with Allen’s interval relations except the overlapping one (https://en.wikipedia.org/wiki/Allen%27s_interval_algebra)


Declare these classes with constructors and fields. 

If needed to overload comparison operators for annotations, these should be based on begin and end fields.


Make a function that from a document with annotations builds a string with each annotation surrounded by Html tags. If the annotation is of type sentence it it will surround the text in a <p> node, if the annotation is of type word it will surround the text with a <span> node. Consider that <p> and <span> nodes might in the future have Html attributes taken from the annotation metadata.


Make a if __name__ == "__main__" section, or a separated test according to your style, which tests the outcome with the following example:


Text:

Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt.


Annotations (type, begin, end):

("sentence", 0, 27)

("sentence", 28, 56)

("sentence", 57, 90)

("word", 22, 26)

("word", 51, 55)

("word", 79, 89)

("word", 0, 5)


The resulting string should be like the following:

<p><span>Lorem</span> ipsum dolor sit <span>amet</span>.</p><p>Consectetur adipiscing <span>elit</span>.</p><p>Sed do eiusmod tempor <span>incididunt</span>.</p>
