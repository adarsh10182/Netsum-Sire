import pandas as pd
from sireproj.models import VesselDisc

tmp_data=pd.read_csv('script/file.csv',index_col=False)

vessels = [
    VesselDisc(
        PDesc = tmp_data['Description'][row],
        Vtype = tmp_data['labels'][row],
    )
    for row in tmp_data.index
]
VesselDisc.objects.bulk_create(vessels)