import time
import threading

heure_q = input("Entrez l'heure que vous souhaitez (exemple heure:minutes:secondes) : ")
heure_separe = heure_q.split(':')
heure = (int(heure_separe[0]), int(heure_separe[1]), int(heure_separe[2]))

reveil_q = input("Entrez l'heure du réveil que vous souhaitez (exemple heure:minutes:secondes) : ")
reveil_separe = reveil_q.split(':')
reveil = (int(reveil_separe[0]), int(reveil_separe[1]), int(reveil_separe[2]))

def choix_mode():
    while True:
        mode = input("Mode d'affichage 12h ou 24h : ")
        if mode == "12h":
            return 12
        elif mode == "24h":
            return 24
        else:
            print("Erreur d'écriture, veuillez écrire soit 12h soit 24h")

mode_affichage = choix_mode()

pause_programme = False

def pause():
    global pause_programme
    while True:
        pause_q = input("             Tapez 'pause' pour mettre en pause l'horloge : ")
        if pause_q == "pause":
            pause_programme = not pause_programme
            if pause_programme:
                print("Horloge mise en pause")
                while pause_programme:
                    resume_q = input("             Tapez 'reprendre' pour reprendre l'horloge : ")
                    if resume_q == "reprendre":
                        pause_programme = not pause_programme
                        print("Horloge reprise")
                        break

def afficher_heure(heure):
    while True:
        if not pause_programme:
            heure = (heure[0],heure[1],heure[2]+1)
            time.sleep(1)
            if heure[2] == 60:
                heure = (heure[0],heure[1]+1,0)
                if heure[1] == 60:
                    heure = (heure[0]+1,0,0)
                    if heure[0] == 24:
                        heure = (0,0,0)

            if mode_affichage == 12:
                if heure[0] < 12:
                    am_pm = "AM"
                else:
                    am_pm = "PM"
                if heure[0] <= 12:
                    hour = heure[0]
                else:
                    hour = heure[0]-12
                print(f"\r{hour:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}", end="")
            else:
                print(f"\r{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}", end="")

            alarme(heure)

def alarme(heure):
    if heure == reveil:
        print("\nLEVE TOI OU JE BRULE TA MAISON")

pause_thread = threading.Thread(target=pause)
pause_thread.start()
afficher_heure(heure)
