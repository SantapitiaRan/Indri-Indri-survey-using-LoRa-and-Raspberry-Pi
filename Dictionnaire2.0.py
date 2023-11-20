stats={"a":10, "b":1, "c":3}
inverse = [(value, key) for key, value in stats.items()]
print(max(inverse)[1])