dict_contatti={}

dict_contatti={"gigi":12345, "paperino":43256, "pluto":548790}

print("I tuoi contatti: ",dict_contatti)

dict_contatti["paperone"]=109872

print("I tuoi contatti: ",dict_contatti)

if "minie" in dict_contatti:
    print("Si")
else:
    print("No")

print(len(dict_contatti))