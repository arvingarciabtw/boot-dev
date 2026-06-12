import type { State } from "./state.ts";

export async function commandExplore(
  state: State,
  ...args: string[]
): Promise<void> {
  const name = args[0];
  console.log(`Exploring ${name}...`);
  console.log("Found Pokemon:");
  const loc = await state.pokeAPI.fetchLocation(name);
  for (const e of loc.pokemon_encounters) {
    console.log(` - ${e.pokemon.name}`);
  }
}
