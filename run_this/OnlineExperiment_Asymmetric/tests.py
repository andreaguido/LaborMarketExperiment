from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.strategymethod, {
            'steffort1' : 2,
            'steffort2' : 2,
            'steffort3' : 2,
            'steffort4' : 2,
            'steffort5' : 2,
            'steffort6' : 2,
            'steffort7' : 2,
            'steffort8' : 2,
            'steffort9' : 2,
            'steffort10' : 2
        })
        yield (pages.strategymethodPOSITIVE,
               {
                   'steffort1': 2,
                   'steffort2': 2,
                   'steffort3': 2,
                   'steffort4': 2,
                   'steffort5': 2,
                   'steffort6': 2,
                   'steffort7': 2,
                   'steffort8': 2,
                   'steffort9': 2,
                   'steffort10': 2,
                   'steffort11': 2,
                   'steffort12': 2
               })

        yield (pages.strategymethodNEGATIVE,
               {
                   'steffort1': 2,
                   'steffort2': 2,
                   'steffort3': 2,
                   'steffort4': 2,
                   'steffort5': 2,
                   'steffort6': 2,
                   'steffort7': 2,
                   'steffort8': 2,
               })

        yield (pages.beliefelicitation, {
            'eleffort1' : 2,
            'eleffort2' : 2,
            'eleffort3' : 2,
            'eleffort4' : 2,
            'eleffort5' : 2,
            'eleffort6' : 2,
            'eleffort7' : 2,
            'eleffort8' : 2,
            'eleffort9' : 2,
            'eleffort10' : 2
        })
        yield (pages.beliefelicitationPOSITIVE,
               {
                   'eleffort1': 2,
                   'eleffort2': 2,
                   'eleffort3': 2,
                   'eleffort4': 2,
                   'eleffort5': 2,
                   'eleffort6': 2,
                   'eleffort7': 2,
                   'eleffort8': 2,
                   'eleffort9': 2,
                   'eleffort10': 2,
                   'eleffort11': 2,
                   'eleffort12': 2
               })

        yield (pages.beliefelicitationNEGATIVE,
               {
                   'eleffort1': 2,
                   'eleffort2': 2,
                   'eleffort3': 2,
                   'eleffort4': 2,
                   'eleffort5': 2,
                   'eleffort6': 2,
                   'eleffort7': 2,
                   'eleffort8': 2,
               })
        yield (pages.beliefworker,
                       {'wagebelief':6
                        })

        yield (pages.Offre_Principal,
                               {'wage':6
                                })

        yield (pages.Choix_Agent,
                                       {'effort':2
                                        })
