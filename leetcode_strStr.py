def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
      return(haystack.find(needle))
    else:
      return -1

'''
Verifica se há um pedaço de um trecho de uma palavra, uma sílaba, na palavra alvo
por exemplo leet em leet code
'''

# Test cases

haystack = 'hello'
needle = 'll'
result = strStr(haystack, needle)
print(f"Resultado do teste 1: {result} (esperado: 2)")

haystack = 'abcde'
needle = 'f'
result = strStr(haystack, needle)
print(f"Resultado do teste 2: {result} (esperado: -1)")
