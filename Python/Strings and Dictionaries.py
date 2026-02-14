# ================================================================
#  Kaggle - Python
#  Exercise: Strings and Dictionaries
# ================================================================


# ----------------------------------------------------------------
#  Q0 - String Basics
# ----------------------------------------------------------------

a = ""
length = 0
q0.a.check()

b = "it's ok"
length = 7
q0.b.check()

c = 'it\'s ok'
length = 7
q0.c.check()

d = """hey"""
length = 3
q0.d.check()

e = '\n'
length = 1
q0.e.check()


# ----------------------------------------------------------------
#  Q1 - Valid Zip Code
# ----------------------------------------------------------------

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) == 5 and zip_code.isdigit():
        return True
    else:
        return False

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Word Search
# ----------------------------------------------------------------

def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Multi-word Search
# ----------------------------------------------------------------

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

# Check your answer
q3.check()
