# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:16:48 2021

@author: Baptiste
"""

import json
from tkinter import *
import phe as paillier



import linmodel
import cust
import servercalc



    
def main():     
    
    linmodel.mainLinModel()
    servercalc.mainServerCalc()
    
    
    print("Saisissez les donnees sous la forme a,b,c,d avec a,b,c et d 4 entiers")
    input1 = input()   
    
    
    pub_key, priv_key = cust.getKeys()
    data = []
    for i in range(4):
        print(input1.split(',')[i] , " est chiffré par ", servercalc.getData().get('values')[i][0][0:12], '...')
        data.append(int(input1.split(',')[i]))
    cust.serializeData(pub_key, data)
    datafile = cust.serializeData(pub_key, data)
    with open('data.json', 'w') as file:
        json.dump(datafile, file)
    
    answer_file = cust.loadAnswer()
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    answer = paillier.EncryptedNumber(answer_key, int(answer_file['values'][0]),
                                  int(answer_file['values'][1]))
    print(priv_key.decrypt(answer))
    
    # Affichage
    
    window = Tk()
    window.title("Simulation")
    window.geometry("1920x1060")
    window.iconbitmap("hash.ico")
    window.config(background='grey')

    # premier texte

    label_title = Label(window,
                    text="Simulation",
                    font=("Courrier, 30"),
                    bg='Grey',
                    fg='white')
    label_title.grid(row=0, column=2)
    
    label_title = Label(window,
                    text="Chiffrement homomorphe",
                    font=("Courrier, 30"),
                    bg='Grey',
                    fg='white')
    label_title.grid(row=1, column=2)    
    # second texte

    label_subtitle1 = Label(window,
                        text="① Utilisateur",
                        font=("Courrier, 25"),
                        bg='white',
                        fg='grey')
    label_subtitle1.grid(row=2, column=1)

    #troisieme texte

    label_subtitle3 = Label(window,
                        text="Les données entrées par l'utilisateur sont :",
                        font=("Courrier,25"),
                        bg='grey',
                        fg='white')
    label_subtitle3.grid(row=3, column=1)

    
    label_subtitle4 = Label(window,
                        text=data,
                        font=("Courrier,500"),
                        bg='grey',
                        fg='white')
    label_subtitle4.grid(row=4, column=1) 
    
    
    label_subtitle3 = Label(window,
                        text="et sont chiffrées respectivement par :",
                        font=("Courrier,25"),
                        bg='grey',
                        fg='white')
    label_subtitle3.grid(row=5, column=1)
    

    label_subtitle5 = Label(window,
                        text=servercalc.getData().get('values')[0][0][0:12]+"...",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=6, column=1)

    label_subtitle5 = Label(window,
                        text=servercalc.getData().get('values')[1][0][0:12]+"...",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=7, column=1)
    
    label_subtitle5 = Label(window,
                        text=servercalc.getData().get('values')[2][0][0:12]+"...",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=8, column=1)

    label_subtitle5 = Label(window,
                        text=servercalc.getData().get('values')[3][0][0:12]+"...",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=9, column=1)
    
    

    label_subtitle2 = Label(window,
                        text="② Serveur externe (cloud)",
                        font=("Courrier, 25"),
                        bg='white',
                        fg='grey')
    label_subtitle2.grid(row=10, column=3)


    label_subtitle5 = Label(window,
                        text="Les coefficients donnés par l'algorithme de Machine Learning à appliqués aux données sont :",
                        font=("Courrier,25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=11, column=3)


    label_subtitle5 = Label(window,
                        text=linmodel.LinModel().getCoef(),
                        font=("Courrier,25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=12, column=3)


    label_subtitle5 = Label(window,
                        text="L'opération \"coefficient i\" multiplié par  l'élément i des données chiffrées donne :",
                        font=("Courrier,25"),
                        bg='grey',
                        fg='white')
    label_subtitle5.grid(row=13, column=3)


    label_subtitle6 = Label(window,
                        text=answer_file['values'][0][0:12]+"...",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle6.grid(row=14, column=3)
    #computeData()[0].ciphertext()



    label_subtitle1 = Label(window,
                        text="③ Utilisateur",
                        font=("Courrier, 25"),
                        bg='white',
                        fg='grey')
    label_subtitle1.grid(row=15, column=1)


    label_subtitle1 = Label(window,
                        text="Récupération du résultat chiffré",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle1.grid(row=16, column=1)

    label_subtitle1 = Label(window,
                        text="Après déchiffrement, on obtient :",
                        font=("Courrier, 25"),
                        bg='grey',
                        fg='white')
    label_subtitle1.grid(row=17, column=1)
    
    
    label_subtitle7 = Label(window,
                        text=priv_key.decrypt(answer),
                        font=("Courrier,35"),
                        bg='grey',
                        fg='white')
    label_subtitle7.grid(row=18, column=1)

#    window.grid_rowconfigure(0, minsize=150)
#    window.grid_rowconfigure(8, minsize=150)
#    window.grid_rowconfigure(5, minsize=150)

    # afficher

    window.mainloop()



if __name__ == "__main__":
    main()
    
    
