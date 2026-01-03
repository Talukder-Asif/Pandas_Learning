import pandas as pd

df = pd.read_csv("Pokemon.csv")

# Filtering means keeping the rows that match a condition

#print(df.to_string())

durablePokemon = df[df["HP"] >= 100]
#print(durablePokemon.to_string())

stringPokemon = df[(df["HP"]>= 100) & (df["Attack"] >= 100)]
#print(stringPokemon .to_string())

strong_fighting_pokemon = stringPokemon[(stringPokemon["Type 1"] == "Fighting") | (stringPokemon["Type 2"] == "Fighting")]
print(strong_fighting_pokemon.to_string())