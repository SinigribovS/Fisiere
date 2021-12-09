f,a,b,c=open('input.txt', 'r',encoding='utf-8'),[],[],[]
print('Nr. Nume Prenume Nota1 Nota2 Nota3')
for i in f: a.append(list(i.rstrip().split(' ')));print(i.rstrip());b.append(i)
with open('rezerva.txt', 'w',encoding='utf-8') as s: s.writelines(b)
print('\nNr. Nume Prenume Media')
for i in a: c.append(' '.join(i[:3])+' '+str(round(sum([float(x) for x in i[3::]])/len(i[3::]),2))); print(' '.join(i[:3])+' '+str(round(sum([float(x) for x in i[3::]])/len(i[3::]),2)))
with open('output.txt', 'w',encoding='utf-8') as g: g.writelines(['%s\n'%i for i in c])