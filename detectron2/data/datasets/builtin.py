# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.


"""
This file registers pre-defined datasets at hard-coded paths, and their metadata.

We hard-code metadata for common datasets. This will enable:
1. Consistency check when loading the datasets
2. Use models on these standard datasets directly and run demos,
   without having to download the dataset annottions

We hard-code some paths to the dataset that's assumed to
exist in "./datasets/".

Users SHOULD NOT use this file to create new dataset / metadata for new dataset.
To add new dataset, refer to the tutorial "docs/DATASETS.md".
"""

import os

from detectron2.data import DatasetCatalog, MetadataCatalog

from .builtin_meta import ADE20K_SEM_SEG_CATEGORIES, _get_builtin_metadata
from .cityscapes import load_cityscapes_instances, load_cityscapes_semantic
from .cityscapes_panoptic import register_all_cityscapes_panoptic
from .coco import load_sem_seg, register_coco_instances
from .coco_panoptic import register_coco_panoptic, register_coco_panoptic_separated
from .lvis import get_lvis_instances_meta, register_lvis_instances
from .pascal_voc import register_pascal_voc

from detectron2.data.datasets.coco import load_coco_json
import json
from detectron2.data.datasets import register_coco_instances
# ==== Predefined datasets and splits for COCO ==========

_PREDEFINED_SPLITS_COCO = {}
_PREDEFINED_SPLITS_COCO["coco"] = {
    "coco_2014_train": ("coco/train2014", "coco/annotations/instances_train2014.json"),
    "coco_2014_val": ("coco/val2014", "coco/annotations/instances_val2014.json"),
    "coco_2014_minival": ("coco/val2014", "coco/annotations/instances_minival2014.json"),
    "coco_2014_minival_100": ("coco/val2014", "coco/annotations/instances_minival2014_100.json"),
    "coco_2014_valminusminival": (
        "coco/val2014",
        "coco/annotations/instances_valminusminival2014.json",
    ),
    "coco_2017_train": ("coco/train2017", "coco/annotations/instances_train2017.json"),
    "coco_2017_val": ("coco/val2017", "coco/annotations/instances_val2017.json"),
    "coco_2017_test": ("coco/test2017", "coco/annotations/image_info_test2017.json"),
    "coco_2017_test-dev": ("coco/test2017", "coco/annotations/image_info_test-dev2017.json"),
    "coco_2017_val_100": ("coco/val2017", "coco/annotations/instances_val2017_100.json"),
}
_PREDEFINED_SPLITS_COCO["coco_ovd"] = {
    "coco_2017_ovd_all_train": ("coco/train2017", "coco/annotations/ovd_ins_train2017_all.json"),
    "coco_2017_ovd_b_train": ("coco/train2017", "coco/annotations/ovd_ins_train2017_b.json"),
    "coco_2017_ovd_t_train": ("coco/train2017", "coco/annotations/ovd_ins_train2017_t.json"),
    "coco_2017_ovd_all_test": ("coco/val2017", "coco/annotations/ovd_ins_val2017_all.json"),
    "coco_2017_ovd_b_test": ("coco/val2017", "coco/annotations/ovd_ins_val2017_b.json"),
    "coco_2017_ovd_t_test": ("coco/val2017", "coco/annotations/ovd_ins_val2017_t.json"),

    
    "fs_coco17_base_train": ("coco/train2017", "coco/annotations/fs_coco17_base_train.json"),
    "fs_coco17_base_val": ("coco/val2017", "coco/annotations/fs_coco17_base_val.json"),   
    # fs coco training datasets
    "fs_coco14_base_train": ("coco/train2014", "coco/annotations/fs_coco14_base_train.json"),
    "fs_coco14_base_val": ("coco/val2014", "coco/annotations/fs_coco14_base_val.json"),   

    "coco_2017_novel_oneshot_s1_r50": ("coco/train2017", "coco/annotations/coco_2017_novel_oneshot_s1_r50.json"),   
    "coco_2017_novel_oneshot_s2_r50": ("coco/train2017", "coco/annotations/coco_2017_novel_oneshot_s2_r50.json"),   
    "coco_2017_novel_oneshot_s3_r50": ("coco/train2017", "coco/annotations/coco_2017_novel_oneshot_s3_r50.json"),   
    "coco_2017_novel_oneshot_s4_r50": ("coco/train2017", "coco/annotations/coco_2017_novel_oneshot_s4_r50.json"),   

    
    "coco_2017_train_oneshot_s1": ("coco/train2017", "coco/annotations/coco_2017_train_oneshot_s1.json"),
    "coco_2017_train_oneshot_s2": ("coco/train2017", "coco/annotations/coco_2017_train_oneshot_s2.json"),
    "coco_2017_train_oneshot_s3": ("coco/train2017", "coco/annotations/coco_2017_train_oneshot_s3.json"),
    "coco_2017_train_oneshot_s4": ("coco/train2017", "coco/annotations/coco_2017_train_oneshot_s4.json"),
    
    "coco_2017_val_oneshot_s1": ("coco/val2017", "coco/annotations/coco_2017_val_oneshot_s1.json"),
    "coco_2017_val_oneshot_s2": ("coco/val2017", "coco/annotations/coco_2017_val_oneshot_s2.json"),
    "coco_2017_val_oneshot_s3": ("coco/val2017", "coco/annotations/coco_2017_val_oneshot_s3.json"),
    "coco_2017_val_oneshot_s4": ("coco/val2017", "coco/annotations/coco_2017_val_oneshot_s4.json"),   
}


