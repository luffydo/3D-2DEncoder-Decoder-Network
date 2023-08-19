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