from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools, random
import numpy as np



author = 'Andrea Guido and Anthropolab IT Team - Lille (Antoine Demyer and Flovic Gosselin)'

doc = """
Labour Market Game
"""



class Constants(BaseConstants):

    name_in_url = 'Beliefs_game_asymmetric_info'
    players_per_group = 2
    num_rounds = 23               #3 trials + 20 of the real game
    Endowment = 12
    instructions_template = 'Andy_asymmetric_info/Summary.html'
    Endowmenthigh= 16             #endowment after positive shock
    Endowmentlow=8                #endowment after negative shock
    round_specials = [8,13,14,18] #these are the rounds with belief elicitation
    bonus_if_in_internal = 5      #this is the belief payment

class Subsession(BaseSubsession):

    draw = models.IntegerField() #1 for positive shock 0 for negative shock                                        #random draw to decide whether + or - shock
    min_wage = models.IntegerField()  # 0 for firing treatment, 1 for baseline
    matching = models.CharField()
    def creating_session(self):
        self.draw = self.session.config['treatment']
        self.matching = self.session.config['matching']
        self.min_wage = self.session.config['minimum_wage']
        print("********This is DRAW********", self.draw)
        if self.matching == 'P':
            for g in self.get_groups():
                #            g.draw = np.random.random_integers(low=0,high=1)
                #            g.draw2 = np.random.random_integers(low=0, high=1)
                for p in g.get_players():
                    p.type = ['principal', 'agent'][p.id_in_group - 1]
            if self.round_number == 1:
                self.group_randomly(fixed_id_in_group=True)
                print("this is the group matrix for round 1", self.get_group_matrix())
            elif self.round_number < 4:
                self.group_like_round(1)
            elif self.round_number == 4:
                self.group_randomly(fixed_id_in_group=True)
                self.group_like_round(4)
            else:
                self.group_like_round(4)
                print("this is the group matrix for round 4", self.get_group_matrix())
        elif self.matching == 'S':
            for g in self.get_groups():
                for p in g.get_players():
                    p.type = ['principal', 'agent'][p.id_in_group - 1]
            self.group_randomly(fixed_id_in_group=True)
            print("this is the group matrix for every round", self.get_group_matrix())


