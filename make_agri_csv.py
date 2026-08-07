import csv, random, itertools, os

random.seed(42)
os.makedirs('output', exist_ok=True)

CROPS = [
    'rice','wheat','maize','cotton','sugarcane','soybean','tomato','potato','onion','chilli',
    'brinjal','cabbage','cauliflower','okra','groundnut','mustard','sunflower','bajra','jowar','ragi',
    'gram','pigeon pea','green gram','black gram','banana','mango','papaya','grapes','pomegranate','citrus',
    'turmeric','ginger','garlic','coriander','cumin'
]

DISEASES = {
    'rice':['blast','brown spot','bacterial leaf blight','tungro virus','sheath blight'],
    'wheat':['rust','powdery mildew','loose smut','karnal bunt','alternaria leaf blight'],
    'maize':['stem borer damage','turcicum leaf blight','banded leaf and sheath blight','downy mildew','fusarium stalk rot'],
    'cotton':['boll rot','leaf curl virus','pink bollworm damage','alternaria leaf spot','bacterial blight'],
    'sugarcane':['red rot','smut','ratoon stunting disease','leaf scald','ring spot'],
    'soybean':['yellow mosaic virus','bacterial pustule','frogeye leaf spot','rust','sudden death syndrome'],
    'tomato':['early blight','late blight','bacterial wilt','leaf curl virus','powdery mildew'],
    'potato':['late blight','early blight','bacterial wilt','mosaic virus','scab'],
    'onion':['purple blotch','downy mildew','neck rot','bacterial rot','stemphylium blight'],
    'chilli':['anthracnose','bacterial leaf spot','leaf curl virus','powdery mildew','dieback'],
    'brinjal':['fruit rot','bacterial wilt','little leaf virus','alternaria leaf spot','mosaic'],
    'cabbage':['black rot','downy mildew','alternaria leaf spot','clubroot','powdery mildew'],
    'cauliflower':['black rot','downy mildew','alternaria leaf spot','clubroot','powdery mildew'],
    'okra':['yellow vein mosaic','powdery mildew','bacterial leaf spot','anthracnose','root-knot nematode'],
    'groundnut':['leaf spot','rust','stem rot','bud necrosis virus','collar rot'],
    'mustard':['alternaria leaf spot','white rust','downy mildew','aphid damage','powdery mildew'],
    'sunflower':['downy mildew','rust','alternaria leaf spot','head rot','sclerotinia head rot'],
    'bajra':['downy mildew','smut','rust','blast','leaf spot'],
    'jowar':['grain mold','anthracnose','downy mildew','leaf blight','rust'],
    'ragi':['blast','helminthosporium leaf spot','smut','rust','bacterial leaf streak'],
    'gram':['wilt','dry root rot','ascochyta blight','botrytis grey mold','alternaria blight'],
    'pigeon pea':['wilt','sterility mosaic','phytophthora blight','alternaria blight','pod borer damage'],
    'green gram':['powdery mildew','yellow mosaic virus','anthracnose','alternaria leaf spot','bacterial leaf spot'],
    'black gram':['powdery mildew','yellow mosaic virus','anthracnose','alternaria leaf spot','bacterial leaf spot'],
    'banana':['panama wilt','sigatoka leaf spot','anthracnose','bacterial wilt','banana bunchy top virus'],
    'mango':['anthracnose','powdery mildew','bacterial canker','spongy tissue','dieback'],
    'papaya':['ring spot virus','powdery mildew','anthracnose','stem canker','bacterial leaf spot'],
    'grapes':['downy mildew','powdery mildew','anthracnose','black rot','botrytis bunch rot'],
    'pomegranate':['bacterial blight','anthracnose','leaf spot','fruit rot','cercospora leaf spot'],
    'citrus':['citrus canker','greening (huanglongbing)','powdery mildew','anthracnose','leaf miner damage'],
    'turmeric':['rhizome rot','leaf blotch','anthracnose','bacterial leaf streak','thrips damage'],
    'ginger':['soft rot','bacterial wilt','rhizome rot','leaf spot','thrips damage'],
    'garlic':['white rot','downy mildew','bacterial soft rot','rust','stemphylium blight'],
    'coriander':['powdery mildew','stem gall','bacterial leaf spot','alternaria blight','downy mildew'],
    'cumin':['alternaria blight','powdery mildew','downy mildew','bacterial leaf spot','aphid damage']
}

SOIL_TYPES = ['black','red','alluvial','laterite','loamy','sandy','clay']

