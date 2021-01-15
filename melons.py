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
    # I kept getting winter squash is yellow REJECTED so I 
    # changed prep_squash to prep(self) because it has to be same as Melon class prep for it to pass through! 
    #Yay! it works!
    def prep(self):
        """Prep the squash by painting it green"""
        #add a method that handles prep(in superclass) this one handles the painting
        robots.cleanerbot.clean(self)
        robots.painterbot.paint(self)
        robots.stickerbot.apply_logo(self)
        
        
    

    pass

