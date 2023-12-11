### ----------- Dataset settings --------------- ###

data = dict(
    dataset_type = 'ArgoverseDataset',
    joblib_batch_size = 100,
    train=dict(
        features = '../features/forecasting_features/forecasting_features_train.pkl',
        pipeline = []
    ),
    test=dict(
        features = '../features/forecasting_features/forecasting_features_val_testmode.pkl',
        pipeline=[]
    ),
    val=dict(
        features = '../features/forecasting_features/forecasting_features_val.pkl',
        pipeline=[]
    )
)

### -----------  Model -----------  ###

model = dict(
    type = 'KNearestNeighbor',
    normalize=True,
    use_delta=True,
    use_map=False,
    use_social=True,
    n_neigh=6,
    obs_len=20,
    pred_len=30,
    model_path = 'checkpoints/S_KNN',
    train_cfg = dict(

    ),
    test_cfg = dict(

    ),
    val_cfg=dict(

    )
)

### -------------- Evaluation ----------------- ###
work_dir = 'work_dirs/knearest_neighbor_nomap_social_neigh6'

_base_ = [
    '../_base_/eval.py'
]