_PREDEFINED_SPLITS_COCO["coco_person"] = {
    "keypoints_coco_2014_train": (
        "coco/train2014",
        "coco/annotations/person_keypoints_train2014.json",
    ),
    "keypoints_coco_2014_val": ("coco/val2014", "coco/annotations/person_keypoints_val2014.json"),
    "keypoints_coco_2014_minival": (
        "coco/val2014",
        "coco/annotations/person_keypoints_minival2014.json",
    ),
    "keypoints_coco_2014_valminusminival": (
        "coco/val2014",
        "coco/annotations/person_keypoints_valminusminival2014.json",
    ),
    "keypoints_coco_2014_minival_100": (
        "coco/val2014",
        "coco/annotations/person_keypoints_minival2014_100.json",
    ),
    "keypoints_coco_2017_train": (
        "coco/train2017",
        "coco/annotations/person_keypoints_train2017.json",
    ),
    "keypoints_coco_2017_val": ("coco/val2017", "coco/annotations/person_keypoints_val2017.json"),
    "keypoints_coco_2017_val_100": (
        "coco/val2017",
        "coco/annotations/person_keypoints_val2017_100.json",
    ),
}


_PREDEFINED_SPLITS_COCO_PANOPTIC = {
    "coco_2017_train_panoptic": (
        # This is the original panoptic annotation directory
        "coco/panoptic_train2017",
        "coco/annotations/panoptic_train2017.json",
        # This directory contains semantic annotations that are
        # converted from panoptic annotations.
        # It is used by PanopticFPN.
        # You can use the script at detectron2/datasets/prepare_panoptic_fpn.py
        # to create these directories.
        "coco/panoptic_stuff_train2017",
    ),
    "coco_2017_val_panoptic": (
        "coco/panoptic_val2017",
        "coco/annotations/panoptic_val2017.json",
        "coco/panoptic_stuff_val2017",
    ),
    "coco_2017_val_100_panoptic": (
        "coco/panoptic_val2017_100",
        "coco/annotations/panoptic_val2017_100.json",
        "coco/panoptic_stuff_val2017_100",
    ),
}


