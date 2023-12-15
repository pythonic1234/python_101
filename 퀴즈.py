personality = str(input("mbti"))
mbti = {
    "E": "당신은 외향적입니다",
    "I": "내향적",
    "N": "감각적",
    "S": "직관적",
    "T": "이성적",
    "F": "감성적",
    "P": "즉흥적",
    "J": "계획적"
}

print(mbti[personality[0]] + mbti[personality[1]] + mbti[personality[2]] + mbti[personality[3]])
