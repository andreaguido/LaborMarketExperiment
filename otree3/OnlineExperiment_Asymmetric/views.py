from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import math



class quiz_1(Page):
    def is_displayed(self):
        return self.round_number==1 and self.subsession.online == 0

class online_quiz_1(Page):
    def is_displayed(self):
        return self.round_number==1 and self.subsession.online == 1

class quiz_2(Page):
    def is_displayed(self):
        return self.round_number==1 and self.subsession.online == 0

class online_quiz_2(Page):
    def is_displayed(self):
        return self.round_number==1 and self.subsession.online == 1

class assign_WORKER(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.player.type=="agent"

class assign_EMPLOYER(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.player.type =="principal"

class Shock(Page):
    def is_displayed(self):
        return self.round_number==14 and self.player.type =="principal"

class Shock_Agent(Page):
    form_model = models.Group
    form_fields = ['steffort']
    def is_displayed(self):
        return self.group.shock_page == 1 and self.player.type =="agent" and (self.group.round_number == 14 or self.group.round_number == 18)
    def effort_max(self):
            return 6

    def vars_for_template(self):
        return {
            'offre_wage': self.group.wage,
            'effort_max':round(math.sqrt(2*self.group.wage),2),
            'num_round':self.subsession.round_number-3,
        }

class Gamestart_Worker(Page):
    def is_displayed(self):
        return self.round_number==4 and self.player.type =="agent"

class Gamestart_Employer(Page):
    def is_displayed(self):
        return self.round_number==4 and self.player.type =="principal"

class employerTasks(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal'
    def vars_for_template(self):
        return {
            'num_round': self.subsession.round_number
        }

class transition_to_normal_rounds(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18)
    def vars_for_template(self):
        return {
            'num_round': self.subsession.round_number
        }

class transition_to_strategy(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18)
    def vars_for_template(self):
        return {
            'num_round': self.subsession.round_number
        }

class beliefelicitation_instructions(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal'
    def vars_for_template(self):
        return{
            'num_round': self.subsession.round_number-3
        }

class beliefelicitation(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal' and self.group.shock_revealed == 0
    form_model= models.Player
    form_fields= ['eleffort1', 'eleffort2','eleffort3','eleffort4','eleffort5','eleffort6','eleffort7','eleffort8','eleffort9','eleffort10','eleffort11', 'eleffort12']
    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_8_1': self.player.in_round(8).eleffort1,
            'pre_eleffort_8_2': self.player.in_round(8).eleffort2,
            'pre_eleffort_8_3': self.player.in_round(8).eleffort3,
            'pre_eleffort_8_4': self.player.in_round(8).eleffort4,
            'pre_eleffort_8_5': self.player.in_round(8).eleffort5,
            'pre_eleffort_8_6': self.player.in_round(8).eleffort6,
            'pre_eleffort_8_7': self.player.in_round(8).eleffort7,
            'pre_eleffort_8_8': self.player.in_round(8).eleffort8,
            'pre_eleffort_8_9': self.player.in_round(8).eleffort9,
            'pre_eleffort_8_10': self.player.in_round(8).eleffort10,
            'pre_eleffort_8_11': self.player.in_round(8).eleffort11,
            'pre_eleffort_8_12': self.player.in_round(8).eleffort12
        }


class beliefelicitationPOSITIVE(Page):
    def is_displayed(self):
        return (self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal' and self.subsession.draw ==1 and self.group.shock_revealed == 1 and self.group.shock_page == 0
    form_model= models.Player
    form_fields= ['eleffort1', 'eleffort2','eleffort3','eleffort4','eleffort5','eleffort6','eleffort7','eleffort8','eleffort9','eleffort10','eleffort11','eleffort12','eleffort13','eleffort14','eleffort15','eleffort16']

    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_13_1': self.player.in_round(13).eleffort1,#to be displayed in round 14
            'pre_eleffort_13_2': self.player.in_round(13).eleffort2,
            'pre_eleffort_13_3': self.player.in_round(13).eleffort3,
            'pre_eleffort_13_4': self.player.in_round(13).eleffort4,
            'pre_eleffort_13_5': self.player.in_round(13).eleffort5,
            'pre_eleffort_13_6': self.player.in_round(13).eleffort6,
            'pre_eleffort_13_7': self.player.in_round(13).eleffort7,
            'pre_eleffort_13_8': self.player.in_round(13).eleffort8,
            'pre_eleffort_13_9': self.player.in_round(13).eleffort9,
            'pre_eleffort_13_10': self.player.in_round(13).eleffort10,
            'pre_eleffort_13_11': self.player.in_round(13).eleffort11,
            'pre_eleffort_13_12': self.player.in_round(13).eleffort12,
            'pre_eleffort_14_1': self.player.in_round(14).eleffort1,#to be displayed in round 18
            'pre_eleffort_14_2': self.player.in_round(14).eleffort2,
            'pre_eleffort_14_3': self.player.in_round(14).eleffort3,
            'pre_eleffort_14_4': self.player.in_round(14).eleffort4,
            'pre_eleffort_14_5': self.player.in_round(14).eleffort5,
            'pre_eleffort_14_6': self.player.in_round(14).eleffort6,
            'pre_eleffort_14_7': self.player.in_round(14).eleffort7,
            'pre_eleffort_14_8': self.player.in_round(14).eleffort8,
            'pre_eleffort_14_9': self.player.in_round(14).eleffort9,
            'pre_eleffort_14_10': self.player.in_round(14).eleffort10,
            'pre_eleffort_14_11': self.player.in_round(14).eleffort11,
            'pre_eleffort_14_12': self.player.in_round(14).eleffort12,
            'pre_eleffort_14_13': self.player.in_round(14).eleffort13,
            'pre_eleffort_14_14': self.player.in_round(14).eleffort14,
            'pre_eleffort_14_15': self.player.in_round(14).eleffort15,
            'pre_eleffort_14_16': self.player.in_round(14).eleffort16
        }

class beliefelicitationPOSITIVE_first_time(Page):
    def is_displayed(self):
        return (self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal' and self.subsession.draw ==1 and self.group.shock_revealed == 1 and self.group.shock_page == 1
    form_model= models.Player
    form_fields= ['eleffort1', 'eleffort2','eleffort3','eleffort4','eleffort5','eleffort6','eleffort7','eleffort8','eleffort9','eleffort10','eleffort11','eleffort12','eleffort13','eleffort14','eleffort15','eleffort16']

    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_13_1': self.player.in_round(13).eleffort1,#to be displayed in round 14
            'pre_eleffort_13_2': self.player.in_round(13).eleffort2,
            'pre_eleffort_13_3': self.player.in_round(13).eleffort3,
            'pre_eleffort_13_4': self.player.in_round(13).eleffort4,
            'pre_eleffort_13_5': self.player.in_round(13).eleffort5,
            'pre_eleffort_13_6': self.player.in_round(13).eleffort6,
            'pre_eleffort_13_7': self.player.in_round(13).eleffort7,
            'pre_eleffort_13_8': self.player.in_round(13).eleffort8,
            'pre_eleffort_13_9': self.player.in_round(13).eleffort9,
            'pre_eleffort_13_10': self.player.in_round(13).eleffort10,
            'pre_eleffort_13_11': self.player.in_round(13).eleffort11,
            'pre_eleffort_13_12': self.player.in_round(13).eleffort12,
            'pre_eleffort_14_1': self.player.in_round(14).eleffort1,#to be displayed in round 18
            'pre_eleffort_14_2': self.player.in_round(14).eleffort2,
            'pre_eleffort_14_3': self.player.in_round(14).eleffort3,
            'pre_eleffort_14_4': self.player.in_round(14).eleffort4,
            'pre_eleffort_14_5': self.player.in_round(14).eleffort5,
            'pre_eleffort_14_6': self.player.in_round(14).eleffort6,
            'pre_eleffort_14_7': self.player.in_round(14).eleffort7,
            'pre_eleffort_14_8': self.player.in_round(14).eleffort8,
            'pre_eleffort_14_9': self.player.in_round(14).eleffort9,
            'pre_eleffort_14_10': self.player.in_round(14).eleffort10,
            'pre_eleffort_14_11': self.player.in_round(14).eleffort11,
            'pre_eleffort_14_12': self.player.in_round(14).eleffort12,
            'pre_eleffort_14_13': self.player.in_round(14).eleffort13,
            'pre_eleffort_14_14': self.player.in_round(14).eleffort14,
            'pre_eleffort_14_15': self.player.in_round(14).eleffort15,
            'pre_eleffort_14_16': self.player.in_round(14).eleffort16
        }

class beliefelicitationNEGATIVE(Page):
    def is_displayed(self):
        return (self.round_number == 14 or self.round_number == 18) and self.player.type == 'principal' and self.subsession.draw ==0
    form_model= models.Player
    form_fields= ['eleffort1', 'eleffort2','eleffort3','eleffort4','eleffort5','eleffort6','eleffort7','eleffort8']

    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_13_1': self.player.in_round(13).eleffort1,  # to be displayed in round 14
            'pre_eleffort_13_2': self.player.in_round(13).eleffort2,
            'pre_eleffort_13_3': self.player.in_round(13).eleffort3,
            'pre_eleffort_13_4': self.player.in_round(13).eleffort4,
            'pre_eleffort_13_5': self.player.in_round(13).eleffort5,
            'pre_eleffort_13_6': self.player.in_round(13).eleffort6,
            'pre_eleffort_13_7': self.player.in_round(13).eleffort7,
            'pre_eleffort_13_8': self.player.in_round(13).eleffort8,
            'pre_eleffort_13_9': self.player.in_round(13).eleffort9,
            'pre_eleffort_13_10': self.player.in_round(13).eleffort10,
            'pre_eleffort_13_11': self.player.in_round(13).eleffort11,
            'pre_eleffort_13_12': self.player.in_round(13).eleffort12,
            'pre_eleffort_14_1': self.player.in_round(14).eleffort1,  # to be displayed in round 18
            'pre_eleffort_14_2': self.player.in_round(14).eleffort2,
            'pre_eleffort_14_3': self.player.in_round(14).eleffort3,
            'pre_eleffort_14_4': self.player.in_round(14).eleffort4,
            'pre_eleffort_14_5': self.player.in_round(14).eleffort5,
            'pre_eleffort_14_6': self.player.in_round(14).eleffort6,
            'pre_eleffort_14_7': self.player.in_round(14).eleffort7,
            'pre_eleffort_14_8': self.player.in_round(14).eleffort8,

        }

class workerTasks(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent'
    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
        }


class strategyinstructions(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent'

class strategymethod(Page):
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent' and self.group.shock_revealed == 0
    form_model= models.Player
    form_fields= ['steffort1', 'steffort2','steffort3','steffort4','steffort5','steffort6','steffort7','steffort8','steffort9','steffort10','steffort11','steffort12']
    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_8_1': self.player.in_round(8).steffort1,
            'pre_eleffort_8_2': self.player.in_round(8).steffort2,
            'pre_eleffort_8_3': self.player.in_round(8).steffort3,
            'pre_eleffort_8_4': self.player.in_round(8).steffort4,
            'pre_eleffort_8_5': self.player.in_round(8).steffort5,
            'pre_eleffort_8_6': self.player.in_round(8).steffort6,
            'pre_eleffort_8_7': self.player.in_round(8).steffort7,
            'pre_eleffort_8_8': self.player.in_round(8).steffort8,
            'pre_eleffort_8_9': self.player.in_round(8).steffort9,
            'pre_eleffort_8_10': self.player.in_round(8).steffort10,
            'pre_eleffort_8_11': self.player.in_round(8).steffort11,
            'pre_eleffort_8_12': self.player.in_round(8).steffort12

        }

class strategymethodPOSITIVE(Page):
    def is_displayed(self):
        return (self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent' and (self.group.shock_revealed == 1) and self.group.shock_page == 0
    form_model= models.Player
    form_fields= ['steffort1', 'steffort2','steffort3','steffort4','steffort5','steffort6','steffort7','steffort8','steffort9','steffort10','steffort11','steffort12', 'steffort13', 'steffort14','steffort14','steffort15','steffort16']
    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_13_1': self.player.in_round(13).steffort1,
            'pre_eleffort_13_2': self.player.in_round(13).steffort2,
            'pre_eleffort_13_3': self.player.in_round(13).steffort3,
            'pre_eleffort_13_4': self.player.in_round(13).steffort4,
            'pre_eleffort_13_5': self.player.in_round(13).steffort5,
            'pre_eleffort_13_6': self.player.in_round(13).steffort6,
            'pre_eleffort_13_7': self.player.in_round(13).steffort7,
            'pre_eleffort_13_8': self.player.in_round(13).steffort8,
            'pre_eleffort_13_9': self.player.in_round(13).steffort9,
            'pre_eleffort_13_10': self.player.in_round(13).steffort10,
            'pre_eleffort_13_11': self.player.in_round(13).steffort11,
            'pre_eleffort_13_12': self.player.in_round(13).steffort12,
            'pre_eleffort_14_1' : self.player.in_round(14).steffort1,
            'pre_eleffort_14_2' : self.player.in_round(14).steffort2,
            'pre_eleffort_14_3' : self.player.in_round(14).steffort3,
            'pre_eleffort_14_4' : self.player.in_round(14).steffort4,
            'pre_eleffort_14_5' : self.player.in_round(14).steffort5,
            'pre_eleffort_14_6' : self.player.in_round(14).steffort6,
            'pre_eleffort_14_7' : self.player.in_round(14).steffort7,
            'pre_eleffort_14_8' : self.player.in_round(14).steffort8,
            'pre_eleffort_14_9' : self.player.in_round(14).steffort9,
            'pre_eleffort_14_10' : self.player.in_round(14).steffort10,
            'pre_eleffort_14_11' : self.player.in_round(14).steffort11,
            'pre_eleffort_14_12' : self.player.in_round(14).steffort12,
            'pre_eleffort_14_13' : self.player.in_round(14).steffort13,
            'pre_eleffort_14_14' : self.player.in_round(14).steffort14,
            'pre_eleffort_14_15' : self.player.in_round(14).steffort15,
            'pre_eleffort_14_16' : self.player.in_round(14).steffort16
        }

class strategymethodPOSITIVE_first_time(Page):
    def is_displayed(self):
        return (self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent' and self.group.shock_revealed == 1 and self.group.shock_page == 1
    form_model= models.Player
    form_fields= ['steffort1', 'steffort2','steffort3','steffort4','steffort5','steffort6','steffort7','steffort8','steffort9','steffort10','steffort11','steffort12','steffort13','steffort14','steffort15','steffort16']
    def vars_for_template(self):
        return{
            'num_round' : self.subsession.round_number,
            'pre_eleffort_13_1': self.player.in_round(13).steffort1,
            'pre_eleffort_13_2': self.player.in_round(13).steffort2,
            'pre_eleffort_13_3': self.player.in_round(13).steffort3,
            'pre_eleffort_13_4': self.player.in_round(13).steffort4,
            'pre_eleffort_13_5': self.player.in_round(13).steffort5,
            'pre_eleffort_13_6': self.player.in_round(13).steffort6,
            'pre_eleffort_13_7': self.player.in_round(13).steffort7,
            'pre_eleffort_13_8': self.player.in_round(13).steffort8,
            'pre_eleffort_13_9': self.player.in_round(13).steffort9,
            'pre_eleffort_13_10': self.player.in_round(13).steffort10,
            'pre_eleffort_13_11': self.player.in_round(13).steffort11,
            'pre_eleffort_13_12': self.player.in_round(13).steffort12,
            'pre_eleffort_14_1' : self.player.in_round(14).steffort1,
            'pre_eleffort_14_2' : self.player.in_round(14).steffort2,
            'pre_eleffort_14_3' : self.player.in_round(14).steffort3,
            'pre_eleffort_14_4' : self.player.in_round(14).steffort4,
            'pre_eleffort_14_5' : self.player.in_round(14).steffort5,
            'pre_eleffort_14_6' : self.player.in_round(14).steffort6,
            'pre_eleffort_14_7' : self.player.in_round(14).steffort7,
            'pre_eleffort_14_8' : self.player.in_round(14).steffort8,
            'pre_eleffort_14_9' : self.player.in_round(14).steffort9,
            'pre_eleffort_14_10' : self.player.in_round(14).steffort10,
            'pre_eleffort_14_11' : self.player.in_round(14).steffort11,
            'pre_eleffort_14_12' : self.player.in_round(14).steffort12,
            'pre_eleffort_14_13' : self.player.in_round(14).steffort13,
            'pre_eleffort_14_14' : self.player.in_round(14).steffort14,
            'pre_eleffort_14_15' : self.player.in_round(14).steffort15,
            'pre_eleffort_14_16' : self.player.in_round(14).steffort16
        }

class beliefworker(Page):
    form_model = models.Player
    form_fields = ['wagebelief']
    def is_displayed(self):
        return (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.player.type == 'agent'
    def vars_for_template(self):
        return{
            'num_round': self.subsession.round_number,
            'min_wage': self.subsession.min_wage,
            'pre_wagebelief_8': self.player.in_round(8).wagebelief,
            'pre_wagebelief_13': self.player.in_round(13).wagebelief,
            'pre_wagebelief_14': self.player.in_round(14).wagebelief,
            'endowment' : self.group.actuale,
            'shock_revealed': self.group.shock_revealed

        }
    def wagebelief_max(self):
        return self.group.actuale

class Offre_Principal(Page):
    form_model = models.Group
    form_fields = ['wage']

    def vars_for_template(self):
        return {
            'num_round': self.subsession.round_number - 3,
            'min_wage': self.subsession.min_wage,
            'shock_revealed': self.group.shock_revealed
        }

    def is_displayed(self):
        return self.player.type == 'principal'

    def wage_max(self):
        return self.group.actuale

    def wage_min(self):
            return self.subsession.min_wage

class Choix_Agent_Firing(Page):

    def is_displayed(self):
        return self.group.wage == 0 and self.player.type == 'agent'
    def vars_for_template(self):
        return {
            'num_round':self.subsession.round_number-3,
        }

class Choix_Agent(Page):
    form_model = models.Group
    form_fields = ['effort']

    def is_displayed(self):
        return self.player.type == 'agent' and (self.round_number!=8 and self.round_number != 13 and self.round_number!=14 and self.round_number != 18) and self.group.wage >0

    def effort_max(self):
            return 6

    def vars_for_template(self):
        return {
            'offre_wage': self.group.wage,
            'effort_max':round(math.sqrt(2*self.group.wage),2),
            'num_round':self.subsession.round_number-3,
            'shock_page':self.group.shock_page
        }


class WaitPage_check_wage_higher_than_12(WaitPage):
    title_text = "Waiting Page"
    body_text = "Please, wait for the decision of your counterpart"
    def after_all_players_arrive(self):
        self.group.check_shock_revealed()
        pass

class WaitPage_compute(WaitPage):
    title_text = "Waiting Page"
    body_text = "Please, wait for the decision of your counterpart"
    def after_all_players_arrive(self):
        self.group.get_variables()
        self.group.calculate_payoff()
        self.group.check_payoff()

class WaitPage_1(WaitPage):
    def after_all_players_arrive(self):
        pass

class WaitPage_2(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    def after_all_players_arrive(self):
        self.group.calculate_payoff_final_1()
        self.group.calculate_payoff_final_2()
        self.group.rounding()

class Results(Page):
    def vars_for_template(self):
        return {
            'offre_wage': self.group.wage,
            'effort': self.group.effort,
            'payoff': self.player.payoff,
            'payoff_other': self.player.get_others_in_group()[0].payoff,
            'num_round': self.subsession.round_number - 3,
            'role': self.player.type,

        }
    def is_displayed(self):
        return self.round_number!=8 and self.round_number!=13 and self.round_number!=14 and self.round_number!=18

class Waitforinstructions(Page):
    def is_displayed(self):
        return  self.round_number == 1 and self.subsession.online == 0

class pace_maker(Page):
    def is_displayed(self):
        return  (self.round_number == 8 or self.round_number == 13 or self.round_number == 14 or self.round_number == 18) and self.subsession.online == 0


class Welcome(Page):
    def is_displayed(self):
        return  self.round_number == 1
    pass

class instructions_1(Page):
    def is_displayed(self):
        return  self.round_number == 1 and self.subsession.online == 0
    pass

class online_instructions_1(Page):
    def is_displayed(self):
        return  self.round_number == 1 and self.subsession.online == 1
    pass

class instructions_2(Page):
    def is_displayed(self):
        return  self.round_number == 1 and self.subsession.online == 0
    pass

class online_instructions_2(Page):
    def is_displayed(self):
        return  self.round_number == 1 and self.subsession.online == 1
    pass

class ResultsStrategy(Page):
    def vars_for_template(self):
        return {
            'offre_wage': self.group.wage,
            'method': self.group.random_task,
            'accuracy': self.player.belief_in_interval,
            'payoff': self.player.payoff,
            'steffort': self.group.steffort,
            'num_round': self.subsession.round_number-3,
            'payoff_other': self.player.get_others_in_group()[0].payoff,
            'role': self.player.type,
        }
    def is_displayed(self):
        return self.round_number==8 or self.round_number==13 or self.round_number==14 or self.round_number==18

class FinalPayoff(Page):
    def vars_for_template(self):
        return {
            'method': self.group.random_task,
            'accuracy': self.player.belief_in_interval,
            'payoff': self.player.payoff,
            'payoff_decisional': self.player.payoff_decisional,
            'payoff_questionnaire': self.player.payoff_questionnaire,
            'final_payoff': self.player.final_payoff,
            'random_round_payoff_1': self.group.random_round_payoff_1-3,
            'random_round_payoff_2': self.group.random_round_payoff_2-3,
            'role': self.player.type,

        }
    def is_displayed(self):
        return self.round_number==Constants.num_rounds
class finalquestionnaire(Page):
    form_model = models.Player
    form_fields = ['gender', 'undergrad', 'comments', 'asymmetry_check']
    def vars_for_template(self):
        return {
            'role': self.player.type
        }
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    instructions_1, #General Information
    online_instructions_1, #General Information
    Waitforinstructions,
    quiz_1, #quiz
    online_quiz_1, #quiz
    Waitforinstructions,
    instructions_2, #Period Types and final remarks
    online_instructions_2, #Period Types and final remarks
    Waitforinstructions,
    quiz_2,
    online_quiz_2,
    Waitforinstructions,
    WaitPage_1,
    Gamestart_Employer,
    Gamestart_Worker,
    assign_WORKER,
    assign_EMPLOYER,
    Shock,
    workerTasks,
    employerTasks,
    beliefelicitation_instructions,
    beliefelicitation,
    beliefelicitationPOSITIVE,
    beliefelicitationNEGATIVE,
    strategyinstructions,
    beliefworker,
    transition_to_strategy,
    strategymethod,
    strategymethodPOSITIVE,
    Offre_Principal,
    WaitPage_check_wage_higher_than_12,
    Shock_Agent,
    #strategymethodPOSITIVE_first_time,
    #beliefelicitationPOSITIVE_first_time,
    WaitPage_1,
    Choix_Agent,
    WaitPage_compute,
    WaitPage_2,
    Results,
    ResultsStrategy,
    transition_to_normal_rounds,
    pace_maker,
    FinalPayoff,
    finalquestionnaire,
]
