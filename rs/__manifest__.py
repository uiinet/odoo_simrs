{
    'name': 'SIM RS',
    'author': "UIINET and Friends",
    'website': "https://gpu.co.id",
    'summary': 'Sistem Informasi Rumah Sakit',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base', 'mail','hr','contacts','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/rs_kamar.csv',
        'data/rs_unit.csv',
      	'data/rs_agama.csv',
      	'data/rs_asal_rujukan.csv',
      	'data/rs_bed.csv',
      	'data/rs_cara_datang.csv',
      	'data/rs_cara_masuk.csv',
      	'data/rs_data_kamar.csv',
      	'data/rs_goldar.csv',
      	'data/rs_stat_kawin.csv',
        'data/rs_hub_pasien.csv',
        'data/rs_gender.csv',
        'data/rs_jenis_bayar.csv',
        'data/hr.department.csv',
        # 'data/sfx_jenis_obat.csv',
        'views/rs_unit_views.xml',
        'views/rs_diagnosa_views.xml',
        'views/rs_grup_diagnosa_views.xml',
        'views/res_partner_pasien_views.xml',
        'views/rs_jenis_bayar_views.xml',
        'views/res_partner_views.xml',
        'views/rs_agama_views.xml',
        'views/rs_goldar_views.xml',
        'views/rs_stat_kawin_views.xml',
        'views/rs_kelas_views.xml',
        'views/rs_prosedur_views.xml',
        'views/rs_gender_views.xml',
        'views/rs_asal_rujukan_views.xml',
        'views/rs_cara_masuk_views.xml',
        'views/rs_cara_datang_views.xml',
        'views/rs_bed_views.xml',
        'views/rs_kamar_views.xml',
        'views/rs_ruang_views.xml',
        'views/rs_hub_pasien_views.xml',
        'views/rs_kun_views.xml',
        'views/rs_department.xml',
        'views/rs_data_kamar_views.xml',
        'views/menus.xml',
    ],

}
