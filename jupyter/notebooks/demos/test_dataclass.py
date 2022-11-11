from dataclasses import dataclass

@dataclass
class GfgArticle():
    """A class for holding an article content"""
 
    # Attributes Declaration
    # using Type Hints
 
    title: str
    author: str
    language: str
    upvotes: int
 
# A DataClass object
article = GfgArticle("DataClasses",
                     "vibhu4agarwal",
                     "Python", 0)
print(article)



##

class NormalArticle():
    """A class for holding an article content"""
 
    # Equivalent Constructor
    def __init__(self, title, author, language, upvotes):
        self.title = title
        self.author = author
        self.language = language
        self.upvotes = upvotes
 
# Two DataClass objects
dClassArticle1 = GfgArticle("DataClasses",
                            "vibhu4agarwal",
                            "Python", 0)
dClassArticle2 = GfgArticle("DataClasses",
                            "vibhu4agarwal",
                            "Python", 0)
 
# Two objects of a normal class
article1 = NormalArticle("DataClasses",
                         "vibhu4agarwal",
                         "Python", 0)
article2 = NormalArticle("DataClasses",
                         "vibhu4agarwal",
                         "Python", 0)