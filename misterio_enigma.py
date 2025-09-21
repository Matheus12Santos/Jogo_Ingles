import os
from tkinter import *
import sys

def resource_path(relative_path):
    """Obtenha o caminho do arquivo, considerando o caminho do executável ou o caminho normal em desenvolvimento."""
    try:
        # PyInstaller cria uma pasta temporária para o executável. O sys._MEIPASS é onde o arquivo é extraído temporariamente.
        base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
        return os.path.join(base_path, relative_path)
    except Exception:
        return os.path.join(os.path.abspath('.'), relative_path)

while True:
    os.system("cls")
    print("------------------------------------------------ O MISTERIO DAS SOMBRAS ------------------------------------------------")
    escolh = int(input("\n    1 - JOGAR\n    2 - CREDITOS\n\n    3 - SAIR\n\nESCOLHA: "))
    match escolh:
        case 1:
            os.system("cls")
            print("------------------------------------------------------\n                       PROLOGO\n------------------------------------------------------")
            print("\n\nVocê é Alex, um investigador renomado em uma cidade antiga cheia de mistérios e segredos.\nHá anos, uma sombra misteriosa vem assombrando a cidade, e ninguém  sabe de  onde ela vem\nou como pará-la.")
            input("\nAperte ENTER para avancar...")
            print("\nUma noite, você recebe uma carta misteriosa que diz:\n     “A chave para a salvação da cidade está em um segredo guardado há séculos. Para descobrir\n      a verdade, você deve desvendar os enigmas da antiga biblioteca. Cada pista foi deixada\n      por aqueles que tentaram antes de você, mas falharam ao não compreender o poder da voz passiva.”")
            input("\nAperte ENTER para avancar...")
            print("\nCom essas palavras em mente, você vai até a biblioteca abandonada, um lugar que poucos\nousam entrar. Lá, você encontra uma série de enigmas e desafios, todos ligados ao uso\nda voz passiva. Se você conseguir resolvê-los, poderá descobrir a verdadeira origem da\nsombra e salvar a cidade. Caso contrário, a cidade será engolida pelas trevas para sempre.")
            input("\nAperte ENTER para explorar a biblioteca...")
            os.system("cls")
            print("------------------------------------------------------\n                    BIBLIOTECA\n------------------------------------------------------")
            print("\n\nEnigma 1: O Primeiro Mistério\n\nVocê entra em uma sala de paredes cobertas por livros antigos. No centro da sala,\nhá uma mesa com um diário aberto. A página que está aberta diz:")
            print("\n       The door ____ (lock) every night at midnight.\n")
            print("A mensagem parece ser uma pista importante. Quando você tenta ler mais, as palavras\ndesaparecem da página, mas você consegue ver uma chave brilhando em um canto da sala.\nPara pegar a chave, você precisa resolver o enigma.")
            eng1 = input("\nResponda: ")

            if eng1.lower() == "is locked":
                os.system("cls")
                print("------------------------------------------------------\n                    BIBLIOTECA\n------------------------------------------------------")
                print("\n\nEnigma 2: A Encruzilhada\n\nApós pegar a chave, você avança para o próximo corredor, onde encontra três portas,\ncada uma com uma inscrição. As portas estão trancadas, mas você percebe que uma delas\nleva à próxima pista. Em uma das portas, está escrito:")
                print("\n       The ancient scroll ____ (discover) in the tomb of the first king.\n")
                eng2 = input("\nResponda: ")

                if eng2.lower() == "was discovered":
                    os.system("cls")
                    print("------------------------------------------------------\n                    BIBLIOTECA\n------------------------------------------------------")
                    print("\n\nEnigma 3: O Código Perdido\n\nVocê chega a uma sala escura, iluminada apenas por velas. No fundo, há uma grande caixa\ntrancada. Na frente dela, um painel com um enigma está escrito:")
                    print("\n       The secret message ____ (write) by the last protector of the city.\n")
                    print("Você precisa preencher a lacuna corretamente para desbloquear a caixa e encontrar o próximo\nitem necessário para sua jornada.")
                    eng3 = input("\nResponda: ")

                    if eng3.lower() == "was written":
                        os.system("cls")
                        print("------------------------------------------------------\n                    BIBLIOTECA\n------------------------------------------------------")
                        print("\n\nEnigma 4: O Relógio Parado\n\nUma enorme parede de relógios antigos ocupa uma parte da sala. Um deles está parado,\ncom uma inscrição abaixo:")
                        print("\n       The clock ____ (repair) by the master clockmaker every year.\n")
                        print("Você percebe que a resposta correta pode dar um impulso para o próximo passo. O relógio\nprecisa ser ajustado para que a sala se abra.")
                        eng4 = input("\nResponda: ")
                        
                        if eng4.lower() == "is repaired":
                            os.system("cls")
                            print("------------------------------------------------------\n                    BIBLIOTECA\n------------------------------------------------------")
                            print("\n\nEnigma 5: O Último Enigma\n\nFinalmente, você chega à última sala, onde a sombra misteriosa parece estar mais forte.\nNo centro, há uma mesa de pedra com uma inscrição final:")
                            print("\n       The final truth ____ (reveal) only when the last enigma is solved.\n")
                            print("Essa é a última pista. Para salvar a cidade, você precisa usar a voz passiva corretamente\ne descobrir o segredo por trás das sombras.")
                            eng5 = input("\nResponda: ")

                            if eng5.lower() == "will be revealed":
                                os.system("cls")
                                print("------------------------------------------------------\n		    O FIM DA SOMBRA\n------------------------------------------------------")
                                print("\n\nVocê deu a resposta final. ""Will be revealed"". A inscrição na mesa de pedra se ilumina\ncom uma luz suave, e a sombra misteriosa no centro da sala, antes ameaçadora, começa a\nse dissipar. Ela se transforma em uma névoa clara e brilhante que revela um amuleto de\ncristal.")
                                print("\nO amuleto pulsa com uma energia pura e revigorante. Você o segura, e a sensação é a de\nque toda a escuridão da cidade, que parecia tão opressiva, começa a se desfazer. As velas\nse acendem em toda a sala, as portas se abrem com um som de boas-vindas e a luz da manhã\nirrompe pelas janelas.")
                                print("\nA cidade está salva. As sombras foram banidas e, por onde você passa, a vida retorna com\ncores vibrantes e um som de alívio. Você não é mais um simples aventureiro; você é o herói\nque desvendou a verdade por trás da escuridão e restaurou a esperança para todos. Sua jornada\nterminou, e a cidade, grata, comemora seu triunfo.\n")
                                print("FIM DE JOGO :P (O.O) :-]")
                                input("\nAperte ENTER para ir ao menu...")
                                continue
                            else:
                                print("\nA resposta que você deu não foi a certa. A inscrição na mesa de pedra, que antes era uma\npromessa, se estilhaça em milhares de pedaços que se dissipam no ar. A sombra misteriosa,\nque antes estava distante, agora te envolve por completo, consumindo a luz e toda a esperança.\nA verdade final nunca foi revelada, e a cidade fica para sempre presa na escuridão.\n\nFIM DE JOGO.")
                                input("\nAperte ENTER para voltar ao menu...")
                                continue
                        else:
                            print("\nO relógio, ao invés de se ajustar, começa a girar furiosamente para trás. Os ponteiros\nse movem cada vez mais rápido, e o som dos seus mecanismos é como um grito estridente\nque ecoa pela sala. A parede inteira de relógios se desintegra em uma nuvem de poeira\ndourada. O tempo se desfez, e com ele, a sua chance de continuar a jornada.\n\nFIM DE JOGO.")
                            input("\nAperte ENTER para voltar ao menu...")
                            continue
                    else:
                        print("\nVocê digitou a resposta e a caixa soltou um ruído seco. Em vez de se abrir, ela começou a\nse dissolver em um pó negro, que se espalhou pelo ar, sufocando as chamas das velas. A\nescuridão total se abate sobre a sala, e você sente a presença misteriosa se aproximar. O\nsegredo permanece trancado para sempre, e sua jornada termina aqui.\n\nFIM DE JOGO.")
                        input("\nAperte ENTER para voltar ao menu...")
                        continue
                else: 
                    print("\nUma escolha errada. A porta que você escolheu tremeu e se fechou com um estrondo,\nfazendo com que as outras duas se solidificassem em pedra. O corredor que antes parecia\ncheio de possibilidades, agora é um beco sem saída. Um ar frio e pesado te envolve e, à\nmedida que a luz do seu lampião se apaga, você percebe que o seu caminho terminou ali.\n\nFIM DE JOGO.")
                    input("\nAperte ENTER para voltar ao menu...")
                    continue
            else:
                print("\nVocê hesitou. A resposta não veio. As palavras no diário, que antes brilhavam, agora se transformam\nem cinzas escuras, cobrindo o chão. A luz da chave cintilante se apaga, deixando na sala na mais\ncompleta escuridão. Um som de porta se fechando para sempre ecoa, e você percebe que a oportunidade\nde desvendar o mistério se foi.\n\nFIM DE JOGO.")
                input("\nAperte ENTER para voltar ao menu...")
                continue
        case 2:
            os.system("cls")
            print("----------------------- CREDITOS ----------------------- ")
            print("\n    Arthur Batista       (Figurante 1) (‾‾o‾‾)")
            print("\n    Gabriel Whanderson   (Figurante 2)  (▀̿Ĺ̯▀̿̿)")
            print("\n    Matheus Santos       (Protagonista) (⌐■_■)")
            input("\n\nAperte ENTER para voltar...")
            continue
        case 3:
            os.system("cls")
            print("----------------------- QUE FRIO (=.=) ----------------------- ")
            print("\nJogo encerrado, RECEBA...\n")
            break
        case _:
            os.system("cls")
            print("----------------------- Ó NOJERA (T_T) ----------------------- ")
            print("\nTres opçoes para apertar e voce ainda conseguiu errar (X_X)")
            ester_egg = int(input("\n\nAperte ENTER para voltar...\n\n\n\nEaster Egg tecla 2."))            
            if ester_egg == 2:
                root = Tk()
                root.iconbitmap(resource_path("images/icone_bitmap.ico"))  # Usando resource_path para o ícone
                root.title("Lucas Enzo (^_____^)")

                # Acessando a imagem corretamente no executável
                img = PhotoImage(file=resource_path("images/ester_egg_image.png"))
                label_image = Label(root, image=img).pack()

                root.mainloop()
            continue