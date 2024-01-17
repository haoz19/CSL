import os

from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.datasets import load_sem_seg

### 这个是和cityscapes完全吻合
SYNSCAPES_SEM_SEG_CATEGORIES = [
    "road", 
    "sidewalk", 
    "building", 
    "wall", 
    "fence", 
    "pole", 
    "light", 
    "sign", 
    "vegetation", 
    "terrain", 
    "sky", 
    "person", 
    "rider", 
    "car", 
    "truck", 
    "bus", 
    "train",
    "motocycle", 
    "bicycle"
]

def register_SYNSCAPES(root):
    #root = os.path.join(root, "synscapes")
    root = "/home/ubuntu/hao/Hao2/maskformer/datasets/synscapes/Synscapes"
    for name, image_dirname, sem_seg_dirname in [
        ("train", "img/rgb", "img/transformed_class")
        #("train", "images", "transformed_labels"),
        # ("test", "images_detectron2/test", "annotations_detectron2/test"),
    ]:
        image_dir = os.path.join(root, image_dirname)
        gt_dir = os.path.join(root, sem_seg_dirname)
        name = f"SYNSCAPES_{name}_sem_seg"
        DatasetCatalog.register(
            name, lambda x=image_dir, y=gt_dir: load_sem_seg(y, x, gt_ext="png", image_ext="png")
        )
        MetadataCatalog.get(name).set(
            stuff_classes=SYNSCAPES_SEM_SEG_CATEGORIES[:],
            image_root=image_dir,
            sem_seg_root=gt_dir,
            evaluator_type="sem_seg",
            ignore_label=255,
        )

_root = os.getenv("DETECTRON2_DATASETS", "datasets")
register_SYNSCAPES(_root)