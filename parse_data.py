
from column_index_map import *
import sys
import pickle

def get_class(actual_next_los):
    actual_next_los = int (actual_next_los)
    if actual_next_los == 1:
        category = 1
    elif actual_next_los == 2:
        category = 2
    elif actual_next_los == 3:
        category = 3
    elif 4 <= actual_next_los <= 6 :
        category = 4
    elif 7 <= actual_next_los <= 13 :
        category = 5
    elif actual_next_los >= 14 :
        category = 6

    return category

def featurize_row(row_data):
    '''
    :param row_data:
    :return:
    '''
    patient_id = row_data[PID_IDX]

    patient_level_feature_vector = [0.0 for xx in range(3)]
    patient_level_feature_vector[0] = float(row_data[GENDER_IDX])

    patient_level_feature_vector[1] = float(row_data[BIRTH_IDX])
    patient_level_feature_vector[2] = float(row_data[RACE_GRP_IDX])

    category = get_class(row_data[NEXT_LOS_IDX])

    admission_level_feature_vector = [0.0 for xx in SRC_TYPES for yy in range(17)]

    src_type = int(row_data[SRC_COL_IDX])# GEt the src type
    comorbidity_idx = COMORB_START_IDX

    if src_type == 0 :
        start_index = 0
        end_index = 17

        while start_index < end_index:
            value = 0.0
            if row_data[comorbidity_idx] != '':
                value = row_data[comorbidity_idx]
            admission_level_feature_vector[start_index] = float (value)
            comorbidity_idx += 1
            start_index += 1
    elif src_type == 1 :
        start_index = 17
        end_index = 34
        while start_index < end_index:
            value = 0.0
            if row_data[comorbidity_idx] != '':
                value = row_data[comorbidity_idx]
            admission_level_feature_vector[start_index] = float (value)
            if (row_data[comorbidity_idx]) == ' ':
                (row_data[comorbidity_idx]) = 0
            comorbidity_idx += 1
            start_index += 1
    elif src_type == 2 :
        start_index = 34
        end_index = 51
        while start_index < end_index:
            value = 0.0
            if row_data[comorbidity_idx] != '':
                value = row_data[comorbidity_idx]
            admission_level_feature_vector[start_index] = float (value)
            if (row_data[comorbidity_idx]) == ' ':
                (row_data[comorbidity_idx]) = 0
            comorbidity_idx += 1
            start_index += 1

    return (patient_id,  patient_level_feature_vector + admission_level_feature_vector, category)

def get_dummy_feature_seq(num_seq_reqd, feature_vector_length=17):
    '''

    :param num_seq_reqd:
    :param feature_vector_length:
    :return:
    '''
    return [0.0 for xx in range(num_seq_reqd) for yy in feature_vector_length]

def read_oshpd_data(file_name):
    fhand = open(file_name)
    fhand.readline()
    XX = []
    YY = []

    for line in fhand:
        row_data =  line.strip().split(',')
        out = featurize_row(row_data)
        XX.append(out[1])
        YY.append(out[2])

    train_dict = {'training_features':XX , 'categories' : YY}


    pickle.dump(train_dict, open("/Users/oshpd/vikhyati/Desktop/training_data.pickle", "wb"))

if __name__ == "__main__":
    file_name =  '/Users/oshpddata/Desktop/vikhyati/OSHPD_CLEAN_LOS.csv'  # Spec
    read_oshpd_data(file_name)



