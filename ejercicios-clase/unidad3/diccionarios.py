# Estados iniciales del juego
caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':1.0, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

print("Valor : ",guerrero['vida'])

#Primera condicion : El caballero tiene el doble de vida y defensa que un guerrero.
caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

#Segunda condicion :  El guerrero tiene el doble de ataque y alcance que un caballero.

guerrero['ataque']  = caballero['ataque']*2
guerrero['alcance']  = caballero['alcance']*2

#Tercera condicion : El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa']/2
arquero['alcance'] = guerrero['alcance']*2

# Mostrar los resultados

print("Caballeros : ",caballero )
print("Guerrero : ",guerrero )
print("Arquero : ",arquero )
