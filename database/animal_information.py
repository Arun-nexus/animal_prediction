animals_info = {
    "lion": "The lion is one of Africa’s most powerful apex predators, known for its muscular build and, in males, a distinctive mane that signals strength and maturity. Lions live in social groups called prides, consisting of related females, their cubs, and a few males. Females perform most of the hunting, using coordination and flanking techniques to bring down prey such as zebras and wildebeests. A lion’s roar can travel up to eight kilometers and is used to defend territory and communicate with the pride. Ecologically, lions play an important role in regulating herbivore populations and maintaining balance in the savanna ecosystem. In machine learning datasets, lions offer high-variance features due to mane texture, lighting changes, and pose diversity, making them valuable for training robust classification models. Despite their strength, lions face threats from habitat loss and conflict with humans, leading to their vulnerable conservation status.",


    "tiger": "Tigers are the largest members of the cat family, instantly recognizable due to their bright orange coats and bold black stripes. These stripes act as camouflage in dense forests and grasslands. Tigers are solitary predators, relying on stealth and explosive power to ambush prey such as deer and wild boars. They are also excellent swimmers, often cooling off in water and using rivers as pathways. Every tiger has a unique stripe pattern, which helps in individual identification. In machine learning datasets, tiger images are useful for contrast-based feature learning because of their sharp stripe boundaries. Tigers are classified as endangered due to poaching, habitat destruction, and fragmentation. Conservation efforts focus on protecting tiger reserves, reducing human conflict, and preventing illegal wildlife trade to ensure the survival of this iconic species.",

    "elephant":  "Elephants are the largest land mammals, known for their intelligence, memory, and social complexity. Their trunks serve as highly versatile tools used for drinking, smelling, grabbing, signaling, and even showing affection. Elephants live in matriarchal herds led by the oldest female, who guides the group based on her experience and memory of water routes. They communicate using low-frequency rumbles that travel several kilometers. Ecologically, elephants shape their environment by uprooting trees, digging waterholes, and dispersing seeds. In image datasets, their distinct size, wrinkled skin, tusks, and trunk shape offer clear visual features for ML models. Despite their importance, elephants face threats from poaching, shrinking habitats, and human-animal conflict, making conservation efforts essential for their long-term survival.",

    "leopard": "The leopard is a highly adaptable big cat known for its golden coat covered with black rosettes. It is an exceptional climber and often drags its prey up trees to avoid competition from lions and hyenas. Leopards inhabit diverse environments, from forests and savannas to mountains. They are stealthy predators with excellent night vision, relying on speed and precision to hunt antelopes, birds, and smaller mammals. In image datasets, their rosette patterns help train models for fine-grained species differentiation. Leopards face risks from habitat encroachment and illegal hunting, making conservation efforts crucial to maintaining their populations in the wild.",

    "black_panther": "A black panther is not a separate species but a melanistic variant of leopards or jaguars. Their dark coat results from excess melanin, although the typical rosette markings remain faintly visible under certain lighting conditions. Black panthers excel in dense forests where their dark fur helps them blend seamlessly into shadows, aiding in stealth-based hunting. They are solitary, primarily nocturnal animals with exceptional climbing and jumping abilities. In machine learning datasets, black panthers provide valuable low-light and dark-texture recognition challenges. They face the same threats as their parent species, primarily habitat loss and illegal poaching.",

    "african_elephant":"African elephants are larger than Asian elephants and have big fan-shaped ears resembling the African continent. Their tusks grow throughout life and are used for digging, stripping bark, and defense. African elephants are ecosystem engineers, creating water access points during dry seasons and dispersing seeds across vast distances. In ML datasets, their wrinkled skin texture and massive shape make them visually distinctive. Despite their protective nature, they face heavy threats from ivory poaching and habitat fragmentation. Conservation programs focus on anti-poaching operations, expanding safe migration corridors, and supporting community-based wildlife management.",

    "bengal_tiger": "The Bengal tiger is the most widespread tiger subspecies, commonly found in India and Bangladesh. It features a bright orange coat with dense black stripes and thrives in habitats ranging from tropical forests to mangrove wetlands such as the Sundarbans. Bengal tigers are powerful ambush predators with strong swimming skills. In ML datasets, they contribute to subspecies-level classification tasks because of their visually distinct stripe density and body shape. Despite being relatively numerous compared to other tiger subspecies, they remain endangered due to poaching, territorial loss, and human-wildlife conflict.",


    "wolf": "Wolves are intelligent, social animals that live in structured packs with alpha, beta, and subordinate members. They communicate using howls, body language, and scent marking. Wolves are endurance-based hunters capable of chasing prey such as deer over long distances. Their coordinated pack behavior allows them to take down animals much larger than themselves. In machine learning datasets, distinguishing wolves from similar dog breeds can be challenging due to overlapping features. Wolves face threats from habitat destruction and conflict with farmers, but conservation efforts have helped restore populations in many regions.",


    "fox": "Foxes are small, adaptable carnivores known for their pointed ears, sharp facial features, and bushy tails. They thrive in forests, grasslands, deserts, and even urban environments. Foxes are solitary hunters and rely on their excellent hearing to detect prey like rodents and birds. They use a wide range of vocal calls and body language for communication. In image datasets, foxes contribute to class diversity due to their varied coat colors and distinctive body shape. Although fox populations remain stable, they face risks from disease, habitat loss, and road accidents.",


    "jaguar":"The jaguar is the largest cat species in the Americas, recognizable by its muscular build and rosette patterns with central spots. Unlike most big cats, jaguars often kill with a powerful skull-crushing bite. They prefer dense rainforests, wetlands, and riverbanks. Jaguars are strong swimmers, frequently hunting aquatic animals as well as larger mammals. In ML datasets, distinguishing jaguar rosettes from leopard rosettes is an important fine-grained learning challenge. Jaguars are near threatened due to habitat destruction, illegal poaching, and fragmentation of forest corridors.",

    "white_tiger":  "White tigers are a rare genetic variant of Bengal tigers, resulting from a recessive gene that causes white fur with black stripes. They are not albino; their eyes are typically blue. Most white tigers exist in captivity where inbreeding is common, often resulting in health issues. In ML datasets, white tigers introduce unique color-based contrast variations that challenge classification models. They do not form a wild breeding population and are primarily maintained in zoos, where ethical concerns remain about their long-term health and genetic diversity."
    ,

    "gray_wolf":  "The gray wolf is the largest and most widespread wolf species. They have thick fur coats that vary in color from white to black. Gray wolves live in tightly bonded packs that work cooperatively to hunt large prey such as elk and deer. Their communication includes howling, facial expressions, and scent marking. In ML datasets, distinguishing gray wolves from domestic dogs requires models to learn subtle differences in skull shape, eye placement, and coat texture. Habitat loss, hunting, and livestock conflict pose ongoing threats, but conservation initiatives have helped some populations recover."
    ,

    "zebra": "Zebras are herbivorous mammals famous for their black-and-white stripes, which act as natural camouflage and may help confuse predators. Each zebra has a unique stripe pattern, similar to a fingerprint. Zebras live in herds and migrate long distances across African grasslands in search of food and water. They rely on strong senses and alert behavior to avoid predators. In ML datasets, zebra stripes provide high-contrast patterns ideal for training classification models on texture recognition. Threats include habitat loss and hunting, though some species remain relatively stable."
    ,

    "deer": "Deer are graceful herbivores found across forests, grasslands, and wetlands. Many male deer species grow antlers, which are shed and regrown annually. Deer rely on acute hearing, sharp vision, and quick reflexes to evade predators. They primarily feed on grass, leaves, and bark. In ML datasets, deer help models generalize across natural backgrounds with trees, grass, and open fields. Threats to deer populations include habitat loss, hunting, and road accidents, although many species remain common worldwide."
    ,

    "bear":  "Bears are large omnivorous mammals found in forests, mountains, and tundras. They have strong limbs, thick fur, and an excellent sense of smell. Depending on the species, their diet can include fruits, fish, insects, honey, and small mammals. Some bears, like the brown bear, hibernate during winter months to conserve energy. In image datasets, bear species add complexity because of size differences, fur color variation, and diverse habitats. Major threats to bears include climate change, habitat destruction, and human-wildlife conflict.",

    "cheetah":  "The cheetah is the fastest land animal, capable of reaching speeds up to 100 km/h in short bursts. Its slender body, long legs, and lightweight frame are built for acceleration. Cheetahs have distinctive black 'tear marks' under their eyes, which help reduce glare while hunting during the day. Unlike most big cats, they rely on speed instead of strength, targeting small to medium-sized prey such as gazelles. They do not roar but produce unique chirping and purring sounds. In image datasets, cheetahs offer strong pattern-recognition value due to their evenly spaced black spots and sleek build. Cheetahs face threats from habitat loss, declining prey populations, and conflict with farmers, making conservation essential for their survival.",

    "hyena": "Hyenas are intelligent carnivores known for their strong jaws, powerful bite force, and unique vocalizations that resemble laughter. They live in matriarchal clans led by dominant females. Hyenas are often misunderstood as scavengers, but they are excellent hunters capable of coordinating attacks on large prey. Their digestive systems allow them to consume bones, skin, and other tough materials. In machine learning datasets, hyenas contribute diverse shapes and fur textures that help models learn multi-species recognition. Despite their adaptability, hyenas face threats from habitat reduction and conflict with human settlements."
    ,

    "gorilla":  "Gorillas are the largest primates and share a significant amount of DNA with humans. They live in social groups led by a dominant silverback male. Gorillas are gentle, intelligent, and primarily herbivorous, feeding on fruits, leaves, and stems. Their communication includes chest-beating, vocal calls, and facial expressions. In ML datasets, gorillas provide strong high-level features such as muscular body structure, facial contours, and large silhouettes. Threats include poaching, habitat destruction, and disease transmission, making them critically endangered in many regions."
    ,

    "chimpanzee":  "Chimpanzees are highly intelligent primates known for tool use, problem-solving skills, and complex social structures. They live in large communities and communicate using gestures, vocalizations, and facial expressions. Chimpanzees are omnivorous and have strong climbing abilities. Their behavioral diversity makes them valuable subjects in cognitive research. In datasets, distinguishing chimpanzees from gorillas or monkeys helps models learn morphological differences. Threats include habitat loss and hunting, placing many populations at risk."
    ,

    "hippopotamus":"The hippopotamus is a large semi-aquatic mammal found in rivers and lakes across Africa. Despite their bulky appearance, hippos are extremely aggressive and fast, especially in water. They spend most of the day submerged to keep their skin cool and come out at night to graze. Hippos have razor-sharp tusks and powerful jaws capable of causing serious damage. In ML datasets, their massive shape and smooth, hairless skin create clear visual boundaries for classification. Habitat loss and territorial conflicts with humans threaten their survival."
    ,

    "rhinoceros": "Rhinoceroses are large herbivores known for their thick skin and one or two horns made of keratin. They have poor eyesight but excellent smell and hearing. Rhinos are generally solitary and feed on grass, leaves, and shoots. In ML datasets, rhinos stand out due to their heavy build and unique horn structure. Sadly, rhinos face extreme threats from poaching driven by illegal horn trade, pushing several species to critically endangered status."
    ,

    "buffalo":  "Buffaloes are large bovines commonly found in Africa and Asia. African Cape buffaloes are known for their unpredictable nature and strong herd instincts. They can be extremely dangerous when threatened. Buffaloes primarily feed on grasses and rely on group defense to protect themselves from predators like lions. In machine learning datasets, buffalo images help models learn large herbivore differentiation. Their major threats include disease, habitat loss, and hunting."
    ,

    "camel":  "Camels are desert-adapted mammals known for their humps, which store fat used for energy. Their long legs, padded feet, and ability to withstand extreme heat make them perfectly suited for arid environments. Camels can go days without water and rehydrate quickly when needed. They have long eyelashes and closable nostrils to protect against sandstorms. In datasets, camels provide unique silhouettes and textures. Threats include habitat changes and overexploitation in some regions."
    ,

    "giraffe":"The giraffe is the tallest land animal, easily identified by its long neck, long legs, and unique coat patterns. Their height allows them to feed on tree foliage unreachable by other herbivores. Each giraffe's spot pattern is unique, aiding identification. They are generally peaceful animals but can deliver powerful kicks when threatened. In ML datasets, giraffes offer strong geometric features due to their unusual body proportions. Threats include habitat fragmentation and illegal hunting."
    ,

    "horse":  "Horses are strong, fast mammals domesticated thousands of years ago for transport, agriculture, and companionship. They have powerful legs, excellent balance, and strong social behavior within herds. Horses communicate through body language, ear movements, and vocal expressions. In machine learning datasets, variations in breed, color, and body shape provide valuable diversity for classification tasks. Modern threats to wild horse populations include habitat reduction and human encroachment."
    ,

    "donkey":  "Donkeys are hardy, domesticated animals known for their strength, endurance, and ability to survive in harsh environments. They are smaller than horses but more durable, often used for carrying loads and transportation. Donkeys are intelligent and cautious, which is sometimes mistaken for stubbornness. In datasets, donkeys contribute variety through coat textures and body proportions. Threats include habitat loss and neglect in regions where they are still used as working animals."
    ,

    "goat":  "Goats are highly adaptable domestic animals found in nearly every region of the world. They are curious, agile, and capable climbers, often seen navigating steep terrain. Goats feed on grass, shrubs, and leaves. Their playful nature and varied coat colors make them visually diverse in datasets. Goats provide milk, meat, and fiber, making them essential livestock in many cultures. Threats include disease and lack of veterinary care in rural areas."
    ,

    "sheep":"Sheep are domesticated herbivores valued for their wool, meat, and milk. They live in flocks and exhibit strong social behavior, often following a leader. Sheep have thick fleece that protects them from cold climates. In ML datasets, sheep images help models learn texture recognition because of their wool patterns. Predators, disease, and poor grazing management pose risks to sheep populations worldwide."
    ,

    "kangaroo":  "Kangaroos are marsupials native to Australia, known for their powerful hind legs and ability to move through jumping. They carry their young, called joeys, in a pouch. Kangaroos feed on grass and vegetation and travel in groups called mobs. In datasets, their unique posture and strong silhouette make them easy for models to classify. Kangaroo populations generally remain stable, though vehicle collisions and habitat changes affect certain regions."
    ,

    "koala": "Koalas are tree-dwelling marsupials native to Australia, known for their round faces, fluffy ears, and calm temperament. They feed almost exclusively on eucalyptus leaves, which provide low nutrition, resulting in their slow lifestyle. Koalas sleep up to 20 hours a day. In machine learning datasets, koalas contribute distinct facial features and fur textures. Threats to koalas include habitat destruction, wildfires, and disease such as chlamydia, putting many populations at risk."
    ,
    "panda":"The giant panda is a black-and-white bear native to China, known for its round face and gentle appearance. Despite belonging to the carnivore family, pandas primarily eat bamboo, consuming several kilograms per day. They are solitary animals and use scent markings to communicate territory boundaries. Pandas spend most of their time feeding or resting due to the low nutritional value of bamboo. In ML datasets, pandas offer high-contrast color patterns that make them easy to classify. Their biggest threats include habitat loss and low reproduction rates, making conservation programs essential for their survival."
    ,

    "polar_bear":  "The polar bear is the largest land carnivore, adapted for life in the Arctic. Its thick white fur and fat layer provide insulation, while large paws help it walk on ice. Polar bears are powerful swimmers and primarily hunt seals by waiting near breathing holes. In datasets, their snowy background often challenges models due to low color variation. Climate change and melting sea ice pose severe threats, making the species vulnerable to decline."
    ,

    "red_panda": "Red pandas are small, tree-dwelling mammals native to the Himalayas and China. They have reddish-brown fur, a long ringed tail, and a cat-like face. Red pandas are expert climbers and feed mainly on bamboo along with fruits and insects. Their shy and nocturnal nature makes them rarely seen in the wild. In ML datasets, their distinct coloration and adorable appearance make them easy targets for classification. Habitat loss and human encroachment have pushed them to endangered status."
    ,

    "crocodile": "Crocodiles are large aquatic reptiles with powerful jaws, armored bodies, and strong tails. They inhabit rivers, lakes, and wetlands and are ambush predators capable of explosive attacks. Their sensory organs allow them to detect vibrations from prey in the water. In ML datasets, crocodiles add unique reptilian textures and long-body features. Major threats include habitat loss and hunting for leather, though many populations remain stable."
    ,

    "alligator":  "Alligators are large reptiles similar to crocodiles but distinguishable by their broader snouts and different tooth alignment. They live in freshwater swamps, rivers, and marshes. Alligators are opportunistic predators that feed on fish, birds, and small mammals. In ML datasets, telling apart alligators and crocodiles helps models learn fine-grained differences. Conservation efforts have helped many alligator populations recover from past hunting pressures."
    ,

    "snake":  "Snakes are limbless reptiles found in nearly every habitat except extreme cold regions. They move using muscular contractions and rely heavily on chemical senses through their forked tongues. Some species are venomous, while others kill prey by constriction. In datasets, snake images challenge models due to long, flexible shapes and varied patterns. Threats include habitat loss, human fear-driven killing, and the illegal pet trade."
    ,

    "lizard": "Lizards are a diverse group of reptiles with thousands of species worldwide. They range from small geckos to large monitor lizards. Many have the ability to detach their tails when threatened. Lizards rely on sunlight to regulate body temperature and typically feed on insects. In ML datasets, their scale patterns and wide morphological variety improve multi-class learning. Habitat loss and urbanization pose risks to many species."
    ,

    "eagle": "Eagles are large birds of prey with sharp talons, keen eyesight, and powerful flight. They typically hunt fish, small mammals, and birds. Eagles build massive nests and often reuse them for years. Their distinctive broad wings make them easily recognizable in flight. In ML datasets, eagles contribute strong silhouette-based features. Many species face threats from habitat loss and pollution, though conservation efforts have helped stabilize some populations."
    ,

    "owl": "Owls are nocturnal birds known for their silent flight, forward-facing eyes, and exceptional hearing. Their rotating heads and camouflage plumage help them hunt rodents and insects at night. Owls communicate using hoots and screeches. In datasets, their round faces and large eyes create unique classification features. Threats include habitat loss and rodenticide poisoning, which reduce prey availability."
    ,

    "parrot": "Parrots are colorful, intelligent birds found in tropical and subtropical regions. They are known for their curved beaks, clawed feet, and ability to mimic sounds. Parrots feed on seeds, fruits, and nuts. Their bright plumage makes them highly visible in ML datasets, aiding classification tasks. Unfortunately, illegal pet trade and habitat destruction have caused declines in many species."
    ,

    "penguin": "Penguins are flightless birds adapted for life in cold waters. Their streamlined bodies and strong flippers make them excellent swimmers. Penguins live in colonies and feed on fish, squid, and krill. Their black-and-white coloration provides camouflage underwater. In ML datasets, penguins offer distinctive shapes and environments. Climate change and overfishing pose major threats to many penguin populations."
    ,

    "flamingo": "Flamingos are tall wading birds known for their bright pink plumage, long legs, and S-shaped necks. Their color comes from carotenoid pigments in their diet. Flamingos feed by filtering algae and small animals from water. They live in large colonies and perform synchronized group displays. In datasets, their unique shape and color provide strong visual features. Habitat loss and pollution threaten many flamingo groups."
    ,

    "duck": "Ducks are waterfowl found in ponds, lakes, rivers, and wetlands. They have broad bills, webbed feet, and waterproof feathers. Ducks are omnivorous, feeding on plants, insects, and small aquatic animals. In ML datasets, their diverse colors and shapes add variability for classification. Threats include pollution, habitat destruction, and hunting in certain regions."
    ,

    "hen":  "Hens are domesticated birds raised worldwide for eggs and meat. They live in flocks and communicate through clucks and chirps. Hens scratch the ground for seeds and insects. Their feathers vary widely in color depending on the breed. In ML datasets, hens are important for agricultural classification tasks. Threats are minimal due to domestication, though disease outbreaks can impact populations."
    ,

    "rooster": "Roosters are male chickens known for their loud crowing and distinctive feather structures, especially long tail feathers and bright combs. They play a protective role in flocks by alerting hens to danger. Roosters are more colorful and aggressive compared to hens. In ML datasets, they add class diversity through shape and color variation. Being domesticated animals, their biggest threats relate to disease and poor livestock management rather than wild predators."
    ,

    "swan":  "Swans are large, elegant waterbirds known for their long curved necks and graceful movement on water. They are strong swimmers and powerful fliers, often migrating long distances. Swans are highly territorial and form long-term monogamous pairs. They feed on aquatic plants, insects, and small fish, using their long necks to reach underwater vegetation. In datasets, swans offer unique silhouette features and white plumage, which challenges models in bright environments. Threats include habitat loss, pollution, and conflict with human activities in lakes and wetlands."
    ,

    "peacock": "The peacock is famous for its spectacular tail feathers, which males fan out in vibrant displays to attract females. The iridescent colors result from microscopic structures that reflect light. Peacocks are ground-dwelling birds that feed on seeds, insects, and small reptiles. In ML datasets, their highly distinctive patterns make classification straightforward. Peacocks face habitat disturbance and predation, though they remain stable in many regions due to cultural protection."
    ,

    "turkey":  "Turkeys are large birds native to North America, known for their fan-shaped tails and wattles. Male turkeys display elaborate courtship behavior, puffing up their feathers and producing gobbling calls. They feed on seeds, berries, insects, and small amphibians. In datasets, turkeys contribute variety through their textured plumage and unique head structure. Threats include habitat loss and hunting, though domesticated populations are widespread."
    ,

    "frog": "Frogs are amphibians with smooth skin, strong hind legs, and the ability to live both in water and on land. They undergo metamorphosis from tadpoles to adults. Frogs play a vital role in controlling insect populations. In ML datasets, frogs challenge models due to small size, varied colors, and wet reflective skin patterns. They face major threats from pollution, habitat drying, and deadly fungal diseases."
    ,

    "toad": "Toads are amphibians similar to frogs but with drier, bumpier skin and shorter legs. They prefer land over water and move through short hopping or crawling. Toads feed on insects and rely on chemical secretions in their skin to deter predators. In datasets, toads add class diversity with their rough textures. Threats include habitat destruction and water pollution, which disrupt breeding cycles."
    ,

    "tortoise":  "Tortoises are slow-moving reptiles with hard, dome-shaped shells. They are strictly land-dwelling and feed on grasses, leaves, and fruits. Tortoises can live for more than 100 years due to slow metabolism and sturdy physiology. In ML datasets, their rigid shapes and textured shells provide clear classification features. They face threats from habitat loss, illegal pet trade, and road accidents."
    ,

    "sea_turtle":  "Sea turtles are marine reptiles that spend most of their lives in the ocean, returning to beaches only to lay eggs. They have streamlined shells and powerful flippers for long-distance swimming. Sea turtles feed on jellyfish, seagrass, and algae depending on the species. In datasets, their underwater backgrounds and smooth shell shapes create unique training samples. Major threats include plastic pollution, fishing nets, and beach habitat destruction."
    ,

    "shark":  "Sharks are apex predators of the ocean, with sharp teeth, powerful swimming capability, and highly developed sensory systems. They detect vibrations and electrical signals to locate prey. Shark species vary widely in size and behavior. In ML datasets, their sleek bodies and aquatic environment provide distinct classification elements. Threats include overfishing, bycatch, and habitat degradation, pushing several species toward endangered status."
    ,

    "dolphin": "Dolphins are intelligent marine mammals known for their playful behavior, complex communication, and high-speed swimming. They use echolocation to navigate and hunt fish. Dolphins live in pods and show advanced social behavior. In ML datasets, dolphins add strong contour-based features due to their streamlined bodies. Threats include water pollution, fishing nets, and noise disturbances that affect their communication."
    ,

    "whale":  "Whales are large marine mammals that include species like blue whales, humpbacks, and orcas. They rely on deep vocal communication, long migrations, and specialized feeding techniques such as filter feeding or cooperative hunting. In image datasets, their massive scale and oceanic backgrounds offer unique classification challenges. Whales face threats from ship collisions, climate change, and noise pollution."
    ,

    "octopus": "The octopus is an intelligent marine invertebrate known for eight flexible arms, soft bodies, and impressive problem-solving skills. They can change color and texture to camouflage instantly. Octopuses feed on crabs, fish, and shellfish. In ML datasets, their variable shapes and textures challenge segmentation models. They face threats from pollution, overfishing, and habitat destruction."
    ,

    "jellyfish":  "Jellyfish are gelatinous marine animals that drift through oceans using rhythmic pulsations. They have long tentacles equipped with stinging cells used to immobilize prey. Jellyfish vary widely in size and transparency. In datasets, their translucent bodies often confuse ML models. While many populations are stable, climate change has caused increases in jellyfish blooms in some oceans."
    ,

    "starfish": "Starfish, or sea stars, are marine echinoderms with five or more arms. They can regenerate lost limbs and feed by extending their stomachs outside their bodies to digest prey. Starfish live on ocean floors and move using tube feet. In ML datasets, their radial symmetry provides visually distinct learning patterns. Pollution and ocean warming threaten some starfish populations."
    ,

    "crab": "Crabs are crustaceans with hard exoskeletons and sideways walking movement. They use claws for defense, communication, and feeding on algae, fish, and detritus. Crabs live in oceans, shores, and mangroves. In ML datasets, crabs add strong edge and shape features due to their rigid body structure. Threats include pollution, overharvesting, and habitat loss."
    ,

    "lobster": "Lobsters are marine crustaceans with long bodies, strong claws, and antennae. They live on the ocean floor and are primarily nocturnal, feeding on fish, mollusks, and plant matter. In datasets, lobsters offer unique textures and shapes for classification. Threats include overfishing, climate change, and habitat degradation affecting coastal ecosystems."
    ,
    "butterfly": "Butterflies are colorful insects known for their delicate wings and transformation lifecycle. They begin as caterpillars, undergo metamorphosis inside a chrysalis, and emerge as winged adults. Butterflies feed on nectar using their long proboscis and play an important role in pollination. Their wing patterns help with camouflage, mating, and predator deterrence. In ML datasets, butterflies are rich in color and symmetry, helping models learn fine-grained classification tasks. Threats include pesticide use, habitat loss, and climate changes that disrupt migration patterns."
    ,

    "moth": "Moths are close relatives of butterflies but are usually nocturnal and have fuzzy bodies with duller wing colors. Some moth species are important pollinators, especially at night, while others are agricultural pests. Moths are attracted to light due to navigational instincts based on moonlight. In datasets, distinguishing moths from butterflies teaches models to recognize subtle morphological differences. Their populations are affected by artificial lighting, habitat destruction, and pesticides."
    ,

    "bee": "Bees are vital pollinators responsible for fertilizing a large portion of the world’s crops and wild plants. They live in colonies with complex social roles, including queen, workers, and drones. Bees communicate using the famous waggle dance to show food locations. In ML datasets, their small size and rapid movement can be challenging to capture. Bees face major threats from habitat loss, pesticides, parasites, and climate change, impacting global food security."
    ,

    "ant": "Ants are social insects living in colonies that can range from a few dozen to millions of individuals. They communicate using pheromones and perform tasks such as foraging, nest building, and defense with strict division of labor. Ants are incredibly strong for their size and can lift many times their own body weight. In ML datasets, ants provide small-object detection challenges. Their populations are stable, though invasive ant species can disrupt ecosystems."
    ,

    "spider":  "Spiders are arachnids known for spinning webs to capture prey. They have eight legs, venomous fangs, and multiple eyes that help detect movement. Spiders play an important role in controlling insect populations. In datasets, their unique body structure and leg patterns provide classification diversity. They face minimal ecological threats, though urbanization reduces habitat for some species."
    ,

    "scorpion":  "Scorpions are arachnids with segmented tails ending in a venomous stinger. They are nocturnal predators feeding on insects and small animals. Scorpions glow under UV light due to chemicals in their exoskeleton. In ML datasets, their sharp silhouettes and distinct shapes help with fine-grained recognition. They primarily face threats from habitat destruction and climate shifts."
    ,

    "bat":"Bats are the only mammals capable of true flight. They use echolocation to navigate in the dark and feed on insects, fruit, or nectar depending on the species. Bats are essential for pollination and pest control. In datasets, low-light bat images challenge classification models. Threats include habitat loss, wind turbines, and diseases like white-nose syndrome, causing population declines."
    ,

    "rat":"Rats are small mammals known for their adaptability and intelligence. They thrive in cities, farms, and forests. Rats are omnivorous and reproduce rapidly. While often considered pests, they play important roles in scientific research. In ML datasets, rats add small-animal variability. Threats to wild rat species include predation and habitat changes, though urban rat populations are booming."
    ,

    "mouse": "Mice are small rodents with excellent hearing and a keen sense of smell. They live in nests within fields, forests, and human structures. Mice are important prey animals in ecosystems and are widely used in genetic and medical research. In ML datasets, their small size and similar appearance to rats create classification challenges. Their biggest threats are predators and human pest control programs."
    ,

    "squirrel": "Squirrels are agile rodents known for their bushy tails and climbing skills. They feed on nuts, seeds, fruits, and sometimes small insects. Squirrels store food for winter and exhibit strong problem-solving abilities. In datasets, their quick movements and varied fur colors add diversity. Threats include habitat loss and vehicle collisions, though many species are common in urban areas."
    ,

    "rabbit": "Rabbits are small herbivorous mammals with long ears and strong hind legs. They live in burrows and reproduce quickly. Rabbits feed on grass, vegetables, and bark. Their alert nature and fast hopping help them escape predators. In ML datasets, rabbits provide unique shape and texture features. Threats include habitat destruction and disease outbreaks such as rabbit hemorrhagic disease."
    ,

    "boar":  "Wild boars are strong, aggressive mammals with tusks and thick fur. They are omnivorous and highly adaptable, living in forests and grasslands. Boars use their snouts to dig for roots and insects. In datasets, their rugged appearance and bulky shape are easy to identify. Threats include overhunting and habitat conflict, though many populations are increasing due to resilience."
    ,

    "hippopotamus_pygmy": "The pygmy hippopotamus is a smaller, more reclusive relative of the common hippo. Found mainly in West African forests, it spends less time in water and is primarily nocturnal. Pygmy hippos feed on leaves and fruits. In datasets, their smooth skin and smaller size distinguish them from larger hippos. They are endangered due to habitat loss and hunting."
    ,

    "lemur": "Lemurs are primates found only in Madagascar. They have large eyes, long tails, and strong climbing abilities. Lemurs are highly social and communicate with scent markings and vocal calls. They feed on fruits, leaves, and insects. In ML datasets, their distinctive faces and ringed tails help with classification. Lemurs are critically endangered due to habitat destruction and illegal hunting."
    ,

    "meerkat": "Meerkats are small mammals living in cooperative groups called mobs. They stand upright to scan for predators and take turns acting as sentinels. Meerkats dig extensive burrow systems and feed on insects, lizards, and small mammals. In datasets, their upright posture and expressive faces offer unique features. Threats include habitat loss and predation, though many populations remain stable."
    ,
    "chimpanzee_bonobo":  "Bonobos are close relatives of chimpanzees and are known for their peaceful, cooperative social structure. They rely on strong social bonding, using grooming and communication to maintain harmony. Bonobos live in dense forests and feed on fruits, leaves, and insects. Their expressive faces and human-like behavior make them valuable in cognitive research. In ML datasets, bonobos offer distinct facial and body features that help models differentiate between primate species. They are endangered due to habitat loss and illegal hunting."
    ,

    "orangutan":  "Orangutans are highly intelligent primates native to the rainforests of Borneo and Sumatra. They have long arms, reddish fur, and primarily arboreal lifestyles. Orangutans build nests in trees and rely on fruits, leaves, and bark for food. They are slow breeders and show complex problem-solving skills. In datasets, their unique face shape and long limbs help ML models distinguish them from other apes. They are critically endangered due to deforestation and illegal wildlife trade."
    ,

    "baboon":  "Baboons are large monkeys found in savannas, forests, and arid regions of Africa. They live in large troops with complex social hierarchies. Baboons are omnivorous and highly adaptable, feeding on fruits, insects, and small animals. Their expressive faces and dog-like muzzles give them a distinctive appearance in datasets. Threats include habitat encroachment and conflict with human settlements."
    ,

    "flamingo_greater": "The greater flamingo is the largest flamingo species, recognized by its long legs, long neck, and pale pink feathers. They feed by filtering small organisms from shallow waters. Flamingos live in large colonies and perform synchronized movements. In ML datasets, their bright colors and tall shapes stand out clearly. Threats include pollution and water level changes affecting wetlands."
    ,

    "stingray": "Stingrays are flat-bodied marine animals related to sharks. They glide gracefully along the ocean floor and use their venomous tail barb for defense. Stingrays feed on shellfish, clams, and small fish. In datasets, their disc-shaped bodies offer unique classification features. Threats include overfishing, habitat loss, and accidental capture in fishing nets."
    ,

    "swordfish": "Swordfish are large predatory fish known for their long, sharp bill used for slashing prey. They are strong, fast swimmers found in deep oceanic waters. Swordfish feed on squid and smaller fish. In ML datasets, their iconic sword-like snout provides clear visual cues. Overfishing and climate-related changes in water temperature pose threats to their populations."
    ,

    "goldfish":  "Goldfish are small, colorful freshwater fish commonly kept as pets. They come in various shapes and fin patterns. Goldfish are omnivorous and prefer slow-moving waters. In ML datasets, their bright colors and rounded shapes make them easily identifiable. Threats mainly include poor tank conditions and invasive spread into local ecosystems when released."
    ,

    "salmon":  "Salmon are migratory fish known for their life cycle of traveling from the ocean back to freshwater streams to spawn. They have streamlined bodies and are powerful swimmers. In datasets, salmon-specific patterns and aquatic backgrounds add variety. Threats include overfishing, pollution, and dam construction blocking migration routes."
    ,

    "frog_tree":  "Tree frogs are small amphibians adapted for life in trees, equipped with sticky toe pads for climbing. They are brightly colored in some species, aiding in camouflage or warning predators. Tree frogs feed on insects and rely on moist habitats. In datasets, their small size and varied backgrounds challenge detection models. Threats include habitat loss and water contamination."
    ,

    "gecko": "Geckos are small lizards known for their ability to climb smooth surfaces using specialized toe pads. They are nocturnal and communicate with chirping sounds. Geckos feed on insects and thrive in warm climates. In ML datasets, their diverse patterns and eye shapes create useful data for classification. Threats include habitat destruction and predation by invasive species."
    ,

    "iguana": "Iguanas are large herbivorous lizards found in tropical forests and coastal areas. They have strong tails, sharp claws, and often bright coloration. Iguanas feed on leaves, flowers, and fruits. In datasets, their unique head spikes and body textures make them easy to classify. Threats include hunting and habitat loss."
    ,

    "hamster": "Hamsters are small rodents commonly kept as pets. They store food in cheek pouches and are most active at night. Hamsters live in burrows and feed on seeds, grains, and vegetables. In ML datasets, their fluffy bodies and small size are good for rodent recognition tasks. Threats are minimal due to domestication, though wild species face habitat loss."
    ,

    "ferret": "Ferrets are domesticated mammals descended from polecats. They are energetic, curious, and used for hunting rodents and as pets. Ferrets have long bodies, sharp senses, and playful behavior. In datasets, their slender shape and fur patterns offer unique models for classification. Threats are limited, but wild relatives face habitat reduction."
    ,

    "weasel":  "Weasels are small carnivores with long slender bodies and short legs. They are fast and excellent hunters, preying on rodents and small birds. Weasels live in forests, grasslands, and agricultural areas. In ML datasets, their small size and quick movement make detection challenging. Threats include habitat loss and conflict with humans."
    ,

    "badger": "Badgers are stout, strong mammals with distinctive facial markings. They dig extensive burrows called setts and feed on insects, small animals, and roots. Badgers have strong claws and thick fur, making them effective diggers and survivors in harsh climates. In ML datasets, their striped faces and body shape provide clear classification features. Threats include road accidents and habitat fragmentation."
}
class_names = [
        "antelope",
        "badger",
        "bat",
        "bear",
        "bee",
        "beetle",
        "bison",
        "boar",
        "butterfly",
        "cat",
        "caterpillar",
        "chimpanzee",
        "cockroach",
        "cow",
        "coyote",
        "crab",
        "crow",
        "deer",
        "dog",
        "dolphin",
        "donkey",
        "dragonfly",
        "duck",
        "eagle",
        "elephant",
        "flamingo",
        "fly",
        "fox",
        "goat",
        "goldfish",
        "goose",
        "gorilla",
        "grasshopper",
        "hamster",
        "hare",
        "hedgehog",
        "hippopotamus",
        "hornbill",
        "horse",
        "hummingbird",
        "hyena",
        "jellyfish",
        "kangaroo",
        "koala",
        "ladybugs",
        "leopard",
        "lion",
        "lizard",
        "lobster",
        "mosquito",
        "moth",
        "mouse",
        "octopus",
        "okapi",
        "orangutan",
        "otter",
        "owl",
        "ox",
        "oyster",
        "panda",
        "parrot",
        "pelecaniformes",
        "penguin",
        "pig",
        "pigeon",
        "porcupine",
        "possum",
        "raccoon",
        "rat",
        "reindeer",
        "rhinoceros",
        "sandpiper",
        "seahorse",
        "seal",
        "shark",
        "sheep",
        "snake",
        "sparrow",
        "squid",
        "squirrel",
        "starfish",
        "swan",
        "tiger",
        "turkey",
        "turtle",
        "whale",
        "wolf",
        "wombat",
        "woodpecker",
        "zebra"
    ]


def get_animal_details(name):
    name = class_names[name]

    name = name.lower()
    for n in animals_info:
        if n == name:
           return(animals_info[n])
    return "this animal was not present in database"
