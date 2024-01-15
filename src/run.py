from data.data_processing import DataProcessing
from feature.feature_extractor import FeatureExtractor
from model.segment_classify import SegmentClassifyModel
from model.separate_detect import SeparateDetectModel

from constant import (
    ROOT_PATH,
    PROCESSED_FEATURE,
    CLASSIFY,
    DETECT,
    MFCC,
    STFT,
    FEATURE_PARAM,
)


# data_processing = DataProcessing(ROOT_PATH)

# lists = data_processing.get_paths(data_processing.new_data_path)
# print(lists)

# if data_processing.is_exist_new_data():
#     data_processing.move_new_to_raw()
#     lists = data_processing.get_paths(data_processing.new_data_path)
#     print(lists)

# train data
# audio_paths = data_processing.get_paths(data_processing.new_data_path)

# feature_extractor = FeatureExtractor(
#     data_root_path=ROOT_PATH,
#     middle_path=f"{PROCESSED_FEATURE}/{CLASSIFY}",
#     feature_type=MFCC,
#     n_classes=8,
#     n_features=40,
#     n_times=20,
#     n_channels=1,
# )

# feature_extractor.feature_extractor(audio_paths)

# audio_paths = data_processing.get_paths(data_processing.new_data_path)
# print(audio_paths)

# feature_dict = FEATURE_PARAM[CLASSIFY][STFT]
# print(feature_dict)

# feature_extractor = FeatureExtractor(
#     data_root_path=f"{ROOT_PATH}/{PROCESSED_FEATURE}",
#     method_type=CLASSIFY,
#     feature_type=STFT,
#     n_fft=feature_dict["n_fftt"],
#     n_times=feature_dict.n_times,
#     hop_length=feature_dict.hop_length,
#     win_length=feature_dict.win_length,
# )

# feature_extractor.feature_extractor(audio_paths)

# segment_classify = SegmentClassifyModel(40, 0.001, 20)

# segment_classify.create_dataset()
# segment_classify.create()
# segment_classify.train()
# segment_classify.evaluate()
# segment_classify.save()

# print(segment_classify.predict("../data/raw/pattern/P1/08/P1_08_0001.m4a", 100, 0))

separate_detect = SeparateDetectModel(40, 0.001, 20, 16)

separate_detect.create_dataset()
separate_detect.create()
separate_detect.train()
separate_detect.evaluate()
separate_detect.save()

print(separate_detect.predict("../data/raw/pattern/P1/08/P1_08_0001.m4a", 100, 0))