article="""
n an alarming trend, millennials, born between 1981 and 1996, have become the subject of a paradox: they are facing a faster decline in health compared to older generations despite a heightened awareness of fitness among younger people.

"""



words=article.split() #공백 기준으로 찢고 단어 리스트 만듬
words.sort() #a부터 오름차순
setWords=set(words) #단어 리스트 세트화
listedWords=list(setWords) #리스트화
listedWords.sort() #a부터 오름차순
print(listedWords)