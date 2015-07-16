from project.classify.models import Classification
from project.models import  Feature
from project import db

def get_user_photo_combos():
     return db.session.query(Classification).distinct(
        Classification.user_id, Classification.photo_id )

def get_classifications_for_user_photo(combo):
    return  Classification.query.filter(
        Classification.user_id==combo.user_id, Classification.photo_id==combo.photo_id).all()


def prepopulate_classify_dict(classify_dict, id, combo):
    classify_dict[id] = {}
    classify_dict[id]['user_id'] = combo.user_id
    classify_dict[id]['photo_id'] = combo.photo_id

    features =  get_features()
    for feature in features:
        classify_dict[id][feature.slug] = 0

    return classify_dict

def get_features():
    return Feature.query.all()

def create_features_dict():
    features_dict = {}
    features =  get_features()

    for feature in features:
        features_dict[feature.id] = feature.slug

    return features_dict


def get_data():
    classify_dict = {}
    classify_list = []

    features = create_features_dict()
    
    # find distinct user-photo combos
    user_photo_combos = get_user_photo_combos()

    for combo in user_photo_combos:
        id = str(combo.user_id) + '_' + str(combo.photo_id)

        # prepopulate classify_dict with false values (0) for each feature
        prepopulate_classify_dict(classify_dict, id, combo)

        # find all classifactions that have the user-photo combo
        classifications =  get_classifications_for_user_photo(combo)

        # mark features as true (1)
        for classification in classifications:
            classify_dict[id][features[classification.feature_id]] = 1

    # turn dictionary into a list
    for key in classify_dict:
        classify_list.append(classify_dict[key])

    return classify_list
