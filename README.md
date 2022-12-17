# CMSC848C_explain_viz

## Setup for LYTNetV2 + LIME

0. Activate python env if desired
1. ``pip install -r requirements.txt``
2. Download LYTNetV2 test dataset from <https://dl.orangedox.com/9ZvH36> and edit ``test_image_directory`` in eye-lime.ipynb to match
3. Run lime-notebook/tutorial-pytorch-catdog.ipynb for LIME;
        Or eye-lime.ipynb for LYTNetV2 + LIME


## Setup for GIT2 Captioner

0. Ensure image to caption is saved (i.e. save output from LIME)
1. ``pip install -r git2-reqs.txt``
2. ``python setup.py build develop``
3. ``cd GenerativeImage2Text``

4a. For one image,
 		
		``AZFUSE_TSV_USE_FUSE=1 python -m generativeimage2text.inference -p "{'type': 'test_git_inference_single_image', \
      		
		'image_path': 'PATH_TO_IMG' \
            	
		'model_name': 'GIT_BASE', \
	        
		'prefix': '', \
	  	
		}"``
	  
4b. For multiple (n) images, 

		``AZFUSE_TSV_USE_FUSE=1 python -m generativeimage2text.inference -p "{'type': 'test_git_inference_single_image', \
     		
		'image_path': ['PATH_TO_IMG_1', ... 'PATH_TO_IMG_N']\
        	
		'model_name': 'GIT_BASE_VATEX', \
	        
		'prefix': '', \
	  	
		}"``

5. Final output should be caption


## Instructions for Manual (Five) Crop + Captioning

0. Activate LIME environment
1. ``python pre_caption_prep.py {PATH_TO_IMG}``
2. Copy output for list of images to caption
3. Deactivate LIME and activate GIT2 environment
4. Run GIT2 command for multiple images (see 4b above) and use previous output  for `image_path`
5. Use captions and pick essential ones for TTS
6. Run TTS on merged final caption and save audio file
