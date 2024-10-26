from ultralytics import YOLO
import json

def predict():
    

    # Load a model
    model = YOLO("models/adharv2.pt")  # pretrained YOLO11n model

    # Run batched inference on a list of images
    result = model("image.png", save=True, conf=0.1,save_txt=True, save_crop = True)  # return a list of Results objects

        # Example usage:
    txt_file = "runs/detect/predict/labels/image.txt"  # Your YOLO txt file
    notes_file = "jsons_notes_file/adhar.json"  # Your notes.json file

    # Load class names from notes.json
    class_names = load_class_names_from_json(notes_file)

    # Convert and get the result as a dict
    annotations_dict = yolo_txt_to_dict(txt_file, class_names)

    # Print or work with the returned dictionary
    print(annotations_dict)
    return annotations_dict

    
    
    
    
    

def load_class_names_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        class_names = {category['id']: category['name'] for category in data['categories']}
    return class_names

# Function to convert YOLO txt annotation to a dictionary (JSON format)
def yolo_txt_to_dict(txt_file, class_names):
    data = []
    with open(txt_file, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            annotation = {
                "class_id": int(class_id),
                "class_name": class_names.get(int(class_id), "Unknown"),  # Get class name from notes.json
                "bbox": {
                    "x_center": x_center,
                    "y_center": y_center,
                    "width": width,
                    "height": height
                }
            }
            data.append(annotation)
    
    # Return data as a dictionary
    return data


