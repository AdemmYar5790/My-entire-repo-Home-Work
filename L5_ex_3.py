def workers_stat():
    workers = [['Stein ', '142.000 \n'], ['Sydorovich ', '15.000 \n'], ['Andronov ', '145.000 \n'], ['Bern ', '80.000 \n'],
               ['Kochurova', '175.000 \n'], ['Weinberg', '27.000 \n'], ['Abramova', '10.000 \n'], ['Salamatin', '67.000 \n'],
               ['Andreev', '55.000 \n'], ['Korneev', '21.000']]
    try:
        with open('ex_3.txt', 'w+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = ['Abramova', 'Sydorovich']
            sum = 0
            for i in range(len(l)):
                bene = int((l[i].split())[1])
                if bene < 20000:
                    poor.append((l[i].split())[0])
                sum += bene
            print(f'The average income of employees is equal to: {sum / len(workers) / 12//2}')
            #from statistics import mean
        #bene.list = [142.000, 15.000, 145.000, 80.000, 175.000, 27.000, 10.000, 67.000, 55.000, 21.000]
        #list_avg = mean (bene.list)
        #print("Average value of the list:\n")
        #print(list_avg)
        #print(round(list_avg, 3))
        print(f'An employee receives less than 20 thousand rubles is: {", ".join(poor)}')
    except FileNotFoundError:
        return 'File not detected.'

workers_stat()