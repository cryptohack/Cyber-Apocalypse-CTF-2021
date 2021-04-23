N, g1, g2 = [11923673180388077888142388182196128172129768936568117848897202840750467563588267200632621033509694174912348667191029543719934278250306572699783244426975738709162881231680914324197401500202556744442337413134063102952568585557573036422876215569433953840661282588663320724181535332983253917448690168483615356665417456300836143362664388144227279939622313188112893422298422309756008288061370775271667422531014160588076933364038056919723407580964931765836334688386223660466742327485623521191923667273628857973743674510542806350134519920134851327588529635179369390647162541516750001971643814203365229825861833419500983858867, 6052148209269354939553471044537860257912619542342999143573332968979185568856522351467865211539069176283587967846460170705112218783592287801949258416714771601375131138627973420811446155593785834811312009569226175763821058237492758326980748786926622206342622775392874076613666328109046029465547038076033544497492883133047136143057891069641548656796092458572006528541388830491481741500061032279001236888634726121071275966314373821800015768911221178772153431772981918580702646111102617317709987746878556804391895117854187941046961952862301276305861765165834905259250134120380184375204155718931751326925135024124430833338, 6074518335652780439230284959855886422825825555504297770539871000400195657378983368834455076598276355273327399137765958217406329414326288545134528549120180305828561657713613224044806459629061837122507031832476089466414308762205257338108898797484015552749658342914497220679404571895582651862079073210846191899929494023707493802585874975614425222831690112782896980912950581948753786806487993887352744576928577299899456916827834872137854766012280230637541594608678741279712393936802618120388063303985286112761847877774037924887117451926856449247174481694108551069551104956867864552228432289532308071138322990943602224853]
c1, c2 = [532167212839837505067757131320122450595032426132268861883054203021985785496135147558218835017676942244370892416151691738117425531568544621227796780139961996039211420532971480525201201950515751153124437508788178178466728993235457141693614515743095284061905930716428969035003769182172207483875194309665355314809939107171552462836009512916742752910085123249660165400324189132036358507087623581356903472866382516922684536133271232237263227629608666048012811055277078027050434920045744360779922978300705997163716390318268331121984863511696712874488487711358069174096540061955150691450989330992367138863851557334910327979, 8131728609731065018458174400328685064879961711596165315627030915794499763458781139868930157511050130067914998385279035231886030785129882408661311656319219680093016994691797309684233405305464631104529673129063123575389120360207464301511780397379824893459945117090656302515226554914216067504257812779765925333706544795811777176521822047466022448037293044057640338760119890766635536469198193747220150947652664923770885666926255163361880679198663187292631767464653397426226514073632107879365141705411412864970520204202432081920625723964640876087489669516883293741236847859193680472473202462206703622400158285964605051078]

# `g1 = g^(r1 * (p - 1)) (mod N)`
#  => `g1` generates a subgroup of the `Z/qZ` component in `Z/NZ`
# Looking at the CRT representation of `g1` (i.e. in `Z/pZ` x `Z/qZ`), this means is has to be `(1, g1 mod q)`
#  (Because we know that `g1^(q - 1) = 1 (mod N)`, so `g1^(q - 1) (mod p)` must be 1, which only happens when `g1 = 1 (mod p)` or `(p - 1) | (q - 1)`)
# And thus, `g1 = 1 (mod p)`, which means we can take `p = gcd(g1 - 1, N)`

# Alternatively, we immediately write `g1 = (g^(r1 (p - 1)) mod p, g1^(r1 (p - 1)) mod q)`
#  and observe that the factor `p - 1` necessarily clears the component mod p

from math import gcd
from Crypto.Util.number import long_to_bytes
p = gcd(g1 - 1, N)


def decrypt(enc, private):
    c1, c2 = enc
    p, q = private
    m1 = c1 * pow(q, -1, p) * q
    m2 = c2 * pow(p, -1, q) * p
    return (m1 + m2) % (p*q)

print(long_to_bytes(decrypt([c1, c2], [p, N // p])))