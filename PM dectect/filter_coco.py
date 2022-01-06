import fiftyone as fo
import fiftyone.zoo as foz


# Load the coco-2017 dataset and assign the class that I want to filtering.
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


# Export the data that filtered with fiftyone and assign dataset type to YOLOv5 type 
dataset.export(
    export_dir=export_dir,
    dataset_type=fo.types.YOLOv5Dataset,
    label_field=label_field
)

# filter the coco dataset with fiftyone 
