#!/bin/bash

version=3
shots=(1 3 5)

for shot in "${shots[@]}"
do
    # TR in EN template
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_gen_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_disc_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_gen_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_disc_en -n ${shot} -o ../data/tr/btwd/temp_en/v${version}

    # TR in TR template
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_gen_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph.json -t morph_disc_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_gen_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/tr/btwd/btwd_prep_post_sample_morph_nonce.json -t morph_disc_tr -n ${shot} -o ../data/tr/btwd/temp_tr/v${version}

    # EN in EN template
    python prepare_data_for_eval.py -d ../data/en/morpholex/MorphoLEX_en_prep_morph_sample.json -t morph_gen_en -n ${shot} -o ../data/en/morpholex/temp_en/v${version}
    python prepare_data_for_eval.py -d ../data/en/morpholex/MorphoLEX_en_prep_morph_sample.json -t morph_disc_en -n ${shot} -o ../data/en/morpholex/temp_en/v${version}
    
    # EN in TR template
    python prepare_data_for_eval.py -d ../data/en/morpholex/MorphoLEX_en_prep_morph_sample.json -t morph_gen_tr -n ${shot} -o ../data/en/morpholex/temp_tr/v${version}
    python prepare_data_for_eval.py -d ../data/en/morpholex/MorphoLEX_en_prep_morph_sample.json -t morph_disc_tr -n ${shot} -o ../data/en/morpholex/temp_tr/v${version}
done