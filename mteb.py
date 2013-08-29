#!@/usr/bin/python
import pickle 
import random
import os
HOME = os.path.expanduser("~")
MTEB = os.path.join(HOME, ".phenny/modules/mteb")

def read_config(name):
  with open(os.path.join(MTEB, name), "rb") as f:
    return pickle.load(f)

def write_config(obj, name):
  with open(os.path.join(MTEB, name), "wb") as f:
    pickle.dump(obj, f)

def mteb(phenny, input):
  if input.startswith(".mteb credits"):
    phenny.say('mteb was created by Christopher Webber after ')
    phenny.say('he witnessed mike thompson eat a baby, which, ')
    phenny.say('while possibly traumatic for Chris, saved the ')
    phenny.say('baby from a lifetime of misery, failure, and boredom.')
    phenny.say(' ')
    phenny.say('Chris\'s current projects on the internet can be found here:')
    phenny.say('http://mediagoblin.org')
    phenny.say('http://dustycloud.org')
    phenny.say('If you have money, you should give some to media goblin.')
    phenny.say(' ')
    phenny.say(' ')
  phenny.say('  MIKE THOMPSON')
  phenny.say('    ||||||')
  phenny.say('   "" \  /')
  phenny.say('   "" o  o     S')
  phenny.say('   "          / \  o')
  phenny.say('   G  vvvvv  |o o|//')
  phenny.say('   | (       \_^_/OOO')
  phenny.say('   \  ^^^^     //o _|\O')
  phenny.say('   /  ____)   o _|_|<')
  phenny.say('  /    \ \\\   /  / \O')
  phenny.say('        \     /  /')
  phenny.say('         EATS BABIES') 
  

mteb.commands = ['mteb']
mteb.priority = 'medium'

def danger(phenny, input):
  phenny.say(" _( )                 ( )_")
  phenny.say("(_, |      __ __      | ,_)")
  phenny.say("   \\\'\    /  ^  \    /'/")
  phenny.say("    '\\\'\,/\      \,/'/'")
  phenny.say("      '\| []   [] |/' ")
  phenny.say("        (_  /^\  _) ")
  phenny.say("          \  ~  /")
  phenny.say("          /HHHHH\ ")
  phenny.say("        /'/{^^^}\\\'\ ")
  phenny.say("    _,/'/'  ^^^  '\\\'\,_ ")
  phenny.say("   (_, |           | ,_) ")
  phenny.say("     (_)           (_) ")

danger.commands = ['danger']
danger.priority = 'medium'

def cweb(phenny, input):
  phenny.say("                  DO")
  phenny.say("                          ,,")
  phenny.say("                         ';;")
  phenny.say("                          ''")
  phenny.say("            ____          ||")
  phenny.say("           ;    \         ||")
  phenny.say("            \,---'-,-,    ||")
  phenny.say("            /     (  o)   ||")
  phenny.say("          (o )__,--'-' \  ||")
  phenny.say(",,,,       ;'uuuuu''   ) ;;")
  phenny.say("\   \      \ )      ) /\//")
  phenny.say(" '--'       \\'nnnnn' /  \ ")
  phenny.say("   \\\\      //'------'    \ ")
  phenny.say("    \\\\    //  \           \ ")
  phenny.say("     \\\\  //    )           ) ")
  phenny.say("      \\\\//     |           |")
  phenny.say("       \\\\     /            |")
  phenny.say("")
  phenny.say("          ALL THE THINGS")

cweb.commands = ['do']
cweb.priority = 'medium'

def myofb(phenny, input):
  phenny.say("make your own fucking bot")

myofb.commands = ['myofb']


def be_an_adult(phenny, input):
  adultstuff = []
  adultstuff.append("a few times a year, I spontaneously decide that I'm ready to be a real adult.  I don't know why I decide this; it always ends terribly for me.  But I do it anyway.  I sit myself down and tell myself how I'm going to start cleaning the house every day and paying my bills on time and replying to emails before my inbox reaches quadruple digits.  Schedules are drafted.  Day-planners are purchased.  I stock up on fancy food because I'm also planning on morphing into a master chef and actually cooking instead of just eating nachos for dinner every night.   I prepare for  my new life as an adult like some people prepare for the apocalypse.")
  adultstuff.append("the guilt from my ignored responsibilities grows so large that merely carrying it around with me feels like a huge responsibility.  It takes up a sizable portion of my capacity, leaving me almost completely useless for anything other than consuming nachos and surfing the internet like an attention-deficient squirrel on PCP. ")
  if input.startswith(".be an adult add"):
    phenny.say("only voytek gets to add stuff to be an adult.  ")
    phenny.say("... ")
    phenny.say("Ironically.")
    phenny.say("But you can ask him real nice and he'll probably add something")
  elif input.startswith(".be an adult linkme"):
    phenny.say("http://http://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html")
  else:
    ri = random.Random()
    phenny.say(adultstuff[ri.randint(0, len(adultstuff)-1)])

