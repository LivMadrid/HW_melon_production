import robots


class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)

# FIXME: Add Squash class definition here.
class Squash(Melon):
    """Squash class with Melon Superclass"""
    def prep_squash(self):
        """Prep the squash by painting it green"""
        #add a method that handles prep(in superclass) this one handles the painting
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
#add a conditional statement so that we can paint squash green 
        if self.color != green:
            robots.painterbot.paint(self)
        
        


    pass

