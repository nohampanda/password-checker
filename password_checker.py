def verifier_long(mdp):
   return len(mdp) >= 8
def verifier_majuscule(mdp):
   for i in mdp:
       if i.isupper():
           return True
   return False
def verifier_chiffre(mdp):
   for i in mdp:
       if i.isdigit():
           return True
   return False
def verifier_symbole(mdp):
   symboles = "!@#$%^&*()-+"
   for i in mdp:
       if i in symboles:
           return True
   return False
mdp = input("Entrez votre mot de passe : ")
score = 0
conseils = []
if verifier_long(mdp):
   score += 1
else:
   
   conseils.append("Le mot de passe doit contenir au moins 8 caractères.")
if verifier_majuscule(mdp):
   score += 1
else:
   conseils.append("Le mot de passe doit contenir au moins une majuscule.")
if verifier_chiffre(mdp):
   score += 1
else:
   conseils.append("Le mot de passe doit contenir au moins un chiffre.")
if verifier_symbole(mdp):
   score += 1
else:
   conseils.append("Le mot de passe doit contenir au moins un symbole.")

if score == 0 or score == 1 :
   print(f"{score}/4 - Mot de passe faible")

elif score == 2:
   print(f"{score}/4 - Mot de passe moyen   ")
elif score == 3:
   print(f"{score}/4 - Mot de passe fort    ")
elif score == 4:
   print(f"{score}/4 - Mot de passe très fort")
if conseils:
   print("Conseils pour améliorer votre mot de passe :")
   for conseil in conseils:
       print("- " + conseil)
else:
       print("Votre mot de passe est très fort !")