SYMPTOMS = {
    'blast':'small spindle-shaped lesions with grey centers and brown margins on leaves',
    'brown spot':'circular to oval brown spots with yellow halos on leaves',
    'bacterial leaf blight':'water-soaked margins and wilting of leaf tips',
    'tungro virus':'stunted growth and yellowing of leaves',
    'sheath blight':'lesions on leaf sheaths and lodging of plants',
    'rust':'orange-brown pustules on leaves and stems',
    'powdery mildew':'white powdery growth on leaves and stems',
    'loose smut':'replacement of grains with black spore masses',
    'karnal bunt':'blackening and foul smell in grains',
    'alternaria leaf blight':'dark spots with concentric rings on leaves',
    'stem borer damage':'dead hearts and white ears in panicles',
    'turcicum leaf blight':'long elliptical lesions on leaves',
    'banded leaf and sheath blight':'banded lesions on leaves and sheaths',
    'downy mildew':'fuzzy growth on leaf undersides and stunting',
    'fusarium stalk rot':'wilting and rotting of stalks',
    'boll rot':'rotting of bolls and defoliation',
    'leaf curl virus':'upward curling and thickening of leaves',
    'pink bollworm damage':'damaged bolls and stained lint',
    'bacterial blight':'water-soaked spots turning necrotic',
    'red rot':'reddening of canes and sour smell',
    'smut':'black spore masses in place of flowers',
    'ratoon stunting disease':'stunted growth and poor tillering',
    'leaf scald':'scalded appearance of leaf margins',
    'ring spot':'circular chlorotic spots on leaves',
    'yellow mosaic virus':'yellow-green mosaic mottling on leaves',
    'bacterial pustule':'raised pustules on leaves and pods',
    'frogeye leaf spot':'grey spots with dark margins on leaves',
    'sudden death syndrome':'rapid wilting and death of plants',
    'early blight':'dark spots with concentric rings on leaves',
    'late blight':'water-soaked lesions turning brown/black',
    'bacterial wilt':'wilting of plants with vascular browning',
    'scab':'rough, corky lesions on tubers',
    'purple blotch':'purple lesions with concentric rings on leaves',
    'neck rot':'rotting at the neck region of bulbs',
    'bacterial rot':'soft, mushy rot with foul smell',
    'stemphylium blight':'brown spots with yellow halos on leaves',
    'anthracnose':'sunken lesions with pink spore masses',
    'bacterial leaf spot':'small water-soaked spots turning necrotic',
    'dieback':'drying of twigs and leaves from tips',
    'fruit rot':'soft rotting of fruits',
    'little leaf virus':'small, distorted leaves and stunting',
    'mosaic':'mottled green-yellow patterns on leaves',
    'black rot':'V-shaped lesions at leaf margins',
    'clubroot':'swollen, deformed roots and stunting',
    'yellow vein mosaic':'yellowing of veins and stunting',
    'root-knot nematode':'galls on roots and stunting',
    'leaf spot':'brown spots with or without halos on leaves',
    'stem rot':'rotting of stems and lodging',
    'bud necrosis virus':'necrotic spots on buds and leaves',
    'collar rot':'rotting at collar region and wilting',
    'white rust':'white pustules on leaves and stems',
    'aphid damage':'curling and yellowing due to sap sucking',
    'head rot':'rotting of flower heads',
    'sclerotinia head rot':'white mycelial growth and rotting of heads',
    'grain mold':'discoloration and moldy growth on grains',
    'helminthosporium leaf spot':'oval brown spots on leaves',
    'bacterial leaf streak':'narrow streaks on leaves',
    'wilt':'yellowing and wilting of plants',
    'dry root rot':'dry rotting of roots and wilting',
    'ascochyta blight':'brown spots with dark margins on leaves and pods',
    'botrytis grey mold':'grey fuzzy growth on pods and leaves',
    'sterility mosaic':'bushy growth and no pods',
    'phytophthora blight':'rapid wilting and rotting',
    'pod borer damage':'holes in pods and reduced yield',
    'panama wilt':'yellowing and wilting of leaves',
    'sigatoka leaf spot':'narrow streaks turning necrotic on leaves',
    'banana bunchy top virus':'bunched, stunted leaves at crown',
    'spongy tissue':'spongy, inedible patches in fruit pulp',
    'ring spot virus':'concentric rings and mottling on leaves and fruits',
    'stem canker':'sunken lesions on stems',
    'greening (huanglongbing)':'yellowing of leaves and bitter fruits',
    'leaf miner damage':'serpentine mines on leaves',
    'rhizome rot':'soft rotting of rhizomes with foul smell',
    'leaf blotch':'brown blotches on leaves',
    'thrips damage':'silvering and curling of leaves',
    'soft rot':'mushy, watery rot of rhizomes',
    'white rot':'white mycelial growth on bulbs',
    'stem gall':'swollen galls on stems and petioles'
}

