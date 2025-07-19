def save(model, file_path):
    if hasattr(model, "save"):
        model.save()
        return
    
    import pickle

    with open(file_path, "wb") as f:
        pickle.dump(model, f)
