import pandas as pd
from sireproj.models import Qtion

tmp_data=pd.read_csv('script/file1.csv',index_col=False)

questns = [
    Qtion(
        Chapter = tmp_data['Chap'][row],
        Stext = tmp_data['Short Text'][row],
        Ftext = tmp_data['Question'][row],
        Qno = tmp_data['No.'][row],
        HQtn = tmp_data['Hardware Response Type'][row],
        PQtn = tmp_data['Process Response Type'][row],
        HuQtn = tmp_data['Human Response Type'][row],
        Qtype = tmp_data['Question Type'][row],
        Chemical = tmp_data['Chemical'][row],
        LNG = tmp_data['LNG'][row],
        LPG = tmp_data['LPG'][row],
        Oil = tmp_data['Oil'][row],
        Conditional = tmp_data['Conditional'][row],
        Roviq = tmp_data['ROVIQ List'][row],
    )
    for row in tmp_data.index
]
Qtion.objects.bulk_create(questns)