PESTS = {
    'rice':'stem borer, leaf folder, brown planthopper, green leafhopper',
    'wheat':'aphids, armyworm, termites, grasshoppers',
    'maize':'stem borer, fall armyworm, aphids, termites',
    'cotton':'pink bollworm, American bollworm, whitefly, aphids, jassids',
    'sugarcane':'top borer, internode borer, whitefly, termites',
    'soybean':'girdle beetle, leaf folder, semilooper, aphids',
    'tomato':'fruit borer, whitefly, leaf miner, aphids',
    'potato':'aphids, whitefly, cutworm, tuber moth',
    'onion':'thrips, leaf miner, aphids',
    'chilli':'aphids, thrips, fruit borer, mites',
    'brinjal':'shoot and fruit borer, aphids, jassids, whitefly',
    'cabbage':'diamondback moth, aphids, head borer',
    'cauliflower':'diamondback moth, aphids, head borer',
    'okra':'shoot and fruit borer, aphids, jassids, whitefly',
    'groundnut':'aphids, thrips, leaf miner, white grub',
    'mustard':'aphids, painted bug, leaf miner',
    'sunflower':'aphids, capitulum borer, leaf miner',
    'bajra':'shoot fly, stem borer, aphids',
    'jowar':'shoot fly, stem borer, aphids, midge',
    'ragi':'stem borer, aphids, leaf miner',
    'gram':'pod borer, aphids, cutworm, thrips',
    'pigeon pea':'pod borer, pod fly, aphids, thrips',
    'green gram':'pod borer, aphids, whitefly, thrips',
    'black gram':'pod borer, aphids, whitefly, thrips',
    'banana':'pseudostem borer, rhizome weevil, aphids, thrips',
    'mango':'fruit fly, mealybug, scale insects, leaf webber',
    'papaya':'fruit fly, aphids, mites, whitefly',
    'grapes':'thrips, mealybug, flea beetle, berry borer',
    'pomegranate':'fruit fly, thrips, mealybug, aphids',
    'citrus':'fruit fly, leaf miner, psylla, scale insects',
    'turmeric':'rhizome scale, thrips, shoot borer',
    'ginger':'rhizome scale, thrips, shoot borer',
    'garlic':'thrips, onion maggot, aphids',
    'coriander':'aphids, semilooper, leaf miner',
    'cumin':'aphids, leaf miner, pod borer'
}

CATS = [
    'Fertilizer','Disease','Pest','Irrigation','Weather','Soil','Government Scheme',
    'Harvesting','Marketing','Organic Farming','Yield Improvement','Seed Selection',
    'Storage','Post-Harvest','Mechanization','Intercropping','Crop Rotation','Water Conservation',
    'Micronutrients','NPK Management','IPM','Weed Management','Protected Cultivation',
    'Greenhouse','Hydroponics','Carbon Farming','Regenerative Agriculture','GAP','Insurance'
]

FERT = [
    "For {crop}, start with a soil test. In most alluvial/loamy soils, apply 80–120 kg N/ha, 40–60 kg P2O5/ha, and 40–60 kg K2O/ha in splits. At sowing, place full P and K plus 1/3 N near the seed. Top-dress remaining N at tillering/vegetative stage and again at flowering. Add 5–10 t/ha FYM or compost before sowing. Use ZnSO4 (20–25 kg/ha) if deficient. Avoid excessive urea to prevent lodging and disease.",
    "Use 60–100 kg N/ha for {crop} depending on rainfall and soil. Apply basal NPK (12:32:16 or 15:15:15) at 150–200 kg/ha at sowing, then top-dress urea in 2–3 splits. Include 20–25 kg/ha ZnSO4 where soils are alkaline. For irrigated conditions, split N at vegetative, flowering, and pod/fruit setting. In rainfed areas, use slow-release N and mulch to reduce losses.",
    "In {crop}, balanced NPK (e.g., 100:50:50) improves yield and resilience. Apply full P and K at sowing; split N in 2–3 doses. Foliar 19:19:19 (2–3 g/L) at flowering boosts fruit set. Add 4–5 t/ha compost + 20 kg/ha ZnSO4 in Zn-deficient black soils. Avoid late heavy N to reduce lodging and pest risk.",
    "For {crop}, target 120–150 kg N/ha in high-yield zones. Use 50% N at sowing, 25% at tillering, 25% at panicle initiation. Apply 60 kg P2O5 and 40–60 kg K2O basally. In acidic soils, liming (2–5 t/ha) improves P availability. Use 10–15 t/ha FYM for soil health. Foliar 2% urea at flowering can help under stress.",
    "In {crop}, apply 80–120 kg N/ha, 40–60 kg P2O5/ha, 40 kg K2O/ha. Use basal NPK (15:15:15) at 150–200 kg/ha, then top-dress urea twice. Add ZnSO4 (20–25 kg/ha) once in 2–3 years. Include 5–10 t/ha FYM before sowing. In saline soils, prefer gypsum and avoid chloride fertilizers."
]

IRR = [
    "For {crop}, maintain soil moisture at 50–60% field capacity. Use drip or furrow irrigation to save 20–30% water. Avoid waterlogging; ensure drainage in heavy soils. Critical stages: sowing, flowering, and pod/fruit set. In summer, irrigate every 5–7 days; in winter, every 8–10 days.",
    "Use 4–6 irrigations for {crop} depending on soil and rainfall. First irrigation 20–25 days after sowing, then at tillering, flowering, and grain filling. Drip/fertigation saves 30–40% water and improves uniformity. Mulching reduces evaporation. Avoid late heavy irrigation to prevent lodging.",
    "In {crop}, schedule irrigation based on soil type: sandy soils need frequent light irrigation; clay soils need fewer but deeper irrigations. Use tensiometer at 15–20 cm depth; irrigate at −20 to −30 kPa. Avoid drought at flowering to prevent yield loss.",
    "For {crop}, maintain even moisture. Deficit at flowering reduces yield by 20–30%. Use alternate furrow irrigation or drip to improve water use efficiency. In water-scarce areas, adopt zero-till and mulching to conserve moisture.",
    "In {crop}, avoid water stress during pod/fruit development. Use deficit irrigation (70–80% ET) in vegetative stage, then full irrigation at flowering and fruit set. Drain fields within 24 hours after heavy rain to prevent root rot."
]

