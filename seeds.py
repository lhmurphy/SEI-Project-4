from pony.orm import db_session
from app import db
from models.Book import Book, Review
from models.Location import Location
from models.User import User, UserSchema

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    schema = UserSchema()
    lhmurphy = User(
        username='lhmurphy',
        email='lhmurphy@hotmail.com',
        password_hash=schema.generate_hash('pass'),
        image='https://pbs.twimg.com/profile_images/1095848308361302021/RZrejye3.jpg'
    )
    elle = User(
        username='elle',
        email='elle@hotmail.com',
        password_hash=schema.generate_hash('pass'),
        image='https://media.licdn.com/dms/image/C5603AQHX0omHmh7fWQ/profile-displayphoto-shrink_800_800/0?e=1565222400&v=beta&t=5pP3yPblEgMO-XljaArDpTJJblOqk0dy5L28S3qbWGQ'
    )
    hugo = User(
        username='hugo',
        email='hugo@hotmail.com',
        password_hash=schema.generate_hash('pass'),
        image='https://media.licdn.com/dms/image/C4E03AQFsE6plNPRwsg/profile-displayphoto-shrink_800_800/0?e=1565222400&v=beta&t=6TGy4Oli2Yc5LRLDCPKuuk850vNQiEUnyVW-g08ocjc'
    )

    amsterdam = Location(name='Amsterdam')
    paris = Location(name='Paris')
    kansas = Location(name='Kansas')
    colombia = Location(name='Colombia')
    austria = Location(name='Austria')
    azerbaijan = Location(name='Azerbaijan')
    belgium = Location(name='Belgium')
    bhutan = Location(name='Bhutan')
    chile = Location(name='Chile')
    copenhagen = Location(name='Copenhagen')
    palestine = Location(name='Palestine')
    london = Location(name='London')
    taiga = Location(name='Taiga')
    oxford = Location(name='Oxford')
    edinburgh = Location(name='Edinburgh')

    the_miniaturist = Book(
    title="The Miniaturist",
    author="Jessie Burton",
    isbn="0062306845",
    genre="Historical Fiction",
    date=2015,
    jacket="https://upload.wikimedia.org/wikipedia/en/thumb/d/db/TheMiniaturist.jpg/220px-TheMiniaturist.jpg",
    description="Set in seventeenth century Amsterdam— \n a city ruled by glittering wealth and oppressive religion—a masterful debut steeped in atmosphere and shimmering with mystery, in the tradition of Emma Donoghue, Sarah Waters, and Sarah Dunant.”There is nothing hidden that will not be revealed . . .“On a brisk autumn day in 1686, eighteen-year-old Nella Oortman arrives in Amsterdam to begin a new life as the wife of illustrious merchant trader Johannes Brandt. But her new home, while splendorous, is not welcoming. Johannes is kind yet distant, \n always locked in his study or at his warehouse office—leaving Nella alone with his sister, the sharp-tongued and forbidding Marin. But Nella’s world changes when Johannes presents her with an extraordinary wedding gift: a cabinet-sized replica of their home. To furnish her gift, Nella engages the services of a miniaturist—an elusive and enigmatic artist whose tiny creations mirror their real-life counterparts in eerie and unexpected ways... Johannes’ gift helps Nella to pierce the closed world of the Brandt household. But as she uncovers its unusual secrets, she begins to understand—and fear—the escalating dangers that await them all. In this repressively pious society where gold is worshipped second only to God, to be different is a threat to the moral fabric of society, and not even a man as rich as Johannes is safe. Only one person seems to see the fate that awaits them. Is the miniaturist the key to their salvation... or the architect of their destruction? Enchanting, beautiful, and exquisitely suspenseful, The Miniaturist is a magnificent story of love and obsession, betrayal and retribution, appearance and truth.",
    fiction=True,
    locations=[amsterdam],
    user=lhmurphy
    )

    all_the_light_we_cannot_see = Book(
    title="All the Light We Cannot See",
    author="Anthony Doerr",
    isbn="1501173219",
    genre="Historical Fiction",
    date=2017,
    jacket="https://images-na.ssl-images-amazon.com/images/I/81v5wp2zeQL.jpg",
    description="From the highly acclaimed, multiple award-winning Anthony Doerr, the stunningly beautiful instant New York Times bestseller about a blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II. Marie-Laure lives in Paris near the Museum of Natural History, where her father works. When she is twelve, the Nazis occupy Paris and father and daughter flee to the walled citadel of Saint-Malo, where Marie-Laure’s reclusive great uncle lives in a tall house by the sea. With them they carry what might be the museum’s most valuable and dangerous jewel. In a mining town in Germany, Werner Pfennig, an orphan, grows up with his younger sister, enchanted by a crude radio they find that brings them news and stories from places they have never seen or imagined. Werner becomes an expert at building and fixing these crucial new instruments and is enlisted to use his talent to track down the resistance. Deftly interweaving the lives of Marie-Laure and Werner, Doerr illuminates the ways, against all odds, people try to be good to one another. Doerr’s “stunning sense of physical detail and gorgeous metaphors” (San Francisco Chronicle) are dazzling. Ten years in the writing, a National Book Award finalist, All the Light We Cannot See is a magnificent, deeply moving novel from a writer “whose sentences never fail to thrill” (Los Angeles Times).",
    fiction=True,
    locations=[paris],
    user=elle
    )

    in_cold_blood = Book(
    title="In Cold Blood",
    author="Truman Capote",
    isbn="0679745580",
    genre="True Crime",
    jacket="https://images-na.ssl-images-amazon.com/images/I/51HX%2B6nWkqL._SX303_BO1,204,203,200_.jpg",
    date=1965,
    description="On November 15, 1959, in the small town of Holcomb, Kansas, four members of the Clutter family were savagely murdered by blasts from a shotgun held a few inches from their faces. There was no apparent motive for the crime, and there were almost no clues. As Truman Capote reconstructs the murder and the investigation that led to the capture, trial, and execution of the killers, he generates both mesmerizing suspense and astonishing empathy. In Cold Blood is a work that transcends its moment, yielding poignant insights into the nature of American violence.",
    fiction=False,
    locations=[kansas],
    user=hugo
    )

    one_hundred_years_of_solitude = Book(
    title="One Hundred Years of Solitude",
    author="Gabriel García Márquez",
    isbn="1000",
    genre="Magical Realism",
    jacket="https://images-na.ssl-images-amazon.com/images/I/91D-NuBThAL.jpg",
    date=1990,
    description="One of the twentieth century's most beloved and acclaimed novels, One Hundred Years of Solitude tells the story of the rise and fall, birth and death of the mythical town of Macondo through the history of the Buendia family. Inventive, amusing, magnetic, sad, and alive with unforgettable men and women--brimming with truth, compassion, and a lyrical magic that strikes the soul--this novel is a masterpiece in the art of fiction.",
    fiction=True,
    locations=[colombia],
    user=lhmurphy
    )

    the_tobacconist = Book(
    title="The Tobacconist",
    author="Robert Seethaler",
    isbn="1770899650",
    genre="Historical Fiction",
    jacket="https://pictures.abebooks.com/isbn/9781770899650-uk.jpg",
    date=2012,
    description="When seventeen-year-old Franz exchanges his home in the idyllic beauty of the Austrian lake district for the bustle of Vienna, his homesickness quickly dissolves amidst the thrum of the city. In his role as apprentice to the elderly tobacconist Otto Trsnyek, he will soon be supplying the great and good of Vienna with their newspapers and cigarettes. Among the regulars is a Professor Freud, whose predilection for cigars and occasional willingness to dispense romantic advice will forge a bond between him and young Franz. It is 1937. In a matter of months Germany will annex Austria and the storm that has been threatening to engulf the little tobacconist will descend, leaving the lives of Franz, Otto and Professor Freud irredeemably changed.",
    fiction=True,
    locations=[austria],
    user=elle
    )

    ali_and_nino_a_love_story = Book(
    title="Ali and Nino: A Love Story",
    author="Kurban Said",
    isbn="1468314408",
    genre="Historical Romance",
    jacket="https://images-na.ssl-images-amazon.com/images/I/41056SHJ3PL._SX299_BO1,204,203,200_.jpg",
    date=2016,
    description="The sweeping tale of love challenged by war, as romantic and gripping as Gone with the Wind or Dr. Zhivago, Ali& Nino portrays, against a glamorously exotic backdrop,the enduring love between childhood friends divided by separate cultures.Ali and Nino grow up together in carefree innocence in Baku, on the Caspian Sea. Here, where East and West collide, they are inevitably drawn into the events of World War I and the Russian Revolution. Torn apart by the turmoil of the divided society around them, Ali joins the defense of Azerbaijan from the onslaught of the Red Army and Nino flees to the safety of Paris with their child, unsure whether they will ever see each other again. This is an unforgettable story of blood feud, adventure, and personal heroism―and a love that endures the upheaval of cultures.",
    fiction=True,
    locations=[azerbaijan],
    user=hugo
    )

    war_and_turpentine = Book(
    title="War and Turpentine",
    author="Stefan Hertmans",
    isbn="0099598043",
    genre="Biographical Fiction",
    jacket="https://images.penguinrandomhouse.com/cover/9781101872116",
    date=2017,
    description="Shortly before his death, Stefan Hertmans' grandfather Urbain Martien gave his grandson a set of notebooks containing the detailed memories of his life. He grew up in poverty around 1900, the son of a struggling church painter who died young, and went to work in an iron foundry at only 13. Afternoons spent with his father at work on a church fresco were Urbain’s heaven; the iron foundry an inferno. During the First World War, Urbain was on the front line confronting the invading Germans, and ever after he is haunted by events he can never forget. The war ends and he marries his great love, Maria Emelia, but she dies tragically in the 1919 flu epidemic. Urbain mourns her bitterly for the rest of his life but, like the obedient soldier he is, he marries her sister at her parents' bidding. The rest is not quite silence, but a marriage with a sad secret at its heart, and the consolations found in art and painting. War and Turpentine is the imaginative reconstruction of a damaged life across the tumultuous decades of the twentieth century; a deeply moving portrayal of family, grief, love and war.",
    fiction=True,
    locations=[belgium],
    user=lhmurphy
    )

    treasures_of_the_thunder_dragon_a_portrait_of_bhutan = Book(
    title="Treasures of the Thunder Dragon: A Portrait of Bhutan",
    author="Queen of Bhutan Ashi Dorji Wangmo Wangchuck",
    isbn="0670999016",
    genre="Biographical Fiction",
    jacket="https://images-na.ssl-images-amazon.com/images/I/51zkj8Aes8L._SX331_BO1,204,203,200_.jpg",
    date=2006,
    description="Long regarded as the Forbidden Land, Bhutanor Druk Yul, the Land of the Thunder Dragonwas virtually closed to the outside world until the 1960s. Even today, little is known about this remote Himalayan Buddhist kingdom nestled between two giant neighbours, India and China. Often described as the Last Shangri La, Bhutan is still a country of pristine forests, alpine valleys and glacial lakes, rich in rare flora and fauna such as the blue poppy, the golden langur and the red panda. As spectacular as its natural beauty are the architecture of its towering dzongs (fortresses) and the art treasures that fill its monasteries and temples. Ashi Dorji Wangmo Wangchucks portrait of her country is a captivating blend of personal memoir, history, folklore and travelogue. It provides unique and intimate insights into Bhutanese culture and society, with its vivid glimpses of life in Bhutans villages and hamlets, monasteries and palaces. Her engaging account of her childhood, growing up in a village in western Bhutan and the changes she witnessed when the country decided to end its isolation also tells a larger storythat of Bhutans rapid transition from a medieval kingdom to a modern nation within the space of a decade. The author shares with us her delight in some of the hidden treasures of her country, which she discovered during her journeys on foot to every corner of Bhutanfrom highland villages in the shadow of the great Himalayan peaks to serene monasteries wreathed in myth and legend to the rainforests in the south and centre of the country, which are among the worlds richest biodiversity hotspots. This book, with its specially commissioned illustrations by young Bhutanese artists, and photographs from the authors family album, is essential reading both for those who plan to visit the Kingdom of the Thunder Dragon and for armchair travellers who yearn to experience the magic of Bhutan through their imaginations.",
    fiction=False,
    locations=[bhutan],
    user=elle
    )

    la_casa_de_los_espiritus_the_house_of_the_spirits = Book(
    title="La Casa de Los Espiritus: The House of the Spirits",
    author="Isabel Allende",
    isbn="10001",
    genre="Literary Fiction",
    jacket="https://images-na.ssl-images-amazon.com/images/I/41XFupEm%2BML._SX322_BO1,204,203,200_.jpg",
    date=2017,
    description="In one of the most important and beloved Latin American works of the twentieth century, Isabel Allende weaves a luminous tapestry of three generations of the Trueba family, revealing both triumphs and tragedies. Here is patriarch Esteban, whose wild desires and political machinations are tempered only by his love for his ethereal wife, Clara, a woman touched by an otherworldly hand. Their daughter, Blanca, whose forbidden love for a man Esteban has deemed unworthy infuriates her father, yet will produce his greatest joy: his granddaughter Alba, a beautiful, ambitious girl who will lead the family and their country into a revolutionary future. The House of the Spirits is an enthralling saga that spans decades and lives, twining the personal and the political into an epic novel of love, magic, and fate.",
    fiction=True,
    locations=[chile],
    user=hugo
    )

    smillas_sense_of_snow = Book(
    title="Smilla’s Sense of Snow",
    author="Peter Hoeg",
    isbn="0385315147",
    genre="Thriller",
    jacket="https://images-na.ssl-images-amazon.com/images/I/91wAm05r2fL.jpg",
    date=1995,
    description="Smilla's Sense of Snow presents one of the toughest heroines in modern fiction. Smilla Qaavigaaq Jaspersen is part Inuit, but she lives in Copenhagen. She is thirty-seven, single, childless, moody, and she refuses to fit in. Smilla's six-year-old Inuit neighbor, Isaiah, manages only with a stubbornness that matches her own to befriend her. When Isaiah falls off a roof and is killed, Smilla doesn't believe it's an accident. She has seen his tracks in the snow, and she knows about snow. She decides to investigate and discovers that even the police don't want her to get involved. But opposition appeals to Smilla. As all of Copenhagen settles down for a quiet Christmas, Smilla's investigation takes her from a fervently religious accountant to a tough-talking pathologist and an alcoholic shipping magnate and into the secret files of the Danish company responsible for extracting most of Greenland's mineral wealth - and finally onto a ship with an international cast of villains bound for a mysterious mission on an uninhabitable island off Greenland. To read Smilla's Sense of Snow is to be taken on a magical, nerve-shattering journey - from the snow-covered streets of Copenhagen to the awesome beauty of the Arctic ice caps. A mystery, a love story, and an elegy for a vanishing way of life, Smilla's Sense of Snow is a breathtaking achievement, an exceptional feat of storytelling.",
    fiction=True,
    locations=[copenhagen],
    user=lhmurphy
    )

    hippie = Book(
    title="Hippie",
    author="Paolo Coelho",
    isbn="978-1786331588",
    genre="Literary Fiction",
    jacket="https://images-na.ssl-images-amazon.com/images/I/41dQTPXDp0L._SX293_BO1,204,203,200_.jpg",
    date=2018,
    description="Drawing on the rich experience of his own life, bestselling author Paulo Coelho takes us back in time to relive the dreams of a generation that longed for peace and dared to challenge the established social order. In HIPPIE, he tells the story of Paulo, a skinny Brazilian with a goatee and long hair, setting off on a journey in search of a deeper meaning for his life. He travels on the famous ‘Death Train to Bolivia’, then on to Peru, later hitchhiking through Chile and Argentina. In the famous Dam Square in Amsterdam he finds young people playing music, while discussing sexual liberation, the expansion of consciousness and the search for an inner truth. There he meets Karla, a Dutch woman in her twenties who has been waiting to find the ideal companion to accompany her on the fabled hippie trail to Nepal. Together with their fellow travellers, they embark on a trip aboard the Magic Bus, heading across Europe and Central Asia to Kathmandu. For everyone, the journey is transformative. For Paulo and Karla it is a life-defining love story that leads to choices that will set the course of the rest of their lives.",
    fiction=True,
    locations=[amsterdam],
    user=elle
    )

    the_hearts_invisible_furies = Book(
    title="The Heart’s Invisible Furies",
    author="John Boyne",
    isbn="978-1784161002",
    genre="Historical Fiction",
    jacket="https://images-na.ssl-images-amazon.com/images/I/514KOtZxHjL._SX328_BO1,204,203,200_.jpg",
    date=2019,
    description="Forced to flee the scandal brewing in her hometown, Catherine Goggin finds herself pregnant and alone, in search of a new life at just sixteen. She knows she has no choice but to believe that the nun she entrusts her child to will find him a better life. Cyril Avery is not a real Avery, or so his parents are constantly reminding him. Adopted as a baby, he’s never quite felt at home with the family that treats him more as a curious pet than a son. But it is all he has ever known. And so begins one man’s desperate search to find his place in the world. Unspooling and unseeing, Cyril is a misguided, heart-breaking, heartbroken fool. Buffeted by the harsh winds of circumstance towards the one thing that might save him from himself, but when opportunity knocks, will he have the courage, finally, take it?",
    fiction=True,
    locations=[amsterdam],
    user=hugo
    )

    us = Book(
    title="Us",
    author="David Nicholls",
    isbn="978-0340897010",
    genre="Historical Fiction",
    jacket="https://images-na.ssl-images-amazon.com/images/I/419jD4jadjL._SX324_BO1,204,203,200_.jpg",
    date=2015,
    description="Douglas Petersen understands his wife's need to 'rediscover herself' now that their son is leaving home. He just thought they'd be doing their rediscovering together. So when Connie announces that she will be leaving, too, he resolves to make their last family holiday into the trip of a lifetime: one that will draw the three of them closer, and win the respect of his son. One that will make Connie fall in love with him all over again. The hotels are booked, the tickets bought, the itinerary planned and printed. What could possibly go wrong?",
    fiction=True,
    locations=[amsterdam],
    user=lhmurphy
    )

    the_dinner = Book(
    title="The Dinner",
    author="Herman Koch",
    isbn="978-1848873827",
    genre="Satire",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/51-q4hmQoKL.jpg",
    date=2012,
    description="A summer's evening in Amsterdam and two couples meet at a fashionable restaurant. Between mouthfuls of food and over the delicate scraping of cutlery, the conversation remains a gentle hum of politeness - the banality of work, the triviality of holidays. But the empty words hide a terrible conflict and, with every forced smile and every new course, the knives are being sharpened... Each couple has a fifteen-year-old son. Together, the boys have committed a horrifying act, caught on camera, and their grainy images have been beamed into living rooms across the nation; despite a police manhunt, the boys remain unidentified - by everyone except their parents. As the dinner reaches its culinary climax, the conversation finally touches on their children and, as civility and friendship disintegrate, each couple shows just how far they are prepared to go to protect those they love.",
    fiction=True,
    locations=[amsterdam],
    user=elle
    )

    the_parisian = Book(
    title="The Parisian",
    author="Isabella Hammad",
    isbn="978-1911214427",
    genre="Historical fiction",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/51M9D8tktKL.jpg",
    date=2019,
    description="As the First World War shatters families, destroys friendships and kills lovers, a young Palestinian dreamer sets out to find himself.\n Midhat Kamal navigates his way across a fractured world, from the shifting politics of the Middle East to the dinner tables of Montpellier and a newly tumultuous Paris. He discovers that everything is fragile: love turns to loss, friends become enemies and everyone is looking for a place to belong.\n Isabella Hammad delicately untangles the politics and personal tragedies of a turbulent era – the Palestinian struggle for independence, the strife of the early twentieth century and the looming shadow of the Second World War. An intensely human story amidst a global conflict, The Parisian is historical fiction with a remarkable contemporary voice.",
    fiction=True,
    locations=[paris, palestine],
    user=elle
    )
    enchantee = Book(
    title="Enchantée",
    author="Gita Trelease",
    isbn="978-1509895977",
    genre="Fantasy/Sci Fi",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/51wvz%2BsBBML.jpg",
    date=2019,
    description="A compellingly beautiful tale of magic, intrigue and deception, set against the backdrop of eighteenth-century Paris on the cusp of revolution.\n Paris in 1789 is a labyrinth of twisted streets, filled with beggars, thieves, revolutionaries – and magicians . . . \nWhen seventeen-year-old Camille is left orphaned, she has to provide for her frail sister and her volatile brother. In desperation, she survives by using the petty magic she learnt from her mother. But when her brother disappears Camille decides to pursue a richer, more dangerous mark: the glittering court of Louis XVI and Marie Antoinette.\nUsing dark magic Camille transforms herself into the ‘Baroness de la Fontaine‘ and presents herself at the court of Versaille, where she soon finds herself swept up in a dizzying life of riches, finery and suitors. But Camille’s resentment of the rich is at odds with the allure of their glamour and excess, and she soon discovers that she’s not the only one leading a double life.",
    fiction=True,
    locations=[paris],
    user=hugo
    )
    the_age_of_light = Book(
    title="The Age of Light",
    author="Whitney Scharer",
    isbn="978-1509889129",
    genre="Art History",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/51D2-aS%2BeqL.jpg",
    date=2019,
    description="‘I’d rather take a picture than be one,’ Lee Miller declares, as she arrives in Paris one cool day in 1929. Lee has left behind her life in New York and a successful modelling career at Vogue to pursue her dream of becoming a photographer. She soon catches the eye of renowned Surrealist artist Man Ray and convinces him to hire her as his assistant. Man is an egotistical, charismatic force, and as Lee becomes both his muse and his protégé, they embark upon a passionate affair.\nLee and Man spend their days working closely in the studio and their nights at smoky cabarets, opium dens and wild parties. But as Lee begins to assert herself, and to create pioneering work of her own, Man’s jealousy spirals out of control, and leads to a betrayal that threatens to destroy them both . . .\nTransporting us from bohemian Paris to the battlefields of WWII, The Age of Light is a powerful and intoxicating story about love, obsession and the personal price of ambition. Based on the incredible true story, in her debut novel Whitney Scharer brings a brilliant and revolutionary artist out of the shadow of a man’s legacy, and into the light.",
    fiction=True,
    locations=[paris, london],
    user=lhmurphy
    )
    fresh_air_and_empty_streets = Book(
    title="Fresh Air and Empty Streets",
    author="Oliver Cable",
    isbn="978-0995450905",
    genre="Literary Fiction",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/51-q4hmQoKL.jpg",
    date=2016,
    description="Fifteen years ago, Alexander left his wife and small child behind to pursue the life of an artist in Paris. Now all grown up, Felix travels to Paris to meet his elusive father. On a journey through smoky jazz bars, artists' studios and along the banks of the Seine, Felix discovers more and more about Alexander, calling into question his long-held beliefs.",
    fiction=True,
    locations=[paris],
    user=elle
    )
    the_last_tudor = Book(
    title="The Last Tudor",
    author="Philippa Gregory",
    isbn="978-1471133077",
    genre="Historical Fiction",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/612miJfoAnL.jpg",
    date=2018,
    description="Jane Grey was Queen of England for nine days. Using her position as cousin to the deceased king, her father and his conspirators put her on the throne ahead of the king’s half-sister Mary, who quickly mustered an army, claimed her crown and locked Jane in the Tower. When Jane refused to betray her Protestant faith, Mary sent her to the executioner’s block. There Jane turned her father’s greedy, failed grab for power into her own brave and tragic martyrdom.\n‘Learn you to die’ is the advice that Jane gives in a letter to her younger sister Katherine, who has no intention of dying. She intends to enjoy her beauty and her youth and find love. But her lineage makes her a threat to the insecure and infertile Queen Mary and, when Mary dies, to her sister Queen Elizabeth, who will never allow Katherine to marry and produce a potential royal heir before she does.  So when Katherine’s secret marriage is revealed by her pregnancy, she too must go to the Tower.\n‘Farewell, my sister,’ writes Katherine to the youngest Grey sister, Mary. A beautiful dwarf, disregarded by the court, Mary finds it easy to keep secrets, especially her own, while avoiding Elizabeth’s suspicious glare. After watching her sisters defy the queen, Mary is aware of her own perilous position as a possible heir to the throne. But she is determined to command her own destiny and be the last Tudor to risk her life in matching wits with her ruthless and unforgiving cousin Elizabeth.",
    fiction=True,
    locations=[london],
    user=hugo
    )
    tiger = Book(
    title="Tiger",
    author="Polly Clark",
    isbn="978-1786485427",
    genre="Literary Fiction",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/41DO3oa3KhL.jpg",
    date=2019,
    description="Set across two continents, Tiger is a sweeping story of survival and redeeming love that plunges the reader into one of the world's last wildernesses with blistering authenticity.\nFrieda is a primatologist, sensitive and solitary, until a violent attack shatters her ordered world. In her new role as a zookeeper, she confronts a very different ward: an injured wild tiger.\nDeep in the Siberian taiga, Tomas, a Russian conservationist, fears that the natural order has toppled. The king tiger has been killed by poachers and a spectacular tigress now patrols his vast territory as her own.\nIn a winter of treacherous competition, the path of the tigress and her cub crosses with an Udeghe huntress and her daughter. Vengeance must follow, and the fates of both tigers and people are transformed.\nLearning of her tiger's past offers Frieda the chance of freedom. Faced with the savage forces of nature, she must trust to her instinct and, like the tiger, find a way to live in the world.",
    fiction=True,
    locations=[london, taiga],
    user=lhmurphy
    )
    once_upon_a_river = Book(
    title="Once Upon a River",
    author="Diane Setterfield",
    isbn="978-0857525659",
    genre="Folklore",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/614xYsB2wSL.jpg",
    date=2019,
    description="On a dark midwinter’s night in an ancient inn on the Thames, the regulars are entertaining themselves by telling stories when the door bursts open and in steps an injured stranger. In his arms is the drowned corpse of a child. \nHours later, the dead girl stirs, takes a breath and returns to life.\nIs it a miracle?\nIs it magic?\nAnd who does the little girl belong to? \nAn exquisitely crafted multi-layered mystery brimming with folklore, suspense and romance, as well as with the urgent scientific curiosity of the Darwinian age, Once Upon a River is as richly atmospheric as Setterfield’s bestseller The Thirteenth Tale.",
    fiction=True,
    locations=[london, oxford],
    user=elle
    )
    the_da_vinci_code = Book(
    title="The Da Vinci Code",
    author="Dan Brown",
    isbn="978-0385504201",
    genre="Thriller",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/513WB5gwT9L.jpg",
    date=2009,
    description="Harvard professor Robert Langdon receives an urgent late-night phone call while on business in Paris: the elderly curator of the Louvre has been brutally murdered inside the museum. Alongside the body, police have found a series of baffling codes. \nAs Langdon and a gifted French cryptologist, Sophie Neveu, begin to sort through the bizarre riddles, they are stunned to find a trail that leads to the works of Leonardo Da Vinci - and suggests the answer to a mystery that stretches deep into the vault of history.\nUnless Langdon and Neveu can decipher the labyrinthine code and quickly assemble the pieces of the puzzle, a stunning historical truth will be lost forever...",
    fiction=True,
    locations=[london, paris, edinburgh],
    user=hugo
    )
    a_murder_is_announced = Book(
    title="A Murder is Announced (Miss Marple)",
    author="Agatha Christie",
    isbn="978-0007120963",
    genre="Mystery",
    jacket="https://images-eu.ssl-images-amazon.com/images/I/519HhpgnzXL.jpg",
    date=2016,
    description="Agatha Christie’s most ingenious murder mystery, reissued with a striking new cover designed to appeal to the latest generation of Agatha Christie fans and book lovers.\nThe villagers of Chipping Cleghorn, including Jane Marple, are agog with curiosity over an advertisement in the local gazette which reads: ‘A murder is announced and will take place on Friday October 29th, at Little Paddocks at 6.30 p.m.’\nA childish practical joke? Or a hoax intended to scare poor Letitia Blacklock? Unable to resist the mysterious invitation, a crowd begins to gather at Little Paddocks at the appointed time when, without warning, the lights go out…",
    fiction=True,
    locations=[],
    user=lhmurphy
    )

    Review(
    content="BRILLIANT!",
    book=the_miniaturist,
    user=lhmurphy
    )

    Review(
    content="Best book ever, loves it!",
    book=the_miniaturist,
    user=lhmurphy
    )

    Review(
    content="I'll be recommending this book to all my friends!",
    book=all_the_light_we_cannot_see,
    user=lhmurphy
    )

    # save the data to the database
    db.commit()
