<h1 align="center">Welcome to Creative optimisation using computer vision algorithms 👋</h1>

## Project Description :book:
> An image of an Ad creative is used as input for a feature extraction pipeline. The pipeline extracts important features from this image. An Ad creative can contain the following elements:
   <ol>
   <li>Text</li>
   <li>Colour</li>
   <li>Objects</li>
   <li>Logo</li>
   <li>Faces</li>
   <li>CTA button</li>
   <li>Engagement button</li>
   </ol>

> Details such as the object location, emotions, button location, colour etc. are features that can all be derived from an image using the pipeline.
After feature extraction, a regression model is able to determine which features lead to an increase in KPI. The KPIs used in this project are: 
<ol>
<li>Engagement Rate</li>
<li>Click Through Rate</li>
</ol>

> This project has applications in the advertising industry where Ads need to be personalised and contain the right content.

## Project Workflow Diagram :clipboard:
![The workflow diagram for this project](https://github.com/benkart-week-11/creative-optimisation-cv/blob/main/workflow-diagram.png?raw=true)

## Project Structure :file_folder:
```
├─ .DS_Store
├─ .github
│  └─ workflows
│     └─ main_model.yaml
├─ .gitignore
├─ LICENSE
├─ README.md
├─ models
│  ├─ build_model.py
│  └─ model_training.png
├─ notebooks
│  ├─ Aesthetic_Features.ipynb
│  ├─ AssetExtractionExtraction.ipynb
│  ├─ DataExtractor.ipynb
│  ├─ FeatureExtraction.ipynb
│  ├─ FeatureSelection.ipynb
│  ├─ ModelDevelopment.ipynb
│  ├─ text_detection.ipynb
│  └─ web_scrab.ipynb
├─ requirements.txt
└─ scripts
   ├─ CTA_extract.ipynb
   ├─ color_comp_texture.py
   ├─ extract_url.ipynb
   ├─ extractor_pipeline.py
   ├─ feature_extractor.py
   ├─ matching_detector.py
   ├─ multiple_face_detect.py
   ├─ object_detector.py
   ├─ select_asset_id.py
   ├─ text_detect.py
   ├─ unzip.py
   └─ url_to_list.ipynb
```
## Authors :busts_in_silhouette:
<ol>
 <li><a href="https://github.com/KaydeeJR">Janerose Njogu</a></li>
 <li><a href="https://github.com/ekubay">Ekubazgi Gebremariam</a></li>
 <li><a href="https://github.com/degagawolde">Degaga Wolde</a></li>
 <li><a href="https://github.com/michaelgetachew-abebe">Michael Getachew</a></li>
 <li><a href="https://github.com/prubayita">Patrick Rubayita</a></li>
 <li><a href="https://github.com/toussyn">Adijat Ojutomori</a></li>
 </ol>
