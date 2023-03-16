from dataclasses import dataclass, fields
import numpy as np
import random

@dataclass
class Features():
    ''' Features of the agents '''
    __slots__ = ['name', 'gender', 'age', 'education', 'employed',
                 'partnership_status', 'pre_existing_depression',
                 'pre_existing_burnout', 'pre_existing_addiction',
                 'pre_existing_chronic_fatigue', 'parenthood',
                 'living_with_child', 'single_parent', 'housing_difficulties',
                 'finance_difficulties', 'pre_existing_health_issues',
                 'partner_difficulties']
    name: int
    gender: int
    age: int
    education: str
    employed: str
    partnership_status: str
    pre_existing_depression: int
    pre_existing_burnout: int
    pre_existing_addiction: int 
    pre_existing_chronic_fatigue: int
    parenthood: int
    living_with_child: int
    single_parent: int
    housing_difficulties: int
    finance_difficulties: int
    pre_existing_health_issues: int
    partner_difficulties: int
    
    def summary(self):
        ''' Generate a summary of the features '''
        for field in fields(self):
            print(f'{field.name}: {getattr(self, field.name)}')
        
@dataclass
class Agent():
    ''' Represents an agent in our small world '''
    features: Features
    n_contacts: int = 0
    
    def summary(self):
       ''' Generate a summary of the features '''
       self.features.summary()
       print(f'n_contacts: {self.n_contacts}')
       
def generate_gender_distribution(n_people, percentage):
    ''' Generates gender distribution
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of male over female (e.g., 50 for 50%)

    Returns
    -------
    gender_distribution : numpy array
        Array of 1s and 0s (1 = female, 0 = male) whose proportions depend on `percentage`.
    '''
    gender_distribution = np.ones(n_people)
    gender_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(gender_distribution)       
    return gender_distribution.astype(int)

def generate_age_distribution(n_people, n_age_groups, start, stop, prob):
    ''' Generates age groups distribution in the population
    Parameters
    ----------
    n_people : int
        Size of the population.
    start : int
        Minimum age.
    stop : int
        Maximum age.
    n_age_groups : int
        Number of age groups.
    prob : list    
        Proportion of age prevalence for each age group (e.g., .25). Number of elements must match value in `n_age_groups`.
        
    Returns
    -------
    age_distribution : numpy array
        Array of age distribution in the population. Proportions depend on `prob`.
    '''

    age_values = np.arange(start, stop)  
    age_groups = np.array_split(age_values, n_age_groups)

    age_distribution = []
    for x in range(n_people):
        idx = np.random.choice(range(len(age_groups)), p=prob)
        age_distribution.append(np.random.choice(age_groups[idx]))
    return age_distribution


def generate_educational_attainment_distribution(n_people, low, medium, high):
    ''' Generate distribution of high, medium and low educational attainments in the population.
    Parameters
    ----------
    n_people : int
        Size of the population.
    low : float
        Probability of low educational attainment prevalence in the population. 
    medium : float
        Probability of medium educational attainment prevalence in the population. 
    high : float
        Probability of high educational attainment prevalence in the population. 
        
    Returns
    ----------
    educational_attainment : list
        List of type of educational attainments in the population.
    '''
    options = {'Low' : low, 
               'Medium' : medium,
               'High' : high}
    
    choices = list(options.keys())
    weights = list(options.values())
    educational_attainment = random.choices(choices, weights, k = n_people) 
    return(educational_attainment)

def generate_employment_distribution(n_people, yes, no_seeking, no_other):
    ''' Generate distribution of employment statuses in the population.
    Parameters
    ----------
    n_people : int
        Size of the population.
    yes : float
        Probability of being employed. 
    no_seeking : float
        Probability of not being employed, but looking for a job. 
    no_other : float
        Probability of not being employed, but not looking for a job. 
        
    Returns
    ----------
    employment : list
        List of employment status in the population.
    '''
    options = {'Yes' : yes, 
               'No, seeking employment' : no_seeking,
               'No, other' : no_other}
    
    choices = list(options.keys())
    weights = list(options.values())
    employment = random.choices(choices, weights, k = n_people) 
    return(employment)

def generate_partnership_statuts_distribution(n_people, single, married, live_in_partner, in_relationship_no_cohabitation, other):
    ''' Generate distribution of partnership statuses in the population.
    Parameters
    ----------
    n_people : int
        Size of the population.
    single : float
        Probability of being single. 
    married : float
        Probability of not married. 
    live_in_partner : float
        Probability of being in a relationship and living together. 
    in_relationship_no_cohabitation : float
        Probability of being in a relationship but not living together.
    other : float
        Probability of being in a partnership status that is none of the above.
        
    Returns
    ----------
    relationship : list
        List of relationship status distribution in the population.
    '''
    options = {'Single' : single, 
               'Married' : married,
               'Live-in partner' : live_in_partner,
               'In relationship, no cohabitation' : in_relationship_no_cohabitation,
               'Other' : other}
    
    choices = list(options.keys())
    weights = list(options.values())
    relationship = random.choices(choices, weights, k = n_people) 
    return(relationship)

def generate_pre_existing_depression_distribution(n_people, percentage):
    ''' Generates proportion of people that experienced depression in the past year 
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    depression_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    depression_distribution = np.ones(n_people)
    depression_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(depression_distribution)       
    return depression_distribution.astype(int)


def generate_pre_existing_burnout_distribution(n_people, percentage):
    ''' Generates proportion of people that experienced burnout in the past year 
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    burnout_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    burnout_distribution = np.ones(n_people)
    burnout_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(burnout_distribution)       
    return burnout_distribution.astype(int)

def generate_pre_existing_addiction_distribution(n_people, percentage):
    ''' Generates proportion of people that experienced addiction in the past year 
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    addiction_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    addiction_distribution = np.ones(n_people)
    addiction_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(addiction_distribution)       
    return addiction_distribution.astype(int)

def generate_pre_existing_fatigue_distribution(n_people, percentage):
    ''' Generates proportion of people that experienced chronic fatigue in the past year 
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    fatigue_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    fatigue_distribution = np.ones(n_people)
    fatigue_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(fatigue_distribution)       
    return fatigue_distribution.astype(int)

def generate_child_distribution(n_people, percentage):
    ''' Generates proportion of people that had a child since 2013
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    child_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    child_distribution = np.ones(n_people)
    child_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(child_distribution)       
    return child_distribution.astype(int)

def generate_living_with_children_distribution(n_people, percentage):
    ''' Generates proportion of people that currently lives with children
    Parameters
    ----------
    n_people : int
        size of the population.
    percentage : int
        ratio of yes (1) over no (0) (e.g., 50 for 50%)

    Returns
    -------
    children_distribution : numpy array
        Array of 1s and 0s (1 = yes, 0 = no) whose proportions depend on `percentage`.
    '''
    children_distribution = np.ones(n_people)
    children_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(children_distribution)       
    return children_distribution.astype(int)