be_an_adult.commands = ['be an adult']
be_an_adult.priority = 'medium'

def cueno(phenny, input):
  if input == ".cueno":
    text = "MICHAEL CUENO"
  else:
    text = input[7:].upper()
  phenny.say("            _..__")
  phenny.say("          .'  I  '.")
  phenny.say("          |.-\"\"\"-.| ")
  phenny.say("         _;.-\"\"\"-.;_")
  phenny.say("     _.-' _..-.-.._ '-._")
  phenny.say("    ';--.-(_o_I_o_)-.--;'")
  phenny.say("=============================")
  phenny.say("  WHO IS %s?!?!?" % text )

cueno.commands = ['cueno']
cueno.priority = 'medium'

def charles_is_happy(phenny, input):
  if input == ".charles is happy":
    text = "i already have everything i want"
  elif input.startswith(".charles is"):
    text = input[12:]
  phenny.say("                   _________________________________")
  phenny.say("        \\\\\\\\\//  /                                  \ ")
  phenny.say("        \\\\\    \ |   The only problem                | ")
  phenny.say("        \\\  <oo) |   with my life is                 | ")
  phenny.say("        \\\C    \ | %s  |" % text)
  phenny.say("        \\\    __\ \___  ____________________________/  ")
  phenny.say("         )    _\       |/ ")
  phenny.say("        /    _\     . ")
  phenny.say("          /`     . ' ")
  phenny.say("       Charles       ")

charles_is_happy.commands = ['charles is']
charles_is_happy.priority = 'medium'        

def fycd(phenny, input):
  if input == ".fycd":
    txt = "CHRIS  DARGIS."
  else:
    txt = input[6:].upper()

  phenny.say('                              ..`           ')                    
  phenny.say('                        :ohmNMMMMmho-         ')                 
  phenny.say('                      omMMMMMMMMMMMMMmo`')                      
  phenny.say('                     +dMMMMMMMMMMMMMMMMs  ')                     
  phenny.say('                    :dMMd+/oossysmNMMMMM`  ')                     
  phenny.say('                    oMMd-         `:+dMM.    ')                   
  phenny.say('                    oMN`-            `MM-      ')                 
  phenny.say('                    /MN`              dM`   ')         
  phenny.say('                    `NN-`-++:. `/+os- ss     ')           
  phenny.say('                    .Ny mdsohh .yo+/o`-s.   ')          
  phenny.say('                     /m`  ``     -.   ..    ')               
  phenny.say('                     `smo   /:``-:   o-.     ')               
  phenny.say('                       /M.  `dMMs    -`       ')               
  phenny.say('                        so`:++y+:/: -.         ')              
  phenny.say('                        :MNMhydh+.odd           ')              
  phenny.say('                       /+MMMo:---/hMN:+          ')            
  phenny.say('                     .ym-MMMMMMMMMMMN`dNs:`      ')              
  phenny.say('                 -+ymMMd :NMMMMMMMMN: NMMMNh+-     ')          
  phenny.say('            ./sdNMMMMMMh  .dMMMMMMm: :MMMMMMMMNho:` ')       
  phenny.say('        `/ymMMMMMMMMMMMh `hMmdmmhso` sMMMMMMMMMMMMMds/`')    
  phenny.say('       +MMMMMMMMMMMMMMMd /yMMMNmdNMm:mMMMMMMMMMMMMMMMMN ')    
  phenny.say('       NMMMMMMMMMMMMMMMN   `hMMMMNh//MMMMMMMMMMMMMMMMMM. ')     
  phenny.say('      `MMMMMMMMMMMMMMMMm`   -MMMM`  sMMMMMMMMMMMMMMMMMMs ')    
  phenny.say('      +MMMMMMMMMMMMMMMMN     sMMN`  dMMMMMMMMMMMMMMMMMMM`')
  phenny.say('                   FUCK  YOU  %s' % txt)

