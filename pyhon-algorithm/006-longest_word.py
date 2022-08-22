sentence = input("Give me a sentence. : ")

word_list = sentence.split()                    # Split metodunun amacı listeye cevirip tüm elemanları itere etmek

longest = 0
i = 0

while i < len(word_list) :
    
    if len(word_list[i]) > longest :
        longest = len(word_list[i])
        
    i += 1
    
print("The length of the longest word : ", longest)
