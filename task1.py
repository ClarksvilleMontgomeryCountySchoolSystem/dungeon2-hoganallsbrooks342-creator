torch_lit = True
if torch_lit:
    outcome = ("Flicker: I can see around me, hazah!")
    good = r"""
    
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
Zot"""

else:
    outcome = ("Doom: I cannot see anything around me im so scared...")
    bad = r"""
           ____
        ,'' _,-`.
      ,'  ,'_|
     /   / <>|
    :   :    \
    :   :    _\
     \   \  -|
      `.  `._|
        `..__`-.' SSt"""
print(outcome)
print(good)