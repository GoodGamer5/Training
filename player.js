const defaultPlayer = { name: "Hero", hp: 100 };
export const getHP = (player) => player.hp;
export const setHP = (player, hp) => ({ ...player, hp });
const named = { getHP, setHP };
export { defaultPlayer, named };