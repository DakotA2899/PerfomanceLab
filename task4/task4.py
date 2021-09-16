from statistics import mean
def steps(file):
    with open("nums.txt") as f:
        text = f.read().splitlines()
    data = [int(item) for item in text]
    s=0
    for i in data:
        s+=abs(i-mean(data))
    print(int(s))
steps("nums.txt")