def register_all_coco(root):
    for dataset_name, splits_per_dataset in _PREDEFINED_SPLITS_COCO.items():
        if dataset_name == 'coco_ovd':  # for zero-shot split
            for key, (image_root, json_file) in splits_per_dataset.items():
                # Assume pre-defined datasets live in `./datasets`.
                register_coco_instances(
                    key,
                    {}, # empty metadata, it will be overwritten in load_coco_json() function
                    os.path.join(root, json_file) if "://" not in json_file else json_file,
                    os.path.join(root, image_root),
                )
        else: # default splits
            for key, (image_root, json_file) in splits_per_dataset.items():
                # Assume pre-defined datasets live in `./datasets`.
                register_coco_instances(
                    key,
                    _get_builtin_metadata(dataset_name),
                    os.path.join(root, json_file) if "://" not in json_file else json_file,
                    os.path.join(root, image_root),
                )

    for (
        prefix,
        (panoptic_root, panoptic_json, semantic_root),
    ) in _PREDEFINED_SPLITS_COCO_PANOPTIC.items():
        prefix_instances = prefix[: -len("_panoptic")]
        instances_meta = MetadataCatalog.get(prefix_instances)
        image_root, instances_json = instances_meta.image_root, instances_meta.json_file
        # The "separated" version of COCO panoptic segmentation dataset,
        # e.g. used by Panoptic FPN
        register_coco_panoptic_separated(
            prefix,
            _get_builtin_metadata("coco_panoptic_separated"),
            image_root,
            os.path.join(root, panoptic_root),
            os.path.join(root, panoptic_json),
            os.path.join(root, semantic_root),
            instances_json,
        )
        # The "standard" version of COCO panoptic segmentation dataset,
        # e.g. used by Panoptic-DeepLab
        register_coco_panoptic(
            prefix,
            _get_builtin_metadata("coco_panoptic_standard"),
            image_root,
            os.path.join(root, panoptic_root),
            os.path.join(root, panoptic_json),
            instances_json,
        )

# ==== Predefined datasets and splits for LVIS ==========


_PREDEFINED_SPLITS_LVIS = {
    # openset setting
    "lvis_v1": {
        "lvis_v1_train": ("coco/", "lvis/lvis_v1_train.json"),
        "lvis_v1_val": ("coco/", "lvis/lvis_v1_val.json"),
        "lvis_v1_test_dev": ("coco/", "lvis/lvis_v1_image_info_test_dev.json"),
        "lvis_v1_test_challenge": ("coco/", "lvis/lvis_v1_image_info_test_challenge.json"),
    },
    # custom image setting
    "lvis_v1_custom_img": {
        "lvis_v1_train_custom_img": ("coco/", "lvis/lvis_v1_train.json"),
        "lvis_v1_val_custom_img": ("coco/", "lvis/lvis_v1_val.json"),
        "lvis_v1_test_dev_custom_img": ("coco/", "lvis/lvis_v1_image_info_test_dev.json"),
        "lvis_v1_test_challenge_custom_img": ("coco/", "lvis/lvis_v1_image_info_test_challenge.json"),
    },
    # regular fully supervised setting
    "lvis_v1_fullysup": {
        "lvis_v1_train_fullysup": ("coco/", "lvis/lvis_v1_train.json"),
        "lvis_v1_val_fullysup": ("coco/", "lvis/lvis_v1_val.json"),
        "lvis_v1_test_dev_fullysup": ("coco/", "lvis/lvis_v1_image_info_test_dev.json"),
        "lvis_v1_test_challenge_fullysup": ("coco/", "lvis/lvis_v1_image_info_test_challenge.json"),
    },
    "lvis_v0.5": {
        "lvis_v0.5_train": ("coco/", "lvis/lvis_v0.5_train.json"),
        "lvis_v0.5_val": ("coco/", "lvis/lvis_v0.5_val.json"),
        "lvis_v0.5_val_rand_100": ("coco/", "lvis/lvis_v0.5_val_rand_100.json"),
        "lvis_v0.5_test": ("coco/", "lvis/lvis_v0.5_image_info_test.json"),
    },
    "lvis_v0.5_cocofied": {
        "lvis_v0.5_train_cocofied": ("coco/", "lvis/lvis_v0.5_train_cocofied.json"),
        "lvis_v0.5_val_cocofied": ("coco/", "lvis/lvis_v0.5_val_cocofied.json"),
    },
}


