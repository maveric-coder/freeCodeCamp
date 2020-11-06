import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**args):
        self.contents = []

        if len(args) == 0:
            print ("at least one argument needed")
            quit()

        for k,v in args.items():
            for i in range(v):
                self.contents.append(k)
	

    def draw(self, n):
        ss = []
        if n>len(self.contents):
            return self.contents
        a1=random.sample(range(len(self.contents)), k=n)
        
        for i in a1:
            ss.append(self.contents[i])
        
        tmp = [self.contents[i] for i in range(len(self.contents)) if not i in a1]
        self.contents=tmp

        return ss

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	expected = []
	print(expected_balls)
	for k,v in expected_balls.items():
		for i in range(v):
		    expected.append(k)
	n=0

	for k in range(num_experiments):
		ch=copy.deepcopy(hat)
		drawn=ch.draw(num_balls_drawn)
		chk=False       
		for e in expected:
		    if e in drawn:
		        chk=True
		        drawn.remove(e)
		    else:
		        chk=False
		        break
		if chk:
		    n+=1
	return n/num_experiments