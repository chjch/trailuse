themes_csv = "app/data/actv_consolidated_themes_cc.csv"
response_csv = "app/data/20211209_deidentifiedtreksdata_v2.csv"
activity_csv = "app/data/activitydata_withRID.csv"
demogr_actv_csv = "app/data/demographic_activity.csv"

actv_column = 'activity_standard2'
top_20_activities = ['Hike',
                     'Horseback ride',
                     'Bike',
                     'Run',
                     'Bird view',
                     'Photograph',
                     'Camp',
                     'Mountain bike',
                     'Walk',
                     'Walk pets',
                     'Exercise',
                     'Relax, rest and unwind',
                     'View wildlife',
                     'Backpack',
                     'Fish',
                     'Solitude',
                     'Hunt',
                     'Snowshoe',
                     'Cross country ski',
                     'Socialize']

rid_column = 'ResponseId'
state_column = 'Q24'
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

covid_questions = ['Q56_1', 'Q56_2', 'Q56_3', 'Q56_4',
                   'Q56_5', 'Q56_6', 'Q56_7']

covid_questions_full = ['Places visited',
                        'Frequency of use',
                        'Number people on trails',
                        'Frequency of volunteering',
                        'Number of different activities',
                        'Trash along trails',
                        'Number of social trails']

response_order = ['Much lower',
                  'Slightly lower',
                  'About the same',
                  'Slightly higher',
                  'Much higher']

GENDER = 'GENDER'
EDUCATION = 'EDUCATION'
AGE = 'AGE'

edu_order = ['High school graduate',
             'Professional degree',
             'Some college',
             '2 year degree',
             '4 year degree',
             'Some graduate school',
             "Master's Degree",
             'Doctorate']

html_text_intro = '''Trails offer a particularly nuanced insight into 
human-nature interaction. While trail spaces attract visitors of all 
demographic groups, there is considerable variation in how each group engages 
with these spaces. This dashboard conveys our research on trails relevant to 
future applications in digital landscape architecture extending beyond the 
scope of trail usage.'''

html_text_covid = '''See the impact of COVID-19 on the respondents’ trail 
experience. Hover over each bar to view its number of responses. Use the 
drop-down menu to view each category.'''

html_text_sunburst = '''The frequency of each trail activity is represented by 
a percentage and a number of responses. Hover over each category to view its 
number of responses. The outer two rings reflect the specific categories of 
activities. The innermost circle displays the overarching groups of 
human-centered activities and nature-centered activities.'''

html_text_chord = '''See the distribution of activities varied by 
respondents’s age and education level. Use the slider to the left of the 
diagram to filter the number of activities by popularity.'''

html_text_map = '''The frequency of trail activities for each U.S. state is 
represented by numeric values and graduated color symbology. Hover over each 
state to view its number of responses. Use the drop-down menu to view a map 
for each activity.'''
