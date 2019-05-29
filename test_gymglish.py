#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
import pytest
from gymglish import CountOccurencesInText


text_one = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes it is true, I like PYTHON
and my name is GEORGES"""
              
text_two = "John O'maley is my friend"     

text_three = """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text_three += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text_three += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text_three += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text_three += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text_three += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text_three += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
text_three += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text_three += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
text_three += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500


@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (3, "Georges", text_one),
    (3, "GEORGES", text_one),
    (3, "georges", text_one),
    (0, "george", text_one),
    (3, "python", text_one),
    (3, "PYTHON", text_one),
    (2, "I", text_one),
    (0, "n", text_one),
    (1, "true", text_one),
    (0, "maley", text_two),
  ]
)
@pytest.mark.short
def test_CountOccurencesInText_short(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Short Test"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )
        
   
@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (3, "Georges", text_three),
    (3, "GEORGES", text_three),
    (3, "georges", text_three),
    (0, "george", text_three),
    (3, "python", text_three),
    (3, "PYTHON", text_three),
    (2, "I", text_three),
    (0, "n", text_three),
    (1, "true", text_three)
  ]
)
@pytest.mark.long
def test_CountOccurencesInText_long(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Long Text"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )


@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (0, "reflexion mirror", "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"),
    (1, "'reflexion mirror'", "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"),
    (1, "reflexion mirror", "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida"),
    (1, "reflexion mirror", "Reflexion Mirror\" in Sopchoppy, Florida")
  ]
)
@pytest.mark.phrase
def test_CountOccurencesInText_phrase(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Phrase Search"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )       
      

@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (1, "reflexion mirror", u"I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida"),
    (1, "reflexion mirror", u"I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida"),
    (1, "legitimate", u"who is approved by OILS is completely legitimate: their employees are of legal working age"),
    (0, "legitimate their", u"who is approved by OILS is completely legitimate: their employees are of legal working age"),
    (1 , "get back to me", u"I hope you will consider this proposal, and get back to me as soon as possible"),
    (1 , "skin-care", u"enable Delavigne and its subsidiaries to create a skin-care monopoly"),
    (1 , "skin-care monopoly", u"enable Delavigne and its subsidiaries to create a skin-care monopoly"),
    (0 , "skin-care monopoly in the US", u"enable Delavigne and its subsidiaries to create a skin-care monopoly"),
    (1 , "get back to me", u"When you know:get back to me")
  ]
)
@pytest.mark.unicode
def test_CountOccurencesInText_unicode(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Unicode"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )     
     
 
@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (1, "don't be left", """emergency alarm warning.
			 Don't be left unprotected. Order your SSSS3000 today!"""),
    (1, "don", """emergency alarm warning.
	       Don't be left unprotected. Order your don SSSS3000 today!"""),
    (1, "take that as a 'yes'", "Do I have to take that as a 'yes'?"),
    (1, "don't take that as a 'yes'", "I don't take that as a 'yes'?"),
    (1 , "take that as a 'yes'", "I don't take that as a 'yes'?"),
    (1 , "don't", "I don't take that as a 'yes'?"),
    (1 , "attaching my c.v. to this e-mail", "I am attaching my c.v. to this e-mail.")
  ]
)
@pytest.mark.misc
def test_CountOccurencesInText_misc(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Misc"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )    
  

@pytest.mark.parametrize("occurrences, sought_fragment, text",
  [
    (1, "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"),
    (1, "Linguist Specialist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"),
    (1, "Laboratory Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"),
    (1, "Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"),
    (1, "Floor", "''Linguist Specialist Found Dead on Laboratory Floor''"),
    (1, "Floor", "__Linguist Specialist Found Dead on Laboratory Floor__"),
    (1, "Floor", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"),
    (1, "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"),
    (1, "Linguist", "''Linguist Specialist Found Dead on Laboratory Floor''"),
    (1, "Linguist", "__Linguist Specialist Found Dead on Laboratory Floor__"),
    (1, "Linguist", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"),
    (1, "Floor", """Look: ''Linguist Specialist Found Dead on Laboratory Floor'' is the headline today.""")    
  ]
)
@pytest.mark.quote
def test_CountOccurencesInText_quotes(occurrences, sought_fragment, text):
    """Test the CountOccurencesInText function - Multiple Quotes"""    
    assert( occurrences == CountOccurencesInText(sought_fragment, text) )       
