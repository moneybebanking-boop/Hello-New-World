goblin_health = 100
sword_damage = 25

print("⚔️ You encounter a Goblin!")
print("👺 Goblin Health:", goblin_health)

while goblin_health > 0:
    input("\nPress Enter to swing your sword... ")

    goblin_health -= sword_damage

    if goblin_health > 0:
        print("💥 You hit the goblin for", sword_damage, "damage!")
        print("👺 Goblin Health is now:", goblin_health)
    else:
        print("💥 You hit the goblin for", sword_damage, "damage!")
        print("👺 Goblin Health is now: 0")
        print("\n🏆 The goblin has been defeated! You win!")
