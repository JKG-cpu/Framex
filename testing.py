from Framex import Frame
from Framex import DynamicEntity
from Framex import Factory

f = Frame()
fact = Factory()

dynamic_sprite = DynamicEntity(
    image = fact.create_surface(
        color = (255, 0, 0),
        alpha = True
    ),
    position = (50, 50),
    player_controlled = True
)
f.add_sprite(dynamic_sprite)

f.run()