# 3D-2DEncoder-Decoder-Network


## Installation

Create a conda environment for 3D-2DEncoder-Decoder-Network. Tested under Python 3.6, 3.7, 3.8.
```commandline
conda create -n rodnet python=3.* -y
conda activate rodnet
```

Install pytorch.
**Note:** 
If you met some issues with environment, feel free to raise an issue.
```commandline
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch  # if not using TDC
```

Install `cruw-devkit` package. 
Please refer to [`cruw-devit`](https://github.com/yizhou-wang/cruw-devkit) repository for detailed instructions.
```commandline
git clone https://github.com/yizhou-wang/cruw-devkit.git
cd cruw-devkit
pip install .
cd ..
```

## Prepare data for RODNet

Download [ROD2021 dataset](https://www.cruwdataset.org/download#h.mxc4upuvacso). 
Follow [this script](https://github.com/yizhou-wang/RODNet/blob/master/tools/prepare_dataset/reorganize_rod2021.sh) to reorganize files as below.

```
data_root
  - sequences
  | - train
  | | - <SEQ_NAME>
  | | | - IMAGES_0
  | | | | - <FRAME_ID>.jpg
  | | | | - ***.jpg
  | | | - RADAR_RA_H
  | | |   - <FRAME_ID>_<CHIRP_ID>.npy
  | | |   - ***.npy
  | | - ***
  | | 
  | - test
  |   - <SEQ_NAME>
  |   | - RADAR_RA_H
  |   |   - <FRAME_ID>_<CHIRP_ID>.npy
  |   |   - ***.npy
  |   - ***
  | 
  - annotations
  | - train
  | | - <SEQ_NAME>.txt
  | | - ***.txt
  | - test
  |   - <SEQ_NAME>.txt
  |   - ***.txt
  - calib
```

Convert data and annotations to `.pkl` files.
```commandline
python tools/prepare_dataset/prepare_data.py \
        --config configs/<CONFIG_FILE> \
        --data_root <DATASET_ROOT> \
        --split train,test \
        --out_data_dir data/<DATA_FOLDER_NAME>
```

## Train models

```commandline
python train_train.py --data_dir data/<DATA_FOLDER_NAME> \
        --log_dir checkpoints/
```

## Inference

```commandline
python test_test.py --data_dir data/<DATA_FOLDER_NAME> \ 
        --checkpoint <CHECKPOINT_PATH> \
        --res_dir results/
```
**Note:** 
The participates need to submit their radar object detection results(--res_dir results/) for the testing set to the [evaluation server](https://codalab.lisn.upsaclay.fr/competitions/1063). The evaluation metrics include AP and AP under four different driving scenarios, i.e., parking lot (PL), campus road (CR), city street (CS), highway (HW). The main score for this challenge is the overall AP. The details of the evaluation method is mentioned in paper.

The submission file should contain 10 different files for 10 testing sequences with the following names:ziptxt
```
    2019_05_28_CM1S013.txt
    2019_05_28_MLMS005.txt
    2019_05_28_PBMS006.txt
    2019_05_28_PCMS004.txt
    2019_05_28_PM2S012.txt
    2019_05_28_PM2S014.txt
    2019_09_18_ONRD004.txt
    2019_09_18_ONRD009.txt
    2019_09_29_ONRD012.txt
    2019_10_13_ONRD048.txt
```