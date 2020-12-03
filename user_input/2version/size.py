import requests
import pandas as pd 

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")

data = r.json()
df1 = pd.DataFrame(data)
df2 = df1[["name","temperament", "weight"]]

# Explode out list of temperament adj
df3 = df2.assign(temperament=df2.temperament.str.split(',')).explode('temperament')

# Clean Data
df3["temperament"] = df3["temperament"].str.lower()
df3["temperament"] = df3["temperament"].str.strip()

# turn df into a dict 
dict_ = df3.to_dict('records')

for i in dict_:
    i["weight"] = i["weight"]["imperial"]
    i["points"] = 0
    i['avg_weight'] = 0
    i['size_category'] = ''


for i in dict_:
    if i["weight"] == 'up - 18':
        i["weight"] = '18 - 18'
    else:
        i["weight"] == i["weight"]

# get avg weights
for i in dict_:
    if len(i["weight"]) == 5:
        i['avg_weight'] = (int(i["weight"][4]) + int(i["weight"][0])) / 2
    elif len(i["weight"]) == 6:
        x =int(i["weight"][4] + i["weight"][5])
        i['avg_weight'] = (x + int(i["weight"][0])) / 2
    elif len(i["weight"]) == 7:
        x =int(i["weight"][5] + i["weight"][6])
        y =int(i["weight"][0] + i["weight"][1])
        i['avg_weight'] = (x + y) / 2
    elif len(i["weight"]) == 8:
        x =int(i["weight"][5] + i["weight"][6] + i["weight"][7])
        y =int(i["weight"][0] + i["weight"][1])
        i['avg_weight'] = (x + y) / 2
    elif len(i["weight"]) == 9:
        x =int(i["weight"][6] + i["weight"][7] + i["weight"][8])
        y =int(i["weight"][0] + i["weight"][1] + i["weight"][2])
        i['avg_weight'] = (x + y) / 2



# Small Dog# 0-20 pounds
# Medium Dog# 21-60 pounds
# Large Dog# 61+ pounds

# categorize dog size based on avg weight
for i in dict_:
    if i["avg_weight"] < 20:
        i["size_category"] = 'small'
    elif i["avg_weight"] < 60:
        i["size_category"] = 'medium'
    else:
        i["size_category"] = 'large'


# get list of adj for the different dog sizes

# large
large_adj = []
for i in dict_: 
    if i["size_category"] == 'large' and i["temperament"] not in large_adj:
        large_adj.append(i["temperament"])

# medium
medium_adj = []
for i in dict_: 
    if i["size_category"] == 'medium' and i["temperament"] not in medium_adj:
        medium_adj.append(i["temperament"])

# small
small_adj = []
for i in dict_: 
    if i["size_category"] == 'small' and i["temperament"] not in small_adj:
        small_adj.append(i["temperament"])