SOIL_T = [
    "Best soils for {crop} are deep, well-drained loamy to clay loam with pH 6.0–7.5. In black soils, ensure good drainage to avoid root diseases. In red soils, add 4–6 t/ha FYM and 20–25 kg/ha ZnSO4. In sandy soils, increase organic matter and use split fertilizer doses.",
    "For {crop}, aim for soil pH 6.5–7.5. In acidic soils, apply lime (2–5 t/ha) 2–3 months before sowing. In alkaline soils, use gypsum (2–5 t/ha) and sulfur amendments. Build organic carbon (>0.75%) with FYM/compost and green manures.",
    "In {crop}, soil testing every 2–3 years optimizes fertilizer use. Target OC >0.8%, available P >20 kg/ha, available K >200 kg/ha. Use micronutrients (Zn, B, S) based on deficiency symptoms and soil tests.",
    "For {crop}, avoid continuous monocropping. Rotate with legumes to improve N and soil health. Add 5–10 t/ha FYM and practice conservation tillage to enhance infiltration and reduce erosion.",
    "In {crop}, heavy clay soils need raised beds and proper drainage. Sandy soils benefit from mulching and frequent light irrigations. Loamy soils are ideal; maintain OC with crop residues and manures."
]

DIS = [
    "In {crop}, {disease} shows {symptoms}. Prevent by using certified seeds, crop rotation, and balanced NPK. For fungal diseases, spray mancozeb 0.25% or carbendazim 0.1% at first sign. Improve drainage and avoid late evening irrigation. Remove infected debris.",
    "Control {disease} in {crop} with integrated measures: resistant varieties, seed treatment (thiram/carbendazim 2 g/kg), and timely sprays. Avoid excessive nitrogen which increases susceptibility. Use biocontrol (Trichoderma 4–5 g/kg seed) for soil-borne diseases.",
    "For {disease} in {crop}, early detection is key. Symptoms include {symptoms}. Spray recommended fungicides (e.g., propiconazole, tebuconazole) at label doses. Practice field sanitation, avoid water stagnation, and maintain plant spacing for airflow.",
    "In {crop}, {disease} spreads in warm, humid conditions. Use protective sprays (mancozeb 0.25%) before monsoon peaks. Combine with resistant varieties and avoid overhead irrigation. Rotate with non-host crops to break disease cycles.",
    "Manage {disease} in {crop} by removing infected plants, improving drainage, and balanced nutrition. Use copper-based fungicides for bacterial diseases; avoid heavy N. Practice 2–3 year rotations and seed treatment to reduce primary inoculum."
]

PST = [
    "Common pests in {crop} include {pests}. Monitor with pheromone traps (10–12/ha). Use need-based sprays: emamectin benzoate or spinosad for larvae; imidacloprid for sucking pests. Preserve natural enemies; avoid broad-spectrum sprays early.",
    "For {crop}, adopt IPM: pheromone traps, light traps, and bird perches. Spray only when ETL is reached. Use neem oil 3% or NSKE 5% for early infestations. Rotate insecticide groups to prevent resistance.",
    "In {crop}, control {pests} with cultural methods: timely sowing, intercropping, and crop rotation. Use biopesticides (Bt, NPV) where available. Spot-spray outbreaks and avoid prophylactic sprays.",
    "In {crop}, pests like {pests} cause yield loss. Use sticky traps for whiteflies/aphids. Apply recommended insecticides at correct doses. Maintain field hygiene and remove weed hosts.",
    "For {crop}, integrate mechanical (handpicking), biological (Trichogramma), and chemical controls. Avoid tank mixes that harm beneficials. Follow label doses and pre-harvest intervals."
]

WTH = [
    "In {crop}, avoid sowing during heatwaves (>38°C). Use early-morning irrigation and mulch to reduce heat stress. For cold waves, ensure adequate soil moisture and avoid late nitrogen. Watch IMD advisories for rainfall and temperature.",
    "Heavy rain during flowering of {crop} causes pollen wash and yield loss. Ensure drainage, use raised beds, and avoid late nitrogen. If lodging risk exists, reduce N and increase K.",
    "In drought-prone areas, select short-duration {crop} varieties. Use mulching, zero-till, and deficit irrigation. Apply 2% KNO3 foliar to mitigate heat stress. Avoid late sowing in rainfed zones.",
    "For {crop}, high humidity favors fungal diseases. Increase plant spacing, avoid overhead irrigation, and use protective fungicides before monsoon peaks. Use weather-based advisories for spray timing.",
    "In {crop}, unexpected hail can damage canopy. Ensure good K nutrition for resilience. After hail, apply broad-spectrum fungicide to prevent secondary infections and maintain drainage."
]

