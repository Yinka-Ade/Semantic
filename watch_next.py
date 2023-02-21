import spacy

nlp = spacy.load('en_core_web_md')

sample = f'''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator
'''

def compare_movies(sample:str) -> str:

    # Read in movies text file
    # Readlines of he text file
    file = open('movies.txt', 'r')
    data = file.readlines()
    
    # Create an empty dictionary where the key is the movie title and
    # the value is the movie discription
    holder = {}
    # Iterate over the text file, strip new line character and split by :
    # Create the dictionary by assigning the first index as the title and 
    # the second index as the movie discription
    
    for line in data:
        split_data = line.strip('\n').split(' :')
        holder[split_data[0]] = split_data[1]
    
    # Initialize maximum similarity as 0 and best match as an empty string
    max_similarity = 0
    best_match = ''

    # Iterate over the dictionary item
    # Check simillarity between the movie sample and the movies in the dictionary
    for title, desc in holder.items():
        similarity = nlp(sample).similarity(nlp(desc))
        # Check for the maximum similarity
        # Make the best match as the title
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = title
            # If best match equals to the title, get the description of the best match key
            if best_match == title:
                movie_description = holder[title]
    return(f'''{best_match}: 
    Description: {movie_description}''')


print(compare_movies(sample))