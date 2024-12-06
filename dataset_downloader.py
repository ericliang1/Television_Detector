import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "coco-2017",
    label_types=["detections"],
    classes=["tv"],
    max_samples=1000,
)