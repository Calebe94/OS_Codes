import subprocess
from random import randint

class SimulationAPI(object):
    __studentsRequesting = int()
    __booksInStock = int()
    __students = dict()
    __studentsRound = list()
    __listBooksInStock = list() # utilizado para realizar os pedidos dos alunos, se o livro estiver nessa lista, ja foi emprestado
    __listBooksRequested = list()
    __round = int() # verificar se essa variavel e igual a __rounds
    __listReady = dict()
    __rounds = int() # verificar se essa variavel a igual a __round
    __round_dict = dict()
    
    def __init__(self):
        self.__studentsRequesting = randint(0,100)
        self.__booksInStock       = randint(1,16)
        self.__defbooks()
        self.__requests()
    
    def nextRound(self):
        self.sort()
        auxList = self.__students.keys()
        count = 0
        self.__round_dict[self.__round] = dict()
        for index in auxList:
            try:
                item = self.__listBooksInStock[count]
                count+=1
                self.__students[index]["when"] = self.__round
                self.__students[index]["permanence"]+=1
                self.__round_dict[self.__round][item] = index
            except IndexError:
                item = "Sem Livro"
            if self.__students[index]["request"] == self.__students[index]["permanence"]:
                self.__students[index]["attendance"] = self.__round
                self.__listReady[index] = self.__students[index]
                del self.__students[index]
            else:
                self.__students[index]["book"] = item
                self.__students[index]["priority"] = float(self.__priority(index))
                
        self.__round+=1
        auxDict = self.__students
        return auxDict
    
    def __priority(self,index):
        #print("Prioridade do Index: "+str(index))
        timeWaiting = self.__students[index]["when"]
        #print("Tempo de espera: "+str(timeWaiting))
        timeWithBook = self.__students[index]["permanence"]
        #print("Tempo com o Livro: "+str(timeWithBook))
        try:
            priority = float((float(timeWaiting) + float(timeWithBook)) / float(timeWaiting)) 
        except ZeroDivisionError:
            priority = 0
        
        return float(priority)
    
    def __defbooks(self):
        for index in range(0,self.__booksInStock): # Se for 0 nao pegou livro
            self.__listBooksInStock.append(index)
            
    def __define_priorities(self):
        aux = self.__students.keys()
        for index in aux:
            self.__students[index]["when"] = float(self.__priority(index))
    
    def sort(self):
        auxStudentsDict = self.getStudents()
        auxList = auxStudentsDict.keys()
        auxDict = dict()
        
        for indexList in auxList:
            for indexVerify in auxList:
                if auxStudentsDict[indexVerify]["priority"] < auxStudentsDict[indexVerify]["priority"]:
                    auxDict = auxStudentsDict[indexVerify]
                    auxStudentsDict[indexVerify] = auxStudentsDict[indexVerify+1]
                    auxStudentsDict[indexVerify+1] = auxDict
        self.__students=auxStudentsDict
        return auxStudentsDict
            
    def __requests(self):
        students = dict()
        for index in range(0,self.__studentsRequesting):
            random = randint(0,100)
            while random in students.keys():
                random = randint(0,100)
            self.__students[random]=dict()
            self.__students[random]["student"]    = int(random)
            self.__students[random]["book"]       = int(0) # Nem sempre sera o mesmo Livro
            request = int(randint(1,5))
            self.__students[random]["request"]    = request # Numero de dias que requisitou o Livro, Deve ser entre 1 e 5 
            self.__students[random]["priority"]   = float(0) # prioridade
            self.__students[random]["permanence"] = int(0) # Tempo que ja ficou com o livro
            self.__students[random]["when"]       = int(self.__round) # Pode ser o numero da rodada
            self.__students[random]["attendance"] = 0
        return students
    
    # Gets and GetterSetterSwitchTweak
    def getStudents(self):
        return self.__students
    def getRounds(self):
        return self.__round
    def getRound(self,index):
        auxList = self.__round_dict[index]
        return auxList
    def getReady(self):
        students = list()
        auxList = self.__listReady.keys()
        for index in auxList:
            students.append("Aluno: {0} +-+ Dias de Atendimento: {1}".format(str(index),str(self.__listReady[index]["attendance"]+1)))
        return students 

def export_file(students):
    arquivo = file("Saida.txt","w")
    string = '\n'.join(str(e) for e in students)
    arquivo.write(str(string))
    #arquivo.writelines(students)
    arquivo.close()

def dailyVisualization():
    
    simulation = SimulationAPI()
    while 1 :
        auxDict = simulation.nextRound()
        auxList = auxDict.keys()
        if len(auxList) == 0:
            break
    for index in range(0, simulation.getRounds()):
        print("Rodada:"+str(index+1))
        aux = simulation.getRound(index)
        livros = aux.items()
        for livro in livros:
            print("Livro:"+str(livro[0])+" +-+ "+"Aluno"+str(livro[1]))
    
    return simulation

def clear():
    subprocess.call("clear")

def options():
    clear()
    print("Para Acessar os Menus Digite:")
    print("1-) Vizualizaco diaria;")
    print("2-) Simulacao Completa;")
    print("0-) Para Sair.")

def choise():
    while 1:
        choice = raw_input()
        if choice in ["0","1","2"]:
            return choice
        else:
            options()
