from dataclasses import dataclass, fields
import numpy as np

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
    name: str
    gender: int
    age: int
    education: str
    employed: bool
    partnership_status: str
    pre_existing_depression: bool
    pre_existing_burnout: bool
    pre_existing_addiction: bool 
    pre_existing_chronic_fatigue: bool
    parenthood: bool
    living_with_child: bool
    single_parent: bool
    housing_difficulties: bool
    finance_difficulties: bool
    pre_existing_health_issues: bool
    partner_difficulties: bool
    
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
        ratio of male over female

    Returns
    -------
    gender_distribution : numpy array
        Array of 1s and 0s (1 = female, 0 = male) 
    '''
    gender_distribution = np.ones(n_people)
    gender_distribution[:int((n_people * percentage) / 100)] = 0
    np.random.shuffle(gender_distribution)       
    return gender_distribution.astype(int)

def generate_age_distribution(n_people, n_age_groups, start, stop, percentage):
    ''' Generates age distribution
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
    percentage : list    
        Proportion of age prevalence for each age group. Number of elements in the list must match value in `n_age_groups`
        
    Returns
    -------
    age_distribution : numpy array
    '''

    age_values = np.arange(start, stop)  
    age_groups = np.array_split(age_values, n_age_groups)

    age_distribution = []
    for x in range(n_people):
        idx = np.random.choice(range(len(age_groups)), p=percentage)
        age_distribution.append(np.random.choice(age_groups[idx]))
    return age_distribution