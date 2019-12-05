from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools, random, numpy



author = ''

doc = """
Modified Gift Exchange Game
"""



class Constants(BaseConstants):

    name_in_url = 'Andy_is_the_best'
    players_per_group = 2
    num_rounds = 20
    Endowment = 10
    instructions_template = 'Andy/Summary.html'
    Endowmenthigh= 12
    Endowmentlow=8

class Subsession(BaseSubsession):

    def creating_session(self):
        for g in self.get_groups():
            g.draw = numpy.random.random_integers(low=0,high=1)
            g.draw2 = numpy.random.random_integers(low=0, high=1)
            for p in g.get_players():
                p.type = ['principal', 'agent'][p.id_in_group - 1]
        # Old
        # Old Type = itertools.cycle(['principal', 'agent'])
        # Old players = self.get_players()
        # Old for p in players:
        # Old     p.type = next(Type)
        # Old Entreprise_players = [p for p in players if p.type == 'principal']
        # Old random.shuffle(Entreprise_players)
        # Old Employe_players = [p for p in players if p.type == 'agent']
        # Old random.shuffle(Employe_players)
        # Old group_matrix = []
        # Old while Entreprise_players:
        # Old     new_group = [
        # Old         Entreprise_players.pop(),
        # Old         Employe_players.pop()
        # Old     ]
        # Old     group_matrix.append(new_group)
        # Old self.set_group_matrix(group_matrix)
        # Old for g in self.get_groups():
        # Old     g.draw = numpy.random.random_integers(low=0,high=1)
        # Old     g.draw2 = numpy.random.random_integers(low=0, high=1)


class Group(BaseGroup):
    actuale = models.IntegerField(initial=Constants.Endowment, min=1, max=100)
    wage = models.IntegerField(min=1)
    effort = models.FloatField(min=0, max=4, widget= widgets.SliderInput(attrs={'step': '0.1'}))
    steffort= models.FloatField(min=0, max=4)
    draw = models.IntegerField(initial=numpy.random.random_integers(low=0,high=1))


    def get_variables(self):
        players = self.get_players()
        for p in players:
            if p.type == 'agent':
                if self.round_number==1 or self.round_number==5 or self.round_number==10 or self.round_number==11 or self.round_number==15:
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
                    else :
                        self.steffort= p.steffort1




    def calculate_payoff(self):
        players= self.get_players()
        if self.round_number >= 10 and self.in_round(10).draw == 1:
            high=1
        else:
            high=0
        for p in players:
            if p.type== 'agent':
                if self.round_number==1 or self.round_number==5 or self.round_number==10 or self.round_number==11 or self.round_number==15:
                    p.payoff = self.wage - ((self.steffort) ** 2) / 2
                else:
                    p.payoff = self.wage - ((self.effort) ** 2) / 2

            else:
                 #if self.round_number==10:
                 #    if self.draw==1:
                 #        p.payoff = (Constants.Endowmenthigh - self.wage) * self.steffort
                 #        self.in_round(self.subsession.round_number + 9).actuale = 12
                 #    else:
                 #        p.payoff = (Constants.Endowmentlow - self.wage) * self.steffort
                 #        self.in_round(self.subsession.round_number + 9).actuale = 8
                if self.round_number <= 10:
                    #if self.round_number != 1 and self.round_number !=5 and self.round_number != 10 and self.round_number != 11 and self.round_number != 15:
                    #    p.payoff = (Constants.Endowment - self.wage)*self.effort
                    if self.round_number == 1 or self.round_number ==5:
                        p.payoff = (Constants.Endowment - self.wage) * self.steffort
                        print("This is ACTUALEEEEEEE", self.actuale)
                    elif self.round_number == 10:
                        p.payoff = (Constants.Endowment - self.wage) * self.steffort
                        print("This is ACTUALEEEEEEE1", self.actuale)
                        if high==1:
                            for g in self.in_rounds(self.round_number+1, Constants.num_rounds):
                                g.actuale = Constants.Endowmenthigh
                        else:
                            for g in self.in_rounds(self.round_number+1, Constants.num_rounds):
                                g.actuale = Constants.Endowmentlow
                    else:
                        p.payoff = (Constants.Endowment - self.wage) * self.effort
                else:

                    if (self.round_number == 11 or self.round_number == 15) and high==1:
                        p.payoff = (self.actuale - self.wage) * self.steffort
                    elif (self.round_number == 11 or self.round_number == 15) and high==0 :
                        p.payoff = (self.actuale - self.wage) * self.steffort
                    elif (self.round_number != 11 and self.round_number != 15) and high == 1:
                        p.payoff = (self.actuale - self.wage) * self.effort
                    else :
                        p.payoff = (self.actuale - self.wage) * self.effort

    def check_payoff(self):
        players= self.get_players()
        for p in players:
            if p.payoff < 0:
                p.payoff=0


class Player(BasePlayer):
    type = models.CharField()

    #FIRM: elicited effort
    eleffort1 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort2 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort3 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort4 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort5 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort6 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort7 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort8 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort9 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort10 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort11 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")
    eleffort12 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}),verbose_name="")

    #WORKER: strategy method effort
    steffort1 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort2 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort3 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort4 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort5 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort6 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort7 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort8 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort9 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort10 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort11 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")
    steffort12 = models.FloatField(min=0, max=4, widget=widgets.SliderInput(attrs={'step': '0.1'}), verbose_name="")

    #WORKER: elicited wage
    wagebelief = models.IntegerField(min=1, verbose_name='')