HRV = [
    "Harvest {crop} at physiological maturity: grains at 20–22% moisture, pods when 80–90% brown. Avoid delayed harvest to reduce shattering and field losses. Use combine harvesters where feasible; dry grains to 12–14% before storage.",
    "For {crop}, harvest in dry weather. Use sharp sickles or mechanical harvesters to minimize losses. Dry produce to safe moisture (grains 12–14%, pulses 10–12%) before storage. Clean and grade before marketing.",
    "In {crop}, early harvest reduces field losses and aflatoxin risk. Dry on clean tarps; avoid direct soil contact. Use moisture meters to ensure safe storage levels. Store in fumigated, rodent-proof structures.",
    "For {crop}, harvest at correct stage to maintain quality. Handle gently to avoid bruising. Sort and grade immediately; pack in clean, dry containers. Avoid evening harvest in high humidity to reduce disease.",
    "In {crop}, timely harvest improves market price. Use mechanical threshers where possible. Dry to safe moisture, clean, and store in hermetic bags or silos to prevent pests and mold."
]

STO = [
    "Store {crop} grains at 12–14% moisture in clean, dry, rodent-proof structures. Treat storage area with malathion dust. Use hermetic bags or PICS bags for pulses. Fumigate with aluminum phosphide if needed, following safety protocols.",
    "For {crop}, ensure produce is dry and clean before storage. Avoid mixing old and new stock. Use neem leaves or botanicals in small stores. Monitor temperature and humidity; aerate if needed.",
    "In {crop}, high moisture leads to mold and mycotoxins. Dry to safe levels, use moisture-proof liners, and keep bags off the floor on pallets. Inspect regularly for pests and dampness.",
    "For {crop}, maintain ventilation in stores. Use insect-proof screens. In humid areas, prefer hermetic storage. Avoid storing near chemicals or fertilizers to prevent contamination.",
    "In {crop}, fumigation should be done by trained personnel. Seal stores properly, use recommended doses, and observe aeration periods before sale or consumption."
]

GOV = [
    "Farmers growing {crop} can benefit from PM-KISAN (₹6,000/year), Kisan Credit Card (subsidized interest), and Soil Health Card (free soil testing). Check with your local agriculture office or CSC for enrollment. Crop insurance under PMFBY is also available.",
    "For {crop}, MSP announcements and procurement vary by state. Register on e-NAM for better market access. FPO membership can improve bargaining power. Explore agri-infrastructure funds for storage and processing.",
    "In {crop}, state schemes may offer seed subsidies, drip irrigation support, and power concessions. Keep Aadhaar, land records, and bank details updated for scheme benefits. Use KCC for working capital and input purchases.",
    "For {crop}, PMFBY provides yield-based insurance at low premium. Enroll through banks or CSC before sowing. Maintain plot-wise records and cooperate during crop cutting experiments for claim settlement.",
    "In {crop}, agri-business ideas can access credit via NABARD and agri-clinics schemes. Explore FPO formation, common facility centers, and market linkage programs. Check state horticulture missions for post-harvest support."
]

ORG = [
    "For organic {crop}, use well-decomposed FYM (10–15 t/ha), vermicompost (2–3 t/ha), and biofertilizers (Rhizobium, PSB, Azotobacter). Avoid synthetic fertilizers and pesticides. Use neem-based products and botanicals for pest control.",
    "In {crop}, adopt crop rotation with legumes, green manures (dhaincha, sunhemp), and mulching. Maintain field sanitation and use resistant varieties. Certification via NPOP/PGS-India adds market value.",
    "For organic {crop}, use Jeevamrut, Panchagavya, and Amritpani as foliar sprays. Manage weeds mechanically and through mulching. Build soil health with diverse rotations and cover crops.",
    "In {crop}, organic systems need strong IPM: traps, biocontrol agents, and botanicals. Ensure adequate K and micronutrients from organic sources. Plan harvest and post-harvest to maintain organic integrity.",
    "For {crop}, organic yields improve over 2–3 years as soil health builds. Use seed treatment with Trichoderma and biofertilizers. Avoid contamination from conventional inputs and maintain buffer zones."
]

MIC = [
    "Zn deficiency in {crop} shows as interveinal chlorosis and stunting. Apply ZnSO4 (20–25 kg/ha) basally or foliar 0.5% ZnSO4 + 0.25% lime. In alkaline soils, band Zn near roots for better uptake.",
    "B deficiency in {crop} causes poor fruit set and hollow stems. Apply borax (10–15 kg/ha) or foliar 0.2% boron at flowering. Avoid overuse; excess B is toxic.",
    "S deficiency in {crop} leads to pale young leaves. Use SSP or gypsum to supply S (20–40 kg/ha). In high-rainfall areas, split S applications to reduce leaching.",
    "Fe deficiency in {crop} shows as interveinal chlorosis in young leaves. Apply Fe-EDDHA foliar (0.5%) or chelated Fe with irrigation. Improve drainage and avoid high pH soils.",
    "Mn deficiency in {crop} causes grey speck and reduced growth. Use MnSO4 foliar (0.2–0.3%) at tillering/vegetative stage. Maintain balanced NPK to improve micronutrient efficiency."
]

