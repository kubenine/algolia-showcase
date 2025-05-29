from django.core.management.base import BaseCommand
from catalogue.models import Book
import random


class Command(BaseCommand):
    help = 'Load sample books for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Number of books to create (default: 50)',
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Sample data - Expanded for ~100+ books
        titles = [
            # Classic Literature
            "The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice",
            "The Catcher in the Rye", "Lord of the Flies", "Animal Farm", "Brave New World",
            "Jane Eyre", "Wuthering Heights", "Great Expectations", "Oliver Twist",
            "A Tale of Two Cities", "David Copperfield", "The Picture of Dorian Gray",
            "Frankenstein", "Dracula", "Dr. Jekyll and Mr. Hyde", "Heart of Darkness",
            "The Stranger", "The Metamorphosis", "Crime and Punishment", "War and Peace",
            "Anna Karenina", "The Brothers Karamazov", "One Flew Over the Cuckoo's Nest",
            "Of Mice and Men", "The Grapes of Wrath", "East of Eden", "Slaughterhouse-Five",
            
            # Fantasy & Science Fiction
            "The Lord of the Rings", "The Hobbit", "Harry Potter and the Philosopher's Stone",
            "The Chronicles of Narnia", "Dune", "Foundation", "The Hitchhiker's Guide to the Galaxy",
            "Ender's Game", "The Martian", "Ready Player One", "Neuromancer", "Blade Runner",
            "The Left Hand of Darkness", "Hyperion", "The Time Machine", "Fahrenheit 451",
            "I, Robot", "2001: A Space Odyssey", "The War of the Worlds", "A Wrinkle in Time",
            "The Giver", "The Handmaid's Tale", "Station Eleven", "The Road", "Never Let Me Go",
            "The Fifth Season", "The Name of the Wind", "The Way of Kings", "American Gods",
            "Good Omens", "The Ocean at the End of the Lane", "The Dark Tower", "It",
            
            # Young Adult & Contemporary
            "The Hunger Games", "Divergent", "The Maze Runner", "The Fault in Our Stars",
            "Looking for Alaska", "The Perks of Being a Wallflower", "Thirteen Reasons Why",
            "Eleanor Oliphant Is Completely Fine", "The Seven Husbands of Evelyn Hugo",
            "Where the Crawdads Sing", "The Silent Patient", "Big Little Lies", "Gone Girl",
            "The Girl with the Dragon Tattoo", "The Girl on the Train", "In the Woods",
            "The Lovely Bones", "Life of Pi", "The Kite Runner", "A Thousand Splendid Suns",
            "The Book Thief", "All the Light We Cannot See", "The Nightingale", "Educated",
            
            # Literary Fiction
            "One Hundred Years of Solitude", "Love in the Time of Cholera", "Beloved",
            "The God of Small Things", "Midnight's Children", "The White Tiger", "Shantaram",
            "The Namesake", "Interpreter of Maladies", "The Joy Luck Club", "Memoirs of a Geisha",
            "Snow Flower and the Secret Fan", "The Help", "Water for Elephants",
            "The Time Traveler's Wife", "The Alchemist", "Life After Life", "Cloud Atlas",
            "The Curious Incident of the Dog in the Night-Time", "Extremely Loud and Incredibly Close",
            "Everything Is Illuminated", "The Brief Wondrous Life of Oscar Wao", "Middlesex",
            
            # Mystery & Thriller
            "The Da Vinci Code", "Angels and Demons", "The Murder of Roger Ackroyd",
            "And Then There Were None", "The Big Sleep", "The Maltese Falcon", "In Cold Blood",
            "The Silence of the Lambs", "Red Dragon", "The Talented Mr. Ripley", "Rebecca",
            "The Woman in White", "The Moonstone", "The Hound of the Baskervilles",
            "Murder on the Orient Express", "The ABC Murders", "Hercule Poirot's Christmas",
            "The Thursday Murder Club", "The Maid", "The Guest List", "Rock Paper Scissors",
            
            # Historical Fiction
            "All Quiet on the Western Front", "The Pillars of the Earth", "Wolf Hall",
            "Bring Up the Bodies", "The Other Boleyn Girl", "Outlander", "Cold Mountain",
            "The English Patient", "Atonement", "Birdsong", "Memoirs of a Geisha",
            "The Poisonwood Bible", "The Secret History", "The Goldfinch", "Donna Tartt",
            
            # Modern Classics & Award Winners
            "The Remains of the Day", "Never Let Me Go", "Klara and the Sun", "The Buried Giant",
            "Lincoln in the Bardo", "The Sellout", "Colson Whitehead", "The Underground Railroad",
            "The Nickel Boys", "Hamnet", "The Vanishing Half", "Such a Fun Age",
            "Normal People", "Conversations with Friends", "My Education", "The Power"
        ]
        
        authors = [
            # Classic Authors
            "F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen",
            "J.D. Salinger", "William Golding", "Aldous Huxley", "Charlotte Brontë", "Emily Brontë",
            "Charles Dickens", "Oscar Wilde", "Mary Shelley", "Bram Stoker", "Robert Louis Stevenson",
            "Joseph Conrad", "Albert Camus", "Franz Kafka", "Fyodor Dostoevsky", "Leo Tolstoy",
            "Ken Kesey", "John Steinbeck", "Kurt Vonnegut",
            
            # Fantasy & Sci-Fi Authors
            "J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis", "Frank Herbert", "Isaac Asimov",
            "Douglas Adams", "Orson Scott Card", "Andy Weir", "Ernest Cline", "William Gibson",
            "Philip K. Dick", "Ursula K. Le Guin", "Dan Simmons", "H.G. Wells", "Ray Bradbury",
            "Madeleine L'Engle", "Lois Lowry", "Margaret Atwood", "Emily St. John Mandel",
            "Cormac McCarthy", "Kazuo Ishiguro", "N.K. Jemisin", "Patrick Rothfuss", "Brandon Sanderson",
            "Neil Gaiman", "Terry Pratchett", "Stephen King",
            
            # Contemporary & YA Authors
            "Suzanne Collins", "Veronica Roth", "James Dashner", "John Green", "Stephen Chbosky",
            "Jay Asher", "Gail Honeyman", "Taylor Jenkins Reid", "Delia Owens", "Alex Michaelides",
            "Liane Moriarty", "Gillian Flynn", "Paula Hawkins", "Tana French", "Alice Sebold",
            "Yann Martel", "Khaled Hosseini", "Markus Zusak", "Anthony Doerr", "Kristin Hannah",
            "Tara Westover",
            
            # Literary Fiction Authors
            "Gabriel García Márquez", "Toni Morrison", "Arundhati Roy", "Salman Rushdie",
            "Aravind Adiga", "Gregory David Roberts", "Jhumpa Lahiri", "Amy Tan", "Arthur Golden",
            "Lisa See", "Kathryn Stockett", "Sara Gruen", "Audrey Niffenegger", "Paulo Coelho",
            "Kate Atkinson", "David Mitchell", "Mark Haddon", "Jonathan Safran Foer",
            "Junot Díaz", "Jeffrey Eugenides",
            
            # Mystery & Thriller Authors
            "Dan Brown", "Agatha Christie", "Raymond Chandler", "Dashiell Hammett", "Truman Capote",
            "Thomas Harris", "Patricia Highsmith", "Daphne du Maurier", "Wilkie Collins",
            "Arthur Conan Doyle", "Richard Osman", "Nita Prose", "Lucy Foley", "Alice Feeney",
            
            # Historical Fiction Authors
            "Erich Maria Remarque", "Ken Follett", "Hilary Mantel", "Philippa Gregory",
            "Diana Gabaldon", "Charles Frazier", "Michael Ondaatje", "Ian McEwan", "Sebastian Faulks",
            "Barbara Kingsolver", "Donna Tartt",
            
            # Modern/Award-winning Authors
            "Kazuo Ishiguro", "George Saunders", "Paul Beatty", "Colson Whitehead", "Maggie O'Farrell",
            "Brit Bennett", "Kiley Reid", "Sally Rooney", "Naomi Alderman", "Elena Ferrante",
            "Chimamanda Ngozi Adichie", "Zadie Smith", "Jennifer Egan", "Celeste Ng", "Min Jin Lee"
        ]
        
        genres = [
            "Fiction", "Science Fiction", "Fantasy", "Mystery", "Romance", "Thriller",
            "Historical Fiction", "Young Adult", "Literary Fiction", "Dystopian",
            "Adventure", "Contemporary Fiction", "Classic Literature", "Magical Realism",
            "Crime", "Horror", "Biography", "Non-Fiction", "Philosophy", "Poetry",
            "Memoir", "True Crime", "Gothic Fiction", "Speculative Fiction", "Steampunk",
            "Urban Fantasy", "Post-Apocalyptic", "Cyberpunk", "Space Opera", "Time Travel",
            "Victorian Literature", "Modernist Literature", "Postmodern Fiction", "Noir",
            "Psychological Thriller", "Domestic Fiction", "Coming of Age", "War Fiction",
            "Southern Gothic", "Feminist Literature", "Postcolonial Literature"
        ]
        
        descriptions = [
            "A captivating tale that explores the depths of human nature and society.",
            "An epic journey through time and space that will leave you breathless.",
            "A thought-provoking story that challenges conventional wisdom.",
            "A beautifully written narrative about love, loss, and redemption.",
            "An unforgettable adventure that spans generations.",
            "A gripping thriller that keeps you on the edge of your seat.",
            "A poignant exploration of family, identity, and belonging.",
            "A masterful work that blends reality with imagination.",
            "A compelling story of courage, sacrifice, and hope.",
            "An intricate plot filled with unexpected twists and turns.",
            "A profound meditation on life, death, and everything in between.",
            "A richly detailed world that comes alive on every page.",
            "A heart-wrenching tale of survival against all odds.",
            "A brilliant examination of power, corruption, and justice.",
            "A sweeping saga that captures the essence of an era.",
            "A tender story about the bonds that connect us all.",
            "A dark and haunting narrative that lingers long after reading.",
            "A witty and insightful commentary on modern society.",
            "A magical realism masterpiece that defies categorization.",
            "A timeless classic that speaks to readers of all ages.",
            "A dystopian vision that feels eerily relevant today.",
            "A psychological exploration of the human condition.",
            "A lyrical and atmospheric tale of mystery and wonder.",
            "A powerful story of resilience and transformation.",
            "An intimate portrait of love and relationships.",
            "A genre-defying work that pushes literary boundaries.",
            "A nostalgic journey through memory and time.",
            "A thriller that combines suspense with deep character development.",
            "A coming-of-age story that resonates across generations.",
            "A historical epic that brings the past vividly to life.",
            "A science fiction adventure with philosophical undertones.",
            "A fantasy tale rich in mythology and world-building.",
            "A mystery that challenges readers to solve the puzzle.",
            "A romance that explores the complexities of human emotion.",
            "A literary masterpiece that redefines the genre.",
            "A speculative fiction work that imagines possible futures.",
            "A memoir-like narrative that feels authentically lived.",
            "A multi-generational story spanning decades.",
            "A psychological study of characters under pressure.",
            "A social commentary wrapped in compelling storytelling."
        ]
        
        # Clear existing books if any
        if Book.objects.exists():
            self.stdout.write(
                self.style.WARNING(f'Deleting {Book.objects.count()} existing books...')
            )
            Book.objects.all().delete()
        
        # Create sample books
        books_created = 0
        for i in range(count):
            title = random.choice(titles)
            author = random.choice(authors)
            genre = random.choice(genres)
            description = random.choice(descriptions)
            published_year = random.randint(1950, 2024)
            
            # Avoid duplicates
            if not Book.objects.filter(title=title, author=author).exists():
                Book.objects.create(
                    title=title,
                    author=author,
                    genre=genre,
                    description=description,
                    published_year=published_year
                )
                books_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {books_created} sample books!')
        )
        
        # Show some stats
        total_books = Book.objects.count()
        unique_authors = Book.objects.values('author').distinct().count()
        unique_genres = Book.objects.values('genre').distinct().count()
        
        self.stdout.write(f'Total books in database: {total_books}')
        self.stdout.write(f'Unique authors: {unique_authors}')
        self.stdout.write(f'Unique genres: {unique_genres}') 