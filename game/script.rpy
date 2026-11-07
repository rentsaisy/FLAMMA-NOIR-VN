# default persistent.scene1_completed = False
# default persistent.scene2_completed = False
# default persistent.scene3_completed = False
# default persistent.scene4_completed = False

# label scene1:

#     # isi Scene 1 kamu di sini

#     $ persistent.scene1_completed = True

#     return

# label scene2:

#     # isi Scene 2 kamu di sini

#     $ persistent.scene2_completed = True

# #     return
 
label tutorial_battle:
    jump tutorial

label scene_1:
    jump firstscene
    
label scene_2:
    jump secondscene
    
label scene_3:
    jump thirdscene

label scene_4:
    jump fourthscene



label start:
    return
