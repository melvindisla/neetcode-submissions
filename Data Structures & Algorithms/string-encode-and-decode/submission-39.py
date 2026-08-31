class Solution:

    delimeter = "#*#XVQ"
    def encode(self, strs: List[str]) -> str:
        # create a return string_final of string
        # loop through the list
        # append each word to the string_final 
        # and append a delimiter (special char) to string_final
        # cases
        # case 1: a list with an empty string   == [""]
        # case 2: a empty list                  == []
        string_final = ""
        
        # check to see if the lsit is empty
        if strs == []:
            return "###"
        
        if strs == [""]:
            return string_final
        
        last_element = strs[-1]

        for i in range(len(strs)):
            # if i is the last element in the array, then dont add the '#'
            string_final += strs[i]
            if i != len(strs)-1:
                string_final += Solution.delimeter
        print(string_final)
        return string_final

    def decode(self, s: str) -> List[str]:
        # cases
        # case 1: a list with an empty string   == [""]
        # case 2: a empty list                  == []
            
        strs = []
        if s == "###":
            return []
        if s == "":
            return [""]
        strs = s.split(Solution.delimeter)
        print(strs)
        return strs