def register_all_lvis(root):
    for dataset_name, splits_per_dataset in _PREDEFINED_SPLITS_LVIS.items():
        for key, (image_root, json_file) in splits_per_dataset.items():
            if dataset_name == "lvis_v1":
                args = {'filter_open_cls': True, 'run_custom_img': False}
            elif dataset_name == 'lvis_v1_custom_img':
                args = {'filter_open_cls': False, 'run_custom_img': True}
            elif dataset_name == 'lvis_v1_fullysup':
                args = {'filter_open_cls': False, 'run_custom_img': False}
            register_lvis_instances(
                key,
                get_lvis_instances_meta(dataset_name),
                os.path.join(root, json_file) if "://" not in json_file else json_file,
                os.path.join(root, image_root),
                args,
            )


# ==== Predefined splits for raw cityscapes images ===========
_RAW_CITYSCAPES_SPLITS = {
    "cityscapes_fine_{task}_train": ("cityscapes/leftImg8bit/train/", "cityscapes/gtFine/train/"),
    "cityscapes_fine_{task}_val": ("cityscapes/leftImg8bit/val/", "cityscapes/gtFine/val/"),
    "cityscapes_fine_{task}_test": ("cityscapes/leftImg8bit/test/", "cityscapes/gtFine/test/"),
}


def register_all_cityscapes(root):
    for key, (image_dir, gt_dir) in _RAW_CITYSCAPES_SPLITS.items():
        meta = _get_builtin_metadata("cityscapes")
        image_dir = os.path.join(root, image_dir)
        gt_dir = os.path.join(root, gt_dir)

        inst_key = key.format(task="instance_seg")
        DatasetCatalog.register(
            inst_key,
            lambda x=image_dir, y=gt_dir: load_cityscapes_instances(
                x, y, from_json=True, to_polygons=True
            ),
        )
        MetadataCatalog.get(inst_key).set(
            image_dir=image_dir, gt_dir=gt_dir, evaluator_type="cityscapes_instance", **meta
        )

        sem_key = key.format(task="sem_seg")
        DatasetCatalog.register(
            sem_key, lambda x=image_dir, y=gt_dir: load_cityscapes_semantic(x, y)
        )
        MetadataCatalog.get(sem_key).set(
            image_dir=image_dir,
            gt_dir=gt_dir,
            evaluator_type="cityscapes_sem_seg",
            ignore_label=255,
            **meta,
        )


# ==== Predefined splits for PASCAL VOC ===========
def register_all_pascal_voc(root):
    SPLITS = [
        ("voc_2007_trainval", "VOC2007", "trainval"),
        ("voc_2007_train", "VOC2007", "train"),
        ("voc_2007_val", "VOC2007", "val"),
        ("voc_2007_test", "VOC2007", "test"),
        ("voc_2012_trainval", "VOC2012", "trainval"),
        ("voc_2012_train", "VOC2012", "train"),
        ("voc_2012_val", "VOC2012", "val"),
    ]
    for name, dirname, split in SPLITS:
        year = 2007 if "2007" in name else 2012
        register_pascal_voc(name, os.path.join(root, dirname), split, year)
        MetadataCatalog.get(name).evaluator_type = "pascal_voc"


def register_all_ade20k(root):
    root = os.path.join(root, "ADEChallengeData2016")
    for name, dirname in [("train", "training"), ("val", "validation")]:
        image_dir = os.path.join(root, "images", dirname)
        gt_dir = os.path.join(root, "annotations_detectron2", dirname)
        name = f"ade20k_sem_seg_{name}"
        DatasetCatalog.register(
            name, lambda x=image_dir, y=gt_dir: load_sem_seg(y, x, gt_ext="png", image_ext="jpg")
        )
        MetadataCatalog.get(name).set(
            stuff_classes=ADE20K_SEM_SEG_CATEGORIES[:],
            image_root=image_dir,
            sem_seg_root=gt_dir,
            evaluator_type="sem_seg",
            ignore_label=255,
        )


