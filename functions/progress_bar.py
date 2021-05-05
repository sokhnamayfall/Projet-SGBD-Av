import tkinter
import tkinter.ttk

def progress_bar():
    def FNC_Depart ( ) :
        WAI_Test.start ( 20 )
        BUT_Depart [ "state" ] = "disabled"
        FNC_Fin ( ) 

    def FNC_Fin ( ) :
        TKI_Principal.wait_variable ( TKV_Progression )
        if TKV_Progression.get ( ) > 98 :
            WAI_Test.stop ( )
            LAB_Valeur [ "text" ] = "Téléchargement terminé !"   
        else :
            LAB_Valeur [ "text" ] = TKV_Progression.get ( )
            FNC_Fin ( )

    TKI_Principal = tkinter.Tk ( )
    TKV_Progression = tkinter.IntVar ( )
    BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )
    BUT_Depart = tkinter.Button ( TKI_Principal , text = "Lancer" , command = FNC_Depart )
    WAI_Test = tkinter.ttk.Progressbar ( TKI_Principal , variable = TKV_Progression , maximum = 100 )
    LAB_Valeur = tkinter.Label ( TKI_Principal )

    LAB_Valeur.pack ( )
    WAI_Test.pack ( )
    BUT_Depart.pack ( )
    BUT_Quitter.pack ( )

    TKI_Principal.mainloop ( )
