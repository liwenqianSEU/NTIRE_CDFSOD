# NTIRE2025_CDFSOD
## The Environments
The evaluation environments we adopted are recorded in the following section. Below are the system requirements and setup instructions for reproducing the evaluation environment.

### Required Environment Setup

- **Step 1**: conda environment create:
  ```bash
    conda create -n cdfsod python=3.9
    conda activate cdfsod
- **Step 2**: install other libs:
  ```bash
    cd NTIRE2025_CDFSOD
    pip install -r requirements.txt
    python -m pip install -e ./
    pip install -e ./
or take it as a reference based on your original environments.

## The Validation Datasets
We take COCO as source data and ArTaxOr, Clipart1k, and DeepFish as validation datasets.

The target datasets could be easily downloaded in the following links: 
- [Dataset and Weights Link from Google Drive](https://drive.google.com/drive/folders/16SDv_V7RDjTKDk8uodL2ubyubYTMdd5q?usp=drive_link)

## The Test Datasets
**The testing datasets could be easily downloaded in the following links:**
- **[Dataset Link from Google Drive](https://drive.google.com/drive/folders/1Pewv7HYacwD5Rrknp5EiAdw8vMbaaFAA?usp=sharing)**

They are organized as follows:

```bash
|NTIRE2025_CDFSOD/datasets/
|--clipart1k/
|   |--annotations
|   |--test
|   |--train
|--ArTaxOr/
|   |--annotations
|   |--test
|   |--train
|--......
```
And the weights should be organized as follows:
```bash
|NTIRE2025_CDFSOD/weights/
|--trained/
|   |--vitl_0089999.pth
|--background/
|   |--background_prototypes.vitl14.pth
```

## Test the baseline model
As the environment is ready, select a different baseline to test
### Run
```
bash main_results.sh
```
## References
```
@inproceedings{fu2025cross,
  title={Cross-domain few-shot object detection via enhanced open-set object detector},
  author={Fu, Yuqian and Wang, Yu and Pan, Yixuan and Huai, Lian and Qiu, Xingyu and Shangguan, Zeyu and Liu, Tong and Fu, Yanwei and Van Gool, Luc and Jiang, Xingqun},
  booktitle={European Conference on Computer Vision},
  pages={247--264},
  year={2025},
  organization={Springer}
}
```
```
@inproceedings{fu2023styleadv,
  title={Styleadv: Meta style adversarial training for cross-domain few-shot learning},
  author={Fu, Yuqian and Xie, Yu and Fu, Yanwei and Jiang, Yu-Gang},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={24575--24584},
  year={2023}
}

@inproceedings{fu2021meta,
  title={Meta-fdmixup: Cross-domain few-shot learning guided by labeled target data},
  author={Fu, Yuqian and Fu, Yanwei and Jiang, Yu-Gang},
  booktitle={Proceedings of the 29th ACM international conference on multimedia},
  pages={5326--5334},
  year={2021}
}

```
