def calc(args, op='+'):
    if op == '+':
        return sum(args)
    elif op == '*':
        value = 1
        for num in args:
            value *= num
        return value

print(calc([1, 1, 4], op='+'))
print(calc([1, 2], op='*'))