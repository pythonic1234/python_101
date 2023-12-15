art1="""
This perplexing phenomenon, initially identified in the United States, is now resonating across major Asian countries, including Korea, Hong Kong and Singapore, countering conventional expectations that the health-savvy younger generation would enjoy increased longevity.
"""

art2="""
Regarding the moves as the DPK’s saber-rattling ahead of next year’s general elections, the PPP is urging Yoon to use his veto power. At the same time, however, concerns over a backlash are rising as the president has already vetoed several bills, and a recent survey showed that the public wants the investigations.
"""

first_words=art1.split()
first_setwords=set(first_words)
inter=setart1.intersection(setart2)
inter.sort()
print(inter)




