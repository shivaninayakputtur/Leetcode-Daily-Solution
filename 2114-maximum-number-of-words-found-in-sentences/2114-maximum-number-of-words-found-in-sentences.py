class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word=0
        for char in sentences:
            words=len(char.split())
            max_word=max(max_word,words)
        return max_word

                 