small_adj = """
    <div class="list-1">
        <input type="checkbox" id="stubborn" name="stubborn" value="stubborn"><label for="stubborn">stubborn</label>
        <input type="checkbox" id="curious" name="curious" value="curious"><label for="curious">curious</label>
        <input type="checkbox" id="playful" name="playful" value="playful"><label for="playful">playful</label>
        <input type="checkbox" id="adventurous" name="adventurous" value="adventurous"><label for="adventurous">adventurous</label>
        <input type="checkbox" id="active" name="active" value="active"><label for="active">active</label>
        <input type="checkbox" id="fun-loving" name="fun-loving" value="fun-loving"><label for="fun-loving">fun-loving</label>
        <input type="checkbox" id="friendly" name="friendly" value="friendly"><label for="friendly">friendly</label>
        <input type="checkbox" id="alert" name="alert" value="alert"><label for="alert">alert</label>
        <input type="checkbox" id="reserved" name="reserved" value="reserved"><label for="reserved">reserved</label>
        <input type="checkbox" id="intelligent" name="intelligent" value="intelligent"><label for="intelligent">intelligent</label>
        <input type="checkbox" id="protective" name="protective" value="protective"><label for="protective">protective</label>
        <input type="checkbox" id="spirited" name="spirited" value="spirited"><label for="spirited">spirited</label>
        <input type="checkbox" id="loyal" name="loyal" value="loyal"><label for="loyal">loyal</label>
        <input type="checkbox" id="companionable" name="companionable" value="companionable"><label for="companionable">companionable</label>
        <input type="checkbox" id="even tempered" name="even tempered" value="even tempered"><label for="even tempered">even tempered</label>
        <input type="checkbox" id="courageous" name="courageous" value="courageous"><label for="courageous">courageous</label>
        <input type="checkbox" id="feisty" name="feisty" value="feisty"><label for="feisty">feisty</label>
        <input type="checkbox" id="affectionate" name="affectionate" value="affectionate"><label for="affectionate">affectionate</label>
        <input type="checkbox" id="cheerful" name="cheerful" value="cheerful"><label for="cheerful">cheerful</label>
        <input type="checkbox" id="gentle" name="gentle" value="gentle"><label for="gentle">gentle</label>
        <input type="checkbox" id="sensitive" name="sensitive" value="sensitive"><label for="sensitive">sensitive</label>
        <input type="checkbox" id="fearless" name="fearless" value="fearless"><label for="fearless">fearless</label>
        <input type="checkbox" id="obedient" name="obedient" value="obedient"><label for="obedient">obedient</label>
        <input type="checkbox" id="lively" name="lively" value="lively"><label for="lively">lively</label>
        <input type="checkbox" id="hardy" name="hardy" value="hardy"><label for="hardy">hardy</label>
        <input type="checkbox" id="assertive" name="assertive" value="assertive"><label for="assertive">assertive</label>
        <input type="checkbox" id="gay" name="gay" value="gay"><label for="gay">gay</label>
        <input type="checkbox" id="sociable" name="sociable" value="sociable"><label for="sociable">sociable</label>
        <input type="checkbox" id="patient" name="patient" value="patient"><label for="patient">patient</label>
        <input type="checkbox" id="adaptable" name="adaptable" value="adaptable"><label for="adaptable">adaptable</label>
        <input type="checkbox" id="sweet-tempered" name="sweet-tempered" value="sweet-tempered"><label for="sweet-tempered">sweet-tempered</label>
        <input type="checkbox" id="happy" name="happy" value="happy"><label for="happy">happy</label>
        <input type="checkbox" id="trainable" name="trainable" value="trainable"><label for="trainable">trainable</label>
        <input type="checkbox" id="vocal" name="vocal" value="vocal"><label for="vocal">vocal</label>
        <input type="checkbox" id="loving" name="loving" value="loving"><label for="loving">loving</label>
        <input type="checkbox" id="cunning" name="cunning" value="cunning"><label for="cunning">cunning</label>
        <input type="checkbox" id="keen" name="keen" value="keen"><label for="keen">keen</label>
        <input type="checkbox" id="easygoing" name="easygoing" value="easygoing"><label for="easygoing">easygoing</label>
        <input type="checkbox" id="athletic" name="athletic" value="athletic"><label for="athletic">athletic</label>
        <input type="checkbox" id="bright" name="bright" value="bright"><label for="bright">bright</label>
        <input type="checkbox" id="self-important" name="self-important" value="self-important"><label for="self-important">self-important</label>
        <input type="checkbox" id="inquisitive" name="inquisitive" value="inquisitive"><label for="inquisitive">inquisitive</label>
        <input type="checkbox" id="watchful" name="watchful" value="watchful"><label for="watchful">watchful</label>
        <input type="checkbox" id="responsive" name="responsive" value="responsive"><label for="responsive">responsive</label>
        <input type="checkbox" id="mischievous" name="mischievous" value="mischievous"><label for="mischievous">mischievous</label>
        <input type="checkbox" id="agile" name="agile" value="agile"><label for="agile">agile</label>
        <input type="checkbox" id="independent" name="independent" value="independent"><label for="independent">independent</label>
        <input type="checkbox" id="cat-like" name="cat-like" value="cat-like"><label for="cat-like">cat-like</label>
        <input type="checkbox" id="proud" name="proud" value="proud"><label for="proud">proud</label>
        <input type="checkbox" id="clever" name="clever" value="clever"><label for="clever">clever</label>
        <input type="checkbox" id="steady" name="steady" value="steady"><label for="steady">steady</label>
        <input type="checkbox" id="devoted" name="devoted" value="devoted"><label for="devoted">devoted</label>
        <input type="checkbox" id="energetic" name="energetic" value="energetic"><label for="energetic">energetic</label>
        <input type="checkbox" id="docile" name="docile" value="docile"><label for="docile">docile</label>
        <input type="checkbox" id="outgoing" name="outgoing" value="outgoing"><label for="outgoing">outgoing</label>
        <input type="checkbox" id="self-confidence" name="self-confidence" value="self-confidence"><label for="self-confidence">self-confidence</label>
        <input type="checkbox" id="lovable" name="lovable" value="lovable"><label for="lovable">lovable</label>
        <input type="checkbox" id="opinionated" name="opinionated" value="opinionated"><label for="opinionated">opinionated</label>
        <input type="checkbox" id="good-natured" name="good-natured" value="good-natured"><label for="good-natured">good-natured</label>
        <input type="checkbox" id="aggressive" name="aggressive" value="aggressive"><label for="aggressive">aggressive</label>
        <input type="checkbox" id="extroverted" name="extroverted" value="extroverted"><label for="extroverted">extroverted</label>
        <input type="checkbox" id="charming" name="charming" value="charming"><label for="charming">charming</label>
        <input type="checkbox" id="quiet" name="quiet" value="quiet"><label for="quiet">quiet</label>
        <input type="checkbox" id="attentive" name="attentive" value="attentive"><label for="attentive">attentive</label>
        <input type="checkbox" id="confident" name="confident" value="confident"><label for="confident">confident</label>
        <input type="checkbox" id="faithful" name="faithful" value="faithful"><label for="faithful">faithful</label>
        <input type="checkbox" id="strong" name="strong" value="strong"><label for="strong">strong</label>
        <input type="checkbox" id="spunky" name="spunky" value="spunky"><label for="spunky">spunky</label>
        <input type="checkbox" id="quick" name="quick" value="quick"><label for="quick">quick</label>
        <input type="checkbox" id="joyful" name="joyful" value="joyful"><label for="joyful">joyful</label>
        <input type="checkbox" id="willful" name="willful" value="willful"><label for="willful">willful</label>
        <input type="checkbox" id="aloof" name="aloof" value="aloof"><label for="aloof">aloof</label>
        <input type="checkbox" id="bold" name="bold" value="bold"><label for="bold">bold</label>  
    </div>
                """


