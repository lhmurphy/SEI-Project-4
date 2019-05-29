from pony.orm import db_session
from app import db
from models.Book import Book
from models.Location import Location
from models.Review import Review

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():

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

    the_miniaturist = Book(
    title="The Miniaturist",
    author="Jessie Burton",
    isbn="0062306845",
    genre="Historical Fiction",
    pub_date=2015,
    book_jacket="https://upload.wikimedia.org/wikipedia/en/thumb/d/db/TheMiniaturist.jpg/220px-TheMiniaturist.jpg",
    description="Set in seventeenth century Amsterdam—a city ruled by glittering wealth and oppressive religion—a masterful debut steeped in atmosphere and shimmering with mystery, in the tradition of Emma Donoghue, Sarah Waters, and Sarah Dunant.”There is nothing hidden that will not be revealed . . .“On a brisk autumn day in 1686, eighteen-year-old Nella Oortman arrives in Amsterdam to begin a new life as the wife of illustrious merchant trader Johannes Brandt. But her new home, while splendorous, is not welcoming. Johannes is kind yet distant, always locked in his study or at his warehouse office—leaving Nella alone with his sister, the sharp-tongued and forbidding Marin. But Nella’s world changes when Johannes presents her with an extraordinary wedding gift: a cabinet-sized replica of their home. To furnish her gift, Nella engages the services of a miniaturist—an elusive and enigmatic artist whose tiny creations mirror their real-life counterparts in eerie and unexpected ways... Johannes’ gift helps Nella to pierce the closed world of the Brandt household. But as she uncovers its unusual secrets, she begins to understand—and fear—the escalating dangers that await them all. In this repressively pious society where gold is worshipped second only to God, to be different is a threat to the moral fabric of society, and not even a man as rich as Johannes is safe. Only one person seems to see the fate that awaits them. Is the miniaturist the key to their salvation... or the architect of their destruction? Enchanting, beautiful, and exquisitely suspenseful, The Miniaturist is a magnificent story of love and obsession, betrayal and retribution, appearance and truth.",
    fiction=True,
    locations=[amsterdam]
    )

    all_the_light_we_cannot_see = Book(
    title="All the Light We Cannot See",
    author="Anthony Doerr",
    isbn="1501173219",
    genre="Historical Fiction",
    pub_date=2017,
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/81v5wp2zeQL.jpg",
    description="From the highly acclaimed, multiple award-winning Anthony Doerr, the stunningly beautiful instant New York Times bestseller about a blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II. Marie-Laure lives in Paris near the Museum of Natural History, where her father works. When she is twelve, the Nazis occupy Paris and father and daughter flee to the walled citadel of Saint-Malo, where Marie-Laure’s reclusive great uncle lives in a tall house by the sea. With them they carry what might be the museum’s most valuable and dangerous jewel. In a mining town in Germany, Werner Pfennig, an orphan, grows up with his younger sister, enchanted by a crude radio they find that brings them news and stories from places they have never seen or imagined. Werner becomes an expert at building and fixing these crucial new instruments and is enlisted to use his talent to track down the resistance. Deftly interweaving the lives of Marie-Laure and Werner, Doerr illuminates the ways, against all odds, people try to be good to one another. Doerr’s “stunning sense of physical detail and gorgeous metaphors” (San Francisco Chronicle) are dazzling. Ten years in the writing, a National Book Award finalist, All the Light We Cannot See is a magnificent, deeply moving novel from a writer “whose sentences never fail to thrill” (Los Angeles Times).",
    fiction=True,
    locations=[paris]
    )

    in_cold_blood = Book(
    title="In Cold Blood",
    author="Truman Capote",
    isbn="0679745580",
    genre="True Crime",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/51HX%2B6nWkqL._SX303_BO1,204,203,200_.jpg",
    pub_date=1965,
    description="On November 15, 1959, in the small town of Holcomb, Kansas, four members of the Clutter family were savagely murdered by blasts from a shotgun held a few inches from their faces. There was no apparent motive for the crime, and there were almost no clues. As Truman Capote reconstructs the murder and the investigation that led to the capture, trial, and execution of the killers, he generates both mesmerizing suspense and astonishing empathy. In Cold Blood is a work that transcends its moment, yielding poignant insights into the nature of American violence.",
    fiction=False,
    locations=[kansas]
    )

    one_hundred_years_of_solitude = Book(
    title="One Hundred Years of Solitude",
    author="Gabriel García Márquez",
    isbn="1000",
    genre="Magical Realism",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/91D-NuBThAL.jpg",
    pub_date=1990,
    description="One of the twentieth century's most beloved and acclaimed novels, One Hundred Years of Solitude tells the story of the rise and fall, birth and death of the mythical town of Macondo through the history of the Buendia family. Inventive, amusing, magnetic, sad, and alive with unforgettable men and women--brimming with truth, compassion, and a lyrical magic that strikes the soul--this novel is a masterpiece in the art of fiction.",
    fiction=True,
    locations=[colombia]
    )

    the_tobacconist = Book(
    title="The Tobacconist",
    author="Robert Seethaler",
    isbn="1770899650",
    genre="Historical Fiction",
    book_jacket="https://pictures.abebooks.com/isbn/9781770899650-uk.jpg",
    pub_date=2012,
    description="When seventeen-year-old Franz exchanges his home in the idyllic beauty of the Austrian lake district for the bustle of Vienna, his homesickness quickly dissolves amidst the thrum of the city. In his role as apprentice to the elderly tobacconist Otto Trsnyek, he will soon be supplying the great and good of Vienna with their newspapers and cigarettes. Among the regulars is a Professor Freud, whose predilection for cigars and occasional willingness to dispense romantic advice will forge a bond between him and young Franz. It is 1937. In a matter of months Germany will annex Austria and the storm that has been threatening to engulf the little tobacconist will descend, leaving the lives of Franz, Otto and Professor Freud irredeemably changed.",
    fiction=True,
    locations=[austria]
    )

    ali_and_nino_a_love_story = Book(
    title="Ali and Nino: A Love Story",
    author="Kurban Said",
    isbn="1468314408",
    genre="Historical Romance",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/41056SHJ3PL._SX299_BO1,204,203,200_.jpg",
    pub_date=2016,
    description="The sweeping tale of love challenged by war, as romantic and gripping as Gone with the Wind or Dr. Zhivago, Ali& Nino portrays, against a glamorously exotic backdrop,the enduring love between childhood friends divided by separate cultures.Ali and Nino grow up together in carefree innocence in Baku, on the Caspian Sea. Here, where East and West collide, they are inevitably drawn into the events of World War I and the Russian Revolution. Torn apart by the turmoil of the divided society around them, Ali joins the defense of Azerbaijan from the onslaught of the Red Army and Nino flees to the safety of Paris with their child, unsure whether they will ever see each other again. This is an unforgettable story of blood feud, adventure, and personal heroism―and a love that endures the upheaval of cultures.",
    fiction=True,
    locations=[azerbaijan]
    )

    war_and_turpentine = Book(
    title="War and Turpentine",
    author="Stefan Hertmans",
    isbn="0099598043",
    genre="Biographical Fiction",
    book_jacket="https://images.penguinrandomhouse.com/cover/9781101872116",
    pub_date=2017,
    description="Shortly before his death, Stefan Hertmans' grandfather Urbain Martien gave his grandson a set of notebooks containing the detailed memories of his life. He grew up in poverty around 1900, the son of a struggling church painter who died young, and went to work in an iron foundry at only 13. Afternoons spent with his father at work on a church fresco were Urbain’s heaven; the iron foundry an inferno. During the First World War, Urbain was on the front line confronting the invading Germans, and ever after he is haunted by events he can never forget. The war ends and he marries his great love, Maria Emelia, but she dies tragically in the 1919 flu epidemic. Urbain mourns her bitterly for the rest of his life but, like the obedient soldier he is, he marries her sister at her parents' bidding. The rest is not quite silence, but a marriage with a sad secret at its heart, and the consolations found in art and painting. War and Turpentine is the imaginative reconstruction of a damaged life across the tumultuous decades of the twentieth century; a deeply moving portrayal of family, grief, love and war.",
    fiction=True,
    locations=[belgium]
    )

    treasures_of_the_thunder_dragon_a_portrait_of_bhutan = Book(
    title="Treasures of the Thunder Dragon: A Portrait of Bhutan",
    author="Queen of Bhutan Ashi Dorji Wangmo Wangchuck",
    isbn="0670999016",
    genre="Biographical Fiction",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/51zkj8Aes8L._SX331_BO1,204,203,200_.jpg",
    pub_date=2006,
    description="Long regarded as the Forbidden Land, Bhutanor Druk Yul, the Land of the Thunder Dragonwas virtually closed to the outside world until the 1960s. Even today, little is known about this remote Himalayan Buddhist kingdom nestled between two giant neighbours, India and China. Often described as the Last Shangri La, Bhutan is still a country of pristine forests, alpine valleys and glacial lakes, rich in rare flora and fauna such as the blue poppy, the golden langur and the red panda. As spectacular as its natural beauty are the architecture of its towering dzongs (fortresses) and the art treasures that fill its monasteries and temples. Ashi Dorji Wangmo Wangchucks portrait of her country is a captivating blend of personal memoir, history, folklore and travelogue. It provides unique and intimate insights into Bhutanese culture and society, with its vivid glimpses of life in Bhutans villages and hamlets, monasteries and palaces. Her engaging account of her childhood, growing up in a village in western Bhutan and the changes she witnessed when the country decided to end its isolation also tells a larger storythat of Bhutans rapid transition from a medieval kingdom to a modern nation within the space of a decade. The author shares with us her delight in some of the hidden treasures of her country, which she discovered during her journeys on foot to every corner of Bhutanfrom highland villages in the shadow of the great Himalayan peaks to serene monasteries wreathed in myth and legend to the rainforests in the south and centre of the country, which are among the worlds richest biodiversity hotspots. This book, with its specially commissioned illustrations by young Bhutanese artists, and photographs from the authors family album, is essential reading both for those who plan to visit the Kingdom of the Thunder Dragon and for armchair travellers who yearn to experience the magic of Bhutan through their imaginations.",
    fiction=False,
    locations=[bhutan]
    )

    la_casa_de_los_espiritus_the_house_of_the_spirits = Book(
    title="La Casa de Los Espiritus: The House of the Spirits",
    author="Isabel Allende",
    isbn="10001",
    genre="Literary Fiction",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/41XFupEm%2BML._SX322_BO1,204,203,200_.jpg",
    pub_date=2017,
    description="In one of the most important and beloved Latin American works of the twentieth century, Isabel Allende weaves a luminous tapestry of three generations of the Trueba family, revealing both triumphs and tragedies. Here is patriarch Esteban, whose wild desires and political machinations are tempered only by his love for his ethereal wife, Clara, a woman touched by an otherworldly hand. Their daughter, Blanca, whose forbidden love for a man Esteban has deemed unworthy infuriates her father, yet will produce his greatest joy: his granddaughter Alba, a beautiful, ambitious girl who will lead the family and their country into a revolutionary future. The House of the Spirits is an enthralling saga that spans decades and lives, twining the personal and the political into an epic novel of love, magic, and fate.",
    fiction=True,
    locations=[chile]
    )

    smillas_sense_of_snow = Book(
    title="Smilla’s Sense of Snow",
    author="Peter Hoeg",
    isbn="0385315147",
    genre="Thriller",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/91wAm05r2fL.jpg",
    pub_date=1995,
    description="Smilla's Sense of Snow presents one of the toughest heroines in modern fiction. Smilla Qaavigaaq Jaspersen is part Inuit, but she lives in Copenhagen. She is thirty-seven, single, childless, moody, and she refuses to fit in. Smilla's six-year-old Inuit neighbor, Isaiah, manages only with a stubbornness that matches her own to befriend her. When Isaiah falls off a roof and is killed, Smilla doesn't believe it's an accident. She has seen his tracks in the snow, and she knows about snow. She decides to investigate and discovers that even the police don't want her to get involved. But opposition appeals to Smilla. As all of Copenhagen settles down for a quiet Christmas, Smilla's investigation takes her from a fervently religious accountant to a tough-talking pathologist and an alcoholic shipping magnate and into the secret files of the Danish company responsible for extracting most of Greenland's mineral wealth - and finally onto a ship with an international cast of villains bound for a mysterious mission on an uninhabitable island off Greenland. To read Smilla's Sense of Snow is to be taken on a magical, nerve-shattering journey - from the snow-covered streets of Copenhagen to the awesome beauty of the Arctic ice caps. A mystery, a love story, and an elegy for a vanishing way of life, Smilla's Sense of Snow is a breathtaking achievement, an exceptional feat of storytelling.",
    fiction=True,
    locations=[copenhagen]
    )

    Review(
    content='Loved this book!',
    book=the_miniaturist
    )

    Review(
    content='AMAZING!',
    book=all_the_light_we_cannot_see
    )

    # save the data to the database
    db.commit()