class Group(BaseGroup):
    actuale = models.IntegerField(initial=Constants.Endowment, min=1, max=100)                                          #endowment
    wage = models.IntegerField(min=0)                                                                                   #the wage snet by the firm
    effort = models.FloatField(min=0, max=6, widget= widgets.SliderInput(attrs={'step': '0.25'}))                        #the effort of worker in normal rounds
    steffort= models.FloatField(min=0, max=6)                                                                           #effort from strategy method

    random_round_payoff_1 = models.IntegerField()                                                                       #rnd draw to choose decisional period to be paid
    random_round_payoff_2 = models.IntegerField()                                                                       # " " questionnaire period to be paid
    random_task = models.IntegerField()                                                                      # task paid
    random_line_belief = models.IntegerField()                                                                 #line of belief table chosen to payment if accurate

    def get_variables(self): #function to get effort stated in the strategy method
        players = self.get_players()
        for p in players:
            if p.type == 'agent':
                if self.round_number==8 or self.round_number==13 or self.round_number==14 or self.round_number==18:
                    if self.wage == 10:
                        self.steffort = p.steffort10
                    elif self.wage == 2:
                        self.steffort= p.steffort2
                    elif self.wage == 3:
                        self.steffort= p.steffort3
                    elif self.wage == 4:
                        self.steffort= p.steffort4
                    elif self.wage == 5:
                        self.steffort= p.steffort5
                    elif self.wage == 6:
                        self.steffort= p.steffort6
                    elif self.wage == 7:
                        self.steffort= p.steffort7
                    elif self.wage == 8:
                        self.steffort= p.steffort8
                    elif self.wage == 9:
                        self.steffort= p.steffort9
                    elif self.wage == 11:
                        self.steffort= p.steffort11
                    elif self.wage == 12:
                        self.steffort= p.steffort12
                    elif self.wage == 13:
                        self.steffort= p.steffort13
                    elif self.wage == 14:
                        self.steffort= p.steffort14
                    elif self.wage == 15:
                        self.steffort= p.steffort15
                    elif self.wage == 16:
                        self.steffort= p.steffort16
                    else:
                        self.steffort= p.steffort1



    def calculate_payoff_final_1(self): #compute payoffs in decisional round
        print("***************COMPUTING PAYOFF 1*************")
        # choose randomly a round
        Liste_round_decisional = random.sample([x for x in list(range(4,Constants.num_rounds+1)) if x not in Constants.round_specials],1)
        self.random_round_payoff_1 = Liste_round_decisional[0]                     #decisional paid round
        self.random_round_payoff_2 = random.sample(Constants.round_specials,1)[0]  #questionnaire paid round
        print("so round Decisional is ", self.random_round_payoff_1)
        print("so round Questionnaire is ", self.random_round_payoff_2)

        print("Direct response method is going on")
        # direct-repsponse method
        for p in self.get_players():
            print("the type of the player", p.type)

            if p.type == "agent":
                p.final_payoff = float(p.in_round(self.random_round_payoff_1).payoff)
                p.payoff_decisional = p.final_payoff
                print("This is the payoff of decisional ", p.payoff_decisional)
            else:
                p.final_payoff = float(p.in_round(self.random_round_payoff_1).payoff)
                p.payoff_decisional = p.final_payoff
                print("This is the payoff of decisional ", p.payoff_decisional)

    def calculate_payoff_final_2(self):  # compute payoffs for questionnaire rounds
            print("***************** I'm in the method calculate payoff final 2 *****************")
            self.random_task = np.random.choice(
                [0, 1], 1,
                p=[0.5, 0.5])[0]
            print("This is the method chosen (BELIEF (1) vs STRATEGY (0) ):", self.random_task)

            if self.random_task == 1:
                # Belief elicitation method
                for p in self.get_players():

                    if p.type == "agent":

                        print("the type is the agent", p.type)
                        print("this is the wage chosen for the strategy method",
                              self.in_round(self.random_round_payoff_2).wage)
                        print("this is the wagebelief " ,
                              p.in_round(self.random_round_payoff_2).wagebelief)

                        # belief accuracy
                        if p.in_round(self.random_round_payoff_2).wagebelief == self.in_round(
                                self.random_round_payoff_2).wage:
                            print("WORKER's beliefs is In the interval")
                            p.belief_in_interval = 1
                            # PAYOFF ASSIGNINIG
                            p.payoff_questionnaire = Constants.bonus_if_in_internal
                            p.final_payoff += Constants.bonus_if_in_internal
                            print("This is the payoff of questionnaire ", p.payoff_questionnaire)
                        else:
                            print("WORKER' belief is Out of interval")
                            p.payoff_questionnaire = 0
                            p.belief_in_interval = 0
                            print("This is the payoff of questionnaire ", p.payoff_questionnaire)

                    else:

                        print("the type is principal", p.type)

                        # draw a random line of the table
                        self.random_line_belief = random.randint(1,
                                                                          self.in_round(
                                                                              self.random_round_payoff_2).actuale)
                        agent = p.get_others_in_group()[0]

                        print("this is the random line chosen from the table in round 2 ",
                              self.random_line_belief)

                        # extract beliefs from the table
                        belief_effort = getattr(p.in_round(self.random_round_payoff_2),
                                                'eleffort{}'.format(self.random_line_belief))
                        print("this is belief effort", belief_effort)
                        #extract strategy effort
                        strategy_effort = getattr(agent.in_round(self.random_round_payoff_2),
                                                  'steffort{}'.format(self.random_line_belief))
                        print("this is strategy effort", strategy_effort)

                        # make the interval
                        upper_bound_belief_effort = strategy_effort + 0.25
                        lower_bound_belief_effort = strategy_effort - 0.25

                        # check if in interval
                        if lower_bound_belief_effort <= belief_effort <= upper_bound_belief_effort:
                            p.belief_in_interval = 1
                            p.payoff_questionnaire = Constants.bonus_if_in_internal
                            print("This is the payoff of questionnaire ", p.payoff_questionnaire)
                            p.final_payoff += Constants.bonus_if_in_internal
                            print("Employer's beliefs are in the interval")
                        else:
                            p.belief_in_interval = 0
                            p.payoff_questionnaire = 0
                            print("This is the payoff of questionnaire ", p.payoff_questionnaire)
                            p.final_payoff += 0
                            print("Employer's beliefs are NOT in the interval")
            else:
                # strategy effort
                print("This is the strategy method")

                # compute payoffs
                for p in self.get_players():
                    if p.type == "agent":
                        p.payoff_questionnaire = float(p.in_round(self.random_round_payoff_2).payoff)
                        print("This is the payoff of questionnaire ", p.payoff_questionnaire)
                        print("I'm here calculating WORKER PAYOFF")
                        p.final_payoff += float(p.in_round(self.random_round_payoff_2).payoff)
                        print("OKAY COMPUTED", p.final_payoff)

                    else:
                        print("I M here computing EMPLOYER's PAYOFF")
                        p.payoff_questionnaire = float(p.in_round(self.random_round_payoff_2).payoff)
                        print("This is the payoff of questionnaire ", p.payoff_questionnaire)
                        p.final_payoff += float(p.in_round(self.random_round_payoff_2).payoff)
                        print("OKAY COMPUTED", p.final_payoff)


    def calculate_payoff(self): #payoffs as the game unravels - not paid
        players= self.get_players()

        # this is to define the post shock endowment
        if self.round_number >= 13 and self.subsession.draw == 1:
            high=1
        else:
            high=0

        # this is to define thz agent's payoff both in normal and elicitation rounds
        for p in players:
            if p.type== 'agent':
                if self.round_number==8 or self.round_number==13 or self.round_number == 14 or self.round_number==18:
                    if self.wage > 0:
                        p.payoff = self.wage - ((self.steffort) ** 2) / 2
                    else:
                        p.payoff = 0
                else:
                    if self.wage > 0:
                        p.payoff = self.wage - ((self.effort) ** 2) / 2
                    else:
                        p.payoff = 0
            else:

                # this is to define the principal's payoff

                if self.round_number <= 13:
                    #if self.round_number != 1 and self.round_number !=5 and self.round_number != 10 and self.round_number != 11 and self.round_number != 15:
                    #    p.payoff = (Constants.Endowment - self.wage)*self.effort
                    if self.round_number == 8 :
                        if self.wage >0:
                            p.payoff = (Constants.Endowment - self.wage) * self.steffort
                            print("This is ACTUALE and the round is 1 or 5", self.actuale)
                        else:
                            p.payoff = Constants.Endowment/2
                    elif self.round_number == 13:
                        if self.wage >0:
                            p.payoff = (Constants.Endowment - self.wage) * self.steffort
                            print("This is ACTUALE and the round is 10", self.actuale)
                        else:
                            p.payoff = Constants.Endowment/2

                        # propagate the shock
                        if high==1:
                            for g in self.in_rounds(self.round_number+1, Constants.num_rounds):
                                g.actuale = Constants.Endowmenthigh
                        else:
                            for g in self.in_rounds(self.round_number+1, Constants.num_rounds):
                                g.actuale = Constants.Endowmentlow
                    else:
                        if self.wage >0:
                            p.payoff = (Constants.Endowment - self.wage) * self.effort
                        else:
                            p.payoff = Constants.Endowment/2
                else:

                    if (self.round_number == 14 or self.round_number == 18) and self.wage >0 :
                        p.payoff = (self.actuale - self.wage) * self.steffort
                    elif (self.round_number == 14 or self.round_number == 18) and self.wage ==0:
                        p.payoff = self.actuale/2
                    else :
                        if self.wage >0:
                            p.payoff = (self.actuale - self.wage) * self.effort
                        else:
                            p.payoff = self.actuale/2

    def rounding(self):
        players= self.get_players()
        for p in players:
            p.final_payoff=round(p.final_payoff,2)

    def check_payoff(self):
        players= self.get_players()
        for p in players:
            if p.payoff < 0:
                p.payoff=0