medium_adj = """
    <div class="list-1">
        <input type='checkbox' id='aloof' name='aloof' value='aloof'><label for='aloof'>aloof</label>
        <input type='checkbox' id='clownish' name='clownish' value='clownish'><label for='clownish'>clownish</label>
        <input type='checkbox' id='dignified' name='dignified' value='dignified'><label for='dignified'>dignified</label>
        <input type='checkbox' id='independent' name='independent' value='independent'><label for='independent'>independent</label>
        <input type='checkbox' id='happy' name='happy' value='happy'><label for='happy'>happy</label>
        <input type='checkbox' id='wild' name='wild' value='wild'><label for='wild'>wild</label>
        <input type='checkbox' id='hardworking' name='hardworking' value='hardworking'><label for='hardworking'>hardworking</label>
        <input type='checkbox' id='dutiful' name='dutiful' value='dutiful'><label for='dutiful'>dutiful</label>
        <input type='checkbox' id='outgoing' name='outgoing' value='outgoing'><label for='outgoing'>outgoing</label>
        <input type='checkbox' id='friendly' name='friendly' value='friendly'><label for='friendly'>friendly</label>
        <input type='checkbox' id='alert' name='alert' value='alert'><label for='alert'>alert</label>
        <input type='checkbox' id='confident' name='confident' value='confident'><label for='confident'>confident</label>
        <input type='checkbox' id='intelligent' name='intelligent' value='intelligent'><label for='intelligent'>intelligent</label>
        <input type='checkbox' id='courageous' name='courageous' value='courageous'><label for='courageous'>courageous</label>
        <input type='checkbox' id='energetic' name='energetic' value='energetic'><label for='energetic'>energetic</label>
        <input type='checkbox' id='loyal' name='loyal' value='loyal'><label for='loyal'>loyal</label>
        <input type='checkbox' id='gentle' name='gentle' value='gentle'><label for='gentle'>gentle</label>
        <input type='checkbox' id='reserved' name='reserved' value='reserved'><label for='reserved'>reserved</label>
        <input type='checkbox' id='protective' name='protective' value='protective'><label for='protective'>protective</label>
        <input type='checkbox' id='strong willed' name='strong willed' value='strong willed'><label for='strong willed'>strong willed</label>
        <input type='checkbox' id='stubborn' name='stubborn' value='stubborn'><label for='stubborn'>stubborn</label>
        <input type='checkbox' id='affectionate' name='affectionate' value='affectionate'><label for='affectionate'>affectionate</label>
        <input type='checkbox' id='obedient' name='obedient' value='obedient'><label for='obedient'>obedient</label>
        <input type='checkbox' id='tenacious' name='tenacious' value='tenacious'><label for='tenacious'>tenacious</label>
        <input type='checkbox' id='devoted' name='devoted' value='devoted'><label for='devoted'>devoted</label>
        <input type='checkbox' id='attentive' name='attentive' value='attentive'><label for='attentive'>attentive</label>
        <input type='checkbox' id='trainable' name='trainable' value='trainable'><label for='trainable'>trainable</label>
        <input type='checkbox' id='reliable' name='reliable' value='reliable'><label for='reliable'>reliable</label>
        <input type='checkbox' id='fearless' name='fearless' value='fearless'><label for='fearless'>fearless</label>
        <input type='checkbox' id='lively' name='lively' value='lively'><label for='lively'>lively</label>
        <input type='checkbox' id='self-assured' name='self-assured' value='self-assured'><label for='self-assured'>self-assured</label>
        <input type='checkbox' id='cautious' name='cautious' value='cautious'><label for='cautious'>cautious</label>
        <input type='checkbox' id='brave' name='brave' value='brave'><label for='brave'>brave</label>
        <input type='checkbox' id='eager' name='eager' value='eager'><label for='eager'>eager</label>
        <input type='checkbox' id='good-natured' name='good-natured' value='good-natured'><label for='good-natured'>good-natured</label>
        <input type='checkbox' id='active' name='active' value='active'><label for='active'>active</label>
        <input type='checkbox' id='rugged' name='rugged' value='rugged'><label for='rugged'>rugged</label>
        <input type='checkbox' id='fierce' name='fierce' value='fierce'><label for='fierce'>fierce</label>
        <input type='checkbox' id='refined' name='refined' value='refined'><label for='refined'>refined</label>
        <input type='checkbox' id='companionable' name='companionable' value='companionable'><label for='companionable'>companionable</label>
        <input type='checkbox' id='joyful' name='joyful' value='joyful'><label for='joyful'>joyful</label>
        <input type='checkbox' id='curious' name='curious' value='curious'><label for='curious'>curious</label>
        <input type='checkbox' id='playful' name='playful' value='playful'><label for='playful'>playful</label>
        <input type='checkbox' id='agile' name='agile' value='agile'><label for='agile'>agile</label>
        <input type='checkbox' id='sweet-tempered' name='sweet-tempered' value='sweet-tempered'><label for='sweet-tempered'>sweet-tempered</label>
        <input type='checkbox' id='amiable' name='amiable' value='amiable'><label for='amiable'>amiable</label>
        <input type='checkbox' id='even tempered' name='even tempered' value='even tempered'><label for='even tempered'>even tempered</label>
        <input type='checkbox' id='excitable' name='excitable' value='excitable'><label for='excitable'>excitable</label>
        <input type='checkbox' id='determined' name='determined' value='determined'><label for='determined'>determined</label>
        <input type='checkbox' id='self-confidence' name='self-confidence' value='self-confidence'><label for='self-confidence'>self-confidence</label>
        <input type='checkbox' id='hardy' name='hardy' value='hardy'><label for='hardy'>hardy</label>
        <input type='checkbox' id='spirited' name='spirited' value='spirited'><label for='spirited'>spirited</label>
        <input type='checkbox' id='good-tempered' name='good-tempered' value='good-tempered'><label for='good-tempered'>good-tempered</label>
        <input type='checkbox' id='keen' name='keen' value='keen'><label for='keen'>keen</label>
        <input type='checkbox' id='responsive' name='responsive' value='responsive'><label for='responsive'>responsive</label>
        <input type='checkbox' id='adaptable' name='adaptable' value='adaptable'><label for='adaptable'>adaptable</label>
        <input type='checkbox' id='quick' name='quick' value='quick'><label for='quick'>quick</label>
        <input type='checkbox' id='territorial' name='territorial' value='territorial'><label for='territorial'>territorial</label>
        <input type='checkbox' id='suspicious' name='suspicious' value='suspicious'><label for='suspicious'>suspicious</label>
        <input type='checkbox' id='loving' name='loving' value='loving'><label for='loving'>loving</label>
        <input type='checkbox' id='quiet' name='quiet' value='quiet'><label for='quiet'>quiet</label>
        <input type='checkbox' id='faithful' name='faithful' value='faithful'><label for='faithful'>faithful</label>
        <input type='checkbox' id='sociable' name='sociable' value='sociable'><label for='sociable'>sociable</label>
        <input type='checkbox' id='trusting' name='trusting' value='trusting'><label for='trusting'>trusting</label>
        <input type='checkbox' id='merry' name='merry' value='merry'><label for='merry'>merry</label>
        <input type='checkbox' id='sensitive' name='sensitive' value='sensitive'><label for='sensitive'>sensitive</label>
        <input type='checkbox' id='kind' name='kind' value='kind'><label for='kind'>kind</label>
        <input type='checkbox' id='bossy' name='bossy' value='bossy'><label for='bossy'>bossy</label>
        <input type='checkbox' id='cheerful' name='cheerful' value='cheerful'><label for='cheerful'>cheerful</label>
        <input type='checkbox' id='watchful' name='watchful' value='watchful'><label for='watchful'>watchful</label>
        <input type='checkbox' id='calm' name='calm' value='calm'><label for='calm'>calm</label>
        <input type='checkbox' id='docile' name='docile' value='docile'><label for='docile'>docile</label>
        <input type='checkbox' id='familial' name='familial' value='familial'><label for='familial'>familial</label>
        <input type='checkbox' id='vocal' name='vocal' value='vocal'><label for='vocal'>vocal</label>
        <input type='checkbox' id='boisterous' name='boisterous' value='boisterous'><label for='boisterous'>boisterous</label>
        <input type='checkbox' id='bold' name='bold' value='bold'><label for='bold'>bold</label>
        <input type='checkbox' id='cooperative' name='cooperative' value='cooperative'><label for='cooperative'>cooperative</label>
        <input type='checkbox' id='tolerant' name='tolerant' value='tolerant'><label for='tolerant'>tolerant</label>
        <input type='checkbox' id='respectful' name='respectful' value='respectful'><label for='respectful'>respectful</label>
        <input type='checkbox' id='dominant' name='dominant' value='dominant'><label for='dominant'>dominant</label>
        <input type='checkbox' id='sturdy' name='sturdy' value='sturdy'><label for='sturdy'>sturdy</label>
        <input type='checkbox' id='bright' name='bright' value='bright'><label for='bright'>bright</label>
        <input type='checkbox' id='benevolent' name='benevolent' value='benevolent'><label for='benevolent'>benevolent</label>
        <input type='checkbox' id='patient' name='patient' value='patient'><label for='patient'>patient</label>
        <input type='checkbox' id='feisty' name='feisty' value='feisty'><label for='feisty'>feisty</label>
        <input type='checkbox' id='charming' name='charming' value='charming'><label for='charming'>charming</label>
        <input type='checkbox' id='diligent' name='diligent' value='diligent'><label for='diligent'>diligent</label>
        <input type='checkbox' id='athletic' name='athletic' value='athletic'><label for='athletic'>athletic</label>
        <input type='checkbox' id='vigilant' name='vigilant' value='vigilant'><label for='vigilant'>vigilant</label>
        <input type='checkbox' id='proud' name='proud' value='proud'><label for='proud'>proud</label>
    </div>
                """


