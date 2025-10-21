while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			move(North)

			if can_harvest():
				harvest()
				if i % 2 != 1:
					till()
					# use_item(Items.Water)
					plant(Entities.Carrot)
				else:
					plant(Entities.Bush)

		move(East)

		if i == 0:
			change_hat(Hats.Gray_Hat)
		elif i == 1:
			change_hat(Hats.Purple_Hat)
		elif i == 2:
			change_hat(Hats.Green_Hat)
		else:
			change_hat(Hats.Brown_Hat)