class Player(BasePlayer):
    type = models.CharField()
    belief_in_interval = models.IntegerField()

    #FIRM: elicited effort
    eleffort1 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort2 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort3 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort4 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort5 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort6 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort7 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort8 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort9 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort10 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort11 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort12 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort13 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort14 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort15 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")
    eleffort16 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}),verbose_name="")

    #WORKER: strategy method effort
    steffort1 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort2 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort3 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort4 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort5 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort6 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort7 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort8 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort9 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort10 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort11 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort12 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort13 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort14 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort15 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")
    steffort16 = models.FloatField(min=0, max=6, widget=widgets.SliderInput(attrs={'step': '0.25'}), verbose_name="")

    #WORKER: elicited wage
    wagebelief = models.IntegerField(min=1, verbose_name='')
    #payoff from questionnaire period chosen randomly
    payoff_questionnaire = models.FloatField(initial=0)
    #payoff from decisional period chosen randomly
    payoff_decisional = models.FloatField(initial=0)
    #Payment at the end of the experiment
    final_payoff = models.FloatField(initial=0)
    #gender
    gender = models.IntegerField(choices=[[1,'Male'], [2,'Female'], [3,'Other']], verbose_name='')
    #education
    undergrad = models.IntegerField(choices=[[1,'Yes'], [0,'No']],verbose_name='')
    #treatment check
    asymmetry_check = models.IntegerField(choices=[[1, 'ONLY EMPLOYERS in this experiment'], [0, 'BOTH EMPLOYERS and WORKERS in this experiment']],
                                          verbose_name="The change in employers' endowment (from $12 to $8) was announced to",
                                          blank=True)
    #comments
    comments = models.TextField(
        blank=True,
        max_length=3000,
        verbose_name = 'Please, write here any comment concerning the experiment (for example: game length, instructions, game). We would love to hear your opinion about it.'

    )