NPK = [
    "Balanced NPK in {crop} improves yield and stress tolerance. Use soil test-based doses; typical ranges: N 80–120, P2O5 40–60, K2O 40–60 kg/ha. Split N in 2–3 doses; place P and K basally near seed.",
    "In {crop}, excessive N without K increases lodging and disease. Maintain K at 50–60 kg/ha for stalk strength. Use 19:19:19 foliar at flowering for fruit set. Add FYM 5–10 t/ha for long-term soil health.",
    "For {crop}, P fixation in alkaline soils reduces efficiency. Band P near roots, use SSP or DAP, and maintain pH 6.5–7.5 with amendments. Add Zn and S where deficient.",
    "In {crop}, high K improves water use efficiency and disease resistance. Apply K in splits; avoid late heavy K. Use SOP or MOP based on crop and soil Cl tolerance.",
    "For {crop}, integrated nutrient management combines FYM, biofertilizers, and mineral fertilizers. Target OC >0.8%, balanced NPK, and micronutrients based on soil tests. Avoid blanket recommendations."
]

IPM = [
    "For {crop}, IPM starts with monitoring: pheromone traps, field scouting, and ETL-based sprays. Use biocontrol (Trichogramma, NPV) and botanicals (neem) early. Rotate insecticide groups to delay resistance.",
    "In {crop}, cultural practices (timely sowing, intercropping, crop rotation) reduce pest pressure. Preserve natural enemies by avoiding broad-spectrum sprays. Use spot treatments for outbreaks.",
    "For {crop}, combine mechanical (handpicking), biological (parasitoids), and chemical controls. Calibrate sprayers; apply at correct growth stage. Follow pre-harvest intervals and safety norms.",
    "In {crop}, light traps and bird perches help manage nocturnal pests. Maintain field hygiene and remove weed hosts. Use need-based sprays only when ETL is crossed.",
    "For {crop}, integrate pheromone traps (10–12/ha), NSKE 5%, and targeted insecticides. Avoid prophylactic sprays. Train labor on safe handling and PPE use."
]

WED = [
    "Weeds in {crop} compete for light, water, and nutrients. Use pre-emergence herbicides (pendimethalin 1.0–1.5 kg/ha) followed by one hand weeding at 25–30 DAS. Mulching and intercropping also suppress weeds.",
    "For {crop}, timely weeding (first 30 days) is critical. Use mechanical weeding or recommended herbicides. Avoid late weeding that damages roots. Maintain crop geometry for canopy closure.",
    "In {crop}, integrate cultural (crop rotation, cover crops), mechanical (hoeing), and chemical weed control. Use herbicide-tolerant varieties where available. Rotate herbicide modes of action to prevent resistance.",
    "For {crop}, hand weeding is effective but labor-intensive. Combine with pre-emergence sprays and mulching. Keep field borders clean to reduce weed seed bank.",
    "In {crop}, avoid waterlogging which favors weeds. Use narrow row spacing and early canopy closure to suppress weeds. Scout fields regularly and remove weeds before seed set."
]

YLD = [
    "To improve yield in {crop}, use certified seeds, optimal plant population, and balanced NPK. Manage pests/diseases proactively and avoid water stress at flowering. Harvest at correct maturity and dry properly.",
    "For {crop}, target 10–15% higher yield by adopting improved varieties, micro-irrigation, and INM. Ensure timely sowing, proper spacing, and timely weeding. Use foliar nutrients at critical stages.",
    "In {crop}, yield gaps arise from poor plant stand, nutrient imbalance, and pest damage. Use soil test-based fertilizers, IPM, and timely irrigation. Record field operations for continuous improvement.",
    "For {crop}, integrate agronomy and protection: quality seeds, seed treatment, balanced fertilizers, and need-based sprays. Avoid late sowing and water stress during reproductive stages.",
    "In {crop}, precision practices (line sowing, fertigation, leaf color chart for N) raise yields. Use crop-specific advisories and weather-based inputs. Maintain field records for next season planning."
]

SED = [
    "Use certified seeds of {crop} for uniform germination and higher yield. Treat seeds with thiram/carbendazim (2 g/kg) or bio-agents (Trichoderma 4–5 g/kg). Store seeds in cool, dry place in moisture-proof bags.",
    "For {crop}, select seeds from healthy plants, free from disease. Maintain seed purity and avoid mixing varieties. Use seed replacement every 2–3 years for best results.",
    "In {crop}, seed rate varies by method: line sowing needs less seed than broadcasting. Calibrate seed drills for uniform spacing. Avoid old or damaged seeds.",
    "For {crop}, seed treatment reduces seed-borne diseases. Use hot water treatment or solarization for some crops. Label bags with variety, lot, and date.",
    "In {crop}, procure seeds from certified agencies. Check germination before sowing; aim for >85%. Avoid storage in humid conditions."
]

MEC = [
    "For {crop}, mechanization (seed drills, rotavators, harvesters) reduces cost and timeliness losses. Calibrate equipment for correct seed rate and spacing. Maintain machines regularly for safety and efficiency.",
    "In {crop}, use power tillers or tractors with appropriate implements. Adopt zero-till where feasible to save time and fuel. Train operators on safe handling and maintenance.",
    "For {crop}, combine harvesters reduce field losses but require proper adjustment. Use moisture meters to decide harvest time. Store machinery under cover to extend life.",
    "In {crop}, drip fertigation systems improve input efficiency. Use filters and pressure regulators; flush lines regularly. Schedule irrigation based on soil moisture and crop stage.",
    "For {crop}, post-harvest mechanization (threshers, graders, dryers) improves quality and reduces losses. Clean and maintain equipment after each season."
]

INC = [
    "Intercropping {crop} with legumes improves soil N and reduces pest pressure. Use compatible row ratios (e.g., 2:1 or 4:2). Manage nutrients and irrigation for both crops.",
    "For {crop}, intercropping with short-duration vegetables increases land productivity. Plan sowing dates to avoid competition. Use balanced fertilizers and timely weeding.",
    "In {crop}, intercropping breaks pest cycles and improves biodiversity. Select crops with different canopy heights and root depths. Monitor for pest shifts and adjust management.",
    "For {crop}, relay cropping or sequential cropping maximizes land use. Maintain soil fertility with FYM and biofertilizers. Use crop-specific herbicides carefully.",
    "In {crop}, intercropping with aromatic or medicinal plants can add income. Ensure market linkages and proper spacing. Manage water and nutrients for both crops."
]

ROT = [
    "Rotate {crop} with non-host crops (e.g., legumes) to break disease and pest cycles. Include green manures to improve soil health. Plan 2–3 year rotations based on soil and water availability.",
    "For {crop}, avoid continuous monoculture. Rotate with cereals/legumes to balance nutrients. Use residue incorporation and cover crops to build organic matter.",
    "In {crop}, rotation reduces soil-borne diseases and weeds. Select crops with different nutrient demands. Maintain field records to plan rotations effectively.",
    "For {crop}, integrate livestock or agroforestry in rotations for diversification. Use manure and compost to recycle nutrients. Monitor soil tests to adjust rotations.",
    "In {crop}, plan rotations around water availability. Use drought-tolerant crops in dry years and high-value crops in wet years. Maintain soil cover year-round."
]

WAT = [
    "Conserve water in {crop} with mulching, zero-till, and micro-irrigation. Schedule irrigation based on soil moisture. Avoid flood irrigation in sandy soils.",
    "For {crop}, use alternate wetting and drying (AWD) where feasible. Recycle field drainage and harvest rainwater in ponds. Maintain field bunds and channels.",
    "In {crop}, deficit irrigation at vegetative stage saves water without yield loss. Use crop residues as mulch to reduce evaporation. Monitor weather forecasts to avoid irrigation before rain.",
    "For {crop}, line canals and use pipes to reduce conveyance losses. Adopt laser leveling for uniform water distribution. Train farmers on efficient irrigation practices.",
    "In {crop}, avoid over-irrigation which leaches nutrients and promotes diseases. Use tensiometers or soil moisture sensors for precise scheduling. Maintain drainage to prevent waterlogging."
]

PRO = [
    "Protected cultivation (shade nets, low tunnels) in {crop} reduces pest and weather damage. Use drip fertigation and mulch. Monitor temperature and humidity to prevent diseases.",
    "For {crop}, greenhouses enable year-round production. Use insect-proof nets, drip irrigation, and balanced fertigation. Train labor on climate management and IPM.",
    "In {crop}, hydroponics saves water and nutrients. Maintain EC and pH in recommended ranges. Use sterile media and prevent root diseases with sanitation.",
    "For {crop}, polyhouses improve yield and quality. Install fans and foggers for climate control. Use reflective mulch and trellising for better light distribution.",
    "In {crop}, protected cultivation reduces pesticide use. Combine with biological controls and hygiene. Plan crop cycles to match market demand."
]

CAR = [
    "Carbon farming in {crop} includes no-till, cover crops, and residue retention. Measure soil organic carbon and adopt practices that increase it. Explore carbon credits via verified programs.",
    "For {crop}, agroforestry and perennial systems sequester more carbon. Use diverse rotations and organic amendments. Maintain records for potential carbon income.",
    "In {crop}, reduced tillage and mulching improve SOC and water retention. Avoid burning residues; incorporate or use for mulch. Align with national carbon initiatives.",
    "For {crop}, integrate livestock and manure management to recycle nutrients and carbon. Use compost and biochar where feasible. Monitor soil health indicators.",
    "In {crop}, precision fertilizer use reduces N2O emissions. Use urease inhibitors and split N applications. Combine with renewable energy for irrigation."
]

REG = [
    "Regenerative agriculture in {crop} focuses on soil health, biodiversity, and water. Use cover crops, minimal tillage, and diverse rotations. Track outcomes with soil tests and yield records.",
    "For {crop}, integrate trees, shrubs, and perennials to enhance resilience. Use organic amendments and biological pest control. Build local knowledge and community practices.",
    "In {crop}, regenerative practices improve long-term profitability. Reduce external inputs, increase on-farm nutrient cycling, and maintain soil cover. Document practices for learning and scaling.",
    "For {crop}, regenerative systems need patient investment. Start with pilot plots, measure soil carbon and yields, and scale gradually. Engage with FPOs for collective action.",
    "In {crop}, combine traditional knowledge with modern science for regenerative outcomes. Use participatory trials and share results with neighbors. Seek technical support from agriculture departments."
]

