from Tkinter import *

# master =  Tk()

# Label(master, text = "executioner").grid(row = 0)
# Label(master, text = "killing_spree").grid(row = 1)
# Label(master, text = "grim_reaper").grid(row = 2)
# Label(master, text = "hat_trick").grid(row = 3)
# Label(master, text = "guardian_angel").grid(row = 4)
# Label(master, text = "highlander").grid(row = 5)
# Label(master, text = "ringout").grid(row = 6)
# Label(master, text = "dominating").grid(row = 7)
# Label(master, text = "archenemy").grid(row = 8)
# Label(master, text = "healer").grid(row = 9)
# Label(master, text = "double_hero_kill").grid(row = 10)
# Label(master, text = "killjoy").grid(row = 11)
# Label(master, text = "summoner").grid(row = 12)
# Label(master, text = "herald").grid(row = 13)
# Label(master, text = "nemesis").grid(row = 14)
# Label(master, text = "first_blood").grid(row = 15)
# Label(master, text = "legionnaire").grid(row = 16)
# Label(master, text = "epic_comeback").grid(row = 17)
# Label(master, text = "assist_spree").grid(row = 18)
# Label(master, text = "power_thief").grid(row = 19)
# Label(master, text = "wingman").grid(row = 20)
# Label(master, text = "elder_shaman").grid(row = 21)
# Label(master, text = "triple_hero_kill").grid(row = 22)
# Label(master, text = "shepherd").grid(row = 23)
# Label(master, text = "rampage").grid(row = 24)
# Label(master, text = "showstopper").grid(row = 25)
# Label(master, text = "revenge").grid(row = 26)
# Label(master, text = "creature_defender").grid(row = 27)
# Label(master, text = "unstoppable").grid(row = 28)
# Label(master, text = "sever_the_bond").grid(row = 29)
# Label(master, text = "protector_savior").grid(row = 0, column = 2)
# Label(master, text = "ghost_hunter").grid(row = 1, column = 2)
# Label(master, text = "king_of_the_mountain").grid(row = 2, column = 2)
# Label(master, text = "shaman").grid(row = 3, column = 2)
# Label(master, text = "comeback").grid(row = 4, column = 2)
# Label(master, text = "raider").grid(row = 5, column = 2)
# Label(master, text = "power_play").grid(row = 6, column = 2)
# Label(master, text = "avenger").grid(row = 7, column = 2)
# Label(master, text = "retribution").grid(row = 8, column = 2)
# Label(master, text = "penta_hero_kill").grid(row = 9, column = 2)
# Label(master, text = "harbinger").grid(row = 10, column = 2)
# Label(master, text = "quadra_hero_kill").grid(row = 11, column = 2)
# Label(master, text = "master_healer").grid(row = 12, column = 2)
# Label(master, text = "survivor").grid(row = 13, column = 2)
# Label(master, text = "exorcist").grid(row = 14, column = 2)
# Label(master, text = "sidekick").grid(row = 15, column = 2)
# Label(master, text = "exterminator").grid(row = 16, column = 2)
# Label(master, text = "triple_threat").grid(row = 17, column = 2)
# Label(master, text = "grandmaster_healer").grid(row = 18, column = 2)
# Label(master, text = "vanguard").grid(row = 19, column = 2)
# Label(master, text = "shooting_star").grid(row = 20, column = 2)
# Label(master, text = "guardian_defender").grid(row = 21, column = 2)
# Label(master, text = "shutout").grid(row = 22, column = 2)
# Label(master, text = "gigantic").grid(row = 23, column = 2)

# entry01 = Entry(master)
# entry02 = Entry(master)

# entry01.grid(row = 0, column = 1)
# entry02.grid(row = 1, column = 1)

root = Tk()
badges = ["executioner", "killing_spree", "grim_reaper", "hat_trick", "guardian_angel", "highlander", "ringout", "dominating", "archenemyhealer",
"double_hero_kill", "killjoy", "summoner", "herald", "nemesis", "first_blood", "legionnaire", "epic_comeback", "assist_spree", "power_thief", "wingman",
"elder_shaman", "triple_hero_kill", "shepherd", "rampage", "showstopper", "revenge", "creature_defender", "unstoppable", "sever_the_bond",
"ghost_hunter", "king_of_the_mountain", "shaman", "comeback", "raider", "power_play", "avenger", "retribution", "penta_hero_kill", "harbinger",
"quadra_hero_kill", "master_healer", "survivor", "exorcist", "sidekick", "exterminator", "triple_threat", "grandmaster_healer", "vanguard",
"shooting_star", "guardian_defender", "shutout", "gigantic", "protector_savior"]

def makeForm(root, fields):
	entries = []
	for badge in badges:
		row = Frame(root)
		label = Label(row, width = 15, text = badge, anchor = "w")
		entry = Entry(row)
		row.pack(side = TOP, fill = X, padx = 5, pady = 5)
		label.pack(side = LEFT)
		entry.pack(side = RIGHT, expand = YES, fill = X)
		entries.append((badge, entry))
	return entries

form = makeForm(root, badges)
	
mainloop()