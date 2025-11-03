from hats import change_my_hat

# TODO: разбить посадки на модули

clear()
do_a_flip()

while True:

	# Столбцы
	for i in range(get_world_size()):

		# Ячейки
		for j in range(get_world_size()):

			if can_harvest():
				harvest()

			if get_entity_type() == Entities.Grass:
				till()
			
			if i < 4 and j > 3: # Верхний левый угол
				plant(Entities.Tree)
			elif i > 3 and j > 3: # Верхний правый угол
				plant(Entities.Pumpkin)
			elif i < 4 and j < 4: # Нижний левый угол
				plant(Entities.Carrot)
			elif i > 3 and j < 4: # Нижний правый угол
				plant(Entities.Cactus)
			
			if num_items(Items.Water) > 15000:
				use_item(Items.Water)
				
			elif get_entity_type() == Entities.Dead_Pumpkin:

				for _ in range(1): 
					till()

				plant(Entities.Pumpkin)

			move(North)
			
			change_my_hat(i)

		move(East)

	do_a_flip()
