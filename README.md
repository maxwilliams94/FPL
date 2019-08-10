# Data Breakdown
JSON data returned from http get request to https://fantasy.premierleague.com/api/bootstrap-static/

Following ```response.data().json()``` json data can be stored within variable ```data```

## data
Dictionary

### data.keys()

#### events
list (len=38) of dict (one for each game week)

#### events[:].keys()
- id: game_week number (1-38)
- name 'Game Week {}'
- deadline_time
- average_entry_score
- finished True/False
- data_checked True/False
- highest_scoring_entry None (until computed I assume)
- deadline_time_epoch 1565373600
- deadline_time_game_offset
- highest_score None (until end of game_week)
- is_previous True/False
- is_current True/False
- is_next True/False
- chip_plays dictionary: bboost, 3xc
- most_selected player id
- most_transferred_in player id
- top_element
- transfers_made
- most_captained
- most_vice_captained

#### game_settings
League settings for size, points, head to head win conditions etc
#### phases
type list of dictionaries for each month
Information on what game weeks fall within each month
#### teams
list of dictionaries for the 20 teams
name
short_name
id
code
wim
loss
draw
played
form
points
position
strength
team_division
unavailable (True/False)
strength_overall_home
strength_overall_away
strength_attack_home
strength_attack_away

#### total_players

#### elements

#### element_stats

#### element_types