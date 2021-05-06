MAX_CHAR = 26;
def countFreq(str1, freq, len1):
     for i in range(len1):
         freq[ord(str1[i]) - ord('a')] += 1;

def canMakePalindrome(freq, len1):

     count_odd = 0;
     for i in range(MAX_CHAR):
         if(freq[i] % 2 != 0):
             count_odd += 1;

     if (len1 % 2 == 0):
         if(count_odd > 0):
             return False;
         else:
             return True;

     if (count_odd != 1):
         return False;
     else:
         return True;

def findOddAndRemoveItsFreq(freq):

     odd_str = " ";
     for i in range(MAX_CHAR):
         if(freq[i]%2 != 0):
             freq[i] -= 1;
             odd_str += chr(i+ord('a'));
             return odd_str;
     return odd_str;


def findPalindromicString(str1):
     len1 = len(str1);

     freq = [0]*MAX_CHAR;
     countFreq(str1, freq, len1);

     if (canMakePalindrome(freq, len1) == False):
         return "No Palindromic String";

     odd_str = findOddAndRemoveItsFreq(freq);

     front_str = " ";
     rear_str = " ";

     for i in range(MAX_CHAR):
         temp = " ";
         if(freq[i] != 0):
             ch = chr(i + ord('a'));


             for j in range(1, int(freq[i]/2)+1):
                 temp += ch;

             front_str += temp;

             rear_str += temp + rear_str;


     return (front_str + odd_str+rear_str);


str1 = "malayalam";
print(findPalindromicString(str1));
















         





















        
