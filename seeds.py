from pony.orm import db_session
from app import db
from models.Book import Book

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():

    Book(
    title="The Miniaturist",
    author="Jessie Burton",
    isbn="0062306845",
    genre="Historical Fiction",
    pub_date=2015,
    book_jacket="https://upload.wikimedia.org/wikipedia/en/thumb/d/db/TheMiniaturist.jpg/220px-TheMiniaturist.jpg",
    description="Set in seventeenth century Amsterdam—a city ruled by glittering wealth and oppressive religion—a masterful debut steeped in atmosphere and shimmering with mystery, in the tradition of Emma Donoghue, Sarah Waters, and Sarah Dunant.”There is nothing hidden that will not be revealed . . .“On a brisk autumn day in 1686, eighteen-year-old Nella Oortman arrives in Amsterdam to begin a new life as the wife of illustrious merchant trader Johannes Brandt. But her new home, while splendorous, is not welcoming. Johannes is kind yet distant, always locked in his study or at his warehouse office—leaving Nella alone with his sister, the sharp-tongued and forbidding Marin. But Nella’s world changes when Johannes presents her with an extraordinary wedding gift: a cabinet-sized replica of their home. To furnish her gift, Nella engages the services of a miniaturist—an elusive and enigmatic artist whose tiny creations mirror their real-life counterparts in eerie and unexpected ways... Johannes’ gift helps Nella to pierce the closed world of the Brandt household. But as she uncovers its unusual secrets, she begins to understand—and fear—the escalating dangers that await them all. In this repressively pious society where gold is worshipped second only to God, to be different is a threat to the moral fabric of society, and not even a man as rich as Johannes is safe. Only one person seems to see the fate that awaits them. Is the miniaturist the key to their salvation... or the architect of their destruction? Enchanting, beautiful, and exquisitely suspenseful, The Miniaturist is a magnificent story of love and obsession, betrayal and retribution, appearance and truth.",
    fiction=True,
    location="Amsterdam"
    )

    Book(
    title="All the Light We Cannot See",
    author="Anthony Doerr",
    isbn="1501173219",
    genre="Historical Fiction",
    pub_date=2017,
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/81v5wp2zeQL.jpg",
    description="From the highly acclaimed, multiple award-winning Anthony Doerr, the stunningly beautiful instant New York Times bestseller about a blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II. Marie-Laure lives in Paris near the Museum of Natural History, where her father works. When she is twelve, the Nazis occupy Paris and father and daughter flee to the walled citadel of Saint-Malo, where Marie-Laure’s reclusive great uncle lives in a tall house by the sea. With them they carry what might be the museum’s most valuable and dangerous jewel. In a mining town in Germany, Werner Pfennig, an orphan, grows up with his younger sister, enchanted by a crude radio they find that brings them news and stories from places they have never seen or imagined. Werner becomes an expert at building and fixing these crucial new instruments and is enlisted to use his talent to track down the resistance. Deftly interweaving the lives of Marie-Laure and Werner, Doerr illuminates the ways, against all odds, people try to be good to one another. Doerr’s “stunning sense of physical detail and gorgeous metaphors” (San Francisco Chronicle) are dazzling. Ten years in the writing, a National Book Award finalist, All the Light We Cannot See is a magnificent, deeply moving novel from a writer “whose sentences never fail to thrill” (Los Angeles Times).",
    fiction=True,
    location="Paris"
    )

    Book(
    title="In Cold Blood",
    author="Truman Capote",
    isbn="0679745580",
    genre="True Crime",
    book_jacket="https://images-na.ssl-images-amazon.com/images/I/51HX%2B6nWkqL._SX303_BO1,204,203,200_.jpg",
    pub_date=1965,
    description="On November 15, 1959, in the small town of Holcomb, Kansas, four members of the Clutter family were savagely murdered by blasts from a shotgun held a few inches from their faces. There was no apparent motive for the crime, and there were almost no clues. As Truman Capote reconstructs the murder and the investigation that led to the capture, trial, and execution of the killers, he generates both mesmerizing suspense and astonishing empathy. In Cold Blood is a work that transcends its moment, yielding poignant insights into the nature of American violence.",
    fiction=False,
    location="Kansas"
    )

    # save the data to the database
    db.commit()
