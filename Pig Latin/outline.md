# About Pig Latin

According to [Wikipedia ](https://en.wikipedia.org/wiki/Pig_Latin)
> **Pig Latin** is a language game or argot in which words in English are
 altered, usually by adding a fabricated suffix or by moving the onset or 
 initial consonant or consonant cluster of a word to the end of the word and
adding a vocalic syllable to create such a suffix.

---
## Basic Rules

**For words that begin with a consonant sound all letters before the first vowel
are placed at the end of the word. Then 'ay' is appended to the end.**

* World = Orldway
* Note = Otenay
* Book = Ookbay


 **For words that begin with a consonant cluster, the entire sound is moved to
the end of the word.**

* The = Ethay
* Thursday = ursdaythay
* Chocolate = Ocolatechay

**For words that begin with a vowel sound, simply add 'ay' to the end of the 
word.**

* Over = Overay
* Islet = Isletay
* __Honest = Honestay__

Note the last example. It begins with a consonant, however, it's normally 
pronounced with a vowel sound in the beginning.

___
## Before building the program
What do I need to know about Python before building this program?

- [x] Able to read string input from a user, or string input from a plain text file.
- [x] Able to manipulate strings  with string concatenation.
- [x]Able to search strings, word by word with lists and manipulate those lists
	- [ ]Basic RegEx skills?
- ?
## A simplified outline

1. Get a string of text from the user.
2. Make the string a list, space separated.
3. Analyze each list item.
4. Check IF the list item begins with a vowel. IF it does, THEN append 'ay'
5. ELSE check if the word begins with one or more consonants. If it does, move
all consonants to the end of the word, then add 'ay'
6. For any word that does not start with a vowel or consonant, leave as is. Ex.
Someone may type, 82Mikey. OPTIONALLY add 'ay', so that 82Mikey = 82Mikeyay.
7. Output the newly translated text to the user.
