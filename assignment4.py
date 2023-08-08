#!/usr/bin/env python
# coding: utf-8

# In[73]:


# question no.1

import re

text='Python Exercises,PHP exercises.'
print(re.sub("[ ,.]",":",text))


# In[4]:


# question no.2
import re
#input.
text="The following example creates an history of india has Got independance of 1947 ."
list= re.findall("[ae]\w+",text)
print(list)


# In[74]:


#question no.3
import re 
text= 'The quick brown fox jumps over the lazy cat.'
print(re.findall (r"\b\w{4,}\b",text))


# In[7]:


#question no.4
import re
text= 'the quick brown fox jumps over the lazy dog'
print (re.findall(r"\b\w{3,5}\b",text))


# In[46]:


#question no.6
import re
items = ["example (.com)", "hr@fliprobo(.com)", "github (.com)", "hello(dtat science world)","data(scientist)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))


# In[45]:


#question no.7
import re 
text="ImportanceOfRegularExpressionsInPython"
print(re.findall ('[A-Z][^A-Z]*',text))


# In[24]:


#question no.10
import re
b= "nidhi nidhinlal@gmail.com"
lst=re.findall('\S+@\S+',b)
print(lst)


# In[25]:


#question no.12
import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[12]:


#question no.13
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[27]:


#QUESTION NO.15
import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


#question no.16
import re
pattern = 'fox'
text = 'The quik brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))


# In[5]:


question no.17
# import re
text = 'Python exercises, PHP exercises,C# exercises'
pattern='exercises'
for match in re.findall(pattern,text):
    print ('Found "%s"' %match)


# In[7]:


#question no.19
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2025-03-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[10]:


#question no.20
def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

print(is_decimal('124.11'))
print(is_decimal('124.1'))
print(is_decimal('124.1'))
print(is_decimal('0.21'))

print(is_decimal('123.1214'))
print(is_decimal('3.124587'))
print(is_decimal('e666.86'))


# In[19]:


#question no.21
import re
text = "The indian cricket team have capacity of 60 memberes. Four 4 memberes are then added to the List."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[72]:


#question no.23
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("regularExpression"))
print(capital_words_spaces("PythonExercisesIsAnImportant"))
print(capital_words_spaces("TopicInPython"))


# In[23]:


#question no.24
import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# In[27]:


#question no.25
import re

def removeDuplicatesFromText(text):
    regex = r'\b(\w+)(?:\W+\1\b)+' 
    return re.sub(regex, r'\1', text, flags=re.IGNORECASE)

str1 = "Hellow hellow world world"
print(removeDuplicatesFromText(str1))


# In[28]:


#question no.26
import re

str1 = "Tutorialspoint123"
print("The given string is")
print(str1)

print("Checking if the given string is alphanumeric")
print(bool(re.match('^[a-zA-Z0-9]+$', str1)))


# In[56]:


#question no.27
import re
 
 
 
def extract_hashtags(text):
 
    regex = "#(\w+)"
 
    hashtag_list = re.findall(regex, text)
 

    print("The hashtags in \"" + text + "\" are :")
    for hashtag in hashtag_list:
        print(hashtag)
 
 
if __name__ == "__main__":
    
    text1 = "RT @KAPIL_KAUSHIK #DOLTIWAL I MEAN #xyabc is hurt by #demonetization as the same has rendered useless"
    
    extract_hashtags(text1)


# In[58]:


#question no.5
document = "example(.com)"
document = re.sub(r'[()]', '', document)

print(document)


# In[67]:


#question no.9
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])",  r"\1 \2", str1)

print(capital_words_spaces("RegularExpression1isAnImportantTopic3InPython"))


# In[70]:


#question no.22
import re
string='947,896,926,524,734,950,642'
number = re.findall('\d+', string)
number = map(int, number)
print("Max_value:",max(number))


# In[ ]:


#question number 8,11,14,18,28,29,30 not answered please help inthese questions

