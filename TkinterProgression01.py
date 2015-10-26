from Tkinter import *

root = Tk()
badges = sorted(["executioner", "killing_spree", "grim_reaper", "hat_trick", "guardian_angel", "highlander", "ringout", "dominating", "archenemy", "healer", "double_hero_kill", "killjoy", "summoner", "herald", "nemesis", "first_blood", "legionnaire", "epic_comeback", "assist_spree", "power_thief", "wingman", "elder_shaman", "triple_hero_kill", "shepherd", "rampage","showstopper", "revenge", "creature_defender", "unstoppable", "sever_the_bond", "ghost_hunter", "king_of_the_mountain", "shaman", "comeback", "raider", "power_play", "avenger", "retribution", "penta_hero_kill", "harbinger", "quadra_hero_kill", "master_healer", "survivor", "exorcist", "sidekick", "exterminator", "triple_threat", "grandmaster_healer", "vanguard", "shooting_star", "guardian_defender", "shutout", "gigantic", "protector_savior"])

def printField():
	print("quantity: %s" % ((form["executioner"].get())))

def makeForm(root, fields):
	entries = {}
	row = 0
	row_new = 0
	for badge in badges:
		label = Label(width = 20, text = badge, anchor = "w")
		entry = Entry(width = 6)
		if row > 30:
			label.grid(row = row_new, column = 2)
			entry.grid(row = row_new, column = 3)
			row_new += 1
		else:
			label.grid(row = row, column = 0)
			entry.grid(row = row, column = 1)
			row += 1
		entries[badge] = entry
	print entries
	bPrint = Button(root, text = "Print", command = printField)
	bPrint.grid()
	return entries
	


form = makeForm(root, badges)
# printField
mainloop()
