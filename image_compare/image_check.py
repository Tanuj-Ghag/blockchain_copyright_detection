# from image_match.goldberg import ImageSignature

# def calc_accuracy(path1, path2):
# 	print(path1, path2)
# 	path1 = str(path1)
# 	path2 = str(path2)
# 	gis = ImageSignature()
# 	a = gis.generate_signature(path1);
# 	b = gis.generate_signature(path2);
# 	dist = gis.normalized_distance(a,b);
# 	return dist;

from PIL import Image
import imagehash

def calc_accuracy(path1, path2):
    try:
        # Open and load the images
        img1 = Image.open(path1)
        img2 = Image.open(path2)

        # Compute the perceptual hash of the images
        hash1 = imagehash.average_hash(img1)
        hash2 = imagehash.average_hash(img2)

        # Calculate the hamming distance between the hashes
        # The Hamming distance is a measure of the number of differing bits between two strings.
        # A lower Hamming distance implies a higher similarity.
        hamming_distance = hash1 - hash2

        return hamming_distance

    except OSError as e:
        print(f"Error: {e}")
        return None
