import SimulationAPI


def main():
    simulation = SimulationAPI.SimulationAPI()
    while 1 :
        auxDict = simulation.nextRound()
        auxList = auxDict.keys()
        if len(auxList) == 0:
            break
    while 1:
        SimulationAPI.options()
        choice = SimulationAPI.choise()
        if choice == "1":
            for index in range(0, simulation.getRounds()):
                print("Rodada:"+str(index+1))
                aux = simulation.getRound(index)
                livros = aux.items()
                for livro in livros:
                    print("Livro:"+str(livro[0])+" +-+ "+"Aluno"+str(livro[1]))
            raw_input("Pressione Qualquer Tecla!")
        elif choice == "2":
            SimulationAPI.export_file(simulation.getReady())
            raw_input("Dados Exportados! Pressione Qualquer Tecla!")
        else:
            break


if __name__ == "__main__":
    main()
