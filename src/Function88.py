def esAnagrama(word1,word2):
    for letter in word1:
        encontre = False
        for letter2 in word2:
            if (letter == letter2):
              encontre = True;
              break
        if encontre == False:
           break
    return encontre