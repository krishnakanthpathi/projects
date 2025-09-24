def factors(num) :
    facts = []
    for i in range(1 , int(num ** .5) + 1 ) :
        if num%i == 0 :
            facts.append(i)
            if i*i != num :
                facts.append(num//i)
    return facts
print(factors(12))