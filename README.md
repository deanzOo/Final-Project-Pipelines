# Install
1. Install python 3.9+
[Official Python Website](http://python.org)
2. Update pip
```
python -m pip install --upgrade pip
```
3. Install requirements

```
pip install -r requirements.txt
```

# Run
```
python make_logo.py set_active 0 - first pipeline
python make_logo.py
python make_logo.py set_active 1 - second pipeline

python deep-logo-gan.py [-h] [--batch_size [BATCH_SIZE]] [--epochs [EPOCHS]] [--sample_period [SAMPLE_PERIOD]] 
                        [--latent_dim [LATENT_DIM]] [--data_dir [DATA_DIR]] [--dataset [DATASET]] 
                        [--conv_padding [CONV_PADDING]] [--use_bias] [--dropout_rate [DROPOUT_RATE]] 
                        [--image_size [IMAGE_SIZE]] [--colors [COLORS]] [--learning_rate [LEARNING_RATE]] 
                        [--out_dir [OUT_DIR]]
