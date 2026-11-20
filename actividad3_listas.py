songs = ["Love story" , "Prelude in E minor Op 28 No. 4" , "Stay" , "Boring" , "Die for you"]
eliminadas = []

songs.append("Time of dying")
print(songs)
songs.insert(1 , "Heart Attack")
print(songs)
lista = ["Bonus Track 1" , "Bonus Track 2"]
songs.extend(lista)
print(songs)

songs.remove("Boring")
eliminadas.append("Boring")
print(songs)

eliminadas.append(songs[0])
songs.pop(0)
print(f"Canciones eliminadas: {eliminadas}")


print(songs)
songs.sort()
print(songs)

print(f"Hay {len(songs)-2} canciones en la lista\nLa primera canción que agregué está en la posición {songs.index("Time of dying")+1}\nBonus Track 1 aparece {songs.count("Bonus Track 1")} vez")
