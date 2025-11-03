from hats import change_my_hat

# TODO: разбить посадки на модули

clear()
do_a_flip()

while True:

	# Столбцы
	for x in range(get_world_size()):

		# Ячейки
		for y in range(get_world_size()):

			if can_harvest():
				harvest()

			if get_entity_type() == Entities.Grass:
				till()

			if x <= get_world_size() / 2 - 1 and y <= get_world_size() / 2 - 1:
				plant(Entities.Carrot)
			elif x >= get_world_size() / 2 and y <= get_world_size() / 2 - 1:
				plant(Entities.Cactus)
			elif x <= get_world_size() / 2 - 1 and y >= get_world_size() / 2:
				plant(Entities.Tree)
			elif x >= get_world_size() / 2 and y >= get_world_size() / 2:
				plant(Entities.Pumpkin)
			
			if num_items(Items.Water) > 15000:
				use_item(Items.Water)
				
			elif get_entity_type() == Entities.Dead_Pumpkin:

				for _ in range(1): 
					till()

				plant(Entities.Pumpkin)

			move(North)
			
			change_my_hat(y)

		move(East)

	clear()
	do_a_flip()
