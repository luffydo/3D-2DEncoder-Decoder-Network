import os

from cruw.cruw import CRUW

rodnet_res_dir = '/home/zdk/RODNet-master/results/156-Multibase-Aug-noattention-nomulti-cycli-loss(max_det15,1e-5)-20230330-094658'  #your inference results
convert_res_dir = '/home/zdk/RODNet-master/zip/156'     

SEQ_NAMES = ['2019_05_28_CM1S013', '2019_05_28_MLMS005', '2019_05_28_PBMS006', '2019_05_28_PCMS004',
             '2019_05_28_PM2S012', '2019_05_28_PM2S014', '2019_09_18_ONRD004', '2019_09_18_ONRD009',
             '2019_09_29_ONRD012', '2019_10_13_ONRD048']

# dataset = CRUW(data_root='/mnt/disk1/CRUW')#"/home/zdk/RODNet-master"
dataset = CRUW(data_root='/home/zdk/RODNet-master')

seq_names = os.listdir(rodnet_res_dir)
if not os.path.exists(convert_res_dir):
    os.makedirs(convert_res_dir)
for seq_name in seq_names:
    if seq_name.upper() in SEQ_NAMES:
        txt_name_in = os.path.join(rodnet_res_dir, seq_name, 'rod_res.txt')
        txt_name_out = os.path.join(convert_res_dir, seq_name.upper() + '.txt')
        with open(txt_name_in, 'r') as f:
            data = f.readlines()
        f_out = open(txt_name_out, 'w')
        for line in data:
            frameid, class_name, rid, aid, conf = line.rstrip().split()
            rid = int(rid)
            aid = int(aid)
            r = dataset.range_grid[rid]
            a = dataset.angle_grid[aid]
            conf = float(conf)
            if conf > 1:
                conf = 1.0
            f_out.write("%s %.4f %.4f %s %.4f\n" % (frameid, r, a, class_name, conf))