fycd.commands = ['fycd']
fycd.priority = 'medium'

def gerron(phenny, input):
  if input == ".gerron":
    txt = "THIS."
  else:
    txt = input[8:].upper()
  phenny.say(' FFFFFFFF  UU      UU    CCCCCC    KK     KK')
  phenny.say(' FF        UU      UU  CC      CC  KK    KK ')
  phenny.say(' FF        UU      UU  CC          KK   KK  ') 
  phenny.say(' FF        UU      UU  CC          KK  KK   ')
  phenny.say(' FFFFFF    UU      UU  CC          KKKK     ')
  phenny.say(' FF        UU      UU  CC          KK KK    ') 
  phenny.say(' FF        UU      UU  CC          KK  KK   ')
  phenny.say(' FF        UU      UU  CC      CC  KK   KK  ')
  phenny.say(' FF         UUUUUUUU     CCCCCC    KK    KK ')
  phenny.say('                                           %s' % txt)

gerron.commands = ['gerron']
fycd.priority = 'medium' 

def fortune(phenny, input):
  fort = read_config("fortune")
  fixinput = input[9:]
    
  ri = random.Random()
  if fixinput.startswith("add"):
    newFort = fixinput[4:]
    fort.append(newFort)
    write_config(fort, "fortune")
    phenny.say("added %s and wrote a new config to disk." % newFort)
  phenny.say(fort[ri.randint(0, len(fort)-1)])

fortune.commands = ['fortune']
fortune.priority = 'medium'

def insult(phenny, input):
  insults = read_config("insult")
  fixinput = input[8:]
  ri = random.Random()
  if fixinput.startswith("add"):
    insult = fixinput[4:]
    insults.append(insult)
    write_config(insults, "insult")
    phenny.say("added %s and wrote a new config to disk." % insult)
  elif fixinput:
    phenny.say("%s: %s" % (fixinput, insults[ri.randint(0, len(insults)-1)]))
  else:
    phenny.say(insults[ri.randint(0, len(insults)-1)])

insult.commands = ['insult']
insult.priority = 'medium'

def quote(phenny, input):
  quotes = read_config("quote")
  fixinput = input[7:]
  ri = random.Random()
  if fixinput.startswith("add"):
    newQuote = fixinput[4:]
    quotes.append(newQuote)
    write_config(quotes, "quote")
    phenny.say("added %s and wrote a new config to disk" % newQuote)
  else:
    phenny.say(quotes[ri.randint(0, len(quotes)-1)])

quote.commands = ['quote']
quote.priority = 'medium'

def ulzo(phenny, input):
  if input == ".ulzo":
    txt = "Rabbitz eat brainz."
  else:
    txt = input.strip(".ulzo ")

  phenny.say(",.   ,.")
  phenny.say("\.\ /,/")
  phenny.say(" Y Y f")
  phenny.say(" |. .|")
  phenny.say("(\"_, l")
  phenny.say(" ,- , \\")
  phenny.say("(_)(_) Y,.")
  phenny.say(" _j _j |,'  %s" % txt)
  phenny.say("(_,(__,'")

ulzo.commands = ['ulzo']
ulzo.priority = 'medium'

def mthelp(phenny, input):
  phenny.say("=================================================")
  phenny.say("    /   mt-bot is really phenny, so supports  ")
  phenny.say("  [\\\"]    all that phenny supports and then some.")
  phenny.say(" /[_]\    Some custom mt bot commands are .mteb ")
  phenny.say("  ] [     .ulzo and .fycd ... if you'd like your ")
  phenny.say(" own command or have an idea for a command, msg ")
  phenny.say(" voytek or write your own damned bot.")
  phenny.say(" ================================================")
  phenny.say(" to get info about built-in phenny commands, ")
  phenny.say(" pm mt-bot \"help\" (which is currently broken?)")
  phenny.say(" mt-bot has hidden, secret commands too.")
  phenny.say(" ================================================")
  phenny.say(" notice: neither mt-bot nor #uic-cs has any ")
  phenny.say(" affiliation with University of Illinois Chicago")
  phenny.say(" except that some of us do or have in the past ")
  phenny.say(" paid them too much money to teach us things we ")
  phenny.say(" could learn on just as well our own.")
  phenny.say(" ================================================")


mthelp.commands = ['help']
mthelp.priority = 'medium'
