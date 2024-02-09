import sys
import os
import  tkinter as tk
import tkinter.messagebox as tk1
import tkinter.filedialog
from pathlib import Path
import time
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import clip
from PIL import Image
from IPython.display import Image
from IPython.core.display import HTML

def vector_search(user_query):

    # Set the paths
    dataset_version = "lite"  # choose "lite" or "full"
    # unsplash_dataset_path = Path("unsplash-dataset") / dataset_version
    unsplash_dataaset_path = OUTPUT_PATH = Path(__file__).parent.parent / "images"
    # features_path = Path("unsplash-dataset") / dataset_version / "features"
    features_path = Path(__file__).parent.parent / "images" / "features"

    # Read the photos table
    # photos = pd.read_csv(unsplash_dataset_path / "photos.tsv000", sep='\t', header=0)

    # Load the features and the corresponding IDs
    photo_features = np.load(features_path / "features.npy")
    photo_ids = pd.read_csv(features_path / "photo_ids.csv")
    photo_ids = list(photo_ids['photo_id'])
    import clip
    import torch

    # Load the open CLIP model
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    search_query = user_query

    with torch.no_grad():
        # Encode and normalize the description using CLIP
        text_encoded = model.encode_text(clip.tokenize(search_query).to(device))
        text_encoded /= text_encoded.norm(dim=-1, keepdim=True)


    # Load the model
    model, preprocess = clip.load("ViT-B/32", device="cuda" if torch.cuda.is_available() else "cpu")

    # Prepare the text
    text = clip.tokenize(["a photo of a cat", "a photo of a dog"]).to(device)

    # Prepare the image
    # image_path = "/Users/samaylakhani/Documents/GitHub/imagine/temp/local_image.png"
    # image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

    # Calculate features
    with torch.no_grad():
        text_features = model.encode_text

        # Retrieve the description vector and the photo vectors
    text_features = text_encoded.cpu().numpy()

    # Compute the similarity between the descrption and each photo using the Cosine similarity
    similarities = list((text_features @ photo_features.T).squeeze(0))

    # Sort the photos by their similarity score
    best_photos = sorted(zip(similarities, range(photo_features.shape[0])), key=lambda x: x[0], reverse=True)



    listIDs = []
    # Iterate over the top 3 results
    for i in range(5):
        # Retrieve the photo ID
        idx = best_photos[i][1]
        photo_id = photo_ids[idx]
        listIDs.append(photo_id)
        # Get all metadata for this photo
        # photo_data = photos[photos["photo_id"] == photo_id].iloc[0]

        # Display the photo
        # display(Image(url=photo_data["photo_image_url"] + "?w=640"))

        # Display the attribution text
        # display(HTML(f'Photo by <a href="https://unsplash.com/@{photo_data["photographer_username"]}?utm_source=NaturalLanguageImageSearch&utm_medium=referral">{photo_data["photographer_first_name"]} {photo_data["photographer_last_name"]}</a> on <a href="https://unsplash.com/?utm_source=NaturalLanguageImageSearch&utm_medium=referral">Unsplash</a>'))
        print()
        
    print(
        "The top 3 photos that match the search query are:",
        listIDs
    )
    listIDs = [int(name.split('_')[-1]) for name in listIDs]

    return listIDs

vector_search("A forest fire.")
