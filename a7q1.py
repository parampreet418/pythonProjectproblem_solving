Scores = [198, 486, 651, 85, 216, 912, 73, 319, 846, 989]
def arraySort():
  for i in range(0, len(Scores)):
    j = i
    for j in range(i + 1, len(Scores)):
        if Scores[i] > Scores[j]:
            dif = Scores[i]
            Scores[i] = Scores[j]
            Scores[j] = dif

def printArray():
    lt_500 = 0
    gt_500 = 0
    for i in range(len(Scores)):
     if (Scores[i] < 500):
        lt_500 = lt_500 + 1
        print(f'Score {Scores[i]} less than 500.')
     else:
        gt_500 = gt_500 + 1
        print(f'Score {Scores[i]} greater than 500.')
def main():
    arraySort()
    printArray()
main()

