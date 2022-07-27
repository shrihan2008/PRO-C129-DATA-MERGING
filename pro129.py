import csv
data=[]
with open('dwarf_stars.csv','r') as f:
    read=csv.reader(f)
    for i in read:
        data.append(i)
nan = f
f= f.dropna()
f=f[f['Radius'].notna()]
f=f[f['Mass'].notna()]
f=f[f['Distance'].notna()]
mass=f["mass"].float()
radius=f["radius"].float()
radius=radius*0.102763
mass=mass*0.000954588


headers=data[0]

star_data=data[1:]
with open('browndwarfs_sorted.csv','a+') as f:
    write=csv.writer(f)
    write.writerow(headers)
    write.writerows(star_data)