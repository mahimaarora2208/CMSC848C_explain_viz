n=$1
AZFUSE_TSV_USE_FUSE=1 python -m generativeimage2text.inference -p "{'type': 'test_git_inference_single_image','image_path': '../img${n}/img${n}_0.png','model_name': 'GIT_BASE', 'prefix': '', }"