GAP_T = [
    "Good Agricultural Practices (GAP) in {crop} include record-keeping, safe pesticide use, and traceability. Follow pre-harvest intervals and maintain field hygiene. Adopt GAP for market access and premiums.",
    "For {crop}, GAP covers seed quality, soil health, water management, and worker safety. Use protective gear, calibrate sprayers, and keep input records. Train labor on safe handling.",
    "In {crop}, GAP improves product quality and reduces residues. Implement standard operating procedures for spraying, harvesting, and packing. Seek certification where markets demand it.",
    "For {crop}, GAP aligns with food safety and export requirements. Maintain field maps, input logs, and harvest records. Use clean containers and cold chain where needed.",
    "In {crop}, GAP reduces risks and builds buyer trust. Regularly audit practices and update SOPs. Engage with buyers to understand quality standards."
]

INS = [
    "Crop insurance (PMFBY) for {crop} covers yield losses due to weather, pests, and diseases. Enroll before sowing through banks or CSC. Cooperate during crop cutting experiments for claim settlement.",
    "For {crop}, insurance complements good agronomy. Keep plot-wise records and photos of damage. Understand exclusions and claim processes. Pay premiums on time.",
    "In {crop}, weather-based insurance can provide quick payouts. Link with local meteorological data. Use insurance as part of risk management, not a substitute for good practices.",
    "For {crop}, explore state-specific insurance top-ups and micro-insurance. Maintain communication with insurance agents. File claims promptly with required documents.",
    "In {crop}, combine insurance with savings and credit for resilience. Diversify crops and income sources. Seek advisory on risk reduction and insurance options."
]

MAP = {
    'Fertilizer':FERT,'Disease':DIS,'Pest':PST,'Irrigation':IRR,'Weather':WTH,'Soil':SOIL_T,
    'Government Scheme':GOV,'Harvesting':HRV,'Marketing':GOV,'Organic Farming':ORG,
    'Yield Improvement':YLD,'Seed Selection':SED,'Storage':STO,'Post-Harvest':STO,
    'Mechanization':MEC,'Intercropping':INC,'Crop Rotation':ROT,'Water Conservation':WAT,
    'Micronutrients':MIC,'NPK Management':NPK,'IPM':IPM,'Weed Management':WED,
    'Protected Cultivation':PRO,'Greenhouse':PRO,'Hydroponics':PRO,'Carbon Farming':CAR,
    'Regenerative Agriculture':REG,'GAP':GAP_T,'Insurance':INS
}

QUESTIONS = [
    "What is the best fertilizer dose and schedule for {crop} in {soil} soil?",
    "How do I manage {disease} in {crop}? What are the symptoms and spray schedule?",
    "Which irrigation method saves the most water for {crop} without reducing yield?",
    "What soil type and pH are ideal for {crop}, and how do I improve my soil?",
    "How can I control {pests} in {crop} using IPM and reduce chemical sprays?",
    "What weather conditions harm {crop} and how do I protect my crop?",
    "When and how should I harvest {crop} to get maximum yield and quality?",
    "How do I store {crop} grains safely to avoid pests and mold?",
    "Which government schemes can I use for {crop} cultivation and marketing?",
    "How do I practice organic farming in {crop} without losing yield?",
    "What are the signs of Zn, B, or S deficiency in {crop} and how do I correct them?",
    "What is a good NPK plan for {crop} to avoid lodging and disease?",
    "How do I implement IPM in {crop} step by step?",
    "What are effective weed control methods for {crop} that are safe and cheap?",
    "How can I increase yield in {crop} with better agronomy and protection?",
    "How do I select and treat seeds for {crop} to improve germination?",
    "Which machines or implements are useful for {crop} to save labor and time?",
    "What are good intercropping options with {crop} to increase income?",
    "How should I plan crop rotation with {crop} to improve soil health?",
    "What water conservation practices work best for {crop} in my area?",
    "How do I set up protected cultivation or greenhouse for {crop}?",
    "What carbon farming practices can I adopt in {crop} fields?",
    "How do I move towards regenerative agriculture in {crop}?",
    "What GAP should I follow for {crop} to meet market and export standards?",
    "How does crop insurance work for {crop} and how do I claim?"
]

rows = []
used = set()
cats_cycle = itertools.cycle(CATS)
crop_cycle = itertools.cycle(CROPS)
TARGET = 1600

while len(rows) < TARGET:
    crop = next(crop_cycle)
    cat = next(cats_cycle)
    disease = random.choice(DISEASES[crop])
    soil = random.choice(SOIL_TYPES)
    q = random.choice(QUESTIONS).format(crop=crop, disease=disease, soil=soil, pests=PESTS[crop])
    ans = random.choice(MAP[cat]).format(crop=crop, disease=disease, symptoms=SYMPTOMS.get(disease, "leaf spots and wilting"), pests=PESTS[crop])
    if len(ans.split()) < 40:
        ans += " Keep records of inputs and yields each season to refine your plan."
    if len(ans.split()) > 120:
        ans = " ".join(ans.split()[:115]) + "."
    key = (cat, crop, q)
    if key in used:
        continue
    used.add(key)
    kws = sorted(set([crop, cat.lower().replace(" ", "_"), disease, soil, "india", "farming", "agriculture"]))
    rows.append([cat, crop, disease, q, ans, ",".join(kws)])

path = "agriculture_knowledge.csv"
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Category", "Crop", "Disease", "Question", "Answer", "Keywords"])
    w.writerows(rows)

print("Generated:", path, "rows:", len(rows))