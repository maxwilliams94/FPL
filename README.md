# Data Breakdown
JSON data returned from http get request to https://fantasy.premierleague.com/api/bootstrap-static/

Following ```response.data().json()``` json data can be stored within variable ```data```

The returned JSON file contains overall statistics (most transfers etc) which links to the dictionary object 'elements' which references player 'id's which can be accessed via ```data['elements'][id]```

## data.keys()

#### events
list (len=38) of dict (one for each game week)

##### events[:].keys()
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
- name
- short_name
- id
- code
- wim
- loss
- draw
- played
- form
- points[]
- position
- strength
- team_division
- unavailable (True/False)
- strength_overall_home
- strength_overall_away
- strength_attack_home
- strength_attack_away

#### total_players
int
#### elements
- list of dictionaries for each player
- chance_of_playing_next_round
- chance_of_playing_this_round
- code
- cost_change_event
- cost_change_event_fall
- cost_change_start
- cost_change_start_fall
- dreamteam_count
- element_type
- ep_next
- ep_this
- event_points
- first_name
- form
- id
- in_dreamteam
- news
- news_added
- now_cost
- photo
- points_per_game
- second_name
- selected_by_percent
- special
- squad_number
- status
- team
- team_code
- total_points
- transfers_in
- transfers_in_event
- transfers_out
- transfers_out_event
- value_form
- value_season
- web_name
- minutes
- goals_scored
- assists
- clean_sheets
- goals_conceded
- own_goals
- penalties_saved
- penalties_missed
- yellow_cards
- red_cards
- saves
- bonus
- bps
- influence
- creativity

#### element_stats
Looks to store elements to be displayed for player stats rather than storing any actual data. This is likely used by their api to acces their elements statitics data, using the label on the website and the name to access the relevant JSON data point.

#### element_types
list (len 4) of the 4 different player positions and position dependant game rules (max allowed, max pick etc)