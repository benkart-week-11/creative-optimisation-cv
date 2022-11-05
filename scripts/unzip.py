import zipfile
with zipfile.ZipFile("/home/michael_getachew/creative-optimization/creative-optimisation-cv/scripts/Challenge_Data.zip", 'r') as zip_ref:
    zip_ref.extractall("/home/michael_getachew/creative-optimization/creative-optimisation-cv/data/")