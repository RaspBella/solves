class solve:
    def __init__(self, number, time, comment, scramble, date, basetime):
        self.number = number
        self.time = time
        self.comment = comment
        self.scramble = scramble
        self.date = date
        self.basetime = basetime


def file_in(filename):
    solves = []
    file = open(filename)
    next(file) #skips first line
    for line in file:
        x = line.split(";")
        solves.append(solve(int(x[0]),x[1],x[2],x[3],x[4],float(x[5].strip())))
    file.close()
    return solves


def print_solve(solve):
    print("Solve number:",solve.number,"\nTime:",solve.time,"\nComment:",solve.comment,"\nScramble:",solve.scramble,"\nDate:",solve.date,"\nBasetime:","{:.2f}".format(solve.basetime),"\n")


def search(query, solves):
    if type(query) == int:
        if not query > len(solves):
            print_solve(solves[query-1])
        else:
            print("Query:",query,"is greater than amount of solves, there are:",len(solves),"\n")
    elif type(query) == float:
        for x in range(len(solves)):
            if solves[x].basetime == query:
                print_solve(solves[x])
    else:
        for x in range(len(solves)):
            if query in solves[x].time:
                print_solve(solves[x])
