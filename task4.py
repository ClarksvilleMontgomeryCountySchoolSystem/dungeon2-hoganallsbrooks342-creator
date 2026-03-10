drawbridge_raised = False
if drawbridge_raised:
    outcome = ("Doom: How will I ever get out of here!")
    bad = r"""      .-._   _ _ _ _ _ _ _ _
 .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
 snd                         (((-'\ .' /
                           _____..'  .'
                          '-._____.-'
"""
else:
    outcome = ("Thunder: Finally, one step closer to being free!")
    good = r"""
            'x|`
          '|xx| `          '|x|
  `   '    |xx|    `   '    |x|`
           |xx|             |x|
  ============|===============|===--
  ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~"""
print(outcome)
print(good)