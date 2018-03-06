# -*- coding: utf-8 -*-

def FizzBizz(num):
    
    answer = ""

    if num == 0:
        answer = 0    
    
    if num % 3 == 0 and num % 5 == 0:
        answer = "FizzBuzz"
    elif num % 3 == 0:
        answer = "Fizz"
    elif num % 5 == 0:
        answer = "Buzz"
    else:
        answer = str(num)
        
    return answer

def Tex_free(age, income, child):
    tex_total = 0
    if age >= 16 and age <= 65: #납세자
        if income < 20000:      #소득 20000달러 미만
            tex_total = income * 0.2
        else:       ## 소득 20000달러 이상
            tex_total = income * 0.5

    if child == True:
        tex_total = tex_total - (tex_total * 0.1)
                
    return int(tex_total)

def Leap_year(year):
    answer = ""
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        answer = "윤년"
    elif year % 4 == 0 and year % 100 == 0:
        answer = "평년"
    elif year % 4 == 0:
        answer = "윤년"
    else:
        answer = str(year)

    return answer
