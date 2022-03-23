def slogan_maker(array):
    ans = []
    array = list(set(array))
    for i in range(len(array)):
        for j in range(len(array)):
            for z in range(len(array)):
                if (array[i] != array[j]) and (array[j] != array[z]) and (array[z] != array[i]):
                    ans.append(array[i] +' '+ array[j] +' '+ array[z])
                pass
    return ans




array = ["super", "hot"]