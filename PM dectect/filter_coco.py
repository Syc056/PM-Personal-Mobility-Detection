import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "coco-2017",
    splits=["validation","train"],
    classes=["person","bicycle","motorcycle"],
    max_sample = 5000,
    shuffle = True
)

session = fo.launch_app(dataset)

export_dir = "C:/Users/sy__c/Desktop/test/filtered_data"
label_field = "ground_truth"

dataset.export(
    export_dir=export_dir,
    dataset_type=fo.types.YOLOv5Dataset,
    label_field=label_field
)