from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        c = 0
        while c != 3:
            print(TrafficLight.__color[c])
            if c == 0:
                sleep(9)
            elif c == 1:
                sleep(7)
            elif c == 2:
                sleep(5)
            c += 1
            continue

t = TrafficLight()
t.running()