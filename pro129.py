import csv
data=[]
with open('dwarf_stars.csv','r') as f:
    read=csv.reader(f)
    for i in read:
        data.append(i)

f=f.dropna()
star_data=data[1:]
headers=data[0]
star_data.sort(key=lambda star_data:star_data[2])
mass=f["Mass"]
mass=float(mass)
radius=f["Radius"]
radius=float(radius)
radius=radius*0.102763
mass=mass*0.000954588

with open('browndwarfs_sorted.csv','a+') as f:
    write=csv.writer(f)
    write.writerow(headers)
    write.writerows(star_data)