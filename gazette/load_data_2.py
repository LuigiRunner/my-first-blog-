import csv

from models import AffairesSansRelation

with open('gazette/affaires_sans_relation.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if row!="Nom et prénom du commercial leader":
            affairessansrelation=AffairesSansRelation()
            affairessansrelation.NomPrenomLeader=row[0]
            affairessansrelation.NumeroChantier=row[1]
            affairessansrelation.NbreLogements=row[2]
            affairessansrelation.DateFinChantier=row[3]
            affairessansrelation.TypeChantier=row[4]
            affairessansrelation.StatutChantier=row[5]
            affairessansrelation.NumeroChantier=row[6]
            affairessansrelation.save()

 



        