datalist=(
artaxor
dior
fish
clipart1k
neu-det
uodd
)
shot_list=(
1
5
10
)
model_list=(
"l"
#"b"
#"s"
)
#--controller 

# CUDA_VISIBLE_DEVICES=0 python tools/train_net.py --num-gpus 1 --config-file configs/artaxor/vitl_shot1_artaxor_finetune.yaml MODEL.WEIGHTS weights/trained/vitl_0089999.pth DE.OFFLINE_RPN_CONFIG configs/RPN/mask_rcnn_R_50_C4_1x_ovd_FSD.yaml OUTPUT_DIR output/vitl/artaxor_1shot_1gpu/

for model in "${model_list[@]}"; do
  for dataset in "${datalist[@]}"; do
    for shot in "${shot_list[@]}"; do
      CUDA_VISIBLE_DEVICES=1 python tools/train_net.py --num-gpus 1 --config-file configs/${dataset}/vit${model}_shot${shot}_${dataset}_finetune.yaml MODEL.WEIGHTS weights/trained/vit${model}_0089999.pth DE.OFFLINE_RPN_CONFIG configs/RPN/mask_rcnn_R_50_C4_1x_ovd_FSD.yaml OUTPUT_DIR output/vit${model}/${dataset}_${shot}shot_1gpu/
    done
  done
done