large_adj = """
    <div class="list-1">
        <input type='checkbox' id='loyal' name='loyal' value='loyal'><label for='loyal'>loyal</label>
        <input type='checkbox' id='independent' name='independent' value='independent'><label for='independent'>independent</label>
        <input type='checkbox' id='intelligent' name='intelligent' value='intelligent'><label for='intelligent'>intelligent</label>
        <input type='checkbox' id='brave' name='brave' value='brave'><label for='brave'>brave</label>
        <input type='checkbox' id='docile' name='docile' value='docile'><label for='docile'>docile</label>
        <input type='checkbox' id='alert' name='alert' value='alert'><label for='alert'>alert</label>
        <input type='checkbox' id='responsive' name='responsive' value='responsive'><label for='responsive'>responsive</label>
        <input type='checkbox' id='dignified' name='dignified' value='dignified'><label for='dignified'>dignified</label>
        <input type='checkbox' id='composed' name='composed' value='composed'><label for='composed'>composed</label>
        <input type='checkbox' id='friendly' name='friendly' value='friendly'><label for='friendly'>friendly</label>
        <input type='checkbox' id='receptive' name='receptive' value='receptive'><label for='receptive'>receptive</label>
        <input type='checkbox' id='faithful' name='faithful' value='faithful'><label for='faithful'>faithful</label>
        <input type='checkbox' id='courageous' name='courageous' value='courageous'><label for='courageous'>courageous</label>
        <input type='checkbox' id='loving' name='loving' value='loving'><label for='loving'>loving</label>
        <input type='checkbox' id='protective' name='protective' value='protective'><label for='protective'>protective</label>
        <input type='checkbox' id='trainable' name='trainable' value='trainable'><label for='trainable'>trainable</label>
        <input type='checkbox' id='dutiful' name='dutiful' value='dutiful'><label for='dutiful'>dutiful</label>
        <input type='checkbox' id='responsible' name='responsible' value='responsible'><label for='responsible'>responsible</label>
        <input type='checkbox' id='affectionate' name='affectionate' value='affectionate'><label for='affectionate'>affectionate</label>
        <input type='checkbox' id='devoted' name='devoted' value='devoted'><label for='devoted'>devoted</label>
        <input type='checkbox' id='playful' name='playful' value='playful'><label for='playful'>playful</label>
        <input type='checkbox' id='assertive' name='assertive' value='assertive'><label for='assertive'>assertive</label>
        <input type='checkbox' id='energetic' name='energetic' value='energetic'><label for='energetic'>energetic</label>
        <input type='checkbox' id='gentle' name='gentle' value='gentle'><label for='gentle'>gentle</label>
        <input type='checkbox' id='confident' name='confident' value='confident'><label for='confident'>confident</label>
        <input type='checkbox' id='dominant' name='dominant' value='dominant'><label for='dominant'>dominant</label>
        <input type='checkbox' id='strong willed' name='strong willed' value='strong willed'><label for='strong willed'>strong willed</label>
        <input type='checkbox' id='stubborn' name='stubborn' value='stubborn'><label for='stubborn'>stubborn</label>
        <input type='checkbox' id='clownish' name='clownish' value='clownish'><label for='clownish'>clownish</label>
        <input type='checkbox' id='obedient' name='obedient' value='obedient'><label for='obedient'>obedient</label>
        <input type='checkbox' id='kind' name='kind' value='kind'><label for='kind'>kind</label>
        <input type='checkbox' id='sweet-tempered' name='sweet-tempered' value='sweet-tempered'><label for='sweet-tempered'>sweet-tempered</label>
        <input type='checkbox' id='steady' name='steady' value='steady'><label for='steady'>steady</label>
        <input type='checkbox' id='bold' name='bold' value='bold'><label for='bold'>bold</label>
        <input type='checkbox' id='proud' name='proud' value='proud'><label for='proud'>proud</label>
        <input type='checkbox' id='fearless' name='fearless' value='fearless'><label for='fearless'>fearless</label>
        <input type='checkbox' id='calm' name='calm' value='calm'><label for='calm'>calm</label>
        <input type='checkbox' id='watchful' name='watchful' value='watchful'><label for='watchful'>watchful</label>
        <input type='checkbox' id='hard-working' name='hard-working' value='hard-working'><label for='hard-working'>hard-working</label>
        <input type='checkbox' id='active' name='active' value='active'><label for='active'>active</label>
        <input type='checkbox' id='easygoing' name='easygoing' value='easygoing'><label for='easygoing'>easygoing</label>
        <input type='checkbox' id='adaptable' name='adaptable' value='adaptable'><label for='adaptable'>adaptable</label>
        <input type='checkbox' id='trusting' name='trusting' value='trusting'><label for='trusting'>trusting</label>
        <input type='checkbox' id='even tempered' name='even tempered' value='even tempered'><label for='even tempered'>even tempered</label>
        <input type='checkbox' id='lovable' name='lovable' value='lovable'><label for='lovable'>lovable</label>
        <input type='checkbox' id='territorial' name='territorial' value='territorial'><label for='territorial'>territorial</label>
        <input type='checkbox' id='familial' name='familial' value='familial'><label for='familial'>familial</label>
        <input type='checkbox' id='rational' name='rational' value='rational'><label for='rational'>rational</label>
        <input type='checkbox' id='cheerful' name='cheerful' value='cheerful'><label for='cheerful'>cheerful</label>
        <input type='checkbox' id='bright' name='bright' value='bright'><label for='bright'>bright</label>
        <input type='checkbox' id='companionable' name='companionable' value='companionable'><label for='companionable'>companionable</label>
        <input type='checkbox' id='keen' name='keen' value='keen'><label for='keen'>keen</label>
        <input type='checkbox' id='reliable' name='reliable' value='reliable'><label for='reliable'>reliable</label>
        <input type='checkbox' id='reserved' name='reserved' value='reserved'><label for='reserved'>reserved</label>
        <input type='checkbox' id='powerful' name='powerful' value='powerful'><label for='powerful'>powerful</label>
        <input type='checkbox' id='stable' name='stable' value='stable'><label for='stable'>stable</label>
        <input type='checkbox' id='quiet' name='quiet' value='quiet'><label for='quiet'>quiet</label>
        <input type='checkbox' id='inquisitive' name='inquisitive' value='inquisitive'><label for='inquisitive'>inquisitive</label>
        <input type='checkbox' id='quick' name='quick' value='quick'><label for='quick'>quick</label>
        <input type='checkbox' id='strong' name='strong' value='strong'><label for='strong'>strong</label>
        <input type='checkbox' id='happy' name='happy' value='happy'><label for='happy'>happy</label>
        <input type='checkbox' id='great-hearted' name='great-hearted' value='great-hearted'><label for='great-hearted'>great-hearted</label>
        <input type='checkbox' id='tolerant' name='tolerant' value='tolerant'><label for='tolerant'>tolerant</label>
        <input type='checkbox' id='mischievous' name='mischievous' value='mischievous'><label for='mischievous'>mischievous</label>
        <input type='checkbox' id='eager' name='eager' value='eager'><label for='eager'>eager</label>
        <input type='checkbox' id='people-oriented' name='people-oriented' value='people-oriented'><label for='people-oriented'>people-oriented</label>
        <input type='checkbox' id='curious' name='curious' value='curious'><label for='curious'>curious</label>
        <input type='checkbox' id='trustworthy' name='trustworthy' value='trustworthy'><label for='trustworthy'>trustworthy</label>
        <input type='checkbox' id='gay' name='gay' value='gay'><label for='gay'>gay</label>
        <input type='checkbox' id='patient' name='patient' value='patient'><label for='patient'>patient</label>
        <input type='checkbox' id='athletic' name='athletic' value='athletic'><label for='athletic'>athletic</label>
        <input type='checkbox' id='thoughtful' name='thoughtful' value='thoughtful'><label for='thoughtful'>thoughtful</label>
        <input type='checkbox' id='generous' name='generous' value='generous'><label for='generous'>generous</label>
        <input type='checkbox' id='outgoing' name='outgoing' value='outgoing'><label for='outgoing'>outgoing</label>
        <input type='checkbox' id='agile' name='agile' value='agile'><label for='agile'>agile</label>
        <input type='checkbox' id='sociable' name='sociable' value='sociable'><label for='sociable'>sociable</label>
        <input type='checkbox' id='bubbly' name='bubbly' value='bubbly'><label for='bubbly'>bubbly</label>
        <input type='checkbox' id='suspicious' name='suspicious' value='suspicious'><label for='suspicious'>suspicious</label>
        <input type='checkbox' id='unflappable' name='unflappable' value='unflappable'><label for='unflappable'>unflappable</label>
        <input type='checkbox' id='sensitive' name='sensitive' value='sensitive'><label for='sensitive'>sensitive</label>
        <input type='checkbox' id='good-natured' name='good-natured' value='good-natured'><label for='good-natured'>good-natured</label>
        <input type='checkbox' id='self-assured' name='self-assured' value='self-assured'><label for='self-assured'>self-assured</label>
        <input type='checkbox' id='lively' name='lively' value='lively'><label for='lively'>lively</label>
        <input type='checkbox' id='tenacious' name='tenacious' value='tenacious'><label for='tenacious'>tenacious</label>
        <input type='checkbox' id='aloof' name='aloof' value='aloof'><label for='aloof'>aloof</label>
        <input type='checkbox' id='clever' name='clever' value='clever'><label for='clever'>clever</label>
        <input type='checkbox' id='fast' name='fast' value='fast'><label for='fast'>fast</label>
        <input type='checkbox' id='self-confidence' name='self-confidence' value='self-confidence'><label for='self-confidence'>self-confidence</label>
    </div>
                """



def size_(user_size):
    if user_size == "small":
        return small_adj
    elif user_size == 'medium':
        return medium_adj
    else:
        return large_adj


# def best_breed():
    for c in adj_list:
        for i in dict_:
            for e in i:
                for t in e:
                    if c == [i][0]["temperament"]:
                        [i][0]["points"] += 1


    df4 = pd.DataFrame(dict_)

    df4 = df4[df4["size_category"] == dog_size[0]]

    df4 = df4[["name", "points"]]

    df5 = df4.groupby(by = ['name']).sum()

    df6 = df5.sort_values("points", ascending = False)
    print(df6.head())