_PREDEFINED_CD = [
    ("DIOR_train", "DIOR/train/new_train", "DIOR/annotations/train.json"),
    ("DIOR_test", "DIOR/test/new_test", "DIOR/annotations/test.json"),
    ("ArTaxOr_train", "ArTaxOr/train", "ArTaxOr/annotations/train.json"),
    ("ArTaxOr_test", "ArTaxOr/test", "ArTaxOr/annotations/test.json"),
    ("UODD_train", "UODD/train", "UODD/annotations/train.json"),
    ("UODD_test", "UODD/test", "UODD/annotations/test.json"),
    ("FISH_train", "FISH/train", "FISH/annotations/train.json"),
    ("FISH_test", "FISH/test", "FISH/annotations/test.json"),
    ("NEUDET_train", "NEU-DET/train", "NEU-DET/annotations/train.json"),
    ("NEUDET_test", "NEU-DET/test", "NEU-DET/annotations/test.json"),
    ("clipart1k_train", "clipart1k/train", "clipart1k/annotations/train.json"),
    ("clipart1k_test", "clipart1k/test", "clipart1k/annotations/test.json"),
    ("dataset1_test", "dataset1/test", "dataset1/annotations/test.json"),
    ("dataset2_test", "dataset2/test", "dataset2/annotations/test.json"),
    ("dataset3_test", "dataset3/test", "dataset3/annotations/test.json")
]

for shot in [1, 5, 10]:
    new_anns = ("DIOR_{}shot".format(shot),
                "DIOR/train/new_train",
                "DIOR/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("ArTaxOr_{}shot".format(shot),
                "ArTaxOr/train",
                "ArTaxOr/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("UODD_{}shot".format(shot),
                "UODD/train",
                "UODD/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    # newly added
    new_anns = ("FISH_{}shot".format(shot),
                "FISH/train",
                "FISH/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("NEUDET_{}shot".format(shot),
                "NEU-DET/train",
                "NEU-DET/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("clipart1k_{}shot".format(shot),
                "clipart1k/train",
                "clipart1k/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset1_{}shot".format(shot),
                "dataset1/train",
                "dataset1/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset2_{}shot".format(shot),
                "dataset2/train",
                "dataset2/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset3_{}shot".format(shot),
                "dataset3/train",
                "dataset3/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset1_{}shot_test".format(shot),
                "dataset1/train",
                "dataset1/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset2_{}shot_test".format(shot),
                "dataset2/train",
                "dataset2/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)

    new_anns = ("dataset3_{}shot_test".format(shot),
                "dataset3/train",
                "dataset3/annotations/{}_shot.json".format(shot))
    _PREDEFINED_CD.append(new_anns)
        
def register_all_CD(root):
    for name, image_dir, json_file in _PREDEFINED_CD:
        with open(os.path.join(root, json_file), "r", encoding="utf-8") as f:
            data = json.load(f)
        classes = [i["name"] for i in data["categories"]]
        register_coco_instances(name, {}, os.path.join(root, json_file), os.path.join(root, image_dir))
        MetadataCatalog.get(name).set(thing_classes=classes)

# True for open source;
# Internally at fb, we register them elsewhere
if __name__.endswith(".builtin"):
    # Assume pre-defined datasets live in `./datasets`.
    _root = os.getenv("DETECTRON2_DATASETS", "datasets")
    register_all_coco(_root)
    register_all_lvis(_root)
    register_all_cityscapes(_root)
    register_all_cityscapes_panoptic(_root)
    register_all_pascal_voc(_root)
    register_all_ade20k(_root)
    # TODO replace to your own dataset path
    _CD_root = os.getenv("DETECTRON2_DATASETS", "/data/user/dataset/")
    register_all_CD(_CD_root)
