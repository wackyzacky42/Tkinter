from Tkinter import *
import time

root = Tk()
badges = sorted(["executioner", "killing_spree", "grim_reaper", "hat_trick", "guardian_angel", "highlander", "ringout", "dominating", "archenemy", "healer", "double_hero_kill", "killjoy", "summoner", "herald", "nemesis", "first_blood", "legionnaire", "epic_comeback", "assist_spree", "power_thief", "wingman", "elder_shaman", "triple_hero_kill", "shepherd", "rampage","showstopper", "revenge", "creature_defender", "unstoppable", "sever_the_bond", "ghost_hunter", "king_of_the_mountain", "shaman", "comeback", "raider", "power_play", "avenger", "retribution", "penta_hero_kill", "harbinger", "quadra_hero_kill", "master_healer", "survivor", "exorcist", "sidekick", "exterminator", "triple_threat", "grandmaster_healer", "vanguard", "shooting_star", "guardian_defender", "shutout", "gigantic", "protector_savior"])

def printField():
	#print("quantity: %s" % ((form["executioner"].get())))
	print form["executioner"].get()
	print form
	
def submitBadges():
#ASSIGN THESE BEFORE BUTTON PRESS
	# dict_form = form
	# dict_changes = dict_form
	print dict_changes
	# print dict_form

	for k in dict_changes:
		# #dict_form = form
		print k
		# # print form[k].get()
		# # print dict_form[k].get()
		dict_changes[str(k)].update(dict_form[k].get())
		#print type(form[k].get())
		# print k
		# if form[k].get() == "":
			# dict_changes[k] = 0
		# else:
			# dict_changes[k] = int(form[k].get())
		# print dict_changes
		# print form
	print dict_changes
	print dict_form
	print form

def makeForm(root, fields):
	entries = {}
	row = 0
	row_new = 0
	for badge in badges:
		label = Label(width = 20, text = badge, anchor = "w")
		entry = Entry(width = 6, textvariable = IntVar())
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
	butt_print = Button(root, text = "Print", command = printField)
	butt_submit = Button(root, text = "Submit", command = submitBadges)
	butt_print.grid()
	butt_submit.grid()
	return entries
	


form = makeForm(root, badges)
dict_changes = {}
dict_form = {}
dict_changes.update(form)

# printField
mainloop()
