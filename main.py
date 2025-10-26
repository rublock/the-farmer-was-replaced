from hats import change_my_hat

clear()
do_a_flip()

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if can_harvest():
				harvest()
				plant(Entities.Tree)
				if i % 2 != 1:
					till()
					use_item(Items.Water)
					plant(Entities.Sunflower)
			elif get_entity_type() == Entities.Dead_Pumpkin:
				till()
				use_item(Items.Water)
			move(North)
			
			change_my_hat(i)

		move(East)
		
