if [ "$1" = "update_category" ]; then
    python crawler_twse_category_volume.py --start_date=20040709
elif [ "$1" = "RNet" ]; then
    python train.py -n RNet --train_record_file=./data/train.npz \
    --hidden_size=75 --rnn=GRU --num_epochs=8 --batch_size=32 \
    --lr=1
else
    echo "Invalid Option Selected"
fi
