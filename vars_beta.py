#!/usr/bin/python
# -*- coding: utf-8 -*-
#This page does not get saved with the save function.
#! = Change and/or add var in save function.
#Materials
wood=10 #logs
water=10 #oz
dirt=10 #lbs
rocks=10 #Qty
#Things you can make
clay=10 #lbs
bowl=10 #Qty
sticks=10 #Qty
#Goodies
coal=1
iron=1
gold=1
diamond=1
copper=1
lapiz=1
zinc=1
cobalt=1
lead=1
mica=1
manganese=1
#Resources that are collected by quests.
aluminum=0
silicon=0
bronze=0
silver=0
#Home storage vars
storage_wood=5
storage_water=5
storage_dirt=5
storage_rocks=5
storage_clay=5
storage_bowl=5
storage_sticks=5
storage_pickaxe=5
storage_shovel=5
storage_axe=5
storage_coal=2
storage_iron=2
storage_gold=2
storage_diamond=2
storage_copper=2
storage_lapiz=2
storage_zinc=2
storage_cobalt=2
storage_mica=2
storage_manganese=2
#Storage
self_storage=300 #Qty of items
home_storage=500 #Qty of items
#Tools
pickaxe=5 #Qty, Can be used 1 time
shovel=2 #Qty, Can be used 1 time
axe=3 #Qty, Can be used 1 time
#Cords
lake1_cords=[27,0,69]
lake2_cords=[27,0,103]
lake3_cords=[27,0,409]
river1_cords=[10,0,32]
river2_cords=[10,0,210]
river3_cords=[10,0,122]
clay_mountian1_cords=[103,100,495]
clay_mountian2_cords=[103,120,123]
clay_mountian3_cords=[103,80,249]
desert1_cords=[521,10,52]
desert2_cords=[521,10,420]
desert3_cords=[521,10,231]
city1_cords=[245,0,245]
city2_cords=[245,0,12]
city3_cords=[245,0,478]
forest1_cords=[34,5,23]
forest2_cords=[34,5,78]
forest3_cords=[34,5,103]
exercise_mountian1_cords=[378,207,300]
#Locations
home_location=[0,0,0]
current_location=[0,0,0]
current_surrounding='home'
#Biomes
water_biomes=['lake #1','lake #2','lake #3','river #1','river #2','river #3']
clay_biomes=['clay mountian #1','clay mountian #2','clay mountian #3']
sand_biomes=['desert #1','desert #2','desert #3','abandoned city','city #1','city #2','city #3']
dirt_biomes=['forest #1','forest #2','forest #3']
#Others
sides=False
money=125 #Default 125
stanima=100#Starting Max 100, Default 100
max_stanima=100#Default 100
exit_pos=['bye','goodbye','exit','leave','moving on','adios','adiÃ³s']
donated_money=0
donated_tf=[0,0,0,0,0,0,0,0,0,0,0] #0=False, 1=True. Items are in order on donate/rewards
go_home=['help','leave','break']
repeat_amount=25
chars_in_line=55
#Quests
quest_count=12
quest1=False
quest2=False
quest3=False
quest4=False
quest5=False
quest6=False
quest7=False
quest8=False
quest9=False
quest10=False
quest11=False
quest12=False
#Uses on cheat codes
cheat_wood_int=0
cheat_dirt_int=0
cheat_water_int=0
cheat_rocks_int=0
cheat_all_int=0
#Cheats unlocked
cheat_wood=False
cheat_dirt=False
cheat_water=False
cheat_rocks=False
cheat_all=False
#Settings
error_message=True
version=True
gather_loop=True
hints_loop=True
hints=True
create_new_save=False
quick_leave=True
hit_to_exit=False
normal_clear=False
run_off=True

#First cord = Area, Second cord = Height, Third cord = distance
#Though all cords = distance
#Lake = 27,0,?
#River = 10,0,?
#Clay mountian = 103,?,?
#Exercise mountian = 378,207,?
#Desert = 521,10,?
#Abandoned city = 245,0,?
#Forest = 34,5,?

#Sell prices
price_wood=2
price_dirt=1
price_water=1
price_rocks=1
price_clay=3
price_bowl=5
price_sticks=1
price_pickaxe=7
price_shovel=4
price_axe=5
price_coal=1
price_iron=3
price_gold=5
price_diamond=7
price_copper=2
price_lapiz=3
price_zinc=3
price_cobalt=4
price_mica=4
price_manganese=5

#Buy prices
buy_price_wood=3
buy_price_dirt=2
buy_price_water=2
buy_price_rocks=2
buy_price_clay=4
buy_price_bowl=7
buy_price_sticks=2
buy_price_pickaxe=9 
buy_price_shovel=5
buy_price_axe=7
buy_price_coal=2
buy_price_iron=4
buy_price_gold=6
buy_price_diamond=8
buy_price_copper=5
buy_price_lapiz=6
buy_price_zinc=5
buy_price_cobalt=6
buy_price_mica=6
buy_price_manganese=7
# --- CODES IN GAME ---
dev_options="W3rS3cur3" #In the main menu enter this code to activate.
cheat_code=""
cheat_amount=10#The amount to add when using cheat code. #MAX IS 25 items



#Stuff not to add into game save
#False = Do not change related vars
#True = Load all related vars to True
set_cheatcode=False
